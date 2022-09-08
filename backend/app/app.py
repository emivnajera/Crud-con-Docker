#Imports Area
from flask import Flask, render_template, request, Response
from flask_pymongo import PyMongo
from bson import json_util


#Incializar Flask
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongodb/ejemplo'
mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/create',methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        carnet = request.form['carnet']
        mongo.db.students.insert_one(
            {'name':name, 'lastname':lastname, 'carnet':carnet}
        )
        return 'Student Created'

@app.route('/read',methods=['GET'])
def read():
    if request.method == 'GET':
        students = mongo.db.students.find()
        response = json_util.dumps(students)
        return Response(response, mimetype='application/json')


@app.route('/update',methods=['POST'])
def update():
    if request.method == 'POST':
        carnet = request.form['carnet']
        new_name = request.form['new_name']
        new_lastname = request.form['new_lastname']
        mongo.db.students.update_one({'carnet':carnet},{'$set':{'name':new_name, 'lastname':new_lastname}})
        return 'Student Updated'

@app.route('/delete',methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        carnet = request.form['carnet']
        mongo.db.students.delete_one({'carnet':carnet})
        return 'Student Deleted'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



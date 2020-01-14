import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('tasks.html', tasks = mongo.db.tasks.find()) # el 'tasks.find()' es el method para buscar entre los records the nuestra collection en MongoDB llamada tasks

@app.route('/add_tasks')
def add_tasks():
    return render_template('addtask.html', 
    categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    task = mongo.db.tasks
    task.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
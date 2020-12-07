from flask import Flask, jsonify, json
from flask_restplus import Namespace, Api, Resource, reqparse, fields, abort
import ast
from models import *
from db import session
from db_cred import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

api = Api(app)
myNamespace = Namespace("tutoFlask-restplus", "todo list sample api")
api.add_namespace(myNamespace)


class TodoTask(object):
    task = myNamespace.model('task', {
        "t_id": fields.Integer(required=False),
        "t_title": fields.String(required=False),
        "t_description": fields.String(required=False),
        "t_done": fields.Boolean(required=False)
    })



request = reqparse.RequestParser()
request.add_argument('task', location='json')


@myNamespace.route("/tasks/<int:task_id>")
class TaskByID(Resource):
    def get(self, task_id=None):
        """Get the details of a task from its id"""
        task = session.query(Task).filter(Task.t_id == task_id).first()
        if not task:
            abort(404, message="Task {} not existing".format(id))
        return task.display()

    def delete(self, task_id):
        """Delete a task from its id"""
        task = session.query(Task).filter(Task.t_id == task_id).first()
        if not task:
            abort(404, message="Task {} not existing".format(id))
        session.delete(task)
        session.commit()
        return jsonify({'resultat suppression de la tache d\'id ' + str(task_id): True})

    @myNamespace.marshal_with(TodoTask.task)
    @myNamespace.expect(request, validate=False)
    def put(self, task_id):
        """Change values of a task from its id"""
        parsed_args = request.parse_args()
        task = session.query(Task).filter(Task.t_id == task_id).first()
        newDataTask = parsed_args['task']
        json_data = ast.literal_eval(newDataTask)
        task.setTitle(json_data.get('t_title'))
        task.setDescription(json_data.get('t_description'))
        task.setStatus(json_data.get('t_done'))
        session.add(task)
        session.commit()
        return task, 201


@myNamespace.route("/tasks")
class TodoTaskList(Resource):
    @myNamespace.marshal_with(TodoTask.task)
    def get(self):
        """Get every task in the list"""
        tasks = session.query(Task).all()
        print(type(tasks))
        return tasks

    @myNamespace.marshal_with(TodoTask.task)
    @myNamespace.expect(request, validate=False)
    def post(self):
        """Add a task to the list"""
        parsed_args = request.parse_args()
        taskToCreate = parsed_args['task']
        json_data = ast.literal_eval(taskToCreate)
        print(json_data)
        newTask = Task(int(json_data.get('t_id')), json_data.get('t_title'), json_data.get('t_description', ""), json_data.get('t_done'))
        print(str(type(newTask)))
        session.add(newTask)
        session.commit()
        return newTask, 201


if __name__ == '__main__':
    app.run(debug=True)

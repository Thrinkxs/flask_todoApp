# from app import app

from flask import Flask, render_template, request, jsonify, Blueprint, url_for, redirect
from models import Todo
from app import db


blueprint = Blueprint('blueprint', __name__)


# @app.route('/')
# def index():
#     return "Hello"

@blueprint.route('/index', methods=['GET'])
@blueprint.route('/todo', methods=['GET'])
@blueprint.route('/', methods=['GET'])
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@blueprint.route('/todo', methods=['POST'])
def add_todo():
    task = request.form['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('blueprint.index'))


@blueprint.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('blueprint.index'))


@blueprint.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('blueprint.index'))

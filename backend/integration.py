import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from models import Todo
from app import create_app, db


class TestTodoRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkavnntb:Lvxr4i1weHxWW5wMRyHoCoPyXPwkfL5J@rain.db.elephantsql.com/mkavnntb'

        self.app.config['TESTING'] = True
        self.app.config['SERVER_NAME'] = 'localhost'

        self.app_context = self.app.app_context()
        self.app_context.push()

        with self.app.app_context():
            db.create_all()
        self.todo = Todo(task="Test Task", completed=False)
        db.session.add(self.todo)
        db.session.commit()

    def tearDown(self):
        self.app_context.pop()

    def test_add_and_delete_todo(self):

        response = self.client.post(
            url_for('blueprint.add_todo'), data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)
        todo = Todo.query.session.get(Todo, self.todo.id)
        self.assertIsNotNone(todo)

        response = self.client.get(
            url_for('blueprint.delete', todo_id=todo.id))
        self.assertEqual(response.status_code, 302)
        todo = Todo.query.session.get(Todo, self.todo.id)
        self.assertIsNone(todo)


if __name__ == '__main__':
    unittest.main()

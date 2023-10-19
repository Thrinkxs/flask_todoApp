import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from models import Todo
from app import create_app, db


class TestCompleteRoute(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkavnntb:Lvxr4i1weHxWW5wMRyHoCoPyXPwkfL5J@rain.db.elephantsql.com/mkavnntb'

        self.app_context = self.app.app_context()
        self.app_context.push()

        with self.app.app_context():
            db.create_all()
        self.todo = Todo(task="Test Task", completed=False)
        db.session.add(self.todo)
        db.session.commit()

    def tearDown(self):
        self.app_context.pop()
        # with self.app.app_context():
        #     db.session.remove()
        #     db.drop_all()

    def test_complete_route(self):
        with self.app.app_context():
            todo = Todo.query.get(self.todo.id)
            response = self.client.get(
                url_for('blueprint.complete', todo_id=todo.id))
            self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()

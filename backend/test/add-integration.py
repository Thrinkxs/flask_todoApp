import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from models import Todo
from app import create_app, db


class TestTodoRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Set up a test database
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_and_delete_todo(self):

        response = self.client.post(
            url_for('blueprint.add_todo'), data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)
        todo = Todo.query.filter_by(task='Test Task').first()
        self.assertIsNotNone(todo)

        response = self.client.get(
            url_for('blueprint.delete', todo_id=todo.id))
        self.assertEqual(response.status_code, 302)
        todo = Todo.query.filter_by(task='Test Task').first()
        self.assertIsNone(todo)


if __name__ == '__main__':
    unittest.main()

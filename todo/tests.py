"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from todo.models import TodoItem


class TodoItemTest(TestCase):

    def test_json(self):
        """Checking json serialization"""
        item = TodoItem(
            title='the title',
            order=2,
            done=False)
        result = item.to_json()
        self.assertEqual(
            result,
            {'title': 'the title',
             'order': 2,
             'done': False})



    def test_rest_empty_views(self):
        response = self.client.get("/rest-empty/todo/")
        self.assertEqual(response.status_code, 200)

    def test_admin_views(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)


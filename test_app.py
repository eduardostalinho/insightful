# -*- coding: utf-8 -*-
import unittest
from app import insightful
from flask.ext.testing import TestCase

STATUS_CODES = {
    'OK': 200,
    'Internal Server Error': 500
}


class InsightfulTestCase(TestCase):
    def create_app(self):
        app = insightful
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(STATUS_CODES['OK'], response.status_code)
        self.assertIn('Generate your insights', response.data)


unittest.main()

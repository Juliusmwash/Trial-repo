#!/usr/bin/python3
"""BaseModel tests module"""

import unittest
import pycodestyle
from models import base_model
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class MyTestCase(unittest.TestCase):
    """BaseModel testcases"""

    def test_base_model_0(self):
        """Check for the base_model module documentation"""
        self.assertTrue(len(base_model.__doc__) > 5)

    def test_base_model_1(self):
        """Check for the BaseModel class documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 5)

    def test_base_model_2(self):
        """Check for the pep8 rules violation"""
        style_guide = pycodestyle.StyleGuide()
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        report = style_guide.check_files([file1, file2])
        self.assertEqual(report.total_errors, 0)

    def test_base_model_3(self):
        """Test id type"""
        obj = BaseModel()
        self.assertTrue(type(obj.id) == str)

    def test_base_model_4(self):
        """Test datetime type (created_at, updated_at)"""
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) == datetime)
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_base_model_5(self):
        """Test __str__ output"""
        test = BaseModel()
        self.assertEqual(test.__str__(), "[" + test.__class__.__name__ + "]" +
                         " (" + test.id + ") " + str(test.__dict__))

    def test_base_model_6(self):
        """Test for id creation"""
        my_first = BaseModel()
        my_second = BaseModel()
        my_third = BaseModel()
        self.assertTrue(my_first.id != my_second.id)
        self.assertTrue(my_third.id != my_second.id)
        self.assertTrue(my_first.id != my_third.id)

    def test_base_model_7(self):
        """Test to_dict method"""
        obj = BaseModel()
        output = obj.to_dict()
        self.assertTrue(type(output["created_at"] == str))
        self.assertTrue(type(output["updated_at"] == str))
        self.assertTrue(type(obj.created_at) == datetime)
        self.assertTrue(type(obj.updated_at) == datetime)
        self.assertEqual(output["created_at"], obj.created_at.isoformat())
        self.assertEqual(output["updated_at"], obj.updated_at.isoformat())

    def test_base_model_8(self):
        """Test with an empty dictionary"""
        my_dict = {}
        obj = BaseModel(**my_dict)
        self.assertTrue(type(obj.id) == str)
        self.assertTrue(type(obj.created_at) == datetime)
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_base_model_9(self):
        """Test with a None argument"""
        obj = BaseModel(None)
        self.assertTrue(type(obj.id) == str)
        self.assertTrue(type(obj.created_at) == datetime)
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_base_model_10(self):
        """Check if object is a basemodel instance"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)


if __name__ == '__main__':
    unittest.main()

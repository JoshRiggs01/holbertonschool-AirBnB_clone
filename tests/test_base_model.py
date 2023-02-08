#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""
    
    def test_init(self):
        """Tests the initialization of a BaseModel instance"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertNotEqual(model.id, str(uuid.uuid4()))
        
    def test_str(self):
        """Tests the string representation of a BaseModel instance"""
        model = BaseModel()
        expected = '[BaseModel] ({}) {{'format(model.id)
        expected += "'id': '{}', ".format(model.id)
        expected += "'created_at': datetime.datetime({}, {}, {}), ".format(
            model.created_at.year, model.created_at.month, model.created_at.day)
        expected += "'updated_at': datetime.datetime({}, {}, {})".format(
            model.updated_at.year, model.updated_at.month, model.updated_at.day)
        expected += '}'
        self.assertEqual(str(model), expected)
        
    def test_save(self):
        """Tests the save method of a BaseModel instance"""
        model = BaseModel()
        created_at = model.created_at
        model.save()
        self.assertNotEqual(model.updated_at, created_at)
        
    def test_to_dict(self):
        """Tests the to_dict method of a BaseModel instance"""
        model = BaseModel()
        dictionary = model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'BaseModel')
        self.assertEqual(dictionary['id'], model.id)
        self.assertEqual(dictionary['created_at'], model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

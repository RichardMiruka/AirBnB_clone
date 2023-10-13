#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_new_instance_has_id_and_dates(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {{'id': '{model.id}', 'created_at': '{model.created_at}', 'updated_at': '{model.updated_at}'}}"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()

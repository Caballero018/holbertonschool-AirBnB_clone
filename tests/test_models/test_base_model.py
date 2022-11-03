#!/usr/bin/python3
""
import json
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ""
    def setUpClass(self):
        self.base1 = BaseModel()
        self.base1.name = "Greg"
        self.base1.my_number = 29
    
    @classmethod
    def tearDownClass(cls):
        del self.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)


    def test_to_dict(self):
        bas = BaseModel()
        sef = {
                'updated_at': bas.updated_at.isoformat(),
                'id': bas.id,
                'created_at': bas.created_at.isoformat(),
                '__class__': 'BaseModel'
            }
        self.assertEqual(bas.to_dict(), sef)

    def test_id(self):
        bas = BaseModel()
        b_id = bas.id
        self.assertEqual(bas.id, b_id)

    def test_created_at(self):
        bas = BaseModel()
        self.assertTrue(type(bas.created_at), datetime)

    def test_str(self):
        bas = BaseModel()
        str_bas = f"[BaseModel] ({bas.id}) {bas.__dict__}"
        self.assertEqual(str_bas, str(bas))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""
import json
import unittest
from models.base_model import BaseModel
from models import storage
import datetime


class TestBaseModel(unittest.TestCase):
    ""
    def test_save(self):
        bas2 = storage.all()
        bas1 = BaseModel()
        val = datetime.datetime.utcnow()
        setattr(bas1, "updated_at", val.isoformat())
        bas1.save()
        self.assertNotEqual(bas1.updated_at, datetime.datetime.now())


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

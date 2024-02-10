#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest):

    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'creat_at'))
        self.assertTrue(hasattr(obj, 'update_at'))

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertnotEqual(obj1.id, obj2.id)

    def test_str_representation(self):
        obj = BaseModel()
        expe_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expe_str)

    def test_to_dict_methode(self):
        obj = BaseModel()
        obj_dict = obj.to_dict
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict[id], obj.id)
        self.assertEqual(obj_dict['creat_at'], obj.created_at)
        self.assertEqual(obj_dict['update_at'], obj.updated_at)


if __name__ == "__main__":
    unittest.main()


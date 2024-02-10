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
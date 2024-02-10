#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStrorage

class Test_init__(unittest.TestCase):
    @patch('models.engine.file_storage.FileStorage.reload')
    def test_stor_relo_(self, o_reload):
        storage = FileStrorage()
        self.assertTrue(o_reload.called)

if __name__ == '__main__':
    unittest.main()

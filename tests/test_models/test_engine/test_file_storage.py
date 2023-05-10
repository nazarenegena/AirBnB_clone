import unittest
import json
import os
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):

       def test_docs(self):

        # test case for all the function calls
        self.assertIsNotNone(FileStorage.all)
        
        # test case for  the reload function
        self.assertIsNotNone(FileStorage.reload)
        
        # testing for the save function
        self.assertIsNotNone(FileStorage.save)
        
        # test case for new function
        self.assertIsNotNone(FileStorage.new)

       
        # test case for object instances
       def testObjInstances(self):
                obj = FileStorage()
                self.assertIsInstance(obj, FileStorage)
  

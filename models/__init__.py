#!/usr/bin/python3

""" the magic method 
for the models directory
"""

from models.engine.file_storage import FileStorage

# variable storage
storage = FileStorage()

# calling the reload function
storage.reload()

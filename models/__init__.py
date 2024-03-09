#!/usr/bin/python3
"""This is a init method form engine package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()

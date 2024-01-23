#!/usr/bin/env python3
"""
Python function that lists all documents in a collection:
"""
import pymongo


def list_all(mongo_collection):
    """
    Function to list all documents in a collection
    """
    if not mongo_collection:
        return []
    all_documents = mongo_collection.find()
    return [post for post in all_documents]

#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Writing strings to Redis
    """

    def __init__(self):
        """
        Storing the instance of the redis cielnt
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key

        Args:
            data: Input data that can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key

        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.IContextHandler import IContextHandler
import redis


class RedisContextHandler(IContextHandler):

    def __init__(self, namespace):
        self.namespace = namespace
        self.redis = redis.StrictRedis(
            port=6380,
            db=0,
            host="tfg-cristina.redis.cache.windows.net",
            password="CHdiaTs1UrnI1oYPZRgjsnYwqTey5GL4kKDZJkGoriM=",
            ssl=False)

    def get_field(self, key):
        return self.redis.get(self._get_key(key))

    def save_field(self, value, key):
        self.redis.set(self._get_key(key), value)

    def _get_key(self, key):
        return key + '_' + self.namespace

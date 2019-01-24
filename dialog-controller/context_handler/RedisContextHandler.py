#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import ssl


class RedisContextHandler:

    def __init__(self, namespace):
        self.namespace = namespace
        context = ssl.create_default_context()
        self.redis = redis.StrictRedis(
            port=6380,
            db=0,
            host="tfgcristina.redis.cache.windows.net",
            password="aKvi+IKiht4VhdVywM7Vx6PltnPHC6wput7KitIOHC0=",
            ssl=True
        )

    def get_field(self, key):
        return self.redis.get(self._get_key(key))

    def save_field(self, value, key):
        self.redis.set(self._get_key(key), value)

    def _get_key(self, key):
        return key + '_' + self.namespace

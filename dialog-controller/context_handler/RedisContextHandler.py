#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis


class RedisContextHandler:

    def __init__(self, namespace):
        self.namespace = namespace
        self.redis = redis.StrictRedis(
            port=6380,
            db=0,
            host="tfg-cristina.context_handler.cache.windows.net",
            password="Rd8eWjpwm4Bt85Dfqk8nF4dpu1j5aNh1qyb+SgAGH68=",
            ssl=True
        )

    def get_field(self, key):
        return self.redis.get(self._get_key(key))

    def save_field(self, value, key):
        self.redis.set(self._get_key(key), value)

    def _get_key(self, key):
        return key + '_' + self.namespace

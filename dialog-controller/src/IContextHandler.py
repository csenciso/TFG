#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IContextHandler:
    def get_field(self, key):
        raise NotImplementedError()

    def save_field(self, value, key):
        raise NotImplementedError()

#!/usr/bin/env python3

from pymemcache.client import base

client = base.Client(('localhost', 11211))
client.set('laptop', 'lenovo')
print(client.get('some_key'))

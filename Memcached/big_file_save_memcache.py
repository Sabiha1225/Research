#!/usr/bin/env python3

from pymemcache.client base
import pickle
import math

client = base.Client(('localhost', 11211))
chunk_size = 1000.0

def getLoopCount(size):
  return math.ceil(size/chunk_size)

def setFile(name, path):
  fileId = open(path, 'rb')
  size = len(fileId.read())
  fileId.seek(0)
  loopCount = int(getLoopCount(size))
  client.set(name, loopcount)
  
  for i in range (loopCount):
    data = fileId.read(int(chunk_size))
    client.set("%s%s%s" % (name, "_", str(i)), data)
    
def getFile(name):
  loopCount = int(client.get(name))
  fileData = ''
  
  for i in range(loopCount):
    data = client.get("%s%s%s" % (name, "_", str(i)))
    fileData = fileData + data
  
  return fileData

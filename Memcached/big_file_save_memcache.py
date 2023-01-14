#!/usr/bin/env python3

from pymemcache.client import base
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
  client.set(name, loopCount)
  
  for i in range (loopCount):
    data = pickle.dumps( fileId.read(int(chunk_size)) )
    client.set("%s%s%s" % (name, "_", str(i)), data)
  
  fileId.close()
    
def getFile(name):
  loopCount = int(client.get(name))
  fileData = b''
  
  for i in range(loopCount):
    data = client.get("%s%s%s" % (name, "_", str(i)))
    fileData = fileData + pickle.loads( data )
  
  return fileData


def main():
  fileName = 'decoder.layer_norm.bias'
  path = './decoder.layer_norm.bias'
  
  setFile(fileName, path)
  
  fileContent = getFile(fileName)
  print(fileContent)
  
  fileDes = open(path + 'test' , 'wb')
  fileDes.write(fileContent)
  fileDes.close()
  
if __name__ == '__main__':
  main()

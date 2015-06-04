__author__ = 'lataman'
import utilities

class scheme(object):
    def __init__(self):
        self.dict = {}

    def add(self,id, alg):
        if not utilities.hasValue(id):
            return
        if id in self.dict:
            self.dict[id].append(alg)
        else:
            self.dict[id] = [alg]

    def getMethod(self, id):
        if id in self.dict:
            return self.dict[id]
        return None

    def getAlg(self, id, iter = 0):
        if id in self.dict and len(self.dict[id]) > iter:
            return self.dict[id][iter]
        return None



def createObject():
    return scheme()
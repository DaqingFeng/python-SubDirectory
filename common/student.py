import sys, os
dir_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(dir_path + "/..")
from utils import helloWorld as instance


class student(object):
    """description of class"""
    Title=""

    def __init__(self, **kwargs):
       return super().__init__(**kwargs)
    
    def getStart(self):
        return instance.helloWorld.getTitle(instance.helloWorld,self.Title)
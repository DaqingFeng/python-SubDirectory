import sys, os
dir_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(dir_path + "/..")
from utils import helloWorld as helloworld


class student(object):
    """description of class"""
    hello=helloworld.helloWorld()
    Title=hello.Descrtion
    Response=""
    ResponseTwo=""
    RemarkPattern=""
    ExchangeStatus=False
    CommodityID=""
    startTime=None
    endTime=None
    def __init__(self, **kwargs):
       return super().__init__(**kwargs)

    def setCommodity(self,commodityId):
        self.CommodityID=commodityId

    def setstartTime(self,starttime):
        self.startTime=starttime

    def setendTime(self,endtime):
       self.endTime=endtime

    
    def setResponseTwo(self,responseTwo):
       self.ResponseTwo=responseTwo
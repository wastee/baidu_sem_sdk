# coding=utf-8
from ApiSDKJsonClient import *


class sms_service_CreativeService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'CreativeService')

    def updateCreative(self, updateCreativeRequest=None):
        return self.execute('updateCreative', updateCreativeRequest)

    def deleteCreative(self, deleteCreativeRequest=None):
        return self.execute('deleteCreative', deleteCreativeRequest)

    def addCreative(self, addCreativeRequest=None):
        return self.execute('addCreative', addCreativeRequest)

    def getCreative(self, getCreativeRequest=None):
        return self.execute('getCreative', getCreativeRequest)



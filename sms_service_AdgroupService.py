# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_AdgroupService(ApiSDKJsonClient):
    def __init__(self, token):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'AdgroupService',
                                  token)

    def addAdgroup(self, addAdgroupRequest=None):
        return self.execute('addAdgroup', addAdgroupRequest)

    def updateAdgroup(self, updateAdgroupRequest=None):
        return self.execute('updateAdgroup', updateAdgroupRequest)

    def deleteAdgroup(self, deleteAdgroupRequest=None):
        return self.execute('deleteAdgroup', deleteAdgroupRequest)

    def getAdgroup(self, getAdgroupRequest=None):
        return self.execute('getAdgroup', getAdgroupRequest)

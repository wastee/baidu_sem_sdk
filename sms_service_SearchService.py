# coding=utf-8
from ApiSDKJsonClient import *


class sms_service_SearchService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'SearchService')

    def getCountById(self, getCountByIdRequest=None):
        return self.execute('getCountById', getCountByIdRequest)

    def getTab(self, getTabRequest=None):
        return self.execute('getTab', getTabRequest)

    def getMaterialInfoBySearch(self, getMaterialInfoBySearchRequest=None):
        return self.execute('getMaterialInfoBySearch', getMaterialInfoBySearchRequest)

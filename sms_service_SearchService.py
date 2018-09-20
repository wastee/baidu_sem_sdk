# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_SearchService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'SearchService',
                                  token)

    def getCountById(self, getCountByIdRequest=None):
        return self.execute('getCountById', getCountByIdRequest)

    def getTab(self, getTabRequest=None):
        return self.execute('getTab', getTabRequest)

    def getMaterialInfoBySearch(self, getMaterialInfoBySearchRequest=None):
        return self.execute('getMaterialInfoBySearch',
                            getMaterialInfoBySearchRequest)

    def getKeywordIdBySearch(self, getKeywordIdBySearchRequest=None):
        return self.execute('getKeywordIdBySearch',
                            getKeywordIdBySearchRequest)

    def getCreativeIdBySearch(self, getCreativeIdBySearchRequest=None):
        return self.execute('getCreativeIdBySearch',
                            getCreativeIdBySearchRequest)

    def getIdsByTabs(self, getIdsByTabsRequest=None):
        return self.execute('getIdsByTabs', getIdsByTabsRequest)

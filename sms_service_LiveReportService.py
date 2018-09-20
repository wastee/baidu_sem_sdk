# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_LiveReportService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'LiveReportService',
                                  token)

    def getAccountLiveData(self, getAccountLiveDataRequest=None):
        return self.execute('getAccountLiveData', getAccountLiveDataRequest)

    def getKeywordLiveData(self, getKeywordLiveDataRequest=None):
        return self.execute('getKeywordLiveData', getKeywordLiveDataRequest)

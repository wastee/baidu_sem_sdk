# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_AccountService(ApiSDKJsonClient):
    def __init__(self, token):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'AccountService',
                                  token)

    def getAccountInfo(self, getAccountInfoRequest=None):
        return self.execute('getAccountInfo', getAccountInfoRequest)

    def updateAccountInfo(self, updateAccountInfoRequest=None):
        return self.execute('updateAccountInfo', updateAccountInfoRequest)

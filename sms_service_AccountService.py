from ApiSDKJsonClient import *


class sms_service_AccountService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'AccountService')

    def getAccountInfo(self, getAccountInfoRequest=None):
        return self.execute('getAccountInfo', getAccountInfoRequest)

    def updateAccountInfo(self, updateAccountInfoRequest=None):
        return self.execute('updateAccountInfo', updateAccountInfoRequest)

# coding=utf-8
from ApiSDKJsonClient import *


class sms_service_ToolkitService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'ToolkitService')

    def getOperationRecord(self, getOperationRecordRequest=None):
        return self.execute('getOperationRecord', getOperationRecordRequest)

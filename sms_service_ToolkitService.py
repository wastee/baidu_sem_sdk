# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_ToolkitService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'ToolkitService',
                                  token)

    def getOperationRecord(self, getOperationRecordRequest=None):
        return self.execute('getOperationRecord', getOperationRecordRequest)

# coding=utf-8
from ApiSDKJsonClient import *


class sms_service_ReportService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'ReportService')

    def getRealTimeQueryData(self, getRealTimeQueryDataRequest=None):
        return self.execute('getRealTimeQueryData', getRealTimeQueryDataRequest)

    def getRealTimePairData(self, getRealTimePairDataRequest=None):
        return self.execute('getRealTimePairData', getRealTimePairDataRequest)

    def getProfessionalReportId(self, getProfessionalReportIdRequest=None):
        return self.execute('getProfessionalReportId', getProfessionalReportIdRequest)

    def getReportState(self, getReportStateRequest=None):
        return self.execute('getReportState', getReportStateRequest)

    def getReportFileUrl(self, getReportFileUrlRequest=None):
        return self.execute('getReportFileUrl', getReportFileUrlRequest)

    def getRealTimeData(self, getRealTimeDataRequest=None):
        return self.execute('getRealTimeData', getRealTimeDataRequest)

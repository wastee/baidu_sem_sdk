from ApiSDKJsonClient import *


class sms_service_LiveReportService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'LiveReportService')

    def getAccountLiveData(self, getAccountLiveDataRequest=None):
        return self.execute('getAccountLiveData', getAccountLiveDataRequest)

    def getKeywordLiveData(self, getKeywordLiveDataRequest=None):
        return self.execute('getKeywordLiveData', getKeywordLiveDataRequest)


if __name__ == '__main__':
    service = sms_service_LiveReportService()
    result = service.getAccountLiveData({
        'dataType': 2,
        'device': 0,
    })
    print(result)

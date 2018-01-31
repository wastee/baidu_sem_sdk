# coding=utf-8
from ApiSDKJsonClient import *


class sms_service_BulkJobService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'BulkJobService')

    def getAllChangedObjects(self, getAllChangedObjectsRequest=None):
        return self.execute('getAllChangedObjects', getAllChangedObjectsRequest)

    def cancelDownload(self, cancelDownloadRequest=None):
        return self.execute('cancelDownload', cancelDownloadRequest)

    def getChangedItemId(self, getChangedItemIdRequest=None):
        return self.execute('getChangedItemId', getChangedItemIdRequest)

    def getChangedScale(self, getChangedScaleRequest=None):
        return self.execute('getChangedScale', getChangedScaleRequest)

    def getAllObjects(self, getAllObjectsRequest=None):
        return self.execute('getAllObjects', getAllObjectsRequest)

    def getFileStatus(self, getFileStatusRequest=None):
        return self.execute('getFileStatus', getFileStatusRequest)

    def getFilePath(self, getFilePathRequest=None):
        return self.execute('getFilePath', getFilePathRequest)

    def getChangedId(self, getChangedIdRequest=None):
        return self.execute('getChangedId', getChangedIdRequest)

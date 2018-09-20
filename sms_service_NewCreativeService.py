# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_NewCreativeService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'NewCreativeService',
                                  token)

    def addBridge(self, addBridgeRequest=None):
        return self.execute('addBridge', addBridgeRequest)

    def addSublink(self, addSublinkRequest=None):
        return self.execute('addSublink', addSublinkRequest)

    def updateSublink(self, updateSublinkRequest=None):
        return self.execute('updateSublink', updateSublinkRequest)

    def deleteSublink(self, deleteSublinkRequest=None):
        return self.execute('deleteSublink', deleteSublinkRequest)

    def addPhone(self, addPhoneRequest=None):
        return self.execute('addPhone', addPhoneRequest)

    def updatePhone(self, updatePhoneRequest=None):
        return self.execute('updatePhone', updatePhoneRequest)

    def updateBridge(self, updateBridgeRequest=None):
        return self.execute('updateBridge', updateBridgeRequest)

    def addEcall(self, addEcallRequest=None):
        return self.execute('addEcall', addEcallRequest)

    def updateEcall(self, updateEcallRequest=None):
        return self.execute('updateEcall', updateEcallRequest)

    def getSublink(self, getSublinkRequest=None):
        return self.execute('getSublink', getSublinkRequest)

    def getBridge(self, getBridgeRequest=None):
        return self.execute('getBridge', getBridgeRequest)

    def getPhone(self, getPhoneRequest=None):
        return self.execute('getPhone', getPhoneRequest)

    def getEcall(self, getEcallRequest=None):
        return self.execute('getEcall', getEcallRequest)

    def getEcallGroup(self, getEcallGroupRequest=None):
        return self.execute('getEcallGroup', getEcallGroupRequest)

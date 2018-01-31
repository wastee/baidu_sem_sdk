from ApiSDKJsonClient import *


class sms_service_CampaignService(ApiSDKJsonClient):
    def __init__(self):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'CampaignService')

    def getCampaign(self, getCampaignRequest=None):
        return self.execute('getCampaign', getCampaignRequest)

    def addCampaign(self, addCampaignRequest=None):
        return self.execute('addCampaign', addCampaignRequest)

    def updateCampaign(self, updateCampaignRequest=None):
        return self.execute('updateCampaign', updateCampaignRequest)

    def deleteCampaign(self, deleteCampaignRequest=None):
        return self.execute('deleteCampaign', deleteCampaignRequest)

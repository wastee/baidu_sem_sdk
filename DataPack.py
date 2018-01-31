class DataPack():
    header = None
    body = None

    def __init__(self, aheader=None, abody=None):
        self.header = aheader
        self.body = abody

    def setHeader(self, header):
        self.header = header

    def setBody(self, body):
        self.body = body
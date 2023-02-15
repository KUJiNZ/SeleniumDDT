import json


class Utilities(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def getJsonData(self):
        return json.load(open(self.filepath))

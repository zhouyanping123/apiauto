import json

class getValueTool():#获取response里的值
    @staticmethod
    def getvalue(param, keys):
        dictr = json.loads(param)
        keylist = keys.split(".")
        keylen = len(keylist)
        if keylen == 1:
            return dictr[keys]
        else:
            for keys in keylist:
                dictr = dictr[keys]
            return dictr
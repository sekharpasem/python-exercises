

class String_Utils(object):

    @classmethod
    def replace(cls, index1, index2, mainstring, replacementstring):
        return mainstring.replace(mainstring[index1:index2], replacementstring)
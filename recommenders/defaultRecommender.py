__author__ = 'zhanyang'

class defaultRecommender(object):

    def __rankRecommender(self, userid):
        pass

    def recommend(self, userid):
        recommeddict = self.__rankRecommender(userid)
        return recommeddict.keys()

    def recommendTopK(self, userid, k):
        recommenddict = self.__rankRecommender(userid)
        if len(recommenddict) > k:
            return [element[0] for element in recommenddict[:k]]
        else:
            return [element[0] for element in recommenddict]

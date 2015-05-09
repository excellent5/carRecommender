__author__ = 'zhanyang'

class defaultRecommender(object):

    def recommend(self, userid):
        recommeddict = self.rankRecommender(userid)
        return recommeddict.keys()

    def recommendTopK(self, userid, k):
        recommenddict = self.rankRecommender(userid)
        if len(recommenddict) > k:
            return [element[0] for element in recommenddict[:k]]
        else:
            return [element[0] for element in recommenddict]

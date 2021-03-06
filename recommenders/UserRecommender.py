__author__ = 'zhanyang'

from similarities.UserSimilarity import UserSimilarity
import operator
from defaultRecommender import defaultRecommender

class UserRecommender(defaultRecommender):

    def __init__(self, usersimilarity, useritemdict):
        defaultRecommender.__init__(self)
        self.similarity = None
        if not isinstance(usersimilarity, UserSimilarity):
            raise Exception("Please give UserSimilarity object")
        self.similarity = usersimilarity.similarity
        self.itemdict = useritemdict

    def rankRecommender(self, userid):
        recommenddict = {}
        if userid not in self.similarity:
            # raise Exception("this user doesn't exist")
            return []
        for neighbour in self.similarity[userid]:
            if neighbour in self.itemdict:
                for car in self.itemdict[neighbour]:
                    if userid in self.itemdict and car not in self.itemdict[userid]:
                        recommenddict[car] = self.itemdict[neighbour][car] * self.similarity[userid][
                            neighbour] + 0 if car not in recommenddict else recommenddict[car]
        return sorted(recommenddict.items(), key=operator.itemgetter(1), reverse=True)

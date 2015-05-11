__author__ = 'zhanyang'

from similarities.ItemSimilarity import ItemSimilarity
import operator
from defaultRecommender import defaultRecommender

class ItemRecommender(defaultRecommender):
    def __init__(self, itemsimilarity, useritemdict):
        self.similarity = None
        if not isinstance(itemsimilarity, ItemSimilarity):
            raise Exception("Please give UserSimilarity object")
        self.similarity = itemsimilarity.similarity
        self.itemdict = useritemdict

    def rankRecommender(self, userid):
        recommenddict = {}
        if userid not in self.itemdict:
            # raise Exception("this user doesn't exist")
            return []
        for car in self.itemdict[userid]:
            if car in self.similarity:
                for similarcar in self.similarity[car]:
                    if similarcar not in self.itemdict[userid]:
                        recommenddict[similarcar] = self.similarity[car][similarcar] * self.itemdict[userid][
                            car] + 0 if similarcar not in recommenddict else recommenddict[similarcar]
        return sorted(recommenddict.items(), key=operator.itemgetter(1), reverse=True)


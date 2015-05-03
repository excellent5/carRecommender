__author__ = 'zhanyang'

from similarities import ItemSimilarity
import operator
import defaultRecommender

class ItemRecommender(defaultRecommender):
    def __init__(self, itemsimilarity, useritemdict):
        self.similarity = None
        if not isinstance(itemsimilarity, ItemSimilarity):
            raise Exception("Please give UserSimilarity object")
        self.similarity = itemsimilarity
        self.itemdict = useritemdict

    def __rankRecommender(self, userid):
        recommenddict = {}
        if userid not in self.itemdict:
            # raise Exception("this user doesn't exist")
            return []
        for car in self.itemdict[userid]:
            if car in self.similarity:
                for similarcar in self.similarity[car]:
                    if similarcar not in self.itemdict[userid]:
                        recommenddict[car] = self.similarity[car][similarcar] * self.itemdict[userid][
                            car] + 0 if car not in recommenddict else recommenddict[car]
        return sorted(recommenddict.items(), key=operator.itemgetter(1), reverse=True)


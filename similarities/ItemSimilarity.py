__author__ = 'zhanyang'

from metrics.calSimilarity import EuclideanDistance, distance2similarity

class ItemSimilarity(object):

    def __init__(self, itemfeaturedict):
        self.similarity = self.__calSimilarityByItem(itemfeaturedict)

    # itemfeaturedict is like {item1: [gearbox, islocal, price], ...}
    # similarity is like {item1: {item2: similarity, ...},
    def __calSimilarityByItem(self, itemfeaturedict):
        similarity = {}
        for item in itemfeaturedict:
            similarity[item] = {}
            for otheritem in itemfeaturedict:
                if item == otheritem:
                    continue
                else:
                    similarity[item][otheritem] = distance2similarity(EuclideanDistance(itemfeaturedict[item],
                                                                                        itemfeaturedict[otheritem]))
        return similarity





__author__ = 'zhanyang'

from metrics.calSimilarity import CosineSimilarity
from utils.fileHandler import getUserFeature
import pickle
import operator

class UserSimilarity(object):

    def __init__(self, **kwargs):
        self.similarity = None
        for name, value in kwargs.items():
            if name == "useritemdict":
                self.similarity = self.__calSimilarityByCF(value)
            elif name == "userfeaturecsv":
                self.similarity = self.__calSimilarityByNormalizedDistance(value)
            elif name == "usersimilaritypickle":
                self.similarity = self.__calSimilarityByPickle(value)
            elif name == "usersimilaritydict":
                self.similarity = value

    def __calSimilarityByCF(self, useritemdict):
        usersimilarity = {}
        for user in useritemdict:
            usersimilarity[user] = {}
            for otheruser in useritemdict:
                if otheruser == user:
                    continue
                useritems = set(useritemdict[user].keys())
                otheruseritems = set(useritemdict[otheruser].keys())
                intersectionitems = useritems.intersection(otheruseritems)
                if len(intersectionitems) != 0:
                    cossim = CosineSimilarity(useritemdict[user], useritemdict[otheruser])
                    usersimilarity[user][otheruser] = cossim
        return usersimilarity

    def __calSimilarityByNormalizedDistance(self, filepath):
        return getUserFeature(filepath)

    def __calSimilarityByPickle(self, filepath):
        return pickle.load(open(filepath, "rb"))

    def cutKNN(self, k):
        for user in self.similarity:
            if len(self.similarity[user]) > k:
                # use top K as neighbour
                self.similarity[user] = dict(sorted(self.similarity[user].items(), key=operator.itemgetter(1), \
                    reverse=True)[:k])

    # return the K Nearest Neighbour of user, format is like: {neighbour1: similarity1, neighbour2: similarity2, ...}
    def getUserKNN(self, user, k):
        if len(self.similarity[user]) > k:
            return dict(sorted(self.similarity[user].items(), key=operator.itemgetter(1), reverse=True)[:k])
        else:
            return self.similarity[user]

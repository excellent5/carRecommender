__author__ = 'zhanyang'

from utils.fileHandler import getUserRentItem
from similarities.UserSimilarity import UserSimilarity
from recommenders.UserRecommender import UserRecommender

if __name__ == "__main__":
    filedir = "/Users/zhanyang/Documents/atzuche/"
    useritemdict = getUserRentItem(filedir + "trainingdata.csv")
    usersimilarity = UserSimilarity(useritemdict=useritemdict)
    userrecommender = UserRecommender(usersimilarity, useritemdict)
    print userrecommender.recommendTopK(4149073, 5)

__author__ = 'zhanyang'

import csv
import random
from metrics.calSimilarity import EuclideanDistance, distance2similarity
from dataprepocessor.normalizer import normalizeCarInfo

# useritemdict is like {userID: {carID: times, ...}, ...}
def getUserRentItem(filepath):
    useritemdict = {}
    with open(filepath, "r") as infile:
        csvreader = csv.DictReader(infile)
        for row in csvreader:
            renter, car = int(row["member_no"]), int(row["car_no"])
            if renter not in useritemdict:
                useritemdict[renter] = {car: 1}
            else:
                useritempreference = useritemdict[renter]
                if car in useritempreference:
                    useritempreference[car] += 1
                else:
                    useritempreference[car] = 1
    return useritemdict


# user distance is like {user1: {user2: distance}}
def getUserFeature(filepath):
    userfeature = {}
    userdistance = {}
    with open(filepath, "r") as infile:
        csvreader = csv.DictReader(infile)
        for row in csvreader:
            distances = {}
            features = [float(row["care_for_autogear"]), float(row["nocare_for_local"]), float(row["avg_seat"]),
                        float(row["year"]), float(row["rent_time"]), float(row["price"])]
            currentuser = int(row["reg_no"])
            for user in userfeature:
                distances[user] = distance2similarity(EuclideanDistance(features, userfeature[user]))
            userfeature[currentuser] = features
            userdistance[currentuser] = distances
    return userdistance


def getItemFeature(filepath):
    itemfeaturedict = {}
    with open(filepath, "r") as infile:
        csvreader = csv.DictReader(infile)
        for row in csvreader:
            car_no = int(row["car_no"])
            features = normalizeCarInfo(row)
            # features = [int(row["gearbox_type"]) - 1, int(row["is_local"]) - 1, float(row["day_price"])/2000]
            itemfeaturedict[car_no] = features
    return itemfeaturedict


def prepareTrainingTestingData(dir, originalfilepath, shuffle=True):
    with open(originalfilepath, "r") as infile:
        content = list(csv.reader(infile))
    header = content[0]
    data = content[1:]
    if shuffle:
        random.shuffle(data)
    splitproportion = 0.7
    splitlinenumber = int(len(data) * splitproportion)
    trainningdata = data[:splitlinenumber]
    testingdata = data[splitlinenumber:]
    with open(dir + "trainingdata.csv", "wb") as outfile:
        csv.writer(outfile).writerows([header] + trainningdata)
    with open(dir + "testingdata.csv", "wb") as outfile:
        csv.writer(outfile).writerows([header] + testingdata)


if __name__ == "__main__":
    prepareTrainingTestingData("/Users/zhanyang/Documents/atzuche/",
                               "/Users/zhanyang/Documents/atzuche/transaction_request.csv")
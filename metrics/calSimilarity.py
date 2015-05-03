__author__ = 'zhanyang'

from math import exp

def EuclideanSimilarity(a, b):
    sum = 0
    for i in range(len(a)):
        sum+=(a[i]-b[i])**2
    return exp(sum**0.5*-1)

def CosineSimilarity(dict1, dict2):
    intersectionsum, dict1sum, dict2sum = 0, 0, 0
    for item in dict1:
        dict1sum += dict1[item] ** 2
        if item in dict2:
            intersectionsum += dict1[item] * dict2[item]
    for item in dict2:
        dict2sum += dict2[item] ** 2
    return intersectionsum / (dict1sum ** 0.5 * dict2sum ** 0.5)


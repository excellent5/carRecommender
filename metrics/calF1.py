__author__ = 'zhanyang'


def F1(predict, fact):
    f1score = -1
    if len(predict) != 0:
        intersection = set(fact).intersection(set(predict))
        if len(intersection) != 0:
            precision = 1.0 * len(intersection) / len(predict)
            recall = 1.0 * len(intersection) / len(fact)
            f1score = 2 * precision * recall / (precision + recall)
    else:
        f1score = 0
    return f1score


def marcoF1(predicts, facts):
    predictnum = 0
    f1scoresum = 0
    if len(predicts) != len(facts):
        raise Exception("You don't input equal number of predict and fact")
    else:
        for i in range(len(predicts)):
            f1score = F1(predicts[i], facts[i])
            if f1score >= 0:
                predictnum += 1
                f1scoresum += f1score
        return 1.0 * f1scoresum / predictnum
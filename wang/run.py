import math

population = []

def f(feature):


def p(feature):
    sum += 0
    for value in population:
        sum += f(feature)
    return f(feature) / sum

def uncertainty_h(features):
    sum = 0
    for feature in features:
        sum += p(feature) * math.log(p(feature))
    return sum * -1

def uncertainty_h2(featuresi, featuresj):
    sumj = 0
    for feature in featuresj:
        sumj += p(feature)
    return sum * -1
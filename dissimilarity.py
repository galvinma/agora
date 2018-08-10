# Dissimilarity score
# Pass in two lists and compare similarity
# Scores from 0 --> m, where m is the number of total attributes
#
def dissimilarity(a,b):
    if len(a) != len (b):
        return -1
    score = 0
    for i,j in zip(a,b):
        if i == j:
            score += 1
    return score

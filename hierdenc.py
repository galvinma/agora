#
# HIERDENC function
#
def cluster(classes, attributes):
    # Initial conditions
    print("Entering HIERDENC function...")
    r = 1       # radius of hypercubes
    k = 0       # number of leaf clusters
    kr = 0      # number of clusters at level r
    clusters = {}
    proceed = true


    

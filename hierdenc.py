from index import hierdenc_index
#
# HIERDENC function
#
def cluster(objects):
    # Initial conditions
    print("Entering HIERDENC function...")
    r = 1       # radius of hypercubes
    k = 0       # number of leaf clusters
    kr = 0      # number of clusters at level r
    clusters = {}
    proceed = bool(1)

    index, dissimilarity_matrix = hierdenc_index(objects, r)

    for k,v in index.items():
        print(str(k)+" "+str(v))
    #
    # while proceed = true:
    #     r = r + 1       # increase radius

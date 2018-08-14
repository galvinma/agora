import csv
from hierdenc import hierdenc
# Place data into map
# {object ID : [NAME, Attributes...]}
#
objects = {}
count = 0
print("Initializing data...")
with open("datasets/soybean-small.data", mode= "r") as f:
    lines = csv.reader(f)
    for line in lines:
        objects[count] = line
        count += 1

clusters, mode_lookup = hierdenc(objects)

for k,v in clusters.items():
    print("Iteration: " + str(k))
    for a,b in v.items():
        print(str(a) + ":" + str(b))

for k,v in mode_lookup.items():
    print(str(k) + ":" + str(v))

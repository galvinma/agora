import csv
from hierdenc import hierdenc
# Place data into map
# {object ID : [NAME, Attributes...]}
#
objects = {}
count = 0
print("Initializing data...")
with open("datasets/soybean-large.data", mode= "r") as f:
    lines = csv.reader(f)
    for line in lines:
        objects[count] = line
        count += 1

clusters = hierdenc(objects)

for k,v in clusters.items():
    print("Iteration: " + str(k))
    for a,b in v.items():
        print(str(a) + ":" + str(b))

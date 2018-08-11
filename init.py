import csv
from hierdenc import hierdenc
# Place data into map
# {object ID : [NAME, Attributes...]}
#
objects = {}
count = 0
with open("datasets/soybean-large.data", mode= "r") as f:
    lines = csv.reader(f)
    for line in lines:
        objects[count] = line
        count += 1

clusters = hierdenc(objects)

for k,v in clusters.items():
    for a,b in v.items():
        print("Key: " + str(a) + " Value: " + str(b))

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

# Print dictionary
# for k,v in objects.items():
#     print("Key: " + str(k) + " , and Value: " + str(v))

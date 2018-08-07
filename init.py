import csv

# Place data into map
classes = []
attributes = []
with open("datasets/soybean-large.data", mode= "r") as f:
    lines = csv.reader(f)
    for line in lines:
        classes.append(line[0])
        attributes.append(line[1:])

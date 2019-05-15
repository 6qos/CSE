import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    for row in reader:
        thing = row[13]
        # print(thing)
        fruit = row[2]
        # print(fruit)
        if fruit == "Fruits":
            print(thing)
            # print(fruit)
            
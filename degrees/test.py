import csv
import sys

names = {}
print(type(names))
people = {}
print(type(people))

with open(f"small/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                print(row["name"].lower())
                print(names[row["name"].lower()])
                names[row["name"].lower()].add(row["id"])
                print(names[row["name"].lower()])


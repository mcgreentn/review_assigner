import csv
import random

class Assigner:
    def __init__(self, file_loc):
        self.read_in_groups(file_loc)

    def read_in_groups(self, file_loc):
        with open(file_loc) as f:
            groups = f.read().splitlines()
        self.groups = groups
    
    def assign_reviews(self, reviews_per_group=3):
        groups = self.groups
        random.shuffle(groups)
        csv_format = []
        for i, group in enumerate(groups):
            reviews = [groups[(i+x) % len(groups)] for x in range(1, reviews_per_group+1)]
            print(f"{group}: {reviews}")
            row = [group] + reviews
            csv_format.append(row)
        



if __name__ == "__main__": 
    assigner = Assigner("input/groups.txt")
    assigner.assign_reviews()
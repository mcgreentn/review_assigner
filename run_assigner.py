from review_assigner.src.assigner import Assigner

assigner = Assigner("input/groups.txt")
assigner.assign_reviews(output_loc="output.csv")
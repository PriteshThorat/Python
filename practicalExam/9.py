'''
Program for set operations
    a) Union
    b) Intersection
    c) Difference
    d) Symmetric difference
'''

set1 = {1, 5, 7, 4, 6}
set2 = {4, 6, 3, 5, 1}

union = set1.union(set2)
inter = set1.intersection(set2)
diff = set1.difference(set2)
symdiff = set1.symmetric_difference(set2)

print(f"The Union of {set1} and {set2} is {union}")
print(f"The Intersection of {set1} and {set2} is {inter}")
print(f"The Difference of {set1} and {set2} is {diff}")
print(f"The Symmetric Difference of {set1} and {set2} is {symdiff}")
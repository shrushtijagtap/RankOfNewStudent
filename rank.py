# There is a classroom with a bunch of students in it. There is an entrance exam to be part of this classroom.

# A bunch of students have already given this exam.
# The ranking of the students is based on the marks they receive.

# For the class:
# Marks = {39, 38, 38, 36, 34, 31, 28}

# Ranking would be:
# 39 = 1
# 38 = 2
# 38 = 2
# 36 = 3
# .
# .
# A new student wants to join the class. That student gives the entrance test, the marks are x.

# Write a program, that will print the rank of this new student in the given class.
# void printRank {ArrayList<Integer> currentMarksOfClass, int newCandidateMark) {
# 	// TODO
# }

# So if the parameters are:  
# - {39, 38, 38, 36, 34, 31, 28}, 38: It should return 2

# - {39, 38, 38, 36, 34, 31, 28}, 37: It should return 3

def find_rank(arr, key):
    temp=0
    rank=0

    if arr[0]<=key:
        return 1

    for i in arr:
        if i > key and i!=temp:
            temp=i
            rank+=1
       
    return rank+1


currentMarksOfClass=[39, 38, 38, 36, 34, 31, 28]
print(find_rank(currentMarksOfClass, 35))

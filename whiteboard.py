# How to solve a problem:
#     Figure out wher the input and its type are
#     Set up a function
#     Figure out what the output and its type are
#     Gather your Knowledge
#     Gathers your contraints (Not Always Necessary)
#     Determine a Logical way to solve the problem
#         Write each step out in English
#         Write each step out in Python-esse (sudo-code)
#     Invike and Test your function

# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
test = ["PPALLP", "PPALLL"]


def check_award(s:str) -> bool:
    absent = 0
    late = 0

    for cou in s:
        if cou == "A":
            absent += 1
            late = 0
        elif cou == "L":
            late += 1
            if late == 3:
                return False
        else:
            late = 0
    if absent >= 2:
        return False
    
    return True

answer = [check_award(a) for a in test]
print(answer)


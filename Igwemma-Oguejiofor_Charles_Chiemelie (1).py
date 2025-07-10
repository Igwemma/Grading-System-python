# Name: Igwemma-Oguejiofor Charles Chiemelie
# Reg num: 2024554064
# Dept: Statistics
# Faculty: Physical Sciences
# Course: COS 102

# Grading System Program

def grade_student(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score <= 69:
        return 'B'
    elif 50 <= score <= 59:
        return 'C'
    elif 40 <= score <= 49:
        return 'D'
    elif 0 <= score <= 39:
        return 'F'
    else:
        return 'Invalid score'

# Example usage
score = int(input("Enter your score: "))
grade = grade_student(score)
print("Your grade is:", grade)

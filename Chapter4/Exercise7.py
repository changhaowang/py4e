#Exercise 7 Page 61
def computegrade(score):
    try:
        score = float(score)
        if 0 <= score <= 0.6:
            return "F"
        elif 0.6 < score <= 0.7:
            return "D"
        elif 0.7 < score <= 0.8:
            return "C"
        elif 0.8 < score <= 0.9:
            return "B"
        elif 0.9 < score <= 1:
            return "A"
        else:
            return "Bad score"
    except:
        return ("Error, please enter numeric number.")


inp_score = input("Please enter your score: ")
grade = computegrade(inp_score)
print(grade)

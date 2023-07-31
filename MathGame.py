questions = ["2 * (6/2)", "2 * 9 - 6 + 1", "167 + 222 - 57" , "62 + (30 * 33)", "231 / 8"]

answers = ['6', '13', '332', '1052', '28.875']

def mathgame():
    print("WELCOME TO THE MATH GAME!")
    score = 0
    for q in range(len(questions)):
        print(questions[q])
        ans = input("Enter answer here: \n") 
        if ans == answers[q]:
            print("CORRECT")
            score += 1
        else:
            print("INCORRECT")
    print("Questions You Got Correct: " + str(score) + "!")
    return q

mathgame()
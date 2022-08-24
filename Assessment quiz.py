from operator import contains


print("Welcome to the music production quiz!")

#determine quiz length
while True:
    quizlength = input("What length do you want the quiz to be? (short, medium, long) ")
    quizlength = quizlength.strip()
    quizlength = quizlength.lower()
    if quizlength == "short" or quizlength == "s":
        endtotal = 5
        quizlength = "short"
        break
    elif quizlength == "medium" or quizlength == "m":
        endtotal = 10
        quizlength = "medium"
        break
    elif quizlength == "long" or quizlength == "l":
        endtotal = 15
        quizlength = "long"
        break
    else:
        print("Invalid answer")

print("You have selected the {} quiz".format(quizlength))

#variables
answers = []
qnum = 0
qcorrect = 0

#question one (S, M, L)
qnum += 1
guesses = 3
while guesses > 0:
    q1answer = input("""Question {}: 
[type: q1] """.format(qnum))
    q1answer = q1answer.strip()
    q1answer = q1answer.lower()
#check if answer is correct
    if q1answer == "q1":
        qcorrect += 1
        print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
        break
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining.".format(guesses))
answers.append(q1answer)

#question two (M, L)
if "medium" in quizlength or "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q2answer = input("""Question {}: 
[type: q2] """.format(qnum))
        q2answer = q2answer.strip()
        q2answer = q2answer.lower()
#check if answer is correct
        if q2answer == "q2":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q2answer)

#question three (L)
if "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q3answer = input("""Question {}: 
[type: q3] """.format(qnum))
        q3answer = q3answer.strip()
        q3answer = q3answer.lower()
#check if answer is correct
        if q3answer == "q3":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q3answer)

#question four (S, M, L)
qnum += 1
guesses = 3
while guesses > 0:
    q4answer = input("""Question {}: 
[type: q4] """.format(qnum))
    q4answer = q4answer.strip()
    q4answer = q4answer.lower()
#check if answer is correct
    if q4answer == "q4":
        qcorrect += 1
        print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
        break
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining.".format(guesses))
answers.append(q4answer)

#question five (M, L)
if "medium" in quizlength or "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q5answer = input("""Question {}: 
[type: q5] """.format(qnum))
        q5answer = q5answer.strip()
        q5answer = q5answer.lower()
#check if answer is correct
        if q5answer == "q5":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q5answer)

#question six (L)
if "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q6answer = input("""Question {}: 
[type: q6] """.format(qnum))
        q6answer = q6answer.strip()
        q6answer = q6answer.lower()
#check if answer is correct
        if q6answer == "q6":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q6answer)

    #question seven (S, M, L)
qnum += 1
guesses = 3
while guesses > 0:
    q7answer = input("""Question {}: 
[type: q7] """.format(qnum))
    q7answer = q7answer.strip()
    q7answer = q7answer.lower()
#check if answer is correct
    if q7answer == "q7":
        qcorrect += 1
        print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
        break
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining.".format(guesses))
answers.append(q7answer)

#question eight (M, L)
if "medium" in quizlength or "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q8answer = input("""Question {}: 
[type: q8] """.format(qnum))
        q8answer = q8answer.strip()
        q8answer = q8answer.lower()
#check if answer is correct
        if q8answer == "q8":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q8answer)

#question nine (L)
if "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q9answer = input("""Question {}: 
[type: q9] """.format(qnum))
        q9answer = q9answer.strip()
        q9answer = q9answer.lower()
#check if answer is correct
        if q9answer == "q9":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q9answer)

    #question ten (S, M, L)
qnum += 1
guesses = 3
while guesses > 0:
    q10answer = input("""Question {}: 
[type: q10] """.format(qnum))
    q10answer = q10answer.strip()
    q10answer = q10answer.lower()
#check if answer is correct
    if q10answer == "q10":
        qcorrect += 1
        print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
        break
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining.".format(guesses))
answers.append(q10answer)

#question eleven (M, L)
if "medium" in quizlength or "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q11answer = input("""Question {}: 
[type: q11] """.format(qnum))
        q11answer = q11answer.strip()
        q11answer = q11answer.lower()
#check if answer is correct
        if q11answer == "q11":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q11answer)

#question twelve (L)
if "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q12answer = input("""Question {}: 
[type: q12] """.format(qnum))
        q12answer = q12answer.strip()
        q12answer = q12answer.lower()
#check if answer is correct
        if q12answer == "q12":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q12answer)

        #question thirteen (S, M, L)
qnum += 1
guesses = 3
while guesses > 0:
    q13answer = input("""Question {}: 
[type: q13] """.format(qnum))
    q13answer = q13answer.strip()
    q13answer = q13answer.lower()
#check if answer is correct
    if q13answer == "q13":
        qcorrect += 1
        print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
        break
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining.".format(guesses))
answers.append(q13answer)

#question fourteen (M, L)
if "medium" in quizlength or "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q14answer = input("""Question {}: 
[type: q14] """.format(qnum))
        q14answer = q14answer.strip()
        q14answer = q14answer.lower()
#check if answer is correct
        if q14answer == "q14":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q14answer)

#question fifteen (L)
if "long" in quizlength:
    qnum += 1
    guesses = 3
    while guesses > 0:
        q15answer = input("""Question {}: 
[type: q15] """.format(qnum))
        q15answer = q15answer.strip()
        q15answer = q15answer.lower()
#check if answer is correct
        if q15answer == "q15":
            qcorrect += 1
            print("Correct! You have answered {} questions correctly so far.".format(qcorrect))
            break
        else:
            guesses -= 1
            print("Incorrect, you have {} guesses remaining.".format(guesses))
    answers.append(q15answer)

#ask to view answers
while True:
    viewanswers = input("Do you want to view your answers? (y/n) ")
    viewanswers = viewanswers.strip()
    viewanswers = viewanswers.lower()
    if viewanswers == "y" or viewanswers == "yes":
        #make sure the answers are appropriate to the quiz length
        if "short" in quizlength:
            print("Your answers were: {}, {}, {}".format(answers[0], answers[1], answers[2], answers[3], answers[4]))
        elif "medium" in quizlength:
            print("Your answers were: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5], answers[6], answers[7], answers[8], answers[9]))
        elif "long" in quizlength:
            print("Your answers were: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5], answers[6], answers[7], answers[8], answers[9], answers[10], answers[11], answers[12], answers[13], answers[14]))
        else:
            print("Error: could not find answers.")
        break
    elif viewanswers == "n" or viewanswers == "no":
        break
    else:
        print("Invalid answer. Please only answer with yes or no.")

#quiz end message
print("""Thank you for playing this quiz!
You answered {}/{} questions correctly!""".format(qcorrect, endtotal))
if qcorrect == 0:
    print("Better luck next time!")
elif qcorrect == endtotal:
    print("Great job!")
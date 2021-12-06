import random
import termcolor
import time
import playsound

# Function Library

def randomGreeting():
    greetingNum = random.randint(0,5)
    greetingsList = open("greetings.txt")
    readLine = greetingsList.readlines()
    print(readLine[greetingNum], end="")
    return

def line():
    print("-----")
    return

def funGame(funCount):
    if funCount.lower() == "yes":
        print("Great to hear!")
    elif funCount.lower() == "no":
        print("Well thats too bad, but give this game a try.")
    else:
        print("I do not understand what you mean, but I'll assume you are having a decent day.")

def challenge1():
    print("Task One:\nBuy some ice cream for your dad.")
    line()
    print("You are on the edge of the pool, and as you look up, you see your dad sweating on the lounge chair to your left.")
    action1 = input("You got out of the pool, and are standing between your dad and the ice cream truck. \nWhere will you go? (Dad/Ice cream truck/Pool)\n")
    while "dad" not in action1.lower():
        while "pool" in action1.lower():
            message = "You jumped back into the pool, but you thought about your dad there, clearly uncomfortable in the blazing sun."
            printString = termcolor.colored(message, "red")
            print(printString)
            action1 = input("You climbed out of the pool again, and are once again standing between your dad and the ice cream truck. \nWhere will you go? (Dad/Ice cream truck/Pool)\n")
        while "truck" in action1.lower() or "ice cream" in action1.lower():
            message = "You approached the ice cream truck, and as you were about to order an ice cream cone, you checked in your pocket and realized you have no money."
            printString = termcolor.colored(message, "red")
            print(printString)
            action1 = input("After embarrassingly walking away from the ice cream truck, you are back in the middle between the ice cream truck and your dad. \nWhere will you go now? (Dad/Ice cream truck/Pool)\n")
        while "ice cream" not in action1.lower() and "pool" not in action1.lower() and "truck" not in action1.lower() and "dad" not in action1.lower():
            message = "I do not know what that means."
            printString = termcolor.colored(message, "yellow")
            print(printString)
            action1 = input("You are still standing between your dad and the ice cream truck. \nWhere will you go? (Dad/Ice cream truck/Pool)\n")
    message = "You approached your dad and asked if he may spare some money for an ice cream, he agrees and gives you enough for only one ice cream."
    printString = termcolor.colored(message, "green")
    print(printString)
    action2 = input("You run back to the ice cream truck, and bought an ice cream cone. Now holding the ice cream cone in your hand, what will you do? (Eat/Give to dad)\n")
    while "eat" not in action2.lower() and "give" not in action2.lower() and "dad" not in action2.lower():
        message = "I do not understand what that means."
        printString = termcolor.colored(message, "yellow")
        print(printString)
        action2 = input("With an ice cream cone still in your hand, what will you do? (Eat/Give to dad)\n")
    if "eat" in action2.lower():
        message = "Well, I guess thats fine too, you never promised your dad an ice cream, but you know better."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    elif "dad" or "give" in action2.lower():
        message = "Well done! Your dad thanks you. In addition, you feel very good for helping someone else."
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    line()
    time.sleep(2)
    return correct

def challenge2():
    print("Task Two:\nStop the bully from taking the little kids ice cream.")
    line()
    action1 = input("After just climbing out of the pool, you are near the bully and the helpless child, you can hear what they are saying. \nWhat do you do now? (Approach the bully/Walk away/Get help from an adult)\n")
    while "walk" not in action1.lower() and "away" not in action1.lower() and "bully" not in action1.lower() and "approach" not in action1.lower() and "adult" not in action1.lower() and "help" not in action1.lower():
        message = "I do not understand what that means."
        printString = termcolor.colored(message, "yellow")
        print(printString)
        action1 = input("What do you do now? (Approach the bully/Walk away/Get help from an adult)\n")
    if "walk" in action1.lower() or "away" in action1.lower():
        message = "You walked away, but as you looked back, you saw the helpless child hand away his ice cream cone.\nStop being a bystander, take action."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    if "approach" in action1.lower() or "bully" in action1.lower():
        message = "You gathered up the courage and walked towards the helpless child, and whispered to him he was safe to leave. After he left, you confronted the bully who is now angry at you."
        printString = termcolor.colored(message, "green")
        print(printString)
        action2 = input("What do you say to the bully now? (Tell him to stop/Ask him what's wrong)\n")
        while "wrong" not in action2.lower():
            while "wrong" not in action2.lower() and "stop" not in action2.lower():
                message = "I do not understand what that means."
                printString = termcolor.colored(message, "yellow")
                print(printString)
                action2 = input("What do you say to the bully? (Tell him to stop/Ask him what's wrong?)\n")
            if "stop" in action2.lower():
                message = "You told him to stop, he returned with, 'mind your own business,' and proceeded to push you out of the way."
                printString = termcolor.colored(message, "red")
                print(printString)
                action2 = input("You caught up with him, and wanted to say something again. (Tell him to stop/Ask him what's wrong)\n")
        message = "You approached him and kindly asked, 'What's wrong? Is your day going poorly?' He responded with how he was also picked on as a child, and how he never had any friends."
        printString = termcolor.colored(message, "green")
        print(printString)
        message = "You told him to stop, and how others will want to be treated how you want to be treated. You also told him people that gets bullied feels how he felt when he used to get picked on, and that is not a pleasant feeling."
        printString = termcolor.colored(message, "green")
        print(printString)
        message = "After a confrontation, he stopped."
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    if "adult" in action1.lower() or "help" in action1.lower():
        message = "You turned and headed to an adult, however, keep in mind that during the time it takes to get an adult, the bully may have already taken the child's ice cream and left the scene."
        printString = termcolor.colored(message, "blue")
        print(printString)
        bullyChance = random.randint(1,2)
        action2 = int(input("Since there is a chance that the bully may leave, you have to correctly guess the number the AI is choosing from 1-2 to finish this task. (1/2)\n"))
        if action2 == bullyChance:
            message = "You came back with an adult to confront the bully. The bully quit his actions."
            printString = termcolor.colored(message, "green")
            print(printString)
            correct = True
        elif action2 != bullyChance:
            message = "Unfortunately, when you came back with an adult, you found that the bully is already gone."
            printString = termcolor.colored(message, "red")
            print(printString)
            correct = False
    line()
    time.sleep(2)
    return correct

def addNumEasy():
    addNum1 = random.randint(0,10)
    addNum2 = random.randint(0,10)
    addResult = addNum1 + addNum2
    print("What is", addNum1, "+", addNum2, "?")
    addInput = int(input())
    if addInput == addResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def minusNumEasy():
    minusNum1 = random.randint(5,10)
    minusNum2 = random.randint(0,5)
    minusResult = minusNum1 - minusNum2
    print("What is", minusNum1, "-", minusNum2, "?")
    minusInput = int(input())
    if minusInput == minusResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def multiplyNumEasy():
    multiplyNum1 = random.randint(0,5)
    multiplyNum2 = random.randint(0,5)
    multiplyResult = multiplyNum1 * multiplyNum2
    print("What is", multiplyNum1, "×", multiplyNum2, "?")
    multiplyInput = int(input())
    if multiplyInput == multiplyResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def addNumHard():
    addNum1 = random.randint(10,30)
    addNum2 = random.randint(10,30)
    addResult = addNum1 + addNum2
    print("What is", addNum1, "+", addNum2, "?")
    addInput = int(input())
    if addInput == addResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def minusNumHard():
    minusNum1 = random.randint(15,30)
    minusNum2 = random.randint(0,15)
    minusResult = minusNum1 - minusNum2
    print("What is", minusNum1, "-", minusNum2, "?")
    minusInput = int(input())
    if minusInput == minusResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def multiplyNumHard():
    multiplyNum1 = random.randint(5,15)
    multiplyNum2 = random.randint(5,15)
    multiplyResult = multiplyNum1 * multiplyNum2
    print("What is", multiplyNum1, "×", multiplyNum2, "?")
    multiplyInput = int(input())
    if multiplyInput == multiplyResult:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct

def finalChallenge():
    Num1 = random.randint(0,30)
    Num2 = random.randint(0,10)
    Num3 = random.randint(5,10)
    Num4 = random.randint(0,5)
    result = Num1 + Num2 * Num3 - Num4
    print("What is", Num1, "+", Num2, "×", Num3, "-", Num4, "?")
    userInput = int(input())
    if userInput == result:
        playsound.playsound("correctding.wav")
        message = "Correct!"
        printString = termcolor.colored(message, "green")
        print(printString)
        correct = True
    else:
        playsound.playsound("wrongsound.mp3")
        message = "Incorrect."
        printString = termcolor.colored(message, "red")
        print(printString)
        correct = False
    return correct
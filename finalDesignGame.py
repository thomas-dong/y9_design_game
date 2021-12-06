import playsound
import time
import art
import functionLibrary as fl

fl.line()
welcomeTo = art.text2art("Welcome      to...")
print(welcomeTo)
time.sleep(1)
gameName = art.text2art("Jabari      Jumps")
print(gameName)
fl.line()
time.sleep(1)
fl.randomGreeting()
name = input("What is your name, if I may ask?\n")
funCount = input("Are you ready to have fun playing this game? (Yes / No)\n")
fl.funGame(funCount)
fl.line()
print("The game starts...")
fl.line()
print("You just finished your swimming lessons, and as you look around, you spot other children climbing up a diving board. As they jump off, they splash into a pool, each with a wide smile on their face. You wish to join them, but you can't bring yourself to jump off of it.")
fl.line()
while fl.challenge1() == False:
    None
print("After your dad thanked you for the ice cream, you turn around and dove into the pool. As you swam around, you saw someone being bullied. You climbed out of the pool, listening closely, you figure that the bully wants the helpless kids ice cream cone.")
fl.line()
while fl.challenge2() == False:
    None
print("Task Three:\nCalculate the height of the diving board")
fl.line()
print("In this minigame, you have to get the math problems right to move on.")
fl.line()
while fl.addNumEasy() == False:
    None
while fl.minusNumEasy() == False:
    None
while fl.multiplyNumEasy() == False:
    None
while fl.addNumHard() == False:
    None
while fl.minusNumHard() == False:
    None
while fl.multiplyNumHard() == False:
    None
fl.line()
print("Now that you exercised your calcualtion skills, you can estimate the diving board.")
fl.line()
while fl.finalChallenge() == False:
    None
print("You calculated the height of the diving board, not too high eh? Well you decided to jump off.")
playsound.playsound("watersplash.mp3")

print("────────────█▄─█─▄▀▀▄─────▄█────────────")
print("────────────█─▀█─█──█──────█────────────")
print("────────────▀──▀──▀▀──▀────▀────────────")
print("████████████████████████████████████████")
print("████████████████████████████████████████")
print("████████████████████████████████████████")
print("███████████████████▒────██▓█████████████")
print("██████████████═──────────█▓▓████████████")
print("███████████▓───────────████══██████─████")
print("██████████────────────══─██──████─────██")
print("█████████─────▒────██────█─█─███──██──▓█")
print("█████▓▓██─────█──▓███────────▓██─████──█")
print("████───██───█▒█──█──█▓───────▓█─▒████──█")
print("███──▓███──███▓─═█──█▓───────██▓█████──█")
print("███──████─═███▒─█▒──██───────████████──█")
print("██──▓████──███──███─▓█───────████████──█")
print("██──█████─██═█─█▒═█─██───────████████─██")
print("██──█████─═█─█────█─█▓───────███████──██")
print("██──█████─────────█─█▒───────███████─███")
print("██──█████─────────█─█────────██████──███")
print("██──▓████─────────█─█───────═█████──████")
print("██───████▒────────█─█───────▓████──█████")
print("██───████▓───────▒█─█───────████──██████")
print("██▒───████───────▒█─█───────███──███████")
print("███────███───────▓█─█───────██──████████")
print("███═───███───────██─█──────▒█▓─█████████")
print("████────██▒──────█▒─███────██─██████████")
print("█████────██───▒▓▓█───██────█▒─██████████")
print("██████────█───███▓───██────█─▓██████████")
print("███████───██──▓█─────█▓───██─███████████")
print("████████───█──═█─█████═───█──▓██████████")
print("████████───██──██████▒────█──────███████")
print("█████████──██──▒─────────██──────███████")
print("█████████──▓█▓───────────███────████████")
print("█████████═─▓██──────────█████─▒█████████")
print("█████████▓─████────────▓████████████████")
print("█████████──████▓──────═█████████████████")
print("████████──██████▓────▓██████████████████")
print("███████▒─███████████████████████████████")
print("█████████████████▒▒▓──██████████████████")
print("█████████████████▒───▓██████████████████")
print("██████████████████───███████████████████")
print("██████████████████──▒███████████████████")
print("████████████████████████████████████████")
print("██████████████████▓▒────████████████████")
print("████████████████─────────▒██████████████")
print("███████████████══█▓█████████████████████")
print("██████████████████████████████▓█████████")
print("█████████████──────────────▓█▒▒█████████")
print("██████████▒██─────═─══════─██▒▓█████████")
print("██████████▓▓█──══════════──██▒██████████")
print("███████████▒█▒─══─═────────█▓▒██████████")
print("███████████▒██──────────▒─▒█▓▓██████████")
print("███████████▒▓█─▒████████████▒▓██████████")
print("███████████▓▒███████▓▓▓▓▓▒▒▒▒███████████")
print("████████████▒█▓▓▒▒▒▒▓▓▓▓▓███████████████")
print("████████████▓▓▓▓████████████████████████")
print("████████████████████████████████████████")

scroll = art.text2art("Scroll Up!")
print(scroll)
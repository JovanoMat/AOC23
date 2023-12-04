print(" ")
print(" AOC 2023 - Day 2 ")
print(" ")



# games = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
# ]

with open('J:\\repos\\AOC23\\day2input.txt', 'r') as file:
    games = file.readlines()
    games = [line.strip() for line in games]

redMax = 12
greenMax = 13
blueMax = 14


total = 0
for game in games:
    splitBySpace = game.split(" ")
    gameId = splitBySpace[1].split(":")[0]

    print(" ")
    print("Game " + gameId)

    iterations = 0
    redAmount = 0
    greenAmount = 0
    blueAmount = 0
    

    gameInvalid = False
    for part in splitBySpace:
        if gameInvalid:
            break
        

        if "blue" in part:
            blueAmount = int(splitBySpace[iterations-1])
            iterations += 1

        elif "green" in part:
            greenAmount = int(splitBySpace[iterations-1])
            iterations += 1

        elif "red" in part:
            redAmount = int(splitBySpace[iterations-1])
            iterations += 1


        else:
            iterations += 1
    
        if ";" in part or part == splitBySpace[-1]:
            print(" ")
            print("Next round")
            if redAmount > redMax or greenAmount > greenMax or blueAmount > blueMax:
                print("exceeded")
                total -= int(gameId)
                gameInvalid = True
            else:
                print(f"red = {redAmount}")
                print(f"green = {greenAmount}")
                print(f"blue = {blueAmount}")
            redAmount = 0
            greenAmount = 0
            blueAmount = 0


    total += int(gameId)

print(total)

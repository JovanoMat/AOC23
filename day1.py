print(" ")
print(" AOC 2023 - Day 1 ")
print(" ")

#codes = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"];

with open('J:\\repos\\AOC23\\day1input.txt', 'r') as file:
    codes = file.readlines()
    codes = [line.strip() for line in codes]



totalSum = 0;
for code in codes:
    new_code = ""
    for char in code:
        if char.isdigit():
            new_code += char
    code = new_code
    code = new_code[0] + new_code[-1]
    totalSum += int(code)

print("Part one answer = " + str(totalSum))
print(" ")



codes2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
    ]

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

totalSum = 0;
for code in codes2:
    new_code = ""
    if "one" in code:
        new_code = code.replace("one", "1")
        print(new_code)
        


    # for char in code:
    #     if char.isdigit():
    #         new_code += char
    # code = new_code
    # code = new_code[0] + new_code[-1]
    # totalSum += int(code)















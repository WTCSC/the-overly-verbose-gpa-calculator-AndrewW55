gpaList = []

def gpaAvg():
    global gpaList
    gpaTotal = 0
    for i in range(len(gpaList)):
        gpaTotal = gpaTotal + gpaList[i]
    return gpaTotal / len(gpaList)

def gpaAsk(num):
    global gpaList
    print("Alright! Now please input your grade for each on a 4 point scale")
    for i in range(num):
        gpaList.append(float(input(f"Grade for class {i+1}: ")))
        if gpaList[i] > 4:
            print("Your grade needs to be on the 4 point scale")
            gpaList[i] = float(input(f"Grade for class {i+1}: "))

def again(ans):
    while True:
        if str.upper(ans) == "Y":
            avgNum = 0
            gpaList = []
            main()
        elif str.upper(ans) == "N":
            quit()
        else:
            print("That's not a valid answer")
            again(input("Try Again?: "))
            

def main():
    global gpaList
    print("Salutations fine shyt! I hope you have had a splendiferous day!")
    gpaAsk(int(input("How many classes are you taking?: ")))
    avgNum = gpaAvg()
    print("Thank you so much jit! I'll get right on it")
    print(f"Your average GPA is: {avgNum}")
    if avgNum <= 1:
        print("Bruh you straight stupid asl")
    elif avgNum <= 2:
        print("It could definitely be worse")
        print("Just keep trying!")
        print("You've got this!")
    elif avgNum <= 3:
        print("Almost there!")
        print("Just a couple higher grades and it could be great!")
    else:
        print("Great job!")
        print("This can get you somewhere awesome for college!")
    again(input("Want to check again?(Y/N): "))
main()
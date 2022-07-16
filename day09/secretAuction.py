# 14 july
biddersList = {
    "name":23
}
isLeft = "yes"

while(isLeft.lower() == "yes"):
    name = input("What is your name : ")
    bid = input("Enter the bid amount : ")
    biddersList[name] =int(bid) #must convert this to int else error can happen anytime
    isLeft = input("Is there any other bidder left (yes or no)")




# Then at last iterate biddersList
Bidder = ""
Bid = 0
for i in biddersList:
    if biddersList[i] > Bid:
        Bid = biddersList[i]
        Bidder = i
print(f"The winner is {Bidder} with bid of {Bid}")


# Must convert string to int in input function
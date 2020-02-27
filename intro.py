#strings and output
msg= "Hello World"
print(msg)
# lists
pets = ["Dog", "Cat", "Fish"]
thepet = pets[1]
print (thepet)
# length $ Types
size = len(pets)
msg = "there are" + str(size)+ "pets"
print (msg)
#loops
for anml in pets:
    print("I wish I had a " + anml)
#user input
ans = input("What kind of a pet do you have?")
print ("you have a " + ans)
# booleans
known = ans in pets
print (" it is " + str(known) + " that i have seen a " + ans)
#branching
if known:
    msg = "My friend has a " + ans
else:
    msg = "I don't know anyone with a " + ans
print(msg)
#dictonary
feels = {"Cat":"selfish" , "Dog":"loyal" , "Fish":"wet"}
if known:
    pre = "e" if ans == "Fish" else ""
    msg = ans + pre + "s are very " + feels.get(ans)
else:
    msg = "I don't know anyone with a " + ans
print(msg)


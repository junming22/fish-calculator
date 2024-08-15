Length = int(input("Please enter the Length: "))
Girth = int(input("Please enter the Girth: "))

# Calculator for fish weight
def add_fishweight(Girth, Length):
    Weight = Girth * Girth * Length/800
    return(Weight)
fishweight = add_fishweight(Girth, Length)
print(f"This is the weight of the fish is: {fishweight}")

# List the fish and weight
def fish():
    fishlist = ["small fish, Medium fish, Big Fish, Giant Fish"]
    return(fishlist)
fishlist = fish()
print(f"This is the: {fishlist}")
def weight():
    weightlist = ["0 to 41 pounds, 42 to 99 pounds, 100 to 174 pounds, > 175 pounds"]
    return(weightlist)
weightlist = weight()
print(f"This is the weight list: {weightlist}")

# Catogory of fish
def Fishsize(fishweight):
    if fishweight < 41:
        classification = "small fish"
    elif fishweight < 99:
        classification = "medium fish"
    elif fishweight < 174:
        classification = "big fish"
    else:
        classification = "giant fish"
    print(f"The fish is classified as a {classification}")

Fishsize(fishweight)





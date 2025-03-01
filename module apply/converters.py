def lbs_to_kg(weight):
    print("converted")
    return weight * 0.45359237

bob = True

def kg_to_lbs(weight):
    print("converted")
    return weight / 0.45359237

def isnight():
    for i in range (30):
        print(i)
    print("night")
    if bob == True:
        return "day"
    else:
        return "night"
    
print(isnight())
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy() #numbers 2 is the original numbers 1 if changed
numbers.append(20) # puts number at end of list
numbers.insert(0, 20)  # where you want to put a number
print(50 in numbers) #checks if 50 in list either true or false
numbers.clear() #clears the list
numbers.pop() #removes the last number in list
print(numbers.index(5)) #shows where 5 is located for this example its at 0
print(numbers.count(5)) #counts how many of that number there is in a list
numbers.remove(7) #removes a number
numbers.reverse() #reverses the list
print(numbers)

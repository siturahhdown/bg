def clip(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":/": "😕"
        }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
        

message = input("> ")
result = clip(message)
print(result) 

#or

message = input("> ")
print(clip(message))
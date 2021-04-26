def arrayCounter(array, threshold):
    high = 0
    low = 0
    for number in array:
        if number > threshold:
            high += 1
        if number < threshold:
            low += 1
    print("above: ", high, ", below: ", low)
 
 
def stringWraping(string, offset):
    characterArray = [character for character in string]
    for iteration in range(offset):
        characterArray.insert(0, characterArray.pop())
    string = "".join(characterArray)
    print(string)
    
    
testArray = [1, 5, 2, 1, 10]
#will run the example from the document
#arrayCounter(testArray, 6)

offset = 2
#will run the example from the document
#stringWraping("MyString", offset)
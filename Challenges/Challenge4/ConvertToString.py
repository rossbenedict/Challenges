def ConvertToString(number):
    print(number)

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    teens = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen",
             "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["hundred"]
    thousands = ["thousand"]
    nextNumber = []

    stringedNumber = str(number)
    allOfIt = len(stringedNumber)
    numberList = list(stringedNumber)


    i = 0
    for i in range(allOfIt):
        dman = numberList[i]
        gman = int(dman)
        newNumber = ones[gman]
        nextNumber.append(newNumber)
        i = i + 1

    nextNumber.insert(1, hundreds[0])
    nextNumber.insert(2, thousands[0])
    nextNumber.insert(5, thousands[0])
    nextNumber.insert(7, hundreds[0])
    nextNumber.insert(8, tens[int(numberList[4])])
    nextNumber.pop(3)
    nextNumber.pop(8)

    finalNumber = ' '.join(nextNumber)

    return ConvertToString(finalNumber)


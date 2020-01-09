def ConvertToString(number):
    print(number)

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    teens = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen",
             "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["hundred"]
    thousands = ["thousand"]
    nextNumber = []
    #finalNumber = []

    stringedNumber = str(number)

    numberList = list(stringedNumber)

    a=0
    for i in numberList:
        juman = numberList[a]
        print(juman)
        juman = int(juman)
        newNumber = ones[juman]
        nextNumber.append(newNumber)
        a = a+1

    nextNumber.insert(1, hundreds[0])
    nextNumber.insert(2, thousands[0])
    nextNumber.insert(5, thousands[0])
    nextNumber.insert(7, hundreds[0])
    nextNumber.insert(8, tens[int(numberList[4])])
    nextNumber.pop(9)
    nextNumber.pop(3)

    print(nextNumber)



    return ConvertToString(nextNumber)


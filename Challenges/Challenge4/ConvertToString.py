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

    numberList = list(stringedNumber)

    for i in range(0, len(stringedNumber)):
        nextNumber.append(ones[int(numberList[i])])

    tenthNumber = int(numberList[5])
    if tenthNumber == 1:
        teenNumber = int(nextNumber[6])
        nextNumber.insert(tenthNumber, teens[teenNumber])
        nextNumber.pop(7)
        nextNumber.pop(6)
    elif int(tenthNumber) > 1:
        nextNumber.insert(tenthNumber, tens[tenthNumber])
        nextNumber.pop(6)

    finalNumber = nextNumber

    #mod function (%) gives the remainder
    #recursive functions

    return ConvertToString(finalNumber)

    #number = 123456

    #partialnumber = number[4:6] = > 456
    #partialnumberHundreds = number[0:3]


    #getNum(number)



#def getNum(smallNumber):


    #need a return to send the info back

# need arra/list
# if number == 0
#     print("zero")
# else


# zertotoTwenty = ["", "one", "two", "three", ..."nineteen"]
# print (zertotoTwenty[3])  #will get three
# tens = ["", "twenty", "thirty"]
#
# partialnumber = number[4:6] => 456
# partialnumberHundreds = number[0:3]
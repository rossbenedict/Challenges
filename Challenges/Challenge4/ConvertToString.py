def ConvertToString(number):
    print(number)

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen",
             "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["hundred"]
    thousands = ["thousand"]

    stringedNumber = str(number)
    lengthNumber = len(stringedNumber)
    stringedLengthNumber = str(lengthNumber)
    print("lengthNumber = " + stringedLengthNumber)

    newNumber = stringedNumber
    print("after string =" + newNumber)
    newNumber.split()
    print(newNumber[0])
    beta = " "

    for i in range(0,lengthNumber):
        alpha = newNumber[i]
        #beta = beta + alpha
        beta = beta + ones[i]

        i += 1

    print(beta)

    print(anotherNumber)

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
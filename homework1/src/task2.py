#Task 2: Implements integers, floating-point numbers, strings, and boolean

#Integer Implementation
def int_mult():
    myInt = 2
    myOtherInt = 3
    intResult = myInt*myOtherInt
    return intResult

#Floating Point Implementation
def float_add():
    aFloat = 5.55
    anotherFloat = 6.78
    floatResult = aFloat + anotherFloat
    return floatResult

#String Implementation
def string_concat():
    str1 = "Hello"
    str2 = "World!"
    concatination = str1 + str2
    return concatination

#Boolean Implementation
def boolean_truth():
    color = "blue"
    boolResult = bool(color)
    return boolResult

#Main

#Printing Results
print(f"The integer result is {IntMult()}")
print(f"The float result is {FloatAdd()}")
print(f"The string result is {StringConcat()}")
print(f"The boolean result is {BooleanTruth()}")
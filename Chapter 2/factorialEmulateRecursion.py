lookupNumber = int(input("Factorial for which number?: "))

callStack = []
callStack.append({'returnAddr':'start', 'number': lookupNumber})
returnValue = None

cnt = 0

while len(callStack) > 0:
    cnt+= 1

    number = callStack[-1]['number']
    returnAddr = callStack[-1]['returnAddr']

    print('*************')
    print('Iteration Count: ', cnt, ' number being processed: ', number,' Return Address: ', returnAddr)
    print('*************')
    print()
    print()


    if returnAddr == 'start': 
        #does it mean I have started working with this number for the first time?
        if number == 1:
            returnValue = 1; #This return value got its value for the first time!
            callStack.pop()
            continue
        else:
            callStack[-1]['returnAddr'] = 'after recursive call'
            #mane nijeke abar call korar kaaj ta hocche ekhane
            #ar function call korle pechone kono ekta call Stack e appended hoi. amra amader call stack e append kore dibo!

            callStack.append({'returnAddr':'start', 'number':number -1})
            continue #eta ka korleo ig kaaj kortoi. karon baki segment o if else er moddhe lekha.

    elif returnAddr == 'after recursive call':
        returnValue = number*returnValue
        callStack.pop()
        continue



print(returnValue)
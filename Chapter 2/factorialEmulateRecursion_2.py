lookupNumber = int(input("number: "))

callStack = []
callStack.append({'returnAddr':'start', 'number':lookupNumber})

returnValue = None

while len(callStack)> 0:
    #top e je ache, or data ber koro age

    number = callStack[-1]['number']
    returnAddr = callStack[-1]['returnAddr']

    if returnAddr == 'start':
        if number == 1:
            returnValue = 1
            callStack.pop()
            continue
        else:
            callStack[-1]['returnAddr'] = 'after recursive call'#call e dhuke gesi. er pore pelei pop kore dibo!
            callStack.append({'returnAddr':'start', 'number': number - 1})#newww callll!

    elif returnAddr == 'after recursive call':
        returnValue = returnValue* number;
        callStack.pop();    
        continue
print(returnValue)

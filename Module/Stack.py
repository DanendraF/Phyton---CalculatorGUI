def stack():
    s = []
    return(s)


def push(s, data):
    s.append(data)


def pop(s):
    data = s.pop()
    return(data)


def peek(s):
    return(s[-1])


def isEmpty(s):
    return(s == [])


def size(s):
    return(len(s))

def dataCheck(data, check, compare):
    # data is kurung dictionary
    # check is result from peek in the stack
    # compare is current data iteration
    # to check if check any in data
    if check in data.values():
        # then check, if values of data is equal with compare
        if data.get(compare) == check:
            return False
    else:
        return True

def compareOperator(data, stack, i):
    # to compare higher level operator
    try: 
        op1 = data[i] 
        op2 = data[peek(stack)] 
        if op1 <= op2:
            return True
        else:
            return False
    except KeyError:  
        return False
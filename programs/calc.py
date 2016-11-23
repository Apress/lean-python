def calc(a, op, b):

    if op not in '+-/*':
        return None, 'Operator must one of be +-/*'
        
    try:
        if op=='+':
            result=a+b
        elif op=='-':
            result=a-b
        elif op=='/':
            result=a/b
        else:
            result=a*b
    except Exception,e:
        return None,e.__class__.__name__

    return result,str(result)


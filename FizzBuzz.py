def FizzBuzz(start, finish):
    outlist = [] 
    for num in range(start, finish + 1): 
        if num % 15 == 0:
            outlist.append("fizzbuzz") 
        elif num % 3 == 0:
            outlist.append("fizz")
        elif num % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(num)
    return(outlist)

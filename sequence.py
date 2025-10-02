def sequence(tup):

    if len(tup) < 2:
        if len(tup) == 1:
            d = 0
            
        else:
            return tup
            
    else:
        d = tup[1] - tup[0]
        
    last_num = tup[-1]
    
    next_three = []
    current_num = last_num
    for i in range(3):
        current_num += d
        next_three.append(current_num)
        
    return tup + tuple(next_three)

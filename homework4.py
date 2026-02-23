def WhoAmI():
    return('zz3457')


def getBondPrice(y, face, couponRate, m, ppy=1):
    periodic_yield = y / ppy
    periodic_coupon = face * couponRate / ppy
    total_periods = m * ppy
    
    bondPrice = 0.0
    for t in range(1, total_periods + 1):
        coupon_pv = periodic_coupon / (1 + periodic_yield) ** t
        bondPrice += coupon_pv
    
    face_pv = face / (1 + periodic_yield) ** total_periods
    bondPrice += face_pv
  
    return(bondPrice)


def getBondDuration(y, face, couponRate, m, ppy = 1):
    periodic_yield = y / ppy
    periodic_coupon = face * couponRate / ppy
    total_periods = m * ppy
    
    total_pvcf = 0.0
    total_t_pvcf = 0.0
    
    for t in range(1, total_periods + 1):
        if t == total_periods:
            cf = periodic_coupon + face
        else:
            cf = periodic_coupon
        
        pv_factor = 1 / (1 + periodic_yield) ** t
        pvcf = cf * pv_factor
        
        total_pvcf += pvcf
        total_t_pvcf += t * pvcf
    
    bondDuration = total_t_pvcf / total_pvcf
    return(bondDuration)


def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0.0
    periodic_coupon = face * couponRate 
    total_periods = m
    
    for period_idx, rate in enumerate(yc, start=1):
        if period_idx == total_periods:
            cf = periodic_coupon + face
        else:
            cf = periodic_coupon
        
        pv_factor = 1 / (1 + rate) ** period_idx
        pvcf = cf * pv_factor
        
        bondPrice += pvcf
    
    return (bondPrice)


def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0.0
    periodic_coupon = face * couponRate
  
    for t, rate in zip(times, yc):
        if t == max(times):  
            cf = periodic_coupon + face
        else:
            cf = periodic_coupon
        
        pv_factor = 1 / (1 + rate) ** t
        pvcf = cf * pv_factor
        
        bondPrice += pvcf
    
    return (bondPrice)


def FizzBuzz(start, finish):
    outlist = [] 
    for num in range(start, finish + 1):  
        if num % 3 == 0 and num % 5 == 0:
            outlist.append("fizzbuzz") 
        elif num % 3 == 0:
            outlist.append("fizz")
        elif num % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(num)
    return(outlist)

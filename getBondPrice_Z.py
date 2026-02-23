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

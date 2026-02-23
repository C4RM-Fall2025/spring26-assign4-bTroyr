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

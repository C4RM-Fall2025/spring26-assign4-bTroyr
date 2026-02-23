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

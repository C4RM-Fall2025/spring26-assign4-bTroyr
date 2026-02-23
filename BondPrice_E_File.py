def getBondPrice_E(face, couponRate, yc):
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

    return(bondPrice)

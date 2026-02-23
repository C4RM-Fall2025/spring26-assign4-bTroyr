def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    for t, y in enumerate(yc, start=1):
        cf = coupon
        if t == len(yc):
            cf += face
        bondPrice += cf / ((1 + y) ** t)

    return (bondPrice)
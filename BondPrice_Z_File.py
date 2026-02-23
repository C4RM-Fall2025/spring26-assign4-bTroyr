def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0.0
    n = len(times)

    for i, (t, y) in enumerate(zip(times, yc), start=1):
        cf = coupon
        if i == n:
            cf += face
        bondPrice += cf / ((1 + y) ** t)

    return (bondPrice)
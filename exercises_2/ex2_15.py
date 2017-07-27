"""
Find potential sources of runtime errors:

dividend = float(input("Please enter the dividend: "))
divisor = float(input("Please enter the divisor: "))
quotient = dividend / divisor
quotient_rounded = math.round(quotient)
"""
#if divisor is 0
dividend = float(input("Please enter the dividend: "))
divisor = float(input("Please enter the divisor: "))
quotient = dividend / divisor
quotient_rounded = round(quotient)
def sqrt(n):
    if n < 0:
        return None

    return MDLRbinsearch(0, n, n, None)

def MDLRbinsearch(left, right, oldnum, checknum ):
    if left > right:
        return checknum
    mid = left + (right - left) // 2
    multiplication = mid * mid
    if multiplication > oldnum:
        return MDLRbinsearch(left, mid - 1, oldnum, checknum)
    elif multiplication == oldnum:
        return mid
    else:
        return MDLRbinsearch(mid + 1, right, oldnum, mid)

##TestCases
print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if  (8 != sqrt(100)) else "Fail")


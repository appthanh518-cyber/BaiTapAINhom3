
def value(baitoanhientai, trangthai):
    p, q, r = trangthai

    C1 = (p == 0 or q == 1)
    C2 = (q == 0 or r == 1)
    C3 = (p == 1)
    C4 = (r == 0)

    diem = 0

    if C1:
        diem += 1

    if C2:
        diem += 1

    if C3:
        diem += 1

    if C4:
        diem += 1

    return diem

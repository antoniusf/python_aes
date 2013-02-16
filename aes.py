import hex as hmod

def mul(a,b):
    p = 0
    for i in range(8):
        if ((b & 1) > 0):
            p = p^a
        if ((a & 0x80) > 0):
            carry = 1
        else:
            carry = 0
        a = (a<<1)&0b011111111
        if (carry == 1):
            a = a^0x1b
        b = b>>1
    return p

def pow2(e):
    if e > 2:
        c = mul(2,2)
        e -= 3
        for i in range(e):
            c = mul(2,c)
    elif e == 2:
        c = 2
    elif e == 1:
        c = 1
    elif e == 0:
        c = 0x8d
    return c

def sbox():#first s-box calculation try; use fsbox for a real s-box
    slist = []
    for i in range(256):
        s = x = i
        for j in range(4):
            h = s>>7
            s <<= 1
            s &= 0b011111111
            s |= h
            x ^= s
        x ^= 99
        slist.append(x)
    return slist

def multinv(a):
    for b in range(256):
        if mul(a,b) == 1:
            break
    return b

def fsbox():
    l = sbox()
    sl2 = []
    for i in range(256):
        sl2.append(l[multinv(i)])
    return sl2

def keysched(key,rcon,slist):
    i = 1
    n = 16
    b = 176
    key = hmod.hexnumber(key)
    i = 1
    while len(key) < b:
        t = key[-4:]
        t.lrot8()
        t.appsbox(slist)
        rcon = hmod.hexnumber(pow2(i))
        rcon<<3
        t^rcon
        t^key[-16:-12]
        key.append(t)

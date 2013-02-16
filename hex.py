class hexnumber:
    def __init__(self, number):
        self.hexlist = []
        if type(number) == int:
            convhex = hex(number)[2:]
        elif type(number) == str:
            convhex = number
        if len(convhex)/2 != len(convhex)//2:
            convhex = "0"+convhex
        for i in range(0,len(convhex),2):
            self.hexlist.append(convhex[i:i+2])

    def value(self):
        return self.hexlist

    def val(self):
        return self.hexlist

    def dec(self):
        a = ""
        for elem in self.hexlist:
            a += elem
        return int(a,16)

    def append(self, number):
        if type(number) == int:
            convhex = hex(number)[2:]
        elif type(number) == str:
            convhex = number
        elif type(number) == hexnumber:
            self.hexlist.extend(number.val())
        else:
            raise ValueError("Number has to be int, str or hexnumber")
        if (type(number) == int) or (type(number) == str):
            if len(convhex)/2 != len(convhex)//2:
                convhex = "0"+convhex
            for i in range(0,len(convhex),2):
                self.hexlist.append(convhex[i:i+2])

    def modbyte(self, byte, number):
        if type(number) != int:
            raise TypeError("Number has to be int")
        if (number > 255) or (number < 0):
            raise ValueError("Number is bigger than one byte")
        if byte >= len(self.hexlist):
            raise IndexError("'byte' index out of range")
        number = hex(number)[2:4]
        self.hexlist[byte] = number

    def readbyte(self, byte):
        return self.hexlist[byte]

##    def hexslice(self,start,stop):
##        numberstring = ""
##        for i in range(start,stop

    def __getitem__(self, key):
        numberstring = ""
        start = key.start
        stop = key.stop
        step = key.step
        if stop == None:
            stop = len(self.hexlist)
        elif stop < 0:
            stop += len(self.hexlist)
        if start == None:
            start = 0
        elif start < 0:
            start += len(self.hexlist)
        if step == None:
            step = 1
        for i in range(start,stop,step):
            numberstring += self.hexlist[i]
        return hexnumber(numberstring)

    def __len__(self):
        return len(self.hexlist)

    def __lshift__(self, other):
        if type(other) != int:
            raise ValueError
        for i in range(other):
            self.hexlist.append('00')

    def lrot8(self):
        hb = self.hexlist[0]
        self.hexlist = self.hexlist[1:]
        self.hexlist.append(hb)

    def appsbox(self, slist):
        self.hexlist = [hex(slist[int(elem,16)])[2:4] for elem in self.hexlist]

    def __xor__(self, other):
        for i in range(len(self.hexlist)):
            self.hexlist[i] = hex(int(self.hexlist[i],16)^int(other.hexlist[i],16))[2:4]

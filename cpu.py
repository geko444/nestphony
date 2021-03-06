class cpu():

    def __init__(self, ram):
        self.pc = 0
        self.sp = 0
        self.acc = 0
        self.x = 0
        self.y = 0
        self.ps = [False] * 8
        self.ram = ram

    def get_carry(self):
        return self.ps[0]

    def set_carry(self, val):
        self.ps[0] = val

    def get_zero(self):
        return self.ps[1]

    def set_zero(self, val):
        self.ps[1] = val

    def get_interrupt(self):
        return self.ps[2]

    def set_interrupt(self, val):
        self.ps[2] = val

    def get_decimal(self):
        return self.ps[3]

    def set_decimal(self, val):
        self.ps[3] = val

    def get_break(self):
        return self.ps[4]

    def set_break(self, val):
        self.ps[4] = val

    def get_overflow(self):
        return self.ps[5]

    def set_overflow(self, val):
        self.ps[5] = val

    def get_negative(self):
        return self.ps[6]

    def set_negative(self, val):
        self.ps[6] = val
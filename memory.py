class memory():
    def __init__(self):
        self.ram = [0] * 0x800
        self.ppu = [0] * 0x8
        self.apu_io = [0] * 0x18
        self.cpu_test = [0] * 0x8
        self.cartridge = [0] * 0xbfe0

    def get(self, addr):
        if addr < 0x2000:
            return self.get_ram(addr)
        elif addr < 0x4000:
            return self.get_ppu(addr)
        elif addr < 0x4018:
            return self.get_apu_io(addr)
        elif addr < 0x4020:
            return self.get_cpu_test(addr)
        else:
            return self.get_cartridge(addr)

    def set(self, addr, val):
        if addr < 0x2000:
            return self.set_ram(addr, val)
        elif addr < 0x4000:
            return self.set_ppu(addr, val)
        elif addr < 0x4018:
            return self.set_apu_io(addr, val)
        elif addr < 0x4020:
            return self.set_cpu_test(addr, val)
        else:
            return self.set_cartridge(addr, val)

    def get_ram(self, addr):
        return self.ram[addr % 0x800]

    def set_ram(self, addr, val):
        self.ram[addr % 0x800] = val

    def get_ppu(self, addr):
        return self.ppu[addr % 0x8]
    
    def set_ppu(self, addr, val):
        self.ppu[addr % 0x8] = val
    
    def get_apu_io(self, addr):
        return self.apu_io[addr]
    
    def set_apu_io(self, addr, val):
        self.apu_io[addr] = val
    
    def get_cpu_test(self, addr):
        return self.cpu_test[addr]
  
    def set_cpu_test(self, addr, val):
        self.cpu_test[addr] = val
        
    def get_cartridge(self, addr):
        return self.cartridge[addr]
    
    def set_cartridge(self, addr, val):
        self.cartridge[addr] = val
    
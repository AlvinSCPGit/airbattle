class Part():
    def __init__(self, max_damage, mesh, is_critical):
        self.max_damage = max_damage
        self.damage = self.max_damage

        # The filename of mesh.
        self.mesh = mesh

        # True if this part is seriously damaged
        self.isbroken = False

        # True if this part is critical. Such as front seat or gas tank.
        self.is_critical = is_critical

class T1_FrontSeat(Part):
    def __init__(self):
        super.__init__(self, 350, "frontseat.png", True)

class T1_Body(Part):
    def __init__(self):
        super.__init__(self, 700, "body.png", True)

class T1_Foil(Part):
    def __init__(self, side):
        mesh = ""
        if side == "left":
            mesh = "left_foil.png"
        if side == "right":
            mesh = "right_foil.png"
        super.__init__(self, 450, mesh, False)

        # String indicates side("left", "right")
        self.side = side

class Assault_HMG(Part):
    def __init__(self):
        super.__init__(self, 750, "assault_hmg.png", False)
        self.cd = 0
        self.loaded = 47

    def shoot(self):
        if self.cd < 1 and self.loaded > 0:
            self.loaded -= 1
            self.cd = 6

    def reload(self):
        self.loaded = 47
        self.cd = 240

    def onTickUpdate(self):
        self.cd -= 1
        if self.cd < 0: self.cd = 0

class SF203():
    def __init__(self):
        self.frontseat = T1_FrontSeat()
        self.body = T1_Body()
        self.leftfoil = T1_Foil("left")
        self.rightfoil = T1_Foil("right")
        self.weapon = Assault_HMG()

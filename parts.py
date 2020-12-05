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
        
    def onTickUpdate(self):
        if self.damage <= 0:
            self.damage = 0
            self.isbroken = True

class Entity():
	def __init__(self):
		self.x = 0
		self.y = 0
		
	def onTickUpdate(self):
		pass
	
	# Render list [offx0, offy0, mesh0, ...]
	def getRenderList(self):
		return []
	
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

class Assault_HMG_Bullet(Entity):
	def __init__(self, lx, ly, dx, dy):
		super.__init__(self)
		self.x = lx
		self.y = ly
		self.dx = dx
		self.dy = dy
		
	def onTickUpdate(self):
		self.x += self.dx
		self.y += self.dy
		
	def getRenderList(self):
		return [0, 0, "assault_hmg_bullet.png"]
class Assault_HMG(Part):
    def __init__(self):
        super.__init__(self, 750, "assault_hmg.png", False)
        self.cd = 0
        self.loaded = 47

    def shoot(self, elist, x, y, dx, dy):
        if self.cd < 1 and self.loaded > 0:
            self.loaded -= 1
            self.cd = 6
			elist.append(Assault_HMG_Bullet(x,y,dx,dy))

    def reload(self):
        self.loaded = 47
        self.cd = 240

    def onTickUpdate(self):
        self.cd -= 1
        if self.cd < 0: self.cd = 0
  
class GTThruster(Part):
    def __init__(self):
        super.__init__(self, 140, "gtthruster.png", True)


	

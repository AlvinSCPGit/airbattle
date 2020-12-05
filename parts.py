import math

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
		self.orient = 0
		
	def onTickUpdate(self):
		pass
	
	# Render list [offx0, offy0, mesh0, ...]
	def getRenderList(self, elist):
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
	def __init__(self, lx, ly, orient):
		super.__init__(self)
		self.x = lx
		self.y = ly
		self.orient = orient
		
	def onTickUpdate(self, elist):
		dx = math.cos(self.orient) / abs(math.cos(self.orient))*3
		dy = math.sin(self.orient) / abs(math.sin(self.orient))*3
		self.x += dx
		self.y += dy
		
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

    def onTickUpdate(self, elist):
        self.cd -= 1
        if self.cd < 0: self.cd = 0
  
class GTThruster(Part):
    def __init__(self):
        super.__init__(self, 140, "gtthruster.png", True)

class SF203(Entity):
	def __init__(self):
		super.__init__(self)
		self.lfoil = T1_Foil("left")
		self.rfoil = T1_Foil("right")
		self.thruster = GTThruster()
		self.lhmg = Assault_HMG()
		self.rhmg = Assault_HMG()
		self.body = T1_Body()
	
	def onTickUpdate(self, elist):
		self.lfoil.onTickUpdate(elist)
		self.rfoil.onTickUpdate(elist)
		self.thruster.onTickUpdate(elist)
		self.lhmg.onTickUpdate(elist)
		self.rhmg.onTickUpdate(elist)
		if self.thruster.damage > 0.33:
			dx = math.cos(self.orient) / abs(math.cos(self.orient))*1
			dy = math.sin(self.orient) / abs(math.sin(self.orient))*1
			self.x += dx
			self.y += dy
		else:
			dx = math.cos(self.orient) / abs(math.cos(self.orient))*0.5
			dy = math.sin(self.orient) / abs(math.sin(self.orient))*0.5
			self.x += dx
			self.y += dy
		
	def attackAt(self, lx, ly):
		self.lhmg.shoot(lx, ly, self.orient)
		
	def getRenderList(self):
		return [-2, -7, self.body.mesh, -11, -1, self.lfoil.mesh, 2, -7, self.rfoil.mesh, -5, -6, self.lhmg.mesh, 3, -6, self.rhmg.mesh, -2, 7, self.thruster.mesh]

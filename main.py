import parts

entity_list = []

# Reserved Index for entities
USER_INDEX = 2
RES_P1PLANE = 0
RES_P2PLANE = 1

running = True
while running:
	
	for e in entity_list:
		e.onTickUpdate(entity_list)

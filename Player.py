class Player(object):
	""" Contains the player's inventory as well as whether they cleared the game or not """
	
	def __init__(self, name):
		self.name = name
		self.clear_game = False
		self.inventory = []
		
	def add_to_inventory(self, item_name):
		self.inventory.append(item_name)
	
	def delete_from_inventory(self, item_name):
		print "It doesn't look like you'll need %s anymore..." % item_name
		self.inventory.remove(item_name)		
	
	def print_inventory(self):
		if not self.inventory:
			print "You have nothing on you!"
		else:
			i = 1;
			print "You checked what you have on you!"
			for item in self.inventory:
				print "%d.) %s" % (i, item)
				i += 1 
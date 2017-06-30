class NPC(object):
	""" This contains what NPCs do when you talk to them or attack them. """
	
	def __init__(self, name, talk_d, attack_d, fatal):
		self.name = name
		self.talk_d = talk_d
		self.attack_d = attack_d
		self.attacked_already = False
		self.talked_already = False
		self.fatal = fatal
		
	def talk_dialogue(self):
		if self.talked_already == True:
			print "%s looks at you annoingly and sighs." % self.name
		else:
			self.talked_already = True	
		print self.talk_d
		
	def attack_dialogue(self, game):
		if self.attacked_already == True:
			print "I don't think that's a good idea to do that..."
		else:
			print self.attack_d
			if self.fatal == True:
				game.game_over(True)
			self.attacked_already = True
	
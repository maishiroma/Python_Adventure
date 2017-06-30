class Room(object):
	""" This contains all of the general functions that a room should have """
	
	# name and desc are strings
	# the exits are all Paths
	# special command is a boolean value that determines if the room has a special command in it
	def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command):
		self.name = name
		self.desc = desc
		self.n_exit = n_exit
		self.e_exit = e_exit
		self.s_exit = s_exit
		self.w_exit = w_exit
		self.special_command = special_command
		
	# Prints out the description of the room as well as all available exits in the room
	def examine_room(self):
		print "%s....%s" % (self.name, self.desc)
		temp = "The available exits are: "
		if self.n_exit is not None and self.n_exit.is_locked == False:
			temp = temp + "north "
		if self.w_exit is not None and self.w_exit.is_locked == False:
			temp = temp + "west "
		if self.s_exit is not None and self.s_exit.is_locked == False:
			temp = temp + "south "
		if self.e_exit is not None and self.e_exit.is_locked == False:
			temp = temp + "east "
		print temp
		
	def go_north(self, game):
		if self.n_exit is None:
			print "There's no path over here..."
		elif self.n_exit.is_locked == True:
			print "The path is blocked...there must be a way through! Maybe look around?"
		else:
			print "You moved to the north exit..."
			game.set_room(self.n_exit.path_destination)
	
	def go_east(self, game):
		if self.e_exit is None:
			print "There's no path over here..."
		elif self.e_exit.is_locked == True:
			print "The path is blocked...there must be a way through! Maybe look around?"
		else:
			print "You move to the east exit..."
			game.set_room(self.e_exit.path_destination)
		
	def go_south(self, game):
		if self.s_exit is None:
			print "There's no path over here..."
		elif self.s_exit.is_locked == True:
			print "The path is blocked...there must be a way through! Maybe look around?"
		else:
			print "You move to the south exit..."
			game.set_room(self.s_exit.path_destination)
		
	def go_west(self, game):
		if self.w_exit is None:
			print "There's no path over here..."
		elif self.w_exit.is_locked == True:
			print "The path is blocked...there must be a way through! Maybe look around?"
		else:
			print "You move to the west exit..."
			game.set_room(self.w_exit.path_destination)
	
	# Overriden in all super classes
	def room_command(self, user_choice, game):
		print "This is suppose to be overidden in certain room instances if needed."
		
	# sets all of the exits of the room. Mostly for convience sake.
	def set_exits(self, n_exit, s_exit, e_exit, w_exit):
		self.n_exit = n_exit
		self.s_exit = s_exit
		self.w_exit = w_exit
		self.e_exit = e_exit


class Path(object):
	""" This allows the player to move from room to room. Some of these are locked until the player does a specified action. """
	
	# path destination is a Room and is locked is a boolean value
	def __init__(self, path_destination, is_locked):
		self.path_destination = path_destination
		self.is_locked = is_locked
		
	# simply unlocks the path to be acessible
	def unlock_path(self):
		if self.is_locked == True:
			self.is_locked = False
	
class RoomWithNPC(Room):
	""" This inherits from Room, but also overrides room_command, since this room has a NPC"""
	
	# npc character is a NPC. Everything else is the same as Room
	def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command, npc_character):
		super(RoomWithNPC, self).__init__(name, desc, n_exit, e_exit, s_exit, w_exit, special_command)
		self.npc_character = npc_character
		
	def room_command(self, user_choice, game):
		""" This will activate depending on the type of NPC. """
		if user_choice == "talk":
			self.npc_character.talk_dialogue()
		elif user_choice == "attack":
			self.npc_character.attack_dialogue(self)
		else:
			print "Huh? The person can't hear you!"
			
class RoomWithPuzzle(Room):
	""" This inherits from Room, but the room_command will vary depending on the way you form the object. """
	
	# puzzle number is an int. Everythign else is the same
	def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command, puzzle_number):
		super(RoomWithPuzzle, self).__init__(name, desc, n_exit, e_exit, s_exit, w_exit, special_command)
		self.puzzle_number = puzzle_number
		self.solved = False
	
	#Overrides the normal method to include a way to tell the player that the room is done.
	def examine_room(self):
		if self.solved == True:
			print "%s....There's nothing of intrest here now..." % self.name
		else:
			print "%s....%s" % (self.name, self.desc)
			
		temp = "The available exits are: "
		if self.n_exit is not None and self.n_exit.is_locked == False:
			temp = temp + "north "
		if self.w_exit is not None and self.w_exit.is_locked == False:
			temp = temp + "west "
		if self.s_exit is not None and self.s_exit.is_locked == False:
			temp = temp + "south "
		if self.e_exit is not None and self.e_exit.is_locked == False:
			temp = temp + "east "
		print temp
		
	def room_command(self, user_choice, game):
		""" Depending on the puzzle number, various things are required here. """
		if self.solved == False:
			if self.puzzle_number == 1:
				# This is the puzzle that requires you to get the branch
				if user_choice == "get branch":
					print "You obtained a branch! It looks sturdy enough to be used as a leverage point..."
					game.player.add_to_inventory("branch")
					self.solved = True
				else:
					print "Hm, you're onto something..."
			elif self.puzzle_number == 2:
				# this is the puzzle that requires you to use the branch to access the trunk
				if user_choice == "use branch" and "branch" in game.player.inventory:
					print "Using the branch, you pryed open the door!"
					print "You looked inside and saw a note! It reads....\nDear Bro, I'm sorry for doing this, but I can't keep this up! You NEED TO USE YOUR DAMN TURN SIGNALS! We can't live like this anymore!"
					print "...after dismissing the note, you remembered that you have something in your trunk. You opened up the trunk and saw a machetti!"
					print "You got a machetti! It looks sharp enough to cut stuff! Why do you have this again?"
					game.player.add_to_inventory("machetti")
					game.player.delete_from_inventory("branch")
					self.solved = True
				else:
					print "Hm, you're onto something..."
			elif self.puzzle_number == 3:
				# this is the puzzle that uses the machetti to cut through the brush
				if user_choice == "use machetti" and "machetti" in game.player.inventory:
					print "Using your Legend of Zelda skills, you slashed through the thick brush that was blocking your path! There's a way through to the east now!"
					self.e_exit.unlock_path()
					self.solved = True
				else:
					print "Hm, you're onto something..."
			elif self.puzzle_number == 4:
				# this is the puzzle that requires the player to sneak past the bear in order to get the shiny key
				if user_choice == "sneak":
					print "Remembering that the best way around the problem is avoiding it, you snuck past the bear with relative ease. With a disgusted look, you dug your hand into the hay pile to snatch the shiny object!"
					print "Turns out it was a key! You have no idea what's it for, but you decided to hold onto it."
					game.player.add_to_inventory("key")
					self.solved = True	
				else:
					print "You tried to do something pretty fancy. In fact, so fancy, you stumbled and accidentally went face first into the bear. Woken up, the bear proceeds to maul you to a pulp."
					game.game_over(True)
			elif self.puzzle_number == 5:
				# this is the puzzle that requires the player to investigate the shack for a long board
				if user_choice == "investigate":
					print "You hiked up the hill towards the empty wooden shack. Inside, there's nothing much of note. You do see a rather large piece of broken plywood protrooding from the ground. It seems to be...beckoning to be picked up."
					print "You got a long board! It looks sturdy enough to support the weight of a person..."
					game.player.add_to_inventory("long board")
					self.solved = True
				else:
					print "Hm, youre onto something..."
			elif self.puzzle_number == 6:
				# this is the puzzle that requires the player to use the long board to cross the river
				if user_choice == "use long board" and "long board" in game.player.inventory:
					print "You carefully placed the long board across the raging river. It looks like the south path can be accessed!"
					self.s_exit.unlock_path()
					game.player.delete_from_inventory("long board")
					self.solved = True
				else:
					print "You were overthinking it, but something had to be done! Well, let's just say you wound up in the river fast floating to a waterfall that leads to a dark hole. Damn, brutal..."
					game.game_over(True)
			elif self.puzzle_number == 7:
				# this is the puzzle that requires the player to use the flashlight to navigate the dark cave
				if user_choice == "use flashlight" and "flashlight" in game.player.inventory:
					print "You took out the flashlight and saw some pretty obvious arrows leading to somewhere. You decided to follow them until a path to the south is reveled!"
					self.s_exit.unlock_path()
					self.solved = True;
			elif self.puzzle_number == 8:
				# this is the puzzle that requires the player to type in a specific code in order to finish the edge
				if user_choice == "1234567890":
					print "The most simpliest answers are the best! It worked! You opened the door and you see...your room? Hah, turns out it was a dream?! What a copout..."
					game.game_over(True)
				elif user_choice == "231":
					print "After typing in the code, you see the light to a grand city! You called out for help and you were saved by some police! You're rescued!"
					game.game_over(False)
				else:
					print "For typing in something dumb, you got shot in the head by a lazer. Sucks to be you."
					game.game_over(True)
			elif self.puzzle_number == 9:
				# this is where the player goes inside the tent to grab the hiker's flashlight
				if user_choice == "get flashlight":
					print "Hoping that he wouldn't notice, you decided to take the guy's flashlight. It's one less thing for him to carry anyway."
					print "You got a flashlight! It has enough juice to last a long time. It's bright too!"
					game.player.add_to_inventory("flashlight")
					self.solved = True
			else:
				print "Huh? This isn't suppose to happen..."
		else:
			print "You already saw everything of intrest here..."
		
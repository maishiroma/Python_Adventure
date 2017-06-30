from sys import exit
from Room import Room
from Room import RoomWithPuzzle
from Room import RoomWithNPC
from Room import Path
from Player import Player
from NPC import NPC

class Game(object):
	""" This contains the main work of the game itself. """

	# the player name is a string 
	def __init__(self, player_name):
		self.player = Player(player_name)
		self.current_room = None
		
	def game_over(self, winOrNot):
		if winOrNot == True:
			print "Damn, you lost. Ah well. There's always next time."
		else:
			print "Congrats! You win the game!"
		exit(0)
		
	def set_room(self, room):
		self.current_room = room
		
	def command_parser(self):
		user_answer = raw_input("> ")
		user_answer.lower()
		if user_answer == "north":
			self.current_room.go_north(self)
		elif user_answer == "east":
			self.current_room.go_east(self)
		elif user_answer == "south":
			self.current_room.go_south(self)
		elif user_answer == "west":
			self.current_room.go_west(self)
		elif user_answer == "examine":
			self.current_room.examine_room()
		elif user_answer == "inventory":
			self.player.print_inventory()
		elif user_answer == "help":
			self.help_command()
		elif self.current_room.special_command == True:
			self.current_room.room_command(user_answer, self)
		else:
			print "What? I can't hear you!"
			
	def help_command(self):
		print "Universal commands are: north, east, south, west, examine, inventory, help."
		print "In some rooms, get (item), talk, attack, use (item) are available as well."
		print "Stuck? Pay attention to room descriptions and what people have to say! They may tell you special commands for certain areas!"
		
	def play_game(self):
		""" Does the work of putting rooms in the game, laying out the map and progression """
		# def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command) for a Room
		# def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command, puzzle_number) for a puzzle Room
		# def __init__(self, name, desc, n_exit, e_exit, s_exit, w_exit, special_command, npc_character) for a room with a NPC		
		start_room = Room("Forest Clearing", "You're in a warmly lit area surrounded by trees. ", None, None, None, None, False)
		tree_with_branch = RoomWithPuzzle("Bushy Tree", "A well grown tree inhabits this part of the woods. One of its branches seems to have fallen to the ground.", None, None, None, None, True, 1)
		hiker_area = RoomWithNPC("Someone's Campsite", "A well cleaned tent area occupies the south part of the area.\nA lone, burly man is sitting on a chair, reading a book called \'Bear Survival\'.", None, None, None, None, True, None)
		hiker_tent = RoomWithPuzzle("Hiker's Tent", "You immediatly regret your decision on coming here. Filtering out the weird stuff, you notice a flashlight in the corner of the room", None, None, None, None, True, 9)
		crash_site = RoomWithPuzzle("Car Crash Site", "A used to be fancy car sits dejectely, smoke and oil leaking out of it. You recalled that this was your sweet ride! To your dismay, the car seems to be sealed shut...maybe if you had some sort of leverage to pull it open?", None, None, None, None, True, 2)
		thick_brush = RoomWithPuzzle("Thorny Path", "A thick, spiky overgrowth blocks the east path. There's no other way around it.", None, None, None, None, True, 3)
		open_field = Room("Forest Entrance", "A vast field of grass occupies this space.", None, None, None, None, False)
		bear_den = RoomWithPuzzle("Grizzly Bear's Den", "A wretched stench greets you as you see a huge grizzly bear sleeping on a leafy patch. There seems to be something gleaming past it though...", None, None, None, None, True, 4)
		hill_shack = RoomWithPuzzle("Hill's Foot", "The old shack looms at the top of the hill. It might be a good idea to investigate it...to the south you see a shriveld old man sitting on a stump.", None, None, None, None, True, 5)
		shack_patio = RoomWithNPC("Sunny Stump", "Upon coming here, the old man seems to be looking at his oddly out of place smartphone.", None, None, None, None, True, None)
		river_area = RoomWithPuzzle("Raging River", "A river stands between you and a dark cave. To the east is a lone, young man sitting on a towel. The river is extrememy fast...", None, None, None, None, True, 6)
		picnic_area = RoomWithNPC("Sunny Spot", "The man appears to be in some sort of weird trance. He looks friendly though. Too friendly maybe.", None, None, None, None, True, None)
		dark_cave = RoomWithPuzzle("Dark Cave Entrance", "There's little light in here to see anything. It might be wise to not go in blindly...", None, None, None, None, True, 7)
		golden_door = RoomWithPuzzle("Gold Door", "After traveling a while, a huge golden door sits in front of you. It reads: \'ENTER PASSWORD\'", None, None, None, None, True, 8)
		
		# def __init__(self, name, talk_d, attack_d, fatal) for a NPC
		npc_1 = NPC("Hiker Joe", "Ahoy, mate! You're looking pretty beaten up! I would help you, but I'm in the middle of bear watching! These woods are filled with them!\nIf you ever see one, sleeping or not, the best thing to do is to SNEAK by them! Trust me.\nHey, if you want some grub, I have some stuff in my tent! Just don't make a bear mess in there! Haha!", "WOAH! What you think you're doing?! You're lucky you're not a bear, since I would immediatly beat your ass up!", False)
		npc_2 = NPC("Hermit Bill", "Hm? What brings you here, sonny? I rarely get visitors around here ever since the bear incident. You look like you want to access the Internet don't you?\nI know you young ones...always wanting to get the Internet without anyone's permission! Well, since you look desperate, I'll let you use mine.\nThe password is 1234567890...oh you're phone's dead? Sucker!", "SON. I'll have you know that I am a secret agent working here to kill anyone that tries to attack me in hopes to get my wifi.\nAnd you done fucked up.", True)
		npc_3 = NPC("High Hugo", "Sup dude? You look like you've been to some shit rave...man...times like this is when you just need to relax and drink some good 231.\nWhat's 231? Dude, that's the bro code for having a good time and when you need a easy solution to something. Remember it well. You'll thank me later.", "ASDFGHJJ TIME TO ACTIVATE BRO TIME! GET REKED!", True)
		
		# def __init__(self, path_destination, is_locked) for a Path
		path1_n = Path(thick_brush, False)
		path1_s = Path(tree_with_branch, False)
		path1_e = Path(hiker_area, False)
		path1_w = Path(crash_site, False)
		path2_n = Path(start_room, False)
		path3_w = Path(start_room, False)
		path3_s = Path(hiker_tent, False)
		path4_n = Path(hiker_area, False)
		path5_e = Path(start_room, False)
		path6_s = Path(start_room, False)
		path6_e = Path(open_field, True)
		path7_n = Path(bear_den, False)
		path7_e = Path(hill_shack, False)
		path7_s = Path(river_area, False)
		path7_w = Path(thick_brush, False)
		path8_w = Path(open_field, False)
		path9_w = Path(open_field, False)
		path9_s = Path(shack_patio, False)
		path10_w = Path(hill_shack, False)
		path11_e = Path(picnic_area, False)
		path11_s = Path(dark_cave, True)
		path11_n = Path(open_field, False)
		path12_n = Path(river_area, False)
		path12_s = Path(golden_door, True)
		path13_n = Path(dark_cave, False)
		
		start_room.set_exits(path1_n, path1_s, path1_e, path1_w)
		tree_with_branch.set_exits(path2_n, None, None, None)
		hiker_area.set_exits(None, path3_s, None, path3_w)
		hiker_tent.set_exits(path4_n, None, None, None)
		crash_site.set_exits(None, None, path5_e,None)
		thick_brush.set_exits(None, path6_s, path6_e, None) 
		open_field.set_exits(path7_n, path7_s, path7_e, path7_w)
		bear_den.set_exits(None, None, None, path8_w)
		hill_shack.set_exits(None, path9_s, None, path9_w)
		shack_patio.set_exits(None, None, None, path10_w)
		river_area.set_exits(path11_n, path11_s, path11_e, None)
		dark_cave.set_exits(path12_n, path12_s, None, None)
		golden_door.set_exits(path13_n, None, None, None)
		
		hiker_area.npc_character = npc_1
		shack_patio.npc_character = npc_2
		picnic_area.npc_character = npc_3
		
		print "You were enjoying a lovely evening on your hot date when suddenly, you forgot to use yout turn signal and ran into another car that was passing by!"
		print "You would have been fine if you weren't on a mountain, but you were and now your car was in a wreck and your date missing!"
		print "It's your goal now to salvage what you can find and get out of here!"
		
		self.set_room(start_room)
		while self.player.clear_game == False:
			print "\n"
			self.current_room.examine_room()
			self.command_parser()
			

########
# Main Method
print "Hello! What is your name? "
name = raw_input("> ")
print "Hello %s! Welcome to the Remasterd Adventure! Enjoy!" % name
game = Game(name)
game.play_game()
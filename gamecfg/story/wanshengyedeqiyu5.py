return {
	fadeOut = 1.5,
	mode = 2,
	id = "WANSHENGYEDEQIYU5",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Halloween Hijinks\n\n<size=45>5 An Uninvited Guest?</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "On the beach near the Halloween party venue, I found a pirate girl wearing a red hat.",
			bgm = "battle-highseasfleet-reborn",
			flashout = {
				black = True,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = True,
				alpha = {
					1,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "When I addressed her...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actorName = "???",
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Shh.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actorName = "???",
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Do you hear the ocean's cries?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "\"You mean the sound of waves hitting shore?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			actorName = "???",
			dir = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmph. I said they're the ocean's cries! Geez!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			action = {
				{
					type = "shake",
					y = 45,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "The pirate girl with the hat turned around and glared at me unhappily.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actorName = "???",
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Who are you?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "(Play along)",
					flag = 1
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			actorName = "???",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Aha, I see. So you're the one that my friends here... Ahem. You're the one that these lasses call the Commander.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actorName = "???",
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I am the mysterious, heartstopping shipgirl who rides wind and waves alike, searching all the seven seas for the beauties of the world...",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Royal Fortune, of the great Tempesta!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			},
			options = {
				{
					content = "(Stare vacantly)",
					flag = 1
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "What?! I just walked into the venue, okay?! Nobody tried to stop me!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "\"In that get-up, you:n't really stand out at a Halloween party. And pirate swords kind of look like Halloween props...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ah, well. This Halloween stuff is fun! But I'm the real thing, got it?! This ain't a costume!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "So, I'm looking for treasure hidden in this venue. Wanna search with me, Commander?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			action = {
				{
					type = "shake",
					y = 45,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "\"Huh? Wait, are you serious about that?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Of course! I'm Royal Fortune of the great Tempesta, after all!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But there are a lot of people here, so I probably won't: anything too crazy.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "If you can't rest easy with me running around,: you'll just have to scour the venue with me!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You're a Commander, aren't ya? Shouldn't you be watching over the shipgirls anyway?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "\"...Well, I definitely can't leave you alone now. I've got no choice; I'll tag along for a little while.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "\"But I haven't heard about any treasure buried in the venue...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "There's treasure! See?! It's written on this flyer!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "I read the flyer, and indeed it said, \"The first person to get the treasure gets free drinks for a week, nya!\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "As a pirate of the great Tempesta, I can't cast aside treasure lying before my very eyes!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*grumble* B-But first, I need food in my belly! Let us set sail toward the smell of delicious food! Yo ho, heave ho!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "She raised the cutlass at her hip and charged toward the food court.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			optionFlag = 1,
			say = "To protect the venue from the cutlass—much more dangerous than the girl wielding it—I rushed after her.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

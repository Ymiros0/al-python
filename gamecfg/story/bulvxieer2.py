return {
	fadeOut = 1.5,
	mode = 2,
	id = "BULVXIEER2",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"All-Love Assault!\n\n<size=45>2. Rain or Shine</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_main_day",
			say = "It's a dark, rainy day at the port...",
			bgm = "story-richang-1",
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
			},
			effects = {
				{
					active = True,
					name = "juqing_xiayu_da"
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Aww... This sucks. I wanted to go on a date with the Commander today...",
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
			expression = 4,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Whoa, speak of the devil! Hey, Commander!",
			painting = {
				alpha = 0.3,
				time = 1
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ Is this a coincidence, or were you coming to see me, hmm?",
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
			bgName = "bg_main_day",
			say = "As I turn the corner leading to my office, I bump into Blücher. She's been waiting here for me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_main_day",
			say = "\"Let me guess. You want me to take you on that date you decided on.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yup! You promised we would! You ready to head out?",
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
					content = "\"I thought we'd go in the evening?\"",
					flag = 1
				},
				{
					content = "\"It's pouring outside.\"",
					flag = 2
				},
				{
					content = "\"Let's go!\"",
					flag = 3
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah, but you're here 'cause you wanted to go now, right?",
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
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Don't tell me you were gonna sit:wn and start working. That's not gonna happen!",
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
			expression = 3,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "So what? I:n't care~",
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
			expression = 4,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "As long as I'm with you, the forecast is all sunshine and clear skies in my heart!",
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
			expression = 3,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 3,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ This rainy day's about to get a whole lot brighter!",
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
			bgName = "bg_main_day",
			say = "She and I go on a stroll around the port in the rain.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_main_day",
			say = "Then, we pass by the Iron Blood:rmitory and come across a friendly face.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 403020,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Morning, Eugen! Whatcha:ing? Going for a walk?",
			hidePaintEquip = True,
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
			actor = 403030,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Well, if it isn't the Commander and my favorite loudmouth.",
			hidePaintEquip = True,
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
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmph! That's no way to talk to your sister!",
			painting = {
				alpha = 0.3,
				time = 1
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yes, yes, I'm so very sorry. Anyway, what are you two up to? Are you on, dare I ask, a date?",
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
					content = "\"We're just walking around the port together.\"",
					flag = 1
				},
				{
					content = "\"Yeah, you could say that.\"",
					flag = 2
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Don't mince your words, Commander! Yes, we ARE on a date!",
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
					name = "juqing_xiayu"
				},
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Let me make this clear! We're not \"just walking around the port,\" we're on a romantic stroll!",
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
					name = "juqing_xiayu"
				},
				{
					active = False,
					name = "speed"
				}
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
			expression = 2,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Uh-huh. I see.",
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
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh my... You two sure got friendly while I wasn't looking.",
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
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "A little warning, Commander – she is extremely passionate when it comes to dates. Try to keep your wits about you, alright?",
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
			expression = 3,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ Love is meant to be expressed loud and clear, you know!",
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
			expression = 4,
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "C'mon, let's get moving, Commander! I've figured out where we're going next. You and I are gonna spend the whooole day together♪",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

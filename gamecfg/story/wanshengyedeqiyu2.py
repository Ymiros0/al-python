return {
	fadeOut = 1.5,
	mode = 2,
	id = "WANSHENGYEDEQIYU2",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Halloween Hijinks\n\n<size=45>2 Faerie Princess' Garden of Rest</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "I faced the old castle, which exuded more awe-inspiring presence than ever on Halloween night.",
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
			say = "The cross at the tip of the tower almost seemed to emit its own light in the moonlight... What sort of being was within?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "I pushed the:or open with that question in my mind.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 206071,
			side = 2,
			bgName = "star_level_bg_162",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "A human intrudes on the sanctuary of the night's scion...",
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
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Unwelcome mortal, for what reason: you disturb my eternal dreams?",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "Sitting on the blood-red throne, Albion—wearing a costume akin to a succubus or vampire—welcomed me in.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "She's acting really different... How should I respond?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"I like your costume, Albion.\"",
					flag = 1
				},
				{
					content = "\"'Tis I, a lowly servant of the night.\"",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "Thank you, Commander... Ah! I mean! Umm...",
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
			expression = 5,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "Ack... How could I drop the act just from hearing my name? I'm sorry, this is so embarrassing...",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "My vampire elders said I could order you around in this costume, but it's still so hard...",
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
			expression = 7,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "Ah, but forget my act... Commander, if you'd please, erm...",
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
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "Would you like to spend some time with me...?",
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
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "Y-you:n't have to try to play along like that...",
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
			expression = 7,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 206071,
			nameColor = "#A9F548FF",
			say = "But... Ahem. \"Underling of Albion,: you desire to spend this delightful night with your master?\"",
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
			optionFlag = 2,
			say = "\"But of course.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "Albion handed me a glass. The crimson liquid within sparkled like ruby in the moonlight.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "\"Is this...wine?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Not quite. It's grape juice colored to look like wine.",
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
			expression = 7,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I think the refreshing sweetness of it is perfect for a night like tonight.",
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
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Umm, so, Comm—ahem. Underling of Albion, per our solemn vow to spend this delightful night together...",
			hidePaintEquip = True,
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
			expression = 3,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "W-well, this is all an act, so why:n't you stay a little longer...",
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
			expression = 5,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Kneel, promise your loyalty, and:... Oh, never mind...",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_162",
			actor = 206071,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Nothing! I said nothing! Please forget what you just heard!",
			hidePaintEquip = True,
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
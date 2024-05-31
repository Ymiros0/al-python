return {
	fadeOut = 1.5,
	mode = 2,
	id = "BIHAIGUANGLIN10",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			soundeffect = "event./battle/boom2",
			side = 2,
			bgName = "bg_daofeng_3",
			nameColor = "#a9f548",
			dir = 1,
			bgmDelay = 1,
			say = "KABOOOOM!",
			bgm = "map-longgong",
			flashin = {
				delay = 1,
				dur = 1,
				black = True,
				alpha = {
					1,
					0
				}
			},
			flashN = {
				color = {
					1,
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2,
						0
					},
					{
						1,
						0,
						0.2,
						0.2
					},
					{
						0,
						1,
						0.2,
						0.4
					},
					{
						1,
						0,
						0.2,
						0.6
					}
				}
			},
			dialogShake = {
				speed = 0.09,
				x = 8.5,
				number = 2
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_daofeng_3",
			dir = 1,
			say = "The seal around the mechanism dissipated under a fiery onslaught from Katsuragi's planes.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			side = 2,
			actorName = "Mysterious Voice",
			bgName = "bg_daofeng_3",
			nameColor = "#ffff4d",
			dir = 1,
			say = "\"Congratulations... But your trial:es not end here. Continue onwards.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_daofeng_3",
			dir = 1,
			say = "As the mysterious voice faded, so too did the violent wind and waves.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_daofeng_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 301290,
			say = "Huh, smashing that thing really did the trick!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 301480,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hey, uh... What's with this pedestal...?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 301470,
			dir = 1,
			nameColor = "#a9f548",
			say = "Yamakaze, I:n't think it's advisable to touch other people's belongings...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "That's right! We're still in enemy territory, so:n't go around touching random objects without telling us first!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 301480,
			dir = 1,
			nameColor = "#a9f548",
			say = "True, True! Phew, that was a close one...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_daofeng_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 301290,
			say = "Say, how'd you know that the building was controlling everything?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "Well, let's just say... This whole thing seems to be based off of the Sakura Empire's rituals, and I happen to know a thing or two about that... *snap*!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_daofeng_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 301290,
			say = "Woaaah! That's incredible, Katsuragi!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "Ahaha! Don't underestimate the power of a full-fledged aircraft carrier!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_daofeng_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 301290,
			say = "I wonder who's more knowledgeable about these things between you and Yura~",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "Uh, about that! Not like it matters, because you have me here!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 301480,
			dir = 1,
			nameColor = "#a9f548",
			say = "Does it really not matter...?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			actor = 307120,
			side = 2,
			bgName = "bg_daofeng_3",
			nameColor = "#a9f548",
			dir = 1,
			say = "O-of course not! What's the point of asking? Let's hurry up and keep moving!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_daofeng_3",
			actor = 307120,
			dir = 1,
			blackBg = True,
			nameColor = "#a9f548",
			say = "Otherwise, we're going to fall behind Team Chikuma! Shimakaze, I'll be counting on you to scout ahead!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		}
	}
}

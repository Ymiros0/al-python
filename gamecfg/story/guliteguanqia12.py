return {
	fadeOut = 1.5,
	mode = 2,
	id = "GULITEGUANQIA12",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			say = "Town - Northeast Sector",
			side = 2,
			bgName = "bg_ssss_1",
			dir = 1,
			bgmDelay = 2,
			bgm = "ssss-az-pv",
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
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800020,
			say = "Everyone's gone, huh.",
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
			actor = 10800010,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "When I was walking to school this morning, the town was still full of people... What happened...?",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 900318,
			say = "The Sirens probably decided that it's not worth the effort to keep up the illusions anymore.",
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
			actor = 202111,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "And, that \"Mujina\" person is out there somewhere.",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "Oh! That reminds me, I saw a familiar face on my way over here!",
			effects = {
				{
					active = True,
					name = "memoryFog"
				}
			},
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
			actor = 10800060,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Who: you think it was?",
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
			actor = 10800050,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Mujina?",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "Eh? How'd you know?!",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 900318,
			say = "I guess you were pretty far away when the kaiju appeared.",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "Oh, so that was the kaiju you defeated earlier?",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "But, I saw her before all that happened! And, she was wearing some kind of weird gear... Now that I think about it, it looked kinda like the rigging we have on now!",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "She was rushing towards the beach... and she looked pretty agitated.",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800060,
			say = "If you asked me, it didn't look like she was off to:minate some kaiju...",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 102163,
			say = "In other words, the Sirens \"promised\" her something, just like with Akane... They must've made her rigging as well.",
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
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 102163,
			say = "But we won't know for sure until we ask her in person...",
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
			actor = 307032,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Until Purifier gets her memories back, we can only pray for more information about who the mastermind behind all this is.",
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
			actor = 307032,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "On the other hand, we can't just leave the situation as it is, particularly when someone from another world is involved.",
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
			actor = 202111,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Ugh, I'm getting exhausted just from thinking about all this...",
			effects = {
				{
					active = False,
					name = "memoryFog"
				}
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
			expression = 1,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 10800020,
			say = "You're welcome to take a nap on my rigging if you're tired~",
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
			actor = 202111,
			side = 2,
			bgName = "bg_ssss_1",
			hidePaintObj = True,
			dir = 1,
			blackBg = True,
			nameColor = "#a9f548",
			say = "That's alright... After all, today's gonna be the day I prove my worth to Bel!",
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

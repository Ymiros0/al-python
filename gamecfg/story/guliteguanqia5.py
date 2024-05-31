return {
	fadeOut = 1.5,
	mode = 2,
	id = "GULITEGUANQIA5",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			bgm = "ssss-az-pv",
			side = 2,
			bgName = "bg_ssss_1",
			dir = 1,
			bgmDelay = 2,
			hidePaintEquip = True,
			actor = 10800010,
			nameColor = "#a9f548",
			say = "Oh, it went through.",
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
			expression = 3,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800010,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hello? Akane? Where are you?",
			hidePaintEquip = True,
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800020,
			dir = 1,
			nameColor = "#a9f548",
			say = "Rikka? Don't worry~ I've got the kaiju in check.",
			hidePaintEquip = True,
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
			say = "In check... What:es she mean by that?",
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
			actor = 10800010,
			dir = 1,
			nameColor = "#a9f548",
			say = "Huh? What: you mean? I:n't get you at all.",
			hidePaintEquip = True,
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
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "The kaiju was headed towards the school, so I stopped it in its tracks~ But wow, I never thought I'd be able to see such an amazing kaiju, hehe.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800020,
			dir = 1,
			nameColor = "#a9f548",
			say = "Did you know? Roon's rigging is super awesome!",
			hidePaintEquip = True,
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
			actor = 102163,
			say = "Roon? Rigging...?",
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
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "Are you listening~? Her main battery's ready to fire, she's about to blow!",
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
			actor = 10800010,
			side = 2,
			bgName = "bg_ssss_1",
			nameColor = "#a9f548",
			dir = 1,
			say = "Um, as I was saying, what exactly a...",
			hidePaintEquip = True,
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
			say = "BOOOOOOM!!!",
			side = 2,
			bgName = "bg_ssss_1",
			dir = 1,
			soundeffect = "event./battle/boom2",
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
			expression = 2,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800010,
			dir = 1,
			nameColor = "#a9f548",
			say = "Wha?! What was that sound?!",
			hidePaintEquip = True,
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
			expression = 1,
			side = 2,
			bgName = "bg_ssss_1",
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "So, did you hear it~? Front row seats to a concerto of cannonfire!",
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
			actor = 102163,
			say = "She's right! The kaiju's stopped moving!",
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
			bgName = "bg_ssss_1",
			paintingNoise = True,
			dir = 1,
			actor = 900318,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Ahahahaha! Anyone who gets in my way... will be torn apart!!",
			effects = {
				{
					active = True,
					name = "speed"
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
			expression = 3,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800010,
			dir = 1,
			nameColor = "#a9f548",
			say = "Is that... Roon? Did she really manage to stop that thing?",
			hidePaintEquip = True,
			effects = {
				{
					active = False,
					name = "speed"
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800020,
			dir = 1,
			nameColor = "#a9f548",
			say = "Yup. She made some kaiju-esque \"rigging\" or something appear, and it packs an insane punch! It also seems to be automated!",
			hidePaintEquip = True,
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
			expression = 3,
			side = 2,
			bgName = "bg_ssss_1",
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "People change when they're thrust into battle. It's sooooo fascinating!",
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
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "Anyway, like I said, there's no need for you to worry about me~ I'll wrap things up over here.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_ssss_1",
			actor = 10800020,
			dir = 1,
			nameColor = "#a9f548",
			say = "Just head to some place safe and wait for me there, okay?",
			hidePaintEquip = True,
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
			paintingNoise = True,
			dir = 1,
			hidePaintEquip = True,
			actor = 10800020,
			nameColor = "#a9f548",
			say = "Kay, well, I'm hanging up now. Hey, Roon! Can you: that one more time?",
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
			dir = 1,
			blackBg = True,
			hidePaintEquip = True,
			actor = 10800010,
			nameColor = "#a9f548",
			say = "She hung up... I have no idea what's going on, but she seems to be:ing... just fine?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		}
	}
}

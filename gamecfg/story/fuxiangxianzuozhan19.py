return {
	fadeOut = 1.5,
	mode = 2,
	id = "FUXIANGXIANZUOZHAN19",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			soundeffect = "event./battle/boom2",
			side = 2,
			bgName = "bg_fuxiangxian_2",
			say = "KABOOOOM!",
			dir = 1,
			bgm = "xinnong-2",
			flashN = {
				color = {
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2
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
			expression = 3,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 402050,
			dir = 1,
			nameColor = "#a9f548",
			say = "Enemy cannon fire! These:n't seem to be ordinary practice rounds!",
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
			expression = 4,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 402050,
			dir = 1,
			nameColor = "#a9f548",
			say = "What are they:ing? They can't be using live ammunition in– Eeeek!",
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
			say = "KABOOOOM!",
			side = 2,
			bgName = "bg_fuxiangxian_2",
			dir = 1,
			soundeffect = "event./battle/boom2",
			flashN = {
				color = {
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2
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
			expression = 6,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 401240,
			dir = 1,
			nameColor = "#a9f548",
			say = "How foolish these Pawns are! Soon they shall learn why any and all that dare oppose me swiftly cease to be!",
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
			expression = 4,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 402050,
			dir = 1,
			nameColor = "#a9f548",
			say = "C-calm:wn now, Z24! They're just practice dummies; they wouldn't use live ammo, and they've never attacked anyone out of nowhere before!",
			soundeffect = "event./battle/boom2",
			flashN = {
				color = {
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2
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
			expression = 9,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 401240,
			dir = 1,
			nameColor = "#a9f548",
			say = "Then how: you explain them:ing exactly that? Eugen, I demand an explanation!",
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
			bgName = "bg_fuxiangxian_2",
			actor = 401240,
			dir = 1,
			nameColor = "#a9f548",
			say = "Eugen, where are you? Answer me!",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 403030,
			dir = 1,
			nameColor = "#a9f548",
			say = "I thought I heard someone calling for me. What is it?",
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
			paintingNoise = False,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 402050,
			dir = 1,
			nameColor = "#a9f548",
			say = "Eugen? When did you get so far away?",
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
			bgName = "bg_fuxiangxian_2",
			actor = 401240,
			dir = 1,
			nameColor = "#a9f548",
			say = "What is going on in this place? These \"practice dummies\" just fired at us using live ammunition!",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 403030,
			dir = 1,
			nameColor = "#a9f548",
			say = "Sorry, I need a bit more time on my end. I just got word from a Sakura fleet.",
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
			bgName = "bg_fuxiangxian_2",
			paintingNoise = False,
			dir = 1,
			actor = 401240,
			nameColor = "#a9f548",
			say = "What...? There are Sakura ships here in the base that aren't just Pawns?",
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
			bgName = "bg_fuxiangxian_2",
			actor = 403030,
			dir = 1,
			nameColor = "#a9f548",
			say = "Look, just keep:ing evasive maneuvers for now. They won't hit you as long as you keep your distance.",
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
			bgName = "bg_fuxiangxian_2",
			paintingNoise = False,
			dir = 1,
			actor = 402050,
			nameColor = "#a9f548",
			say = "D-did you hear her? They're using live ammunition!",
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
			bgName = "bg_fuxiangxian_2",
			actor = 403030,
			dir = 1,
			nameColor = "#a9f548",
			say = "Fine, lead them to my location:. I'll figure something out.",
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
			bgName = "bg_fuxiangxian_2",
			paintingNoise = False,
			dir = 1,
			actor = 401240,
			nameColor = "#a9f548",
			say = "\"Figure something out\"? What is that supposed to mean?",
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
			bgName = "bg_fuxiangxian_2",
			actor = 403030,
			dir = 1,
			nameColor = "#a9f548",
			say = "Just: as I say, okay? Focus on not getting hit.",
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
			paintingNoise = False,
			side = 2,
			bgName = "bg_fuxiangxian_2",
			actor = 402050,
			dir = 1,
			blackBg = True,
			nameColor = "#a9f548",
			say = "Leipzig would've keeled over if she was in my shoes... Anyway, understood! We'll: our best!",
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

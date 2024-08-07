return {
	fadeOut = 1.5,
	mode = 2,
	id = "NIZHUANCAIHONGZHITA4",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			say = "Tower of Midgard - Pier",
			side = 2,
			bgName = "bg_midgard_2",
			dir = 1,
			bgmDelay = 1,
			bgm = "bsm-4",
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
			dir = 1,
			side = 2,
			bgName = "bg_midgard_2",
			say = "Not long after the girls finished their meals, the ground began to rumble.",
			dialogShake = {
				speed = 0.08,
				x = 15,
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
			expression = 1,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 403100,
			say = "Hey, who put the facility on vibrate?",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "That's just the Singularity generator powering up. Nothing to worry about.",
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
			actor = 403090,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hi there, Strasser! Just making sure. we've gotta go stand guard around the facility, right?",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "Correct, and you are to stay on guard until Ulrich's team finishes and returns from the Singularity. Understood?",
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
			actor = 403090,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "You got it! And if it goes well, Eisen and I will finally get some time off!",
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
			actor = 407030,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "The key word is, \"if.\" The Sirens will start coming for the Tower now that we've lost our active camouflage.",
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
			actor = 403090,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Not a problem! I could use some after-lunch exercise.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406010,
			say = "This is Weser. I have a report to make.",
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
			bgName = "bg_midgard_2",
			expression = 2,
			dir = 1,
			actor = 406010,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "The Sirens have indeed noticed us and are on their way to attack.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "Already? They're faster than I expected.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "Sooo, there's good news and bad news. Which: you want to hear first?",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "It makes no difference. Just tell me.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "Okay, the good news is, the Siren forces consist of mostly mass-produced ships.",
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
			bgName = "bg_midgard_2",
			expression = 1,
			dir = 1,
			actor = 408120,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "And the bad news is... they're all heading straight for us, almost like they're being pulled in by gravity!",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "I see... So you were scouting all this time? Is that why you weren't at the cafeteria?",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "Yeah. I saw Weser head out, so I thought I'd better tag along!",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 402060,
			say = "So neither of you have had lunch...",
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
			bgName = "bg_midgard_2",
			expression = 4,
			dir = 1,
			actor = 408120,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Nah, we just went and ate at a different cafeteria!",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "Anyway, we can't really enter the Singularity yet, can we? Sirens come first, right?",
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
			actor = 407030,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Indeed. We must seize the initiative against them.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "Your team, however, will proceed to the Singularity's entrance. Ulrich is waiting for you there.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 403100,
			say = "You sure you:n't need our help?",
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
			actor = 407030,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Would you not waste time questioning my orders? My mission is to ensure you get inside the Singularity.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 407030,
			say = "And your mission is to explore the Singularity and return safely. Remember that.",
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
			actor = 403100,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "You're the boss... Then let's not keep Ulrich waiting.",
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
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 403100,
			say = "Let's go, Elbe, Magde, and U-1206.",
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
			actor = 403100,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Oh, and Heinrich, good luck with the Sirens and all that.",
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
			actor = 403090,
			side = 2,
			bgName = "bg_midgard_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Thanks, but I:n't need luck! I've got a belly full of food and I'm ready to: some damage!",
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
			bgName = "bg_midgard_2",
			dir = 1,
			blackBg = True,
			actor = 403090,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Time to go! Let's get 'em, Eisen!",
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
		}
	}
}

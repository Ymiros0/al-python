return {
	id = "ANJINBUYECHENG7",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_154",
			say = "Ten minutes later...",
			bgm = "story-antarctica-serious",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "login",
			say = "That building is the Manjuu Tower.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "I hope you're satisfied with your delivery.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "main1",
			say = "Allow me to introduce myself properly. I'm Sovetsky Soyuz, a member of the resistance.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Tallinn from Block 33's security office contacted me.",
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
					content = "Tallinn did that?",
					flag = 1
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Yep. I:n't know the details, but security told me everything.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "main2",
			say = "If not for their nanocircuit, I wouldn't have found you anywhere near as quickly.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "They promised to keep the riots from getting close to the Manjuu Tower, too.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "As a result, it all worked out.",
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
			actor = 705021,
			side = 2,
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Charging in head-on would be reckless. We'll have to detour around the security force's defensive line.",
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
			bgName = "star_level_bg_154",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "We're running straight up to the top floor of the tower. Get ready.",
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
			bgName = "star_level_bg_154",
			say = "The already-familiar weightlessness comes over me again, and we charge directly to the top-floor office of the Manjuu Tower.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "*CRASH!*",
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
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "mission",
			say = "...We've arrived at the target area.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Through that elevator, we can reach the data center up above.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "This is the end. It's up to you to remake the Sleepless City with your own hands...",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "And end all of this.",
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
			actorName = "???",
			bgName = "bg_story_task",
			nameColor = "#FF9B93",
			say = "Heehee. I will say, it is an admirable idea.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_story_task",
			nameColor = "#FF9B93",
			say = "However... You're far too naïve.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_story_task",
			nameColor = "#FF9B93",
			say = "Well:ne on a successful delivery, Agent Arctic Hare – Sovetsky Soyuz.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "The leather chair behind the office's desk spins around to reveal the person sitting in it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "main4",
			say = "Boss... Avrora?",
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
			actor = 0,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Commander",
			nameColor = "#A9F548FF",
			say = "(They know each other?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Why are you here, Boss?\"",
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
			actor = 705021,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "touch",
			say = "W-wait. It can't be...",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Well, aren't you smart?",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "You already understand the situation. But of course – you are my dear subordinate.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "headtouch",
			say = "The resistance... was working with the Great all along?",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Working WITH the Great? Hmm, not quite.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "The Great:esn't understand that the resistance is the True master of the city.",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Without the resistance, the order of this city would have collapsed a long time ago.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "The hope we provide unites this city.",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Unfortunately, that manjuu fool is in cahoots with the mafia now...",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "He:esn't know that Poltava's ambition won't be so easily sated...",
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
					content = "So the resistance attacked Valiant, after all?",
					flag = 1
				}
			}
		},
		{
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Heehee, how slanderous. I didn't fire the gun.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "But that's enough. This farce is coming to an end.",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Playtime is over, Knight. Why:n't you just give up and hand over the Ascension Box?",
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
					content = "I refuse...",
					flag = 1
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "Is that so?",
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
			actor = 702012,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			nameColor = "#FF9B93",
			say = "Do it, Agent Arctic Hare.",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "touch",
			say = "......",
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
			actor = 705021,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = ".........",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "Wh-why aren't you:ing it?",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "...!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "By the time Avrora turns to Soyuz, a flash bang is already on its way to her.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "*CRASH!*",
			soundeffect = "event./battle/boom2",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
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
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "Kh... You betray me?!",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "main1",
			say = "Comrade Commander, this way!",
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
			bgName = "bg_story_task",
			say = "\"Thank you for using the Manjuu Tower elevator. Selection. top floor.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = True,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
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
			bgName = "bg_story_task",
			say = "\"Please input access key.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = "main3",
			say = "Comrade Commander, use the Ascension Box!",
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
			actor = 705021,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "There's no time—",
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
			bgName = "bg_story_task",
			say = "There's a whoosh as the pursuer's bullet strikes the wall of the elevator.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "I won't let you go that easily...!",
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
			bgName = "bg_story_task",
			factiontag = "Resistance Agent",
			dir = 1,
			actor = 705021,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Leave her to me. Commander... Do the right thing!",
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
					content = "(Use the Ascension Box.)",
					flag = 1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "You used the Ascension Box!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			icon = {
				scale = 2,
				image = "Props/story_tongtianzhixia",
				pos = {
					0,
					0
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "Welcome back, Administrator. Have a pleasant day.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Resistance Leader",
			dir = 1,
			actor = 702012,
			nameColor = "#FF9B93",
			say = "Noooooo!",
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
			bgName = "bg_story_task",
			say = "Avrora fires a few more shots, but an energy barrier is deployed just in time to stop them.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "The elevator:or inexorably closes.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			actor = 9702070,
			factiontag = "Illusion",
			dir = 1,
			blackBg = True,
			nameColor = "#A9F548FF",
			say = "It's time to end this, Knight.",
			painting = {
				alpha = 0.3,
				time = 1
			},
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
			blackBg = True,
			say = ".........",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			blackBg = True,
			say = "......",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
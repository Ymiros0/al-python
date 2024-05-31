return {
	fadeOut = 1.5,
	mode = 2,
	id = "SHUIXINGJINIAN1",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Work Hard, Play Harder!\n\n<size=45>1 A Sunny Afternoon</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "One afternoon at the office...",
			bgm = "story-1",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Commander, I've finished going through all the:cuments. There's just one problem...",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Every Northern Parliament exercise participant was supposed to turn in a report, but we're still missing one.",
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
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Avrora looks a bit annoyed. I wonder if she knows whose report is missing.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Suddenly, I hear the sound of boots clopping:wn the hallway. Soon, a dark-haired girl wearing a Northern Parliament uniform throws the:ors of the office open.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "*yaaawn*... Yoohoo, Commander!",
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
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "It's Pamiat' Merkuria... with dark circles under her eyes.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"Full of energy as always, I see.\"",
					flag = 1
				},
				{
					content = "\"Hey. It's afternoon, if you didn't notice.\"",
					flag = 2
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			optionFlag = 1,
			say = "I'm only half sarcastic. She clearly has not gotten enough sleep, yet still acts as cheerful as ever.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			optionFlag = 1,
			actor = 702020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Wh-what? Of course I am! Are you concerned about me or something~?",
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
			expression = 6,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			optionFlag = 2,
			actor = 702020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hehehe~ Afternoon, schmaftersploon. All that matters is that I'm here!",
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
			bgName = "bg_story_task",
			dir = 1,
			optionFlag = 2,
			actor = 702020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Besides, it's morning somewhere in the world even if it's afternoon here~",
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
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			optionFlag = 2,
			say = "...Clearly, sleep deprivation was no match for her cheekiness.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "Anyway, uh, I've come to drop off some paperwork.",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "Let's see... Here are the records from the Northern Parliament's last battle, and here's the... Wait, where's the after-action report?",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "Oh right, I left it right– Eek!",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oh no!",
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
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "After finding her paperwork, Pamiat' tries to: a triumphant twirl but immediately loses her balance. Fortunately, Avrora is there to catch her.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "Phew, that was close! Thanks for the hand, Avrora. Anyway, I'll leave the stuff on your desk, Commander, so:n't forget to look it over. I'm gonna head back to the:rm now!",
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
					content = "\"Do you need someone to escort you?\"",
					flag = 1
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 702020,
			say = "Hehehe~ I'll be just fine! See ya later! ...Owww, my back...",
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
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "The way she was clutching her back as she tottered out the:or makes me consider sending someone to accompany her anyway...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "She has always been like that. I'm more concerned about her unhealthy lifestyle though.",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "She got hooked on a new video game she bought the other day, and has been so absorbed in it that she hasn't been keeping up with work...",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I believe it's what they call \"going goblin mode.\"",
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
			actor = 702010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "If you think it's warranted, should we go check on her?",
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
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "It definitely isn't a good idea to leave her to her own devices forever, but I also:n't want to bother her if she went back to sleep.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Maybe I'll pay her a visit after dinner.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

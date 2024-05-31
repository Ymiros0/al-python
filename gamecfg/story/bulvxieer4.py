return {
	fadeOut = 1.5,
	mode = 2,
	id = "BULVXIEER4",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"All-Love Assault!\n\n<size=45>4. To Go Beyond the Port</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "It's a regular, uneventful day...",
			bgm = "story-richang-2",
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
			bgName = "bg_story_task_2",
			say = "Today it's back to work. I'm chewing through paperwork when suddenly, Blücher speaks up.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 403020,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Hmm... Where should we go on a date after work today...",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Maybe the Scharlachroter Tresen? No, we've been there so many times you're probably bored with it...",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "What about the aquarium? It's comfy and tranquil, but we won't have much time before they close...",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Thoughts, Commander? Where: you wanna go?",
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
					content = "\"Scharlachroter Tresen.\"",
					flag = 1
				},
				{
					content = "\"The aquarium.\"",
					flag = 2
				},
				{
					content = "\"You decide.\"",
					flag = 3
				},
				{
					content = "\"I'm working overtime today.\"",
					flag = 4
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ Then that's where we'll go!",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Eugen recommended the coffee soda with extra sugar. We should give it a try! I bet it tastes as sweet as my love:es!",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh boy, I can't wait for this shift to end!",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ Aquarium it is! Mind if I go grab my camera before we head out?",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I wanna take pics of the fish, and more importantly, of you, my sweetheart~",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 3,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh☆ The place:esn't matter as long as I'm there, am I right?",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 3,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I couldn't agree more~ Wherever I am, I'm happy if you're by my side♪",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 3,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I love you so much, Commander! I'll let my gut decide where we'll go!",
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
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 4,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "NO! You are NOT working overtime, full stop!",
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
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			dir = 1,
			optionFlag = 4,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmph! If you're gonna be that way, I'll just decide on my own!",
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
			bgName = "bg_story_task_2",
			say = "Eugen was right about Blücher. She is mind-bogglingly passionate when it comes to dates.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "Of course, that's just how she expresses her honest – albeit overbearing – affection.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "Having known her for a while now, I've more or less gotten used to it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...There we go, all:ne! I've even made plans for dates several days from now~",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, by the way! I wanna travel somewhere with you on your next holiday! Like to a ski resort or something!",
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
			bgName = "bg_story_task_2",
			say = "\"You want to go skiing?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 403020,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Yeah! I know a great resort! It just takes some time to get there~",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "We've been all around the port already, and I wanna see the world with you!",
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
			bgName = "bg_story_task_2",
			dir = 1,
			hidePaintEquip = True,
			actor = 403020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "That, and I wanna say and hear \"I love you\" in novel, romantic places~ Heheh♡",
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

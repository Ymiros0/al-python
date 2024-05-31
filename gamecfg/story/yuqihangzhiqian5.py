return {
	id = "YUQIHANGZHIQIAN5",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"The Bon Before the Voyage\n\n<size=45>5 Before the Launch</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "For a fourth time, I stand before the:or to the Cruise Planning Committee.",
			bgm = "story-richang-10",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Right as I press my ear against the:or, it suddenly opens.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "Heehee. Here to eavesdrop again, are you, dear human?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = False,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
				black = False,
				alpha = {
					1,
					0
				}
			},
			options = {
				{
					content = "Huh? How long have you known?",
					flag = 1
				},
				{
					content = "I haven't broken my promise! Long Island never spoke TO me!",
					flag = 2
				}
			}
		},
		{
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "Since the first time you set foot outside your office. \"You're as subtle as a brick through a window.\"",
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
			bgName = "star_level_bg_169",
			dir = 1,
			optionFlag = 2,
			actor = 900429,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "\"Of course. Whatever you say.\" Oh, you are such a darling human, making clever excuses.",
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
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Don't be alarmed, though. Long Island:esn't know that you're here.",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "Her attention is solely on her work, if you can call it that. \"She's concentrating, in her own way.\"",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Let me guess... You knew I'd come here, so you specifically put Long Island in charge of the phone.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "\"Heehee. I thought it was obvious.\" We knew that curiosity would get the better of you, yet you didn't have the heart to break your promise.",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "So it was easy to surmise that you'd walk the razor's edge, coming here merely to eavesdrop.",
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
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "And so, we employed Long Island and knowingly let you listen in on her. \"It's adorable how predictable you are, human.\"",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "Don't worry about what she said on the phone. All the things she discussed have been brought before the Central Committee.",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "All the inane ideas, discarded. \"And all the good ones, kept.\"",
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
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Now all you need to:, dear human, is be patient and wait.",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "They KEPT some of the ideas? So:...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Did they keep the onboard garden?",
					flag = 1
				},
				{
					content = "Did they keep the onboard aquarium?",
					flag = 2
				},
				{
					content = "Don't tell me they kept the blast:or!",
					flag = 3
				},
				{
					content = "Please:n't tell me they kept the ammo storage!",
					flag = 4
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "Heehee. A promise is a promise, dear human. No amount of pleading will coax an answer out of Emden. \"Remember, it's meant to be a surprise.\"",
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
			actor = 900429,
			side = 2,
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Although, there is actually important one thing WE were hoping to ask YOU.",
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
			bgName = "star_level_bg_169",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 900429,
			say = "Have you thought of a name for the cruise ship yet?",
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

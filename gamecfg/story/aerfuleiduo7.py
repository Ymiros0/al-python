return {
	fadeOut = 1.5,
	mode = 2,
	id = "AERFULEIDUO7",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"The Sensationalist Sensation\n\n<size=45>Someone Else's Front-Page News</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "Early morning, several days later...",
			bgmDelay = 2,
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
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "*yaaawn*... Morning, Commander.",
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
			say = "Alfredo enters my office looking sleep-deprived. Again. She's been like this for the past few days, in fact.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Mgh... Hey, I'm fine. Don't worry about me...",
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
			actor = 601080,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I've just been really busy making articles out of the material I got from the ball...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Sorry 'bout my lack of energy. I know you've been singlehandedly:ing all the work I'm supposed to: as your secretary. I really appreciate it!",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Now my slacking days are over, though! The latest issue of the Port Journal is finished! It's all about the ball. Check it out!",
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
			say = "She hands me the magazine, which:es have the look of a magnum opus about it. However, her expression turns from elated to sour.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Unfortunately, my work was for nothing...",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "All because of THIS!",
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_story_task_2",
			say = "She hands me another newspaper. The front page features a bold headline...",
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
			say = "\"You Will Not Believe Who the Commander Danced With at the Ball!\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "Below it is a picture of me and Alfredo in the middle of our dance. It seems someone photographed us without our knowledge.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Frickin' Aoba!",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "She knew you're all the buzz right now and she beat me to it!",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Urgh! The headline just reeks of sensationalism, too! I can't believe she stole my spotlight with THIS of all things!",
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
			say = "It's pretty hypocritical to call others sensationalist, considering the headline she herself chose, but I digress.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "\"Look at this way – you still made front-page news.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			say = "\"Maybe not in the way you'd hoped, but the fact remains that you're the talk of the port now.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Oh please! That's not funny, Commander!",
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "*sigh*... Even though I got played for a fool, somehow I:n't feel salty about it.",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Because at the end of the day, I did get to have an unforgettable dance with you♪",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Hey, that gives me an idea! I could always embellish a few details and feature that story in the next issue!",
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
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Then throw in a spicy headline, like... \"The Secret Romance Between the Commander and a Dancer\"! Yeah, THAT'LL cause a real sensation!",
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
			say = "\"I invoke my right to remain anonymous.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Nuooooooooooooooo!",
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

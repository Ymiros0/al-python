return {
	id = "HAITIAN1",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Set Sail! An Inspiration-Seeking Journey\n\n<size=45>1 Writer's Block</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "Port - Office",
			bgm = "story-richang-2",
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
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Commander, I've brought you the itinerary for next week. Please go over it.",
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
			hidePaintObj = True,
			say = "Hai Tien, the newly-appointed secretary ship, hands me a schedule for the upcoming week as well as the corresponding task list.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "The schedule is packed with detailed notes, and the task list is numbered in order of priority. Everything is logically arranged and beyond reproach.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "However–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "The super-focused girl:esn't seem to notice that there are some peculiar strips of paper stuck to the:cuments she just handed me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(\"She leaps as hard as she can into the arms of the one she loves...\" Scribbles. \"Her lover's embrace is so strong, yet so very warm...\" More scribbles.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Scribbles... \"The rain surrounds the two of them like a silken veil, casting the illusion that nothing exists between heaven and earth except for each other...\" Scribbles.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Huh. Is this a story that Hai Tien has been working on?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(There are a lot of things scribbled out, and she clearly threw the paper into a shredder... Maybe she's been struggling with her work?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Though, writing a novel is a time-consuming process. Formulating the story's framework is no easy feat...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "After gathering my thoughts, I decide to...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Give Hai Tien the rest of the day off.",
					flag = 1
				},
				{
					content = "Ask Hai Tien about the matter.",
					flag = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "Mm. According to the itinerary, I should be able to take care of everything on my own today.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "Why:n't you go back and get some rest? Oh, but I:n't mind if you'd like to stay in the office to get your personal work:ne.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "(There's no point making wild speculation. I might as well ask her since she's already here...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "Hai Tien, has something been bothering you lately?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Huh? What: you mean by...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "D-did I: something to displease you? Have I failed to meet your expectations as secretary ship in any way?",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "That's not it at all. If anything, you've been:ing remarkably well considering you were just assigned the job.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "You've already helped me in a whole lot of ways, so I'd like to take this opportunity to return the favor.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Umm... If that's the case, I will accept your gracious offer.",
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
			actor = 502070,
			say = "...So that's basically the gist of things.",
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
			expression = 6,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "I've been going through a bit of writer's block, and now I can't come up with anything remotely satisfying anymore...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Have you tried drawing inspiration from other works? Maybe a song or an old masterpiece of some sort?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "The girl shakes her head helplessly.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "I already tried that, but it didn't: anything.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Oh, I've got just the thing! You know how in the olden days, people would take long journeys through the rivers and mountains to draw inspiration for their poetry?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Why:n't we go on a camping trip of our own and give that a try? Maybe you'll find your inspiration somewhere along the way!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

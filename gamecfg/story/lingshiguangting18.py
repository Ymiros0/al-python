return {
	fadeOut = 1.5,
	mode = 2,
	id = "LINGSHIGUANGTING18",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			bgm = "hunhe-level",
			actor = 204030,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "\"Thank you for coming. It would be my pleasure to contribute to this operation with a speech and tactical advice.\"",
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
			},
			effects = {
				{
					active = True,
					name = "jinguang"
				},
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			paintingNoise = False,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			say = "Morale was high among the Royal Navy during Operation Siren. They were eager to join arms with the Eagle Union and repel the Sirens from the NA Ocean.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			},
			effects = {
				{
					active = False,
					name = "jinguang"
				}
			}
		},
		{
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "This goes further back... The other blueprint ships and I were put in the reserve and ordered to guard the Royal Islands.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"Another operation where I:n't get the sortie order...\"",
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
			bgName = "bg_story_task",
			say = "The handful of girls who weren't part of the operation proper were gathered in a briefing room on the Royal Islands.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"I recognise her... That's Vanguard, of Her Majesty's palace guard.\"",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205130,
			say = "\"*sigh*... Stuck here again while the others brave the frontlines.\"",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205130,
			say = "\"Standing guard during Her Majesty's meetings is an important duty, sure, but I was hoping for a little action.\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "I felt a strange sense of closeness to her after overhearing her little monologue.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "She scarcely sees any action as she's usually tasked with VIP protection... I, meanwhile, am a blueprint ship who is next to impossible to field.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"...It makes me wonder. What is 'glory' to her?\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"As a shipgirl and a Royal Knight, she must yearn to fight alongside her compatriots as well.\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"We've both been relegated to benchwarmer duty, it seems.\"",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205130,
			say = "\"Hm? Yeah, apparently. I'm going to be restless for a good while.\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"Likewise. Say, you know about the upcoming exercise? Why:n't we have a friendly duel around:?\"",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205130,
			say = "\"I'm up for that. Let me just check if my schedule allows for it...\"",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205130,
			say = "\"...Oh, it seems sadly not. I have important business on the day of the exercise.\"",
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
			actor = 205130,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"But rest assured, we will have our duel the next time the circumstances permit it!\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "My chance to ask Vanguard how she felt about being excluded from Operation Siren slipped me by...",
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
			actor = 299020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Looking back at it now, what even was that \"important business\"?",
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
			stopbgm = True,
			mode = 1,
			blackBg = True,
			effects = {
				{
					active = False,
					name = "memoryFog"
				}
			},
			effects = {
				{
					active = True,
					name = "jinguang"
				}
			},
			sequence = {
				{
					"",
					2
				}
			}
		}
	}
}

return {
	fadeOut = 1.5,
	mode = 2,
	id = "ZHIHUIMIAO1",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			bgName = "bg_story_task",
			say = "————！~~~",
			effects = {
				{
					active = True,
					name = "miaoMove"
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "Nyaaargh! Stop darting all over the place, nya!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			},
			actorPosition = {
				x = -750,
				y = 0
			},
			action = {
				{
					type = "move",
					dur = 0.5,
					x = 750,
					y = 0
				}
			}
		},
		{
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "*Pant*... *pant*... Unya? Commander, you're back! Perfect timing, nya! Come help me catch these little buggers, nya!",
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
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "Commander, you saved my hide, nya...",
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
			effects = {
				{
					active = False,
					name = "miaoMove"
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
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "What are these things, nya? Hehe, I thought you'd ask that! These little guys are the results of countless hours of hard work and collaboration between Akashi and the Research Department!",
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
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			withoutPainting = True,
			say = "They're called \"Meowfficers,\" nya!",
			effects = {
				{
					active = True,
					name = "miaoShow"
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
			actor = 312010,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "Allow me to introduce them to you!",
			effects = {
				{
					active = False,
					name = "miaoShow"
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

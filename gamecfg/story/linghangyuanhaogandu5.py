return {
	defaultTb = 1007,
	mode = 2,
	fadeOut = 1.5,
	id = "LINGHANGYUANHAOGANDU5",
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Convergence of Hearts\n\n<size=45>5 Favorite Stories</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			say = "I've drawn up a list of activities for TB based on her wishes.",
			bgm = "qe-ova-1",
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
			effects = {
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Truth be told, I'm not sure which of these you'll like...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-sad2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Actually, I like everything on the list.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			say = "Without any sound or warning, TB appears before my eyes.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Oh. Can you tell me why you like them?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-doubt1",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Why? Because I feel they're right.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Liking something and thinking something is right are very different things...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "There are things that people like:ing even if they know it's wrong. Like eating candy before dinner, for example.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			tbActor = True,
			side = 2,
			bgName = "bg_project_tb_room2",
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-doubt2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...That's so complicated.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "I want you to: something for me. Can you clear your head and not think of anything?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-doubt3",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "What:?",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Then think of the most fun thing you know.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-doubt2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
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
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-talking1",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hearing you tell me stories.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Got it. You like stories,:.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			tbActor = True,
			side = 2,
			bgName = "bg_project_tb_room2",
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-answer10",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "No, it's not the stories themselves.",
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
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-talking2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "When you read to me before bedtime, that's what I like.",
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
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-shy",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It makes me feel warm... and safe.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(That hasn't changed since she was little.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "I'll read you a story before bed tonight if you want!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-answer2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Sure.",
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
			expression = 9,
			side = 2,
			bgName = "bg_project_tb_room2",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-2-laugh1",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "If you wanna: it every night... that's fine, too.",
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

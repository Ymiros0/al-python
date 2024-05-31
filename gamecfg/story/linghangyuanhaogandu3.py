return {
	defaultTb = 1001,
	mode = 2,
	fadeOut = 1.5,
	id = "LINGHANGYUANHAOGANDU3",
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Convergence of Hearts\n\n<size=45>3 Your Story</size>",
					1
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-talking2",
			bgm = "qe-ova-10",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Tell me a story.",
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
			},
			effects = {
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			say = "TB has started developing an interest in the stories in picture books.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			say = "I read a story to her once a day, but only when it's time for bed.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "But it's not even close to bedtime yet.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-doubt2",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Pleeease...",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Fine. It's not every day she asks for something with a \"please.\")",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			say = "I come back with a handful of books I've read to her lately. She:esn't seem very interested, though.",
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
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-talking1",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Not like these...",
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
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-angry",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You already told these stories.",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Do you want to hear a new one,:?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-answer16",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah! Tell me a new story!",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Oh, boy. What type of story should I tell her? That's the question...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "A story about a battle.",
					flag = 1
				},
				{
					content = "A story about her.",
					flag = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "Do you want to hear a story about a battle?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			optionFlag = 1,
			voice = "event./educate/tb/educate-tb-1-answer10",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...No.",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "(She flat-out said no!)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "(Okay, need to choose a different story.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "A story about her.",
					flag = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "(That should work. I'll make up a story based on her.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "But where to start...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			optionFlag = 2,
			voice = "event./educate/tb/educate-tb-1-doubt1",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hm...?",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "(I've got it. The story will be about TB's pursuit of a personality.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			say = "As the story went on, TB slowly but surely slipped off into slumberland.",
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
			expression = 8,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-call1",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'm like... a navigator...",
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
			expression = 8,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-1-sad1",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "And brave...",
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
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			say = "She mutters something in her half-asleep state.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Yes you are, TB. You're so brave.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_project_tb_room1",
			tbActor = True,
			dir = 1,
			voice = "event./educate/tb/educate-tb-story-1-4",
			actor = 1001,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*yawn*... Zzz...",
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

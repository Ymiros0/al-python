return {
	defaultTb = 1007,
	mode = 2,
	fadeOut = 1.5,
	id = "LINGHANGYUANYANGCHENGJIHUA17",
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			say = "The school is hosting a camping trip for the students, which of course includes TB.",
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
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "That's enough snacks for the trip. Now just to figure out what to: about your lunch.",
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
			voice = "event./educate/tb/educate-tb-2-shock1",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "My lunch?",
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
			voice = "event./educate/tb/educate-tb-2-answer2",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I wanna make it myself.",
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
			say = "No. You'll hurt yourself.",
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
			say = "She certainly has grown, but she's still too young to be left alone in a place with gas flames and sharp knives.",
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
			voice = "event./educate/tb/educate-tb-2-answer3",
			actor = 1007,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But you let me help that one time!",
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
			say = "Yeah, but...",
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
			say = "She has a point, actually. I let her: it once when she was younger, and she's only grown since:.",
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
			say = "Alright, alright. Let's start with frying an egg.",
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
			say = "40 minutes later...",
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
			side = 2,
			actorName = "TB",
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Hey... How come the egg always burns when I try to fry it?",
			voice = "event./educate/tb/educate-tb-story-2-15",
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
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			say = "Shaking the pan, she shoots me a confused look. The surface of the still-soft yolk breaks and the inside spills out everywhere.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "TB",
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I'm:ing it EXACTLY like you showed me...",
			voice = "event./educate/tb/educate-tb-story-2-16",
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
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "It's the oil. You're heating it too much. Also, you're tossing the pan too soon.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			say = "She gives a sideways glance to the plate of failed previous attempts and a look of hopelessness creeps through on her face.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			say = "I taught her how to: it in detail and took precautions so she wouldn't hurt herself...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			say = "Even so, she's at risk of being burned by the fire and the drops of sizzling oil flying everywhere, which she:esn't seem to fear in the least. I'm worried that her sense of danger may be underdeveloped.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_cg12",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "*sigh*...",
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
			say = "Determined not to let food go to waste, TB ate all the fried eggs she burned over her many attempts.",
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
			bgName = "bg_project_tb_room2",
			hidePaintObj = True,
			say = "I think she won't want to even hear the word \"egg\" for a while.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

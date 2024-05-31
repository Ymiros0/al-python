return {
	fadeOut = 1.5,
	mode = 2,
	defaultTb = 1101,
	id = "LINGHANGYUANTANXIN16",
	placeholder = {
		"tb"
	},
	scripts = {
		{
			tbActor = True,
			side = 2,
			bgName = "bg_project_tb_room3",
			actorName = "TB",
			bgm = "qe-ova-12",
			actor = 1101,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "{tb}, is there anything else I can: for you? Like give you a shoulder massage, or something.",:
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
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "You've:ne your chores and finished your homework. That's plenty. You can just relax now.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 1101,
			nameColor = "#A9F548FF",
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			actorName = "TB",
			side = 2,
			say = "Yes, but those are things I was meant to: anyway. So, if you:n't need a shoulder rub, how about...",
			tbActor = True,
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "bg_project_tb_room3",
			actorName = "TB",
			tbActor = True,
			actor = 1101,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I know! Why:n't I make dinner? Although, we:n't have many ingredients... I'll fry some eggs for the extra nutrition!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Hold your horses. Frying eggs is my job!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_project_tb_room3",
			actorName = "TB",
			tbActor = True,
			actor = 1101,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Is it? But...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Egg-frying is dangerous business. Let me handle that at the very least!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			say = "The memory of when she tried it still burns bright in my mind.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_project_tb_room3",
			actorName = "TB",
			tbActor = True,
			actor = 1101,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmph. Then after dinner's over, I won't speak to you until tomorrow.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_project_tb_room3",
			actorName = "TB",
			tbActor = True,
			actor = 1101,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "(I'm not a kid anymore. I can fry an egg just fine...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_project_tb_room3",
			hidePaintObj = True,
			say = "Sure enough, she didn't say a word to me after we ate dinner. Kids her age... So hard to work with.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

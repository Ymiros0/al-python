return {
	fadeOut = 1.5,
	mode = 2,
	id = "HAIDAORICHANG5",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Uncharted Summer\n\n<size=45>A Place to Dock</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "I got a message from Z23, telling me to meet her at a certain spot.",
			bgmDelay = 2,
			bgm = "theme-SeaAndSun-soft",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Good news, Commander. We've managed to survey most of the island.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "It's even larger than I thought, and strangely, it:esn't appear in any writings or on any maps.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I'm starting to think we're the first to discover and explore it.",
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
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "\"It only appears during a storm, yet isn't part of a Mirror Sea...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "\"Maybe Royal Fortune's mysterious treasure map is the real deal after all.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Perhaps so. That aside, what: you think about this area?",
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
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "I'm standing on a beach flanking a bay, surrounded by cliffs on two sides and a flat plain on the north-facing side.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "One thing immediately comes to mind.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"This is an ideal location for a harbor.\"",
					flag = 1
				},
				{
					content = "\"This is the perfect spot to build a factory.\"",
					flag = 2
				}
			}
		},
		{
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "Yes! I wholly agree!",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "A... factory? To make what, exactly?",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Sure, there's a forest nearby, and you have ready access to water, but the question is...",
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
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			optionFlag = 2,
			say = "\"You:n't need to evaluate it in earnest. I was just kidding.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Oh, you were joking? Like Ayanami was earlier with her video game talk...",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "I'd like you both to take being shipwrecked a little more seriously, please.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "See, what I thought is that this would make the perfect place to build a harbor.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "It's just the thing we need to transport and store what goods we find.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Granted, we:n't have anything TO store at the moment, but still.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I say we get started now, so that our rescuers have a good place to anchor once they arrive.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Let's start by making a small pier,: expand it into a big harbor, and finally, build a storage depot.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Does that sound good, Commander?",
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
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "\"Yes. Logistics are a problem we must solve before we can further develop the island.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "\"I'm impressed, Z23. We only just arrived, and you've already thought this far ahead.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Thank you. The more you plan ahead, the better.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "By the way, I found several spots where we can gather materials during my survey earlier.",
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
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Shall we go give them a look?",
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
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			say = "\"Sure. Securing resources is our top priority. If we can map out the island's terrain at the same time, that's two birds with one stone.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 401230,
			side = 2,
			bgName = "bg_summerisland_map",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Absolutely! Come with me!",
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
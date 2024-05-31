return {
	fadeOut = 1.5,
	mode = 2,
	id = "HAIDAORICHANG14",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Uncharted Summer\n\n<size=45>Safety...First?</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			say = "Our scouting and development of the island continue without issue.",
			bgmDelay = 2,
			bgm = "level02",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			say = "In the seas around the island...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 807010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Our northern patrols are complete. Nothing out of the ordinary.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 902010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "East's all good, too!",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 802020,
			say = "The west is safe, as well. Our recon is proceeding outward in the same direction.",
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
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805010,
			say = "At present, nothing unusual has been spotted to the south. Everyone, continue as planned.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 902010,
			say = "Cardinal, we've been at it for so long now. How about we just call it safe?",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 903020,
			say = "That won't:. We know nothing about this island.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 903020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "And we plan to turn it into a resort,:n't we? We should take safety seriously.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 907010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Instead of complaining, La Galissonnière, focus on your work.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 902010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah, yeah.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 902010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'm EVEN willing to dive and search underwater if it means making sure the coast is clear for the Commander and our friends.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 808010,
			say = "No worries! I've already checked underwater with my mass-produced ships~ We didn't find anything, of course.",
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
			bgName = "bg_unnamearea_1",
			paintingNoise = True,
			dir = 1,
			actor = 902010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I-I was just kidding, geez!",
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
			expression = 2,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805010,
			say = "(Hahaha! It seems there's nothing to worry about at this time.)",
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
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805010,
			say = "(But something tells me this island is a little bit too bountiful...)",
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
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805010,
			say = "Regardless, it must be thanks to the blessing of the Iris that we were able to happen upon such natural riches.",
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
			expression = 4,
			side = 2,
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805010,
			say = "We'll leave the next round of patrols to the mass-produced ships. As for us, it's about time we help develop the island.",
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
			side = 2,
			actorName = "Everyone",
			bgName = "bg_unnamearea_1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Roger!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

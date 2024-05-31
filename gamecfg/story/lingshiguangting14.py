return {
	fadeOut = 1.5,
	mode = 2,
	id = "LINGSHIGUANGTING14",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			expression = 2,
			side = 2,
			bgName = "bg_camelot_7",
			dir = 1,
			bgmDelay = 1,
			bgm = "theme-royalknights-battle",
			actor = 900233,
			nameColor = "#ffff4d",
			hidePaintObj = True,
			say = "This is as far as I can go. The permanent anchorage is just up ahead.",
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
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			actor = 900233,
			say = "You'll find Elizabeth in there. Steer clear of the surveillance cameras and you'll be fine.",
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
			expression = 1,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			actor = 900233,
			say = "Go get her: make a break for it. Don't go messing with stuff, and:n't make a damn scene!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			actor = 201340,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Not to be rude, but you've been making a scene since we first met you...",
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
			expression = 1,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			actor = 900233,
			say = "What was that, you little–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			actor = 900233,
			say = "<Protocol revision. Task \"Mainframe Protection\" has been prioritized over \"Reenactment.\" Immediate action required to preserve branch.>",
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
			expression = 1,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			actor = 900233,
			say = "...What? You gotta be shittin' me, Observer! You want me to take THAT thing on by myself?! Ugghh!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			dir = 1,
			side = 2,
			bgName = "bg_camelot_7",
			say = "Purifier suddenly became possessed, and just as suddenly went back to normal. Without saying another word, she turned her back on the shipgirls and ran off.",
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
			actor = 202310,
			side = 2,
			bgName = "bg_camelot_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Vanguard, I have a clear shot. Shall I?",
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
			bgName = "bg_camelot_7",
			dir = 1,
			blackBg = True,
			actor = 205130,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Hold your fire. She's up to something, but rescuing Her Majesty comes first.",
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

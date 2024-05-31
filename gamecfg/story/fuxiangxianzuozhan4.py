return {
	id = "FUXIANGXIANZUOZHAN4",
	mode = 2,
	once = True,
	fadeType = 1,
	fadein = 1.5,
	scripts = {
		{
			paintingNoise = True,
			side = 2,
			actor = 407030,
			nameColor = "#a9f548",
			dir = 1,
			say = "Heinrich,: you copy?",
			bgm = "story-6",
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
			paintingNoise = False,
			actor = 403090,
			dir = 1,
			nameColor = "#a9f548",
			say = "Loud and clear!",
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
			paintingNoise = True,
			nameColor = "#a9f548",
			side = 2,
			actor = 407030,
			dir = 1,
			say = "The enemy aircraft have changed their attack pattern. Are you en route to the airfield?",
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
			paintingNoise = False,
			side = 2,
			actor = 403090,
			nameColor = "#a9f548",
			dir = 1,
			say = "Yep-yep! Headed there to take out some stray enemies!",
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
			paintingNoise = True,
			nameColor = "#a9f548",
			side = 2,
			actor = 407030,
			dir = 1,
			say = "Hold. Before you enter battle, first check the Stronghold's Control status so you:n't get blindsided by enemy aircraft.",
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
			paintingNoise = False,
			nameColor = "#a9f548",
			side = 2,
			actor = 403090,
			dir = 1,
			say = "Roger-dodger!",
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

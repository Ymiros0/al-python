return {
	id = "GWORLD104C",
	mode = 2,
	once = True,
	fadeType = 1,
	skipTip = False,
	fadein = 1.5,
	scripts = {
		{
			paintingNoise = True,
			side = 2,
			actor = 900284,
			nameColor = "#a9f548",
			dir = 1,
			say = "An item container has been located. To commence recovery of it, simply move your fleet onto it.",
			bgm = "story-richang",
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
			actor = 900284,
			nameColor = "#a9f548",
			side = 2,
			paintingNoise = True,
			dir = 1,
			say = "Commencing inventory tutorial.",
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

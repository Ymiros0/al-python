return {
	id = "GWORLD103A",
	mode = 2,
	once = True,
	fadeType = 1,
	skipTip = False,
	fadein = 1.5,
	scripts = {
		{
			paintingNoise = True,
			side = 2,
			bgm = "level02",
			actor = 900284,
			dir = 1,
			nameColor = "#a9f548",
			say = "Tutorial commencing. Transferring data...",
			voice = "event./tb/8/tb-8",
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
			side = 2,
			actor = 900284,
			nameColor = "#a9f548",
			dir = 1,
			say = "Data transfer complete. I will now explain my tactical assistance features.",
			voice = "event./tb/29/tb-29",
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

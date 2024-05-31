return {
	id = "GWORLD103D",
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
			say = "Scan complete. Now displaying results of zone reconnaissance on screen.",
			bgm = "level02",
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
			say = "Orders received. Commencing test of Scanning Mode.",
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

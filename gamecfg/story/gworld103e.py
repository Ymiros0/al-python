return {
	id = "GWORLD103E",
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
			say = "Scattered Siren hostiles have been detected.",
			voice = "event./tb/41/tb-41",
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
			say = "Scanning Mode has been calibrated. Scanning Mode can now be used on hostile fleets and points of interest such as item nodes.",
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

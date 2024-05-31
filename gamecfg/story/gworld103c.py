return {
	id = "GWORLD103C",
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
			say = "Special orders to the fleet can also be issued using my intermediary relay module. This will invariably ensure the message reaches its addressee.",
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
			paintingNoise = True,
			side = 2,
			actor = 900284,
			nameColor = "#a9f548",
			dir = 1,
			say = "...Orders received. Commencing test of order function.",
			voice = "event./tb/12/tb-12",
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

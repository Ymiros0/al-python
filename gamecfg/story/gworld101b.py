return {
	id = "GWORLD101B",
	mode = 2,
	once = True,
	fadeType = 1,
	fadein = 1.5,
	scripts = {
		{
			actor = 107070,
			nameColor = "#a9f548",
			side = 2,
			bgm = "level02",
			dir = 1,
			say = "Woah~ You sure:n't beat around the bush, Commander! But now, it’s my turn!",
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
			say = "Objective identified. repel Hornet in this exercise.",
			voice = "event./tb/22/tb-22",
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

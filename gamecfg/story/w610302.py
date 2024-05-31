return {
	id = "W610302",
	mode = 2,
	skipTip = False,
	once = True,
	scripts = {
		{
			paintingNoise = True,
			nameColor = "#a9f548",
			side = 2,
			actor = 900284,
			dir = 1,
			say = "Arrived at point of interest. Do you want to commence supply retrieval operations?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			options = {
				{
					content = "Let’s: it.",
					flag = 1
				},
				{
					content = "No thanks.",
					flag = 2
				}
			}
		}
	}
}

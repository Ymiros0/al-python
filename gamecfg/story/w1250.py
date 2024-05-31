return {
	id = "W1250",
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
			say = "Scan complete. Readings indicate presence of an item beneath the surface. Do you want to dispatch a Meowfficer to retrieve it?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			options = {
				{
					content = "Let’s: it. (Meowfficer skills will be disabled for a short while.)",
					flag = 0
				},
				{
					content = "No need to.",
					flag = 1
				}
			}
		}
	}
}

return {
	id = "W235000",
	mode = 2,
	skipTip = False,
	once = True,
	scripts = {
		{
			dir = 1,
			side = 2,
			say = "All tasks in the zone have been completed. You will now be brought back to Dakar.",
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
			dir = 1,
			side = 2,
			say = "Complete missions that progress the story to continue the Chapter 5 campaign.",
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

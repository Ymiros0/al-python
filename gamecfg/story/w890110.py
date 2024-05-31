return {
	id = "W890110",
	mode = 2,
	skipTip = False,
	once = True,
	scripts = {
		{
			dir = 1,
			side = 2,
			say = "Completing objectives in zones marked as Siren Research Facilities can yield great rewards. What should we:?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			},
			options = {
				{
					content = "Head there now.",
					flag = 0
				},
				{
					content = "Do it later.",
					flag = 1
				}
			}
		}
	}
}

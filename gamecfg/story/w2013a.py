return {
	id = "W2013A",
	mode = 2,
	skipTip = False,
	once = True,
	scripts = {
		{
			dir = 1,
			side = 2,
			say = "Scan complete. Current energy level. 2. Rewards may be claimed now, or you can deposit more Energy Matrixes for additional rewards. What: you wish to:?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			options = {
				{
					content = "Claim the rewards.",
					flag = 1
				},
				{
					content = "Do nothing for now.",
					flag = 2
				}
			}
		}
	}
}

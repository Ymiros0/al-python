return {
	id = "W1022",
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
			say = "Power source has been installed. Booting device...",
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
			nameColor = "#a9f548",
			side = 2,
			actor = 900284,
			dir = 1,
			say = "Analysis complete. Data acquired on Siren enhancement modules from this sector.",
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
			say = "A capability-improving rigging augmentation is available. Which would you like to augment?",
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
					content = "Increase Offensive Adaptability.",
					flag = 0
				},
				{
					content = "Increase Survival Adaptability.",
					flag = 1
				},
				{
					content = "Increase Tactical Adaptability.",
					flag = 2
				},
				{
					content = "None, maybe next time.",
					flag = 3
				}
			}
		}
	}
}

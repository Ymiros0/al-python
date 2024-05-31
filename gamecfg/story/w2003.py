return {
	id = "W2003",
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
			say = "Scan complete. This device appears to be capable of controlling abnormal ice floes.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			options = {
				{
					content = "Destroy the device.",
					flag = 0
				},
				{
					content = "Do nothing for now.",
					flag = 1
				}
			}
		}
	}
}

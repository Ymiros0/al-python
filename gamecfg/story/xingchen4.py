return {
	fadeOut = 1.5,
	mode = 3,
	once = True,
	id = "XINGCHEN4",
	occlusion = 0.8,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Bits of Courage \n\n<size=45>IV 「Letter to Stardust」</size>",
					1
				}
			}
		},
		{
			bgName = "bg_story_star2",
			blackBg = True,
			flashout = {
				black = True,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = True,
				alpha = {
					1,
					0
				}
			}
		}
	}
}

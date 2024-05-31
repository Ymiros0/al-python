return {
	id = "UI20101",
	mode = 3,
	noWaitFade = True,
	once = True,
	scripts = {
		{
			actor = 107020,
			nameColor = "#a9f548",
			bgName = "bg_story_6",
			side = 0,
			bgspeed = 2,
			blackBg = True,
			say = "<size=33>Hold your positions! Don't fire unless fired upon!</size>",
			effects = {
				{
					active = True,
					name = "UIhuohua"
				}
			}
		},
		{
			actor = 107020,
			nameColor = "#a9f548",
			side = 0,
			blackBg = True,
			say = "<size=33>But if they mean to have a war...</size>"
		},
		{
			actor = 107020,
			nameColor = "#a9f548",
			side = 0,
			blackBg = True,
			say = "<size=33>Let it begin!</size>"
		},
		{
			sequenceSpd = 2,
			mode = 1,
			bgFade = True,
			effects = {
				{
					active = False,
					name = "UIhuohua"
				}
			},
			sequence = {
				{
					"          Chapter 2 - <size=43.5>Battle of Coral Sea</size>  \n\n\n\n",
					2
				}
			}
		}
	}
}

return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DTOUCH1104",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "主人，请您再离天狼星近一些……",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dispatcher = {
				name = STORY_EVENT.TEST,
				data = {
					op_list = {
						{
							skip = False,
							name = "surprise2",
							type = "action"
						}
					}
				},
				callbackData = {
					hideUI = True,
					name = STORY_EVENT.TEST_DONE
				}
			}
		}
	}
}

return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DTOUCH1103",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "淑女的礼仪，天狼星也记得呢。",
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
							name = "surprise1",
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

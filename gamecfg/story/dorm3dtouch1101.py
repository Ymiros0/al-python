return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DTOUCH1101",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "这样的姿势，会适合天狼星吗？",
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
							name = "shy",
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

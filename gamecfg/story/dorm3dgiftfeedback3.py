return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DGIFTFEEDBACK3",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "没想到主人您会送天狼星这本书呢，一定是天狼星的觉悟还不够……！",
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
		},
		{
			say = "天狼星一定会好好研读这本书，成为让主人赞不绝口的完美女仆！",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

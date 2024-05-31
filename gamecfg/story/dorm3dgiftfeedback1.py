return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DGIFTFEEDBACK1",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "这是您送给我的茶具……？天狼星真是受宠若惊……我慷慨的主人！",
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
		},
		{
			say = "天狼星一定会好好爱惜它，然后用它冲泡美味的红茶来招待主人！",
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
							name = "Bow",
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

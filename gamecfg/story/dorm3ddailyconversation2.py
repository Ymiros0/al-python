return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DDAILYCONVERSATION2",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "主人，请您不要乱动。",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actorName = "指挥官",
			nameColor = "#a9f548",
			say = "……？",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			say = "主人的眼睛，果然很漂亮呢。",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dispatcher = {
				name = STORY_EVENT.TEST,
				data = {
					op_list = {
						{
							param = "Play",
							name = "surprise1",
							time = 0,
							type = "action"
						}
					}
				},
				callbackData = {
					hideUI = False,
					name = STORY_EVENT.TEST_DONE
				}
			}
		},
		{
			say = "只是这样看着……就让人忍不住沉溺在您的目光之中了。",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			say = "那么，就请允许天狼星用这种方式来开启全新的一天吧，还请您闭上眼……",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"你闭上了双眼\n\n天狼星：我骄傲的主人……（亲吻声）",
					1
				}
			}
		},
		{
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

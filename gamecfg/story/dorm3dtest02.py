return {
	hideRecord = True,
	dialogbox = 2,
	mode = 2,
	alpha = 0,
	id = "DORM3DTEST02",
	hideSkip = True,
	hideAuto = True,
	scripts = {
		{
			say = "对话2",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dispatcher = {
				name = STORY_EVENT.TEST,
				data = {
					op_list = {
						{
							skip = True,
							name = "surprise2",
							type = "action"
						},
						{
							skip = False,
							time = 2,
							type = "wait"
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
			say = "对话1",
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
							name = "Tianlangxing02_Zoulangdengdai",
							time = 0,
							type = "timeline",
							touchs = {
								{
									pos = {
										10,
										10
									}
								},
								{
									pos = {
										-100,
										-10
									}
								},
								{
									pos = {
										200,
										-100
									}
								},
								{
									pos = {
										-300,
										200
									}
								}
							}
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
			nameColor = "#A9F548FF",
			side = 2,
			hidePaintObj = True,
			recallOption = False,
			say = "第二个分区，名为《夕阳》，同样摆放着四副画作——",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "查看《跛脚巨人》",
					flag = 1
				},
				{
					content = "查看《值得警戒》",
					flag = 2
				},
				{
					content = "查看《被孤立的巨人》",
					flag = 3
				},
				{
					content = "查看《圣诞之夜静悄悄》",
					flag = 4
				}
			},
			dispatcher = {
				name = STORY_EVENT.TEST,
				data = {
					op_list = {
						{
							skip = False,
							name = "Tianlangxing01_Jinmenjieshao",
							time = 0,
							type = "timeline",
							options = {
								{
									flag = 1,
									content = "查看《跛脚巨人》"
								},
								{
									flag = 2,
									content = "查看《值得警戒》"
								},
								{
									flag = 3,
									content = "查看《被孤立的巨人》"
								},
								{
									flag = 4,
									content = "查看《圣诞之夜静悄悄》"
								}
							}
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
			say = "对话3",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}

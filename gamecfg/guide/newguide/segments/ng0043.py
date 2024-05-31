return {
	id = "NG0043",
	events = {
		{
			alpha = 0.6,
			style = {
				text = "Tap on the building with an ! over it to have a look!",
				mode = 1,
				posY = 250,
				dir = -1,
				posX = -92,
				def uiFunc:()
					local var_1_0 = {}

					if not pg.NewStoryMgr.GetInstance().IsPlayed(VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_MAIN_STAGE)):
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/main/title"
						})
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/main/tip"
						})

					if not pg.NewStoryMgr.GetInstance().IsPlayed(VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_SUB_STAGE)):
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/sub/title"
						})
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/sub/tip"
						})

					if not pg.NewStoryMgr.GetInstance().IsPlayed(VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_EXCHANGE)):
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/exchange/title"
						})
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/exchange/tip"
						})

					if not pg.NewStoryMgr.GetInstance().IsPlayed(VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_SCHEDULE)):
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/billboard/title"
						})
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/billboard/tip"
						})

					if not pg.NewStoryMgr.GetInstance().IsPlayed(VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_HALL)):
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/honor/title"
						})
						table.insert(var_1_0, {
							path = "/UICamera/Canvas/UIMain/VoteEntranceUI(Clone)/bg/honor/tip"
						})

					return var_1_0
			}
		}
	}
}

local var_0_0 = class("PtTemplatePage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.slider = arg_1_0.findTF("slider", arg_1_0.bg)
	arg_1_0.step = arg_1_0.findTF("step", arg_1_0.bg)
	arg_1_0.progress = arg_1_0.findTF("progress", arg_1_0.bg)
	arg_1_0.displayBtn = arg_1_0.findTF("display_btn", arg_1_0.bg)
	arg_1_0.awardTF = arg_1_0.findTF("award", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	if arg_2_0.ptData:
		arg_2_0.ptData.Update(arg_2_0.activity)
	else
		arg_2_0.ptData = ActivityPtData.New(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.displayBtn, function()
		arg_3_0.emit(ActivityMediator.SHOW_AWARD_WINDOW, PtAwardWindow, {
			type = arg_3_0.ptData.type,
			dropList = arg_3_0.ptData.dropList,
			targets = arg_3_0.ptData.targets,
			level = arg_3_0.ptData.level,
			count = arg_3_0.ptData.count,
			resId = arg_3_0.ptData.resId,
			unlockStamps = arg_3_0.ptData.GetDayUnlockStamps()
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		local var_5_0
		local var_5_1

		if arg_3_0.activity.getConfig("config_client") != "":
			var_5_0 = arg_3_0.activity.getConfig("config_client").linkActID

			if var_5_0:
				var_5_1 = getProxy(ActivityProxy).getActivityById(var_5_0)

		if not var_5_0:
			arg_3_0.emit(ActivityMediator.BATTLE_OPERA)
		elif var_5_1 and not var_5_1.isEnd():
			arg_3_0.emit(ActivityMediator.BATTLE_OPERA)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		local var_6_0 = {}
		local var_6_1 = arg_3_0.ptData.GetAward()
		local var_6_2 = getProxy(PlayerProxy).getRawData()
		local var_6_3 = pg.gameset.urpt_chapter_max.description[1]
		local var_6_4 = LOCK_UR_SHIP and 0 or getProxy(BagProxy).GetLimitCntById(var_6_3)
		local var_6_5, var_6_6 = Task.StaticJudgeOverflow(var_6_2.gold, var_6_2.oil, var_6_4, True, True, {
			{
				var_6_1.type,
				var_6_1.id,
				var_6_1.count
			}
		})

		if var_6_5:
			table.insert(var_6_0, function(arg_7_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_ITEM_BOX,
					content = i18n("award_max_warning"),
					items = var_6_6,
					onYes = arg_7_0
				}))

		seriesAsync(var_6_0, function()
			local var_8_0, var_8_1 = arg_3_0.ptData.GetResProgress()

			arg_3_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_3_0.ptData.GetId(),
				arg1 = var_8_1
			})), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_9_0):
	local var_9_0 = arg_9_0.ptData.getTargetLevel()
	local var_9_1 = arg_9_0.activity.getConfig("config_client").story

	if checkExist(var_9_1, {
		var_9_0
	}, {
		1
	}):
		pg.NewStoryMgr.GetInstance().Play(var_9_1[var_9_0][1])

	if arg_9_0.step:
		local var_9_2, var_9_3, var_9_4 = arg_9_0.ptData.GetLevelProgress()

		setText(arg_9_0.step, var_9_2 .. "/" .. var_9_3)

	local var_9_5, var_9_6, var_9_7 = arg_9_0.ptData.GetResProgress()

	setText(arg_9_0.progress, (var_9_7 >= 1 and setColorStr(var_9_5, COLOR_GREEN) or var_9_5) .. "/" .. var_9_6)
	setSlider(arg_9_0.slider, 0, 1, var_9_7)

	local var_9_8 = arg_9_0.ptData.CanGetAward()
	local var_9_9 = arg_9_0.ptData.CanGetNextAward()
	local var_9_10 = arg_9_0.ptData.CanGetMorePt()

	setActive(arg_9_0.battleBtn, var_9_10 and not var_9_8 and var_9_9)
	setActive(arg_9_0.getBtn, var_9_8)
	setActive(arg_9_0.gotBtn, not var_9_9)

	local var_9_11 = arg_9_0.ptData.GetAward()

	updateDrop(arg_9_0.awardTF, var_9_11)
	onButton(arg_9_0, arg_9_0.awardTF, function()
		arg_9_0.emit(BaseUI.ON_DROP, var_9_11), SFX_PANEL)

def var_0_0.OnDestroy(arg_11_0):
	return

def var_0_0.GetWorldPtData(arg_12_0, arg_12_1):
	if arg_12_1 <= pg.TimeMgr.GetInstance().GetServerTime() - (ActivityMainScene.Data2Time or 0):
		ActivityMainScene.Data2Time = pg.TimeMgr.GetInstance().GetServerTime()

		arg_12_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
			cmd = 2,
			activity_id = arg_12_0.ptData.GetId()
		})

return var_0_0

local var_0_0 = class("NewOrleansMapPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.item = arg_1_0.findTF("item", arg_1_0.bg)
	arg_1_0.itemMask = arg_1_0.findTF("icon_mask", arg_1_0.item)
	arg_1_0.gotaskBtn = arg_1_0.findTF("gotask", arg_1_0.bg)
	arg_1_0.gobattleBtn = arg_1_0.findTF("gobattle", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_data")

	arg_2_0.taskIDList = _.flatten(var_2_0)
	arg_2_0.taskProxy = getProxy(TaskProxy)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.gobattleBtn, function()
		local var_4_0 = getProxy(ActivityProxy).getActivityById(pg.activity_const.NEW_ORLEANS_Map_BATTLE.act_id)

		if not var_4_0 or var_4_0.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))

			return

		arg_3_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.gotaskBtn, function()
		local var_5_0 = getProxy(ActivityProxy).getActivityById(pg.activity_const.NEW_ORLEANS_Map_BATTLE.act_id)

		if not var_5_0 or var_5_0.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))

			return

		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {
			page = "activity"
		}))

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0 = arg_6_0.findCurTaskIndex()
	local var_6_1 = arg_6_0.taskIDList[var_6_0]
	local var_6_2 = arg_6_0.taskProxy.getTaskVO(var_6_1)

	arg_6_0.curTaskVO = var_6_2

	local var_6_3 = var_6_2.getConfig("award_display")[1]
	local var_6_4 = {
		type = var_6_3[1],
		id = var_6_3[2],
		count = var_6_3[3]
	}

	updateDrop(arg_6_0.item, var_6_4)
	onButton(arg_6_0, arg_6_0.item, function()
		arg_6_0.emit(BaseUI.ON_DROP, var_6_4), SFX_PANEL)

	local var_6_5 = var_6_2.getTaskStatus()

	setActive(arg_6_0.itemMask, var_6_5 == 2)

def var_0_0.OnDestroy(arg_8_0):
	return

def var_0_0.findCurTaskIndex(arg_9_0):
	local var_9_0

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.taskIDList):
		if arg_9_0.taskProxy.getTaskVO(iter_9_1).getTaskStatus() <= 1:
			var_9_0 = iter_9_0

			break
		elif iter_9_0 == #arg_9_0.taskIDList:
			var_9_0 = iter_9_0

	return var_9_0

return var_0_0

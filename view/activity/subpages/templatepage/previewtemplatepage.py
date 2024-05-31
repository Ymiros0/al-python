local var_0_0 = class("PreviewTemplatePage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.btnList = arg_1_0.findTF("btn_list", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	arg_2_0.initBtn()
	eachChild(arg_2_0.btnList, function(arg_3_0)
		arg_2_0.btnFuncList[arg_3_0.name](arg_3_0))

def var_0_0.initBtn(arg_4_0):
	local function var_4_0(arg_5_0)
		local var_5_0 = getProxy(ActivityProxy).getActivityById(arg_5_0)

		if not var_5_0 or var_5_0 and var_5_0.isEnd():
			return True
		else
			return False

	local var_4_1 = arg_4_0.activity.getConfig("config_client")

	arg_4_0.btnFuncList = {
		def task:(arg_6_0)
			onButton(arg_4_0, arg_6_0, function()
				if var_4_1.taskLinkActID and var_4_0(var_4_1.taskLinkActID):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_4_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {
					page = "activity"
				})),
		def academy:(arg_8_0)
			onButton(arg_4_0, arg_8_0, function()
				arg_4_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.NAVALACADEMYSCENE, {
					page = "activity"
				})),
		def shop:(arg_10_0)
			local var_10_0 = _.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_11_0)
				return arg_11_0.getConfig("config_client").pt_id == pg.gameset.activity_res_id.key_value)

			onButton(arg_4_0, arg_10_0, function()
				if var_4_1.shopLinkActID and var_4_0(var_4_1.shopLinkActID):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_4_0.emit(ActivityMediator.GO_SHOPS_LAYER, {
					warp = NewShopsScene.TYPE_ACTIVITY,
					actId = var_10_0 and var_10_0.id
				})),
		def build:(arg_13_0)
			onButton(arg_4_0, arg_13_0, function()
				if var_4_1.buildLinkActID and var_4_0(var_4_1.buildLinkActID):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_4_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
					page = BuildShipScene.PAGE_BUILD,
					projectName = BuildShipScene.PROJECTS.ACTIVITY
				})),
		def fight:(arg_15_0)
			onButton(arg_4_0, arg_15_0, function()
				if var_4_1.fightLinkActID and var_4_0(var_4_1.fightLinkActID):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_4_0.emit(ActivityMediator.BATTLE_OPERA)),
		def lottery:(arg_17_0)
			onButton(arg_4_0, arg_17_0, function()
				if var_4_1.lotteryLinkActID and var_4_0(var_4_1.lotteryLinkActID):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_4_0.emit(ActivityMediator.GO_LOTTERY)),
		def memory:(arg_19_0)
			return,
		def activity:(arg_20_0)
			return,
		def mountain:(arg_21_0)
			return,
		def skinshop:(arg_22_0)
			onButton(arg_4_0, arg_22_0, function()
				arg_4_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP))
	}

return var_0_0

local var_0_0 = class("BackHillSummerPark2022Scene", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "BackHillSummerParkUI"

var_0_0.edge2area = {
	default = "_SDPlace"
}

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0._bg = arg_2_0.findTF("BG")
	arg_2_0._map = arg_2_0.findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1:
		local var_2_0 = arg_2_0._map.GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0

	arg_2_0._shipTpl = arg_2_0.findTF("ship")
	arg_2_0._upper = arg_2_0.findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1:
		local var_2_2 = arg_2_0._upper.GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2

	arg_2_0._SDPlace = arg_2_0._tf.Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.BackHillSummerParkGraph"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/Back"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Home"), function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.summerland_tip.tip
		}), SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_ICECREAM)

	arg_3_0.InitStudents(var_3_0 and var_3_0.id, 2, 4)
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "bingqilin", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 41))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "qimazhan", function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.ISUZU_SPORTS_SKIN_ID
		}))
	setActive(arg_3_0.map_shujvhuigu, PLATFORM_CODE == PLATFORM_US)
	setActive(arg_3_0.upper_shujvhuigu, PLATFORM_CODE == PLATFORM_US)

	if PLATFORM_CODE == PLATFORM_US:
		local function var_3_1()
			arg_3_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.SUMMARY)

		arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "shujvhuigu", var_3_1)

	arg_3_0.BindItemSkinShop()
	arg_3_0.BindItemBuildShip()
	arg_3_0.UpdateView()

def var_0_0.UpdateView(arg_10_0):
	local function var_10_0()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_ICECREAM)

	setActive(arg_10_0.upper_bingqilin.Find("Tip"), var_10_0())

	local function var_10_1()
		local var_12_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ISUZU_SPORTS_SKIN_ID)

		return Activity.IsActivityReady(var_12_0)

	setActive(arg_10_0.upper_qimazhan.Find("Tip"), var_10_1())

	local function var_10_2()
		if PLATFORM_CODE != PLATFORM_US:
			return

		local var_13_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_13_0)

	setActive(arg_10_0.upper_shujvhuigu.Find("Tip"), var_10_2())

def var_0_0.IsShowMainTip(arg_14_0):
	local function var_14_0()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_ICECREAM)

	local function var_14_1()
		local var_16_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ISUZU_SPORTS_SKIN_ID)

		return Activity.IsActivityReady(var_16_0)

	local function var_14_2()
		if PLATFORM_CODE != PLATFORM_US:
			return

		local var_17_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_17_0)

	return var_14_0() or var_14_1() or var_14_2()

def var_0_0.willExit(arg_18_0):
	arg_18_0.clearStudents()
	var_0_0.super.willExit(arg_18_0)

return var_0_0

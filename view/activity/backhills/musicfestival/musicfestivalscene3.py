local var_0_0 = class("MusicFestivalScene3", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "MusicFestivalUI3"

var_0_0.edge2area = {
	default = "_SDPlace"
}

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0._map = arg_2_0.findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1:
		local var_2_0 = arg_2_0._map.GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0

	arg_2_0._upper = arg_2_0.findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1:
		local var_2_2 = arg_2_0._upper.GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2

	arg_2_0._SDPlace = arg_2_0._upper.Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0._shipTpl = arg_2_0._map.Find("ship")
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.MusicFestivalGraph3"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/Back"), function()
		arg_3_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Home"), function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.idol3rd_houshan.tip
		}), SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MUSIC_FESTIVAL_ID_3)

	arg_3_0.InitStudents(var_3_0 and var_3_0.id, 3, 4)
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "xiaoyouxi", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 16))

	local var_3_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.MUSIC_FESTIVAL_PT_ID_3)

	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "huodongye", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_3_1.id
		}))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "dalaozhang", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.IDOL_MEDAL_COLLECTION_SCENE3))
	arg_3_0.BindItemActivityShop()
	arg_3_0.BindItemSkinShop()
	arg_3_0.BindItemBuildShip()
	arg_3_0.BindItemBattle()
	arg_3_0.UpdateView()

def var_0_0.MiniGameTip():
	return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MUSIC_FESTIVAL_ID_3)

def var_0_0.MedalTip():
	local var_11_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

	return Activity.IsActivityReady(var_11_0)

def var_0_0.ActivityTip():
	local var_12_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MUSIC_FESTIVAL_PT_ID_3)

	return Activity.IsActivityReady(var_12_0)

def var_0_0.UpdateView(arg_13_0):
	setActive(arg_13_0.upper_xiaoyouxi.Find("Tip"), var_0_0.MiniGameTip())
	setActive(arg_13_0.upper_dalaozhang.Find("Tip"), var_0_0.MedalTip())
	setActive(arg_13_0.upper_huodongye.Find("Tip"), var_0_0.ActivityTip())

def var_0_0.IsShowMainTip(arg_14_0):
	if arg_14_0 and not arg_14_0.isEnd():
		return var_0_0.MiniGameTip() or var_0_0.MedalTip() or var_0_0.ActivityTip()

def var_0_0.willExit(arg_15_0):
	arg_15_0.clearStudents()
	var_0_0.super.willExit(arg_15_0)

return var_0_0

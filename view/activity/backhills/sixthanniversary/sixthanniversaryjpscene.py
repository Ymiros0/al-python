local var_0_0 = class("SixthAnniversaryJPScene", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "SixthAnniversaryJPUI"

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

	arg_2_0._upper = arg_2_0.findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1:
		local var_2_2 = arg_2_0._upper.GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2

	arg_2_0._SDPlace = arg_2_0._tf.Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0._shipTpl = arg_2_0._map.Find("ship")
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.SixthAnniversaryJPGraph"))

	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_CHT:
		setActive(arg_2_0.map_shujuhuigu, True)
		setActive(arg_2_0.upper_shujuhuigu, True)
	else
		setActive(arg_2_0.map_shujuhuigu, False)
		setActive(arg_2_0.upper_shujuhuigu, False)

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/Back"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Home"), function()
		arg_3_0.quickExitFunc(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.jp6th_biaohoushan_help.tip
		}), SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_ZUMA)

	arg_3_0.InitStudents(var_3_0 and var_3_0.id, 2, 3)
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "jiujiuwenquan", function()
		arg_3_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.SIXTH_ANNIVERSARY_JP_HOTSPRING))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "shujuhuigu", function()
		arg_3_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.SUMMARY))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "shijiandiaocha", function()
		pg.SceneAnimMgr.GetInstance().SixthAnniversaryJPCoverGoScene(SCENE.SIXTH_ANNIVERSARY_JP_DARK))
	arg_3_0.BindItemSkinShop()
	arg_3_0.BindItemBuildShip()
	arg_3_0.UpdateView()

	local var_3_1 = pg.activity_template[ActivityConst.MINIGAME_ZUMA].config_client.biaohoushanstory

	pg.NewStoryMgr.GetInstance().Play(var_3_1)

def var_0_0.HotSpringTip():
	local var_10_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	return Activity.IsActivityReady(var_10_0)

def var_0_0.ZumaTip():
	return LaunchBallActivityMgr.IsTip(ActivityConst.MINIGAME_ZUMA) or LaunchBallTaskMgr.GetRedTip()

def var_0_0.UpdateView(arg_12_0):
	setActive(arg_12_0.upper_jiujiuwenquan.Find("Tip"), var_0_0.HotSpringTip())
	setActive(arg_12_0.upper_shijiandiaocha.Find("Tip"), var_0_0.ZumaTip())

def var_0_0.willExit(arg_13_0):
	arg_13_0.clearStudents()
	var_0_0.super.willExit(arg_13_0)

def var_0_0.IsShowMainTip(arg_14_0):
	if arg_14_0 and not arg_14_0.isEnd():
		return var_0_0.HotSpringTip() or var_0_0.ZumaTip()

def var_0_0.onBackPressed(arg_15_0):
	arg_15_0.emit(var_0_0.ON_HOME)

return var_0_0

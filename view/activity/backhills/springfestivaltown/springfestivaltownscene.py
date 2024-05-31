local var_0_0 = class("SpringFestivalTownScene", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "SpringFestivalTownUI"

def var_0_0.getBGM(arg_2_0):
	return "story-china"

var_0_0.HUB_ID = 5
var_0_0.edge2area = {
	default = "_middle",
	["9_9"] = "_bottom",
	["4_4"] = "_front"
}

def var_0_0.init(arg_3_0):
	arg_3_0.top = arg_3_0.findTF("top")
	arg_3_0._closeBtn = arg_3_0.findTF("top/return_btn")
	arg_3_0._homeBtn = arg_3_0.findTF("top/return_main_btn")
	arg_3_0._helpBtn = arg_3_0.findTF("top/help_btn")
	arg_3_0._map = arg_3_0.findTF("map")

	for iter_3_0 = 0, arg_3_0._map.childCount - 1:
		local var_3_0 = arg_3_0._map.GetChild(iter_3_0)
		local var_3_1 = go(var_3_0).name

		arg_3_0["_" .. var_3_1] = var_3_0

	arg_3_0._front = arg_3_0._map.Find("top")
	arg_3_0._middle = arg_3_0._map.Find("middle")
	arg_3_0._bottom = arg_3_0._map.Find("bottom")
	arg_3_0.containers = {
		arg_3_0._front,
		arg_3_0._middle,
		arg_3_0._bottom
	}
	arg_3_0._shipTpl = arg_3_0._map.Find("ship")
	arg_3_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.SpringFestivalTownGraph"))
	arg_3_0._upper = arg_3_0.findTF("upper")
	arg_3_0.usableTxt = arg_3_0.top.Find("usable_count/Text").GetComponent(typeof(Text))
	arg_3_0.diedieleTF = arg_3_0.top.Find("diediele_count")
	arg_3_0.diedieleTxt = arg_3_0.diedieleTF.Find("Text").GetComponent(typeof(Text))
	arg_3_0.effectReq = LoadPrefabRequestPackage.New("ui/map_donghuangchunjie", "map_donghuangchunjie", function(arg_4_0)
		setParent(arg_4_0, arg_3_0._map, False)

		local var_4_0 = GameObject.Find("UICamera/Canvas").GetComponent(typeof(Canvas)).sortingOrder
		local var_4_1 = arg_4_0.GetComponentsInChildren(typeof(Renderer))

		for iter_4_0 = 0, var_4_1.Length - 1:
			var_4_1[iter_4_0].sortingOrder = var_4_0 + 1

		arg_3_0.mapeffect = arg_4_0).Start()

	arg_3_0.managedTween(LeanTween.value, None, go(arg_3_0._map), System.Action_UnityEngine_Color(function(arg_5_0)
		go(arg_3_0._map).GetComponent(typeof(Image)).material.SetColor("_Color", arg_5_0)), Color(0, 0, 0, 0), Color(1, 1, 0, 0), 1.5).setLoopPingPong(-1)

def var_0_0.didEnter(arg_6_0):
	local var_6_0 = getProxy(MiniGameProxy)

	onButton(arg_6_0, arg_6_0._closeBtn, function()
		arg_6_0.emit(var_0_0.ON_BACK))
	onButton(arg_6_0, arg_6_0.diedieleTF, function()
		arg_6_0.emit(NewYearFestivalMediator.ON_OPEN_PILE_SIGNED))
	onButton(arg_6_0, arg_6_0._homeBtn, function()
		arg_6_0.emit(var_0_0.ON_HOME))
	onButton(arg_6_0, arg_6_0._helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_chunjie_feast.tip
		}))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "kaihongbao", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SUBLAYER, Context.New({
			mediator = RedPacketMediator,
			viewComponent = RedPacketLayer,
			def onRemoved:()
				if arg_6_0.mapeffect:
					setActive(arg_6_0.mapeffect, True)
		}), function()
			if arg_6_0.mapeffect:
				setActive(arg_6_0.mapeffect, False)))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "danianshou", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.BEAT_MONSTER_NIAN_2020
		}))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "dafuweng", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.MONOPOLY_2020
		}))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "diediele", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 9))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "jianzao", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		}))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "sishu", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.COLORING))
	arg_6_0.InitFacilityCross(arg_6_0._map, arg_6_0._upper, "pifushangdian", function()
		arg_6_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.SKINSHOP))
	pg.UIMgr.GetInstance().OverlayPanel(arg_6_0.top, False)
	arg_6_0.InitStudents(ActivityConst.ACTIVITY_478, 3, 5)
	arg_6_0.UpdateView()

def var_0_0.UpdateView(arg_20_0):
	local var_20_0
	local var_20_1
	local var_20_2 = getProxy(ActivityProxy)
	local var_20_3 = getProxy(MiniGameProxy)
	local var_20_4 = arg_20_0._upper.Find("danianshou/tip")
	local var_20_5 = var_20_2.getActivityById(ActivityConst.BEAT_MONSTER_NIAN_2020)

	setActive(var_20_4, var_20_5 and var_20_5.readyToAchieve())

	local var_20_6 = arg_20_0._upper.Find("dafuweng/tip")
	local var_20_7 = var_20_2.getActivityById(ActivityConst.MONOPOLY_2020)

	setActive(var_20_6, var_20_7 and var_20_7.readyToAchieve())

	local var_20_8 = arg_20_0._upper.Find("sishu/tip")

	setActive(var_20_8, getProxy(ColoringProxy).CheckTodayTip())

	local var_20_9 = arg_20_0._upper.Find("jianzao/tip")

	setActive(var_20_9, False)

	local var_20_10 = arg_20_0._upper.Find("pifushangdian/tip")

	setActive(var_20_10, False)

	local var_20_11 = arg_20_0._upper.Find("kaihongbao/tip")

	setActive(var_20_11, RedPacketLayer.isShowRedPoint())

	local var_20_12 = var_20_3.GetHubByHubId(arg_20_0.HUB_ID)
	local var_20_13 = arg_20_0._upper.Find("diediele/tip")

	setActive(var_20_13, var_20_12.count > 0)
	arg_20_0.UpdateDieDieleCnt(var_20_12)

def var_0_0.UpdateDieDieleCnt(arg_21_0, arg_21_1):
	arg_21_0.usableTxt.text = "X" .. arg_21_1.count
	arg_21_0.diedieleTxt.text = arg_21_1.usedtime .. "/" .. arg_21_1.getConfig("reward_need")

def var_0_0.TryPlayStory(arg_22_0):
	return

def var_0_0.willExit(arg_23_0):
	arg_23_0.effectReq.Stop()

	arg_23_0.mapeffect = None

	pg.UIMgr.GetInstance().UnOverlayPanel(arg_23_0.top, arg_23_0._tf)
	arg_23_0.clearStudents()

return var_0_0

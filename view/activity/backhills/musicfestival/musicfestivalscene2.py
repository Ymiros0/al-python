local var_0_0 = class("MusicFestivalScene2", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "MusicFestivalUI2"

var_0_0.edge2area = {
	default = "_middle"
}

def var_0_0.init(arg_2_0):
	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0._map = arg_2_0.findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1:
		local var_2_0 = arg_2_0._map.GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0

	arg_2_0._stageShip = arg_2_0._map.Find("stageship")
	arg_2_0._shipTpl = arg_2_0._map.Find("ship")
	arg_2_0._upper = arg_2_0.findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1:
		local var_2_2 = arg_2_0._upper.GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2

	arg_2_0.modelTip = arg_2_0.upper_model.Find("tip")

	setActive(arg_2_0.modelTip, False)

	arg_2_0._middle = arg_2_0._map.Find("middle")
	arg_2_0.containers = {
		arg_2_0._middle
	}
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.MusicFestivalGraph2"))

	local var_2_4 = arg_2_0._tf.GetComponentInParent(typeof(UnityEngine.Canvas))
	local var_2_5 = var_2_4 and var_2_4.sortingOrder

	arg_2_0._map.GetComponent(typeof(UnityEngine.Canvas)).sortingOrder = var_2_5 - 2

	local var_2_6 = GetComponent(arg_2_0._map, "ItemList")

	for iter_2_2 = 1, 3:
		local var_2_7 = var_2_6.prefabItem[iter_2_2 - 1]
		local var_2_8 = tf(Instantiate(var_2_7))

		setParent(var_2_8, arg_2_0._map)

	arg_2_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/return_btn"), function()
		arg_3_0.emit(var_0_0.ON_BACK))
	onButton(arg_3_0, arg_3_0.findTF("top/return_main_btn"), function()
		arg_3_0.emit(var_0_0.ON_HOME))
	onButton(arg_3_0, arg_3_0.findTF("top/help_btn"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.music_main.tip
		}))

	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MUSIC_FESTIVAL_ID_2)

	arg_3_0.InitStudents(var_3_0 and var_3_0.id, 3, 4)
	onButton(arg_3_0, arg_3_0.upper_model, function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_3_0.id
		}))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "jichangwutai", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 16))

	local var_3_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PT_BUFF)

	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "leijipt", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_3_1.id
		}))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "bujishangdian", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_ACTIVITY
		}))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "huangzhuangshangdian", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.SKINSHOP))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "xianshijianzao", function()
		arg_3_0.emit(MusicFestivalMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		}))
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "jinianzhang", function()
		local var_13_0 = Context.New({
			mediator = IdolMedalCollectionMediator,
			viewComponent = IdolMedalCollectionView2
		})

		arg_3_0.emit(MusicFestivalMediator.GO_SUBLAYER, var_13_0))
	arg_3_0.BindItemBattle()
	arg_3_0.updateStageShip()
	arg_3_0.UpdateView()

def var_0_0.UpdateView(arg_14_0):
	local var_14_0 = getProxy(ActivityProxy)
	local var_14_1
	local var_14_2 = var_14_0.getActivityById(ActivityConst.MUSIC_FESTIVAL_ID_2)
	local var_14_3 = getProxy(MiniGameProxy).GetHubByHubId(var_14_2.getConfig("config_id"))
	local var_14_4 = var_14_3.count > 0
	local var_14_5 = arg_14_0.upper_jichangwutai.Find("tip")

	setActive(var_14_5, var_14_4)

	local var_14_6 = var_14_3.usedtime >= var_14_3.getConfig("reward_need") and var_14_3.ultimate == 0

	setActive(arg_14_0.modelTip, var_14_6)

	local var_14_7 = var_14_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_PT_BUFF)
	local var_14_8 = arg_14_0.upper_leijipt.Find("tip")
	local var_14_9 = var_14_7.readyToAchieve()

	setActive(var_14_8, var_14_9)

	local var_14_10 = arg_14_0.upper_jinianzhang.Find("tip")
	local var_14_11 = var_0_0.MedalTip()

	setActive(var_14_10, var_14_11)

def var_0_0.getStageShip(arg_15_0):
	local var_15_0 = getProxy(ActivityProxy)
	local var_15_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.MUSIC_FESTIVAL_ID_2)

	if not var_15_1:
		return

	local var_15_2 = var_15_1.getConfig("config_client")
	local var_15_3 = var_15_2 and var_15_2.stage_on_ship

	if var_15_3:
		local var_15_4 = #var_15_3

		return var_15_3[math.random(1, var_15_4)], var_15_3.action[1]

def var_0_0.updateStageShip(arg_16_0):
	local var_16_0, var_16_1 = arg_16_0.getStageShip()

	if not var_16_0:
		return

	arg_16_0.loader.GetSpine(var_16_0, function(arg_17_0)
		arg_17_0.transform.localScale = Vector3(0.63, 0.63, 1)
		arg_17_0.transform.localPosition = Vector3.zero

		arg_17_0.transform.SetParent(arg_16_0._stageShip, False)
		arg_17_0.transform.SetSiblingIndex(1)
		setActive(arg_16_0._stageShip, True)
		arg_17_0.GetComponent(typeof(SpineAnimUI)).SetAction(var_16_1, 0), arg_16_0._stageShip)

def var_0_0.getStudents(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0 = {}
	local var_18_1 = getProxy(ActivityProxy).getActivityById(arg_18_0)

	if not var_18_1:
		return var_18_0

	local var_18_2 = var_18_1.getConfig("config_client")

	var_18_2 = var_18_2 and var_18_2.stage_off_ship

	if var_18_2:
		local var_18_3 = Clone(var_18_2)
		local var_18_4 = math.random(arg_18_1, arg_18_2)
		local var_18_5 = #var_18_3

		while var_18_4 > 0 and var_18_5 > 0:
			local var_18_6 = math.random(1, var_18_5)

			table.insert(var_18_0, var_18_3[var_18_6])

			var_18_3[var_18_6] = var_18_3[var_18_5]
			var_18_5 = var_18_5 - 1
			var_18_4 = var_18_4 - 1

	return var_18_0

def var_0_0.MedalTip():
	local var_19_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

	return Activity.IsActivityReady(var_19_0)

def var_0_0.IsShowMainTip(arg_20_0):
	local var_20_0 = getProxy(ActivityProxy)
	local var_20_1 = var_20_0.getActivityById(ActivityConst.MUSIC_FESTIVAL_ID_2)

	assert(var_20_1)

	local function var_20_2()
		local var_21_0 = var_20_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_PT_BUFF)

		return var_21_0 and not var_21_0.isEnd() and var_21_0.readyToAchieve()

	local var_20_3 = var_0_0.MedalTip

	local function var_20_4()
		local var_22_0 = getProxy(MiniGameProxy).GetHubByHubId(var_20_1.getConfig("config_id"))

		return var_22_0.usedtime >= var_22_0.getConfig("reward_need") and var_22_0.ultimate == 0

	local function var_20_5()
		return getProxy(MiniGameProxy).GetHubByHubId(var_20_1.getConfig("config_id")).count > 0

	return var_20_2() or var_20_3() or var_20_4() or var_20_5()

def var_0_0.willExit(arg_24_0):
	arg_24_0.clearStudents()
	var_0_0.super.willExit(arg_24_0)

return var_0_0

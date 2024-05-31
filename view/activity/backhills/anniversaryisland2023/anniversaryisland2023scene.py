local var_0_0 = class("AnniversaryIsland2023Scene", import("view.activity.BackHills.TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "AnniversaryIsland2023UI"

var_0_0.edge2area = {
	default = "_SDPlace"
}
var_0_0.Buildings = {
	[24] = "craft",
	[25] = "adventure",
	[26] = "dining",
	[23] = "living"
}

def var_0_0.Ctor(arg_2_0):
	var_0_0.super.Ctor(arg_2_0)

	arg_2_0.loader = AutoLoader.New()

def var_0_0.preload(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.CalculateSceneLevel()

	arg_3_0.loader.LoadBundle("ui/" .. arg_3_0.getUIName() .. "_level" .. var_3_0, arg_3_1)

def var_0_0.init(arg_4_0):
	arg_4_0.top = arg_4_0.findTF("top")
	arg_4_0._bg = arg_4_0.findTF("BG")
	arg_4_0._map = arg_4_0.findTF("map")

	for iter_4_0 = 0, arg_4_0._map.childCount - 1:
		local var_4_0 = arg_4_0._map.GetChild(iter_4_0)
		local var_4_1 = go(var_4_0).name

		arg_4_0["map_" .. var_4_1] = var_4_0

	arg_4_0._upper = arg_4_0.findTF("upper")

	for iter_4_1 = 0, arg_4_0._upper.childCount - 1:
		local var_4_2 = arg_4_0._upper.GetChild(iter_4_1)
		local var_4_3 = go(var_4_2).name

		arg_4_0["upper_" .. var_4_3] = var_4_2

	arg_4_0._SDPlace = arg_4_0._tf.Find("SDPlace")
	arg_4_0.containers = {
		arg_4_0._SDPlace
	}
	arg_4_0._shipTpl = arg_4_0._map.Find("ship")
	arg_4_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.AnniversaryIsland2023Graph"))

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("top/Back"), function()
		arg_5_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.findTF("top/Home"), function()
		arg_5_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.haidaojudian_help.tip
		}), SFX_PANEL)

	local var_5_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

	arg_5_0.InitStudents(var_5_0 and var_5_0.id, 3, 4)

	for iter_5_0, iter_5_1 in pairs(arg_5_0.Buildings):
		arg_5_0.InitFacilityCross(arg_5_0._map, arg_5_0._upper, iter_5_1, function()
			arg_5_0.emit(BackHillMediatorTemplate.GO_SUBLAYER, Context.New({
				mediator = AnniversaryIslandBuildingUpgrade2023WindowMediator,
				viewComponent = AnniversaryIslandBuildingUpgrade2023Window,
				data = {
					buildingID = iter_5_0
				}
			})))
		eachChild(arg_5_0._map.Find(iter_5_1), function(arg_10_0)
			GetComponent(arg_10_0, typeof(Image)).alphaHitTestMinimumThreshold = 0.5

			setActive(arg_10_0, False))

	eachChild(arg_5_0._map.Find("xianshijianzao"), function(arg_11_0)
		GetComponent(arg_11_0, typeof(Image)).alphaHitTestMinimumThreshold = 0.5)
	eachChild(arg_5_0._map.Find("huanzhuangshangdian"), function(arg_12_0)
		GetComponent(arg_12_0, typeof(Image)).alphaHitTestMinimumThreshold = 0.5)
	eachChild(arg_5_0._map.Find("taskboard"), function(arg_13_0)
		GetComponent(arg_13_0, typeof(Image)).alphaHitTestMinimumThreshold = 0.5)

	GetComponent(arg_5_0._map.Find("bigmap"), typeof(Image)).alphaHitTestMinimumThreshold = 0.5

	arg_5_0.InitFacilityCross(arg_5_0._map, arg_5_0._upper, "craft", function()
		arg_5_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_WORKBENCH))
	arg_5_0.InitFacilityCross(arg_5_0._map, arg_5_0._upper, "taskboard", function()
		local var_15_0 = Context.New()

		SCENE.SetSceneInfo(var_15_0, SCENE.ISLAND_TASK)
		arg_5_0.emit(BackHillMediatorTemplate.GO_SUBLAYER, var_15_0))
	arg_5_0.InitFacilityCross(arg_5_0._map, arg_5_0._upper, "bigmap", function()
		arg_5_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
			checkMain = True
		}))
	arg_5_0.InitFacilityCross(arg_5_0._map, arg_5_0._upper, "giftmake", function()
		arg_5_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.SCULPTURE))
	arg_5_0.BindItemSkinShop()
	arg_5_0.BindItemBuildShip()
	arg_5_0.RegisterDataResponse()
	arg_5_0.UpdateView()

def var_0_0.UpdateActivity(arg_18_0, arg_18_1):
	arg_18_0.UpdateView()

def var_0_0.RegisterDataResponse(arg_19_0):
	arg_19_0.Respones = ResponsableTree.CreateShell({})

	arg_19_0.Respones.SetRawData("view", arg_19_0)

	local var_19_0 = _.values(arg_19_0.Buildings)

	for iter_19_0, iter_19_1 in ipairs(var_19_0):
		arg_19_0.Respones.AddRawListener({
			"view",
			iter_19_1
		}, function(arg_20_0, arg_20_1)
			if not arg_20_1:
				return

			setActive(arg_20_0["map_" .. iter_19_1].Find(tostring(arg_20_1)), True)

			if arg_20_1 - 1 > 0:
				setActive(arg_20_0["map_" .. iter_19_1].Find(tostring(arg_20_1 - 1)), False)

			local var_20_0 = arg_20_0["map_" .. iter_19_1].Find(tostring(arg_20_1))

			arg_20_0.loader.GetSpriteQuiet("ui/" .. arg_19_0.getUIName() .. "_atlas", iter_19_1 .. "_" .. arg_20_1, var_20_0, True)

			GetComponent(arg_20_0["map_" .. iter_19_1], typeof(Button)).targetGraphic = GetComponent(var_20_0, typeof(Image))

			local var_20_1 = arg_20_0["upper_" .. iter_19_1]

			if not var_20_1 or IsNil(var_20_1.Find("Level")):
				return

			arg_20_0.loader.GetSpriteQuiet("ui/" .. arg_19_0.getUIName() .. "_atlas", tostring(arg_20_1), var_20_1.Find("Level"), True))

	arg_19_0.Respones.AddRawListener(_.values(arg_19_0.Buildings), function(...)
		local var_21_0 = 0
		local var_21_1 = {
			...
		}

		for iter_21_0 = 1, table.getCount(arg_19_0.Buildings):
			var_21_0 = var_21_0 + (var_21_1[iter_21_0] or 1)

		arg_19_0.Respones.sceneLevel = math.floor(var_21_0 / 4))
	arg_19_0.Respones.AddRawListener({
		"sceneLevel",
		"view"
	}, function(arg_22_0, arg_22_1, arg_22_2, arg_22_3)
		local var_22_0 = arg_22_1[1]
		local var_22_1 = arg_22_1[2]

		local function var_22_2(arg_23_0)
			setActive(var_22_1["map_" .. arg_23_0].Find(tostring(var_22_0)), True)

			if arg_22_2[1]:
				setActive(var_22_1["map_" .. arg_23_0].Find(tostring(arg_22_2[1])), False)

			local var_23_0 = {
				huanzhuangshangdian = "skinshop",
				xianshijianzao = "buildship",
				taskboard = "taskboard"
			}
			local var_23_1 = var_22_1["map_" .. arg_23_0].Find(tostring(var_22_0))

			var_22_1.loader.GetSpriteQuiet("ui/" .. arg_19_0.getUIName() .. "_level" .. var_22_0, var_23_0[arg_23_0], var_23_1, True)

			GetComponent(var_22_1["map_" .. arg_23_0], typeof(Button)).targetGraphic = GetComponent(var_23_1, typeof(Image))

		var_22_2("xianshijianzao")
		var_22_2("huanzhuangshangdian")
		var_22_2("taskboard")
		var_22_1.loader.GetSpriteQuiet("ui/" .. arg_19_0.getUIName() .. "_atlas", "title_" .. var_22_0, var_22_1.findTF("top/Title/Number"), True)
		var_22_1.loader.GetSpriteQuiet("ui/" .. arg_19_0.getUIName() .. "_level" .. var_22_0, "bg", var_22_1.findTF("map")), {
		useOldRef = True
	})

	local var_19_1 = {
		"taskboard",
		"bigmap",
		"giftmake"
	}

	table.insertto(var_19_1, var_19_0)

	for iter_19_2, iter_19_3 in ipairs(var_19_1):
		arg_19_0.Respones.AddRawListener({
			"view",
			iter_19_3 .. "Tip"
		}, function(arg_24_0, arg_24_1)
			local var_24_0 = arg_24_0["upper_" .. iter_19_3]

			if not var_24_0 or IsNil(var_24_0.Find("Tip")):
				return

			setActive(var_24_0.Find("Tip"), arg_24_1))

	arg_19_0.Respones.hubData = {}

	arg_19_0.Respones.AddRawListener({
		"view",
		"hubData"
	}, function(arg_25_0, arg_25_1)
		arg_25_0.gameCountTxt.text = "X " .. arg_25_1.count, {
		strict = True
	})
	arg_19_0.Respones.AddRawListener({
		"view",
		"materialCount"
	}, function(arg_26_0, arg_26_1)
		arg_26_0.materialTxt.text = arg_26_1)

def var_0_0.PlayStory():
	local var_27_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)
	local var_27_1 = var_27_0.GetTotalBuildingLevel()
	local var_27_2 = {
		False,
		var_27_0.getConfig("config_client").lv2Story,
		var_27_0.getConfig("config_client").lv3Story,
		var_27_0.getConfig("config_client").lv4Story
	}

	table.SerialIpairsAsync(var_27_2, function(arg_28_0, arg_28_1, arg_28_2)
		if arg_28_0 <= var_27_1 and arg_28_1:
			pg.NewStoryMgr.GetInstance().Play(arg_28_1, arg_28_2)
		else
			arg_28_2())

def var_0_0.UpdateView(arg_29_0):
	AnniversaryIsland2023Scene.PlayStory()

	local var_29_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

	for iter_29_0, iter_29_1 in pairs(arg_29_0.Buildings):
		arg_29_0.Respones[iter_29_1] = var_29_0.data1KeyValueList[2][iter_29_0] or 1
		arg_29_0.Respones[iter_29_1 .. "Tip"] = arg_29_0.UpdateBuildingTip(var_29_0, iter_29_0)

	local var_29_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH)

	arg_29_0.Respones.craftTip = arg_29_0.Respones.craftTip or var_29_1.HasAvaliableFormula() and getProxy(SettingsProxy).IsTipWorkbenchDaily()

	local function var_29_2()
		local var_30_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

		return Activity.IsActivityReady(var_30_0)

	arg_29_0.Respones.bigmapTip = tobool(var_29_2())

	local function var_29_3()
		return getProxy(ActivityTaskProxy).getActTaskTip(ActivityConst.ISLAND_TASK_ID)

	arg_29_0.Respones.taskboardTip = tobool(var_29_3())

	local function var_29_4()
		local var_32_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SCULPTURE)

		return Activity.IsActivityReady(var_32_0)

	arg_29_0.Respones.giftmakeTip = tobool(var_29_4())

def var_0_0.CalculateSceneLevel(arg_33_0):
	return getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2).GetTotalBuildingLevel()

def var_0_0.UpdateBuildingTip(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = var_0_0.super.UpdateBuildingTip(arg_34_0, arg_34_1, arg_34_2)

	if var_34_0:
		local var_34_1 = arg_34_1.data1KeyValueList[2][arg_34_2] or 1

		var_34_0 = var_34_0 and var_34_1 <= arg_34_1.GetTotalBuildingLevel()

	return var_34_0

def var_0_0.willExit(arg_35_0):
	arg_35_0.clearStudents()
	var_0_0.super.willExit(arg_35_0)

def var_0_0.IsShowMainTip(arg_36_0):
	if arg_36_0 and not arg_36_0.isEnd():
		local function var_36_0()
			local var_37_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

			return Activity.IsActivityReady(var_37_0)

		local function var_36_1()
			local var_38_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

			for iter_38_0, iter_38_1 in ipairs(var_38_0.GetBuildingIds()):
				if AnniversaryIsland2023Scene.UpdateBuildingTip(None, var_38_0, iter_38_1):
					return True

			if getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH).HasAvaliableFormula() and getProxy(SettingsProxy).IsTipWorkbenchDaily():
				return True

		local function var_36_2()
			return getProxy(ActivityTaskProxy).getActTaskTip(ActivityConst.ISLAND_TASK_ID)

		local function var_36_3()
			local var_40_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SCULPTURE)

			return Activity.IsActivityReady(var_40_0)

		return var_36_0() or var_36_1() or var_36_2() or var_36_3()

return var_0_0

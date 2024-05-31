local var_0_0 = class("AmusementParkScene", import("..TemplateMV.BackHillTemplate"))

var_0_0.UIName = "AmusementParkUI"
var_0_0.edge2area = {
	default = "map_middle",
	["1_1"] = "map_top"
}
var_0_0.Buildings = {
	[9] = "xuanzhuanmuma",
	[10] = "guoshanche",
	[12] = "haidaochuan",
	[11] = "tiaolouji"
}

def var_0_0.init(arg_1_0):
	arg_1_0.top = arg_1_0.findTF("Top")
	arg_1_0._map = arg_1_0.findTF("map")

	for iter_1_0 = 0, arg_1_0._map.childCount - 1:
		local var_1_0 = arg_1_0._map.GetChild(iter_1_0)
		local var_1_1 = go(var_1_0).name

		arg_1_0["map_" .. var_1_1] = var_1_0

	arg_1_0._shipTpl = arg_1_0._map.Find("ship")
	arg_1_0.containers = {
		arg_1_0.map_middle,
		arg_1_0.map_top
	}
	arg_1_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.AmusementParkGraph"))
	arg_1_0._upper = arg_1_0.findTF("upper")

	for iter_1_1 = 0, arg_1_0._upper.childCount - 1:
		local var_1_2 = arg_1_0._upper.GetChild(iter_1_1)
		local var_1_3 = go(var_1_2).name

		arg_1_0["upper_" .. var_1_3] = var_1_2

	arg_1_0.gameCountTxt = arg_1_0.top.Find("GameCount/text").GetComponent(typeof(Text))
	arg_1_0.materialTxt = arg_1_0.top.Find("MaterialCount/text").GetComponent(typeof(Text))

	setActive(arg_1_0.map_huiyichengbao, PLATFORM_CODE == PLATFORM_CH)
	setActive(arg_1_0.upper_huiyichengbao, PLATFORM_CODE == PLATFORM_CH)
	arg_1_0.RegisterDataResponse()

	arg_1_0.loader = AutoLoader.New()

def var_0_0.RegisterDataResponse(arg_2_0):
	arg_2_0.Respones = ResponsableTree.CreateShell({})

	arg_2_0.Respones.SetRawData("view", arg_2_0)

	local var_2_0 = {
		"guoshanche",
		"haidaochuan",
		"xuanzhuanmuma",
		"tiaolouji"
	}

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		arg_2_0.Respones.AddRawListener({
			"view",
			iter_2_1
		}, function(arg_3_0, arg_3_1)
			if not arg_3_1:
				return

			arg_3_0.loader.GetSpriteQuiet("ui/AmusementParkUI_atlas", "entrance_" .. iter_2_1 .. arg_3_1, arg_3_0["map_" .. iter_2_1])

			local var_3_0 = arg_3_0["upper_" .. iter_2_1]

			if not var_3_0 or IsNil(var_3_0.Find("Level")):
				return

			setText(var_3_0.Find("Level"), "LV." .. arg_3_1))

	local var_2_1 = {
		"guoshanche",
		"haidaochuan",
		"xuanzhuanmuma",
		"tiaolouji",
		"dangaobaoweizhan",
		"jiujiuduihuanwu"
	}

	for iter_2_2, iter_2_3 in ipairs(var_2_1):
		arg_2_0.Respones.AddRawListener({
			"view",
			iter_2_3 .. "Tip"
		}, function(arg_4_0, arg_4_1)
			local var_4_0 = arg_4_0["upper_" .. iter_2_3]

			if not var_4_0 or IsNil(var_4_0.Find("Tip")):
				return

			setActive(var_4_0.Find("Tip"), arg_4_1))

	arg_2_0.Respones.hubData = {}

	arg_2_0.Respones.AddRawListener({
		"view",
		"hubData"
	}, function(arg_5_0, arg_5_1)
		arg_5_0.gameCountTxt.text = "X" .. arg_5_1.count, {
		strict = True
	})
	arg_2_0.Respones.AddRawListener({
		"view",
		"materialCount"
	}, function(arg_6_0, arg_6_1)
		arg_6_0.materialTxt.text = arg_6_1)

def var_0_0.didEnter(arg_7_0):
	onButton(arg_7_0, arg_7_0.top.Find("Back"), function()
		arg_7_0.emit(var_0_0.ON_BACK))
	onButton(arg_7_0, arg_7_0.top.Find("Home"), function()
		arg_7_0.emit(var_0_0.ON_HOME))
	onButton(arg_7_0, arg_7_0.top.Find("Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.amusementpark_help.tip
		}))
	onButton(arg_7_0, arg_7_0.top.Find("Invitation"), function()
		local var_11_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CLIENT_DISPLAY)

		if var_11_0 and not var_11_0.isEnd():
			arg_7_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ACTIVITY, {
				id = var_11_0.id
			}))
	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "jiujiuduihuanwu", function()
		arg_7_0.emit(AmusementParkMediator.GO_SUBLAYER, Context.New({
			mediator = AmusementParkShopMediator,
			viewComponent = AmusementParkShopPage
		})))

	for iter_7_0, iter_7_1 in pairs(arg_7_0.Buildings):
		arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, iter_7_1, function()
			arg_7_0.emit(BackHillMediatorTemplate.GO_SUBLAYER, Context.New({
				mediator = BuildingUpgradeMediator,
				viewComponent = BuildingUpgradeLayer,
				data = {
					buildingID = iter_7_0
				}
			})))

	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "dangaobaoweizhan", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 23))
	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "huiyichengbao", function()
		arg_7_0.emit(AmusementParkMediator.GO_SCENE, SCENE.SUMMARY))
	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "xianshijianzao", function()
		arg_7_0.emit(AmusementParkMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		}))
	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "huanzhuangshandian", function()
		arg_7_0.emit(AmusementParkMediator.GO_SCENE, SCENE.SKINSHOP))

	local var_7_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)

	arg_7_0.InitStudents(var_7_0 and var_7_0.id, 2, 3)
	arg_7_0.UpdateView()
	arg_7_0.loader.LoadPrefab("ui/houshan_caidai", "", function(arg_18_0)
		setParent(arg_18_0, arg_7_0._map))

def var_0_0.UpdateActivity(arg_19_0, arg_19_1):
	arg_19_0.activity = arg_19_1
	arg_19_0.Respones.xuanzhuanmuma = arg_19_1.data1KeyValueList[2][9] or 1
	arg_19_0.Respones.guoshanche = arg_19_1.data1KeyValueList[2][10] or 1
	arg_19_0.Respones.tiaolouji = arg_19_1.data1KeyValueList[2][11] or 1
	arg_19_0.Respones.haidaochuan = arg_19_1.data1KeyValueList[2][12] or 1

	local var_19_0 = next(arg_19_1.data1KeyValueList[1])

	arg_19_0.Respones.materialCount = arg_19_1.data1KeyValueList[1][var_19_0] or 0

	arg_19_0.UpdateView()

def var_0_0.UpdateView(arg_20_0):
	local var_20_0
	local var_20_1 = getProxy(ActivityProxy)

	arg_20_0.Respones.xuanzhuanmumaTip = arg_20_0.UpdateBuildingTip(arg_20_0.activity, 9)
	arg_20_0.Respones.guoshancheTip = arg_20_0.UpdateBuildingTip(arg_20_0.activity, 10)
	arg_20_0.Respones.tiaoloujiTip = arg_20_0.UpdateBuildingTip(arg_20_0.activity, 11)
	arg_20_0.Respones.haidaochuanTip = arg_20_0.UpdateBuildingTip(arg_20_0.activity, 12)

	local var_20_2 = var_20_1.getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)
	local var_20_3 = getProxy(MiniGameProxy).GetHubByHubId(var_20_2.getConfig("config_id"))
	local var_20_4 = var_20_3.count > 0

	arg_20_0.Respones.dangaobaoweizhanTip = var_20_4

	arg_20_0.UpdateHubData(var_20_3)

	arg_20_0.Respones.jiujiuduihuanwuTip = AmusementParkShopPage.GetActivityShopTip()

def var_0_0.UpdateHubData(arg_21_0, arg_21_1):
	arg_21_0.Respones.hubData.count = arg_21_1.count
	arg_21_0.Respones.hubData.usedtime = arg_21_1.usedtime
	arg_21_0.Respones.hubData.id = arg_21_1.id

	arg_21_0.Respones.PropertyChange("hubData")

def var_0_0.willExit(arg_22_0):
	arg_22_0.clearStudents()
	var_0_0.super.willExit(arg_22_0)

return var_0_0

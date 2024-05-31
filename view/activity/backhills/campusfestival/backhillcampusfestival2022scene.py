local var_0_0 = class("BackHillCampusFestival2022Scene", import("..TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "BackHillCampusFestivalUI"

var_0_0.edge2area = {
	default = "_SDPlace"
}
var_0_0.Buildings = {
	[19] = "teachingbuilding",
	[20] = "astrologerstent",
	[21] = "stage",
	[22] = "shoppingstreet"
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

	setActive(arg_2_0.map_Decoration, False)

	arg_2_0._SDPlace = arg_2_0._map.Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0.gameCountTxt = arg_2_0.top.Find("GameCount/Text").GetComponent(typeof(Text))
	arg_2_0.materialTxt = arg_2_0.top.Find("Material/Text").GetComponent(typeof(Text))
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.BackHillCampusFestiva2022Graph"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/Back"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Home"), function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.backhill_campusfestival_tip.tip
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Invitation"), function()
		local var_7_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.INVITATION_JP_FIFTH)

		if var_7_0 and not var_7_0.isEnd():
			arg_3_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ACTIVITY, {
				id = var_7_0.id
			}))

	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_CAKEMAKING)

	arg_3_0.InitStudents(var_3_0 and var_3_0.id, 3, 4)
	arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "cakeshop", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 42))

	for iter_3_0, iter_3_1 in pairs(arg_3_0.Buildings):
		arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, iter_3_1, function()
			arg_3_0.emit(BackHillMediatorTemplate.GO_SUBLAYER, Context.New({
				mediator = BuildingUpgradeMediator,
				viewComponent = BuildingUpgradeLayer,
				data = {
					buildingID = iter_3_0
				}
			})))

	setActive(arg_3_0.upper_shujvhuigu, PLATFORM_CODE == PLATFORM_JP)

	if PLATFORM_CODE == PLATFORM_JP:
		local function var_3_1()
			arg_3_0.emit(NewYearFestivalMediator.GO_SCENE, SCENE.SUMMARY)

		arg_3_0.InitFacilityCross(arg_3_0._map, arg_3_0._upper, "shujvhuigu", var_3_1)

	arg_3_0.BindItemSkinShop()
	arg_3_0.BindItemBuildShip()
	arg_3_0.RegisterDataResponse()
	arg_3_0.UpdateView()

def var_0_0.UpdateActivity(arg_11_0, arg_11_1):
	if arg_11_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF:
		arg_11_0.UpdateView()

local var_0_1 = {
	Vector2(-744, -187.3),
	Vector2(-744, -187.3),
	Vector2(-801.7, -149)
}

def var_0_0.RegisterDataResponse(arg_12_0):
	arg_12_0.Respones = ResponsableTree.CreateShell({})

	arg_12_0.Respones.SetRawData("view", arg_12_0)

	local var_12_0 = _.values(arg_12_0.Buildings)

	for iter_12_0, iter_12_1 in ipairs(var_12_0):
		arg_12_0.Respones.AddRawListener({
			"view",
			iter_12_1
		}, function(arg_13_0, arg_13_1)
			if not arg_13_1:
				return

			arg_13_0.loader.GetSpriteQuiet("ui/" .. arg_12_0.getUIName() .. "_atlas", "entrance_" .. iter_12_1 .. arg_13_1, arg_13_0["map_" .. iter_12_1], True)

			local var_13_0 = arg_13_0["upper_" .. iter_12_1]

			if not var_13_0 or IsNil(var_13_0.Find("Lv")):
				return

			setText(var_13_0.Find("Lv"), arg_13_1))

	arg_12_0.Respones.AddRawListener({
		"view",
		"stage"
	}, function(arg_14_0, arg_14_1)
		local var_14_0 = arg_14_0.map_stage

		setAnchoredPosition(var_14_0, var_0_1[arg_14_1]))

	local var_12_1 = {
		"cakeshop",
		"shujvhuigu"
	}

	table.insertto(var_12_1, var_12_0)

	for iter_12_2, iter_12_3 in ipairs(var_12_1):
		arg_12_0.Respones.AddRawListener({
			"view",
			iter_12_3 .. "Tip"
		}, function(arg_15_0, arg_15_1)
			local var_15_0 = arg_15_0["upper_" .. iter_12_3]

			if not var_15_0 or IsNil(var_15_0.Find("Tip")):
				return

			setActive(var_15_0.Find("Tip"), arg_15_1))

	arg_12_0.Respones.hubData = {}

	arg_12_0.Respones.AddRawListener({
		"view",
		"hubData"
	}, function(arg_16_0, arg_16_1)
		arg_16_0.gameCountTxt.text = "X " .. arg_16_1.count, {
		strict = True
	})
	arg_12_0.Respones.AddRawListener({
		"view",
		"materialCount"
	}, function(arg_17_0, arg_17_1)
		arg_17_0.materialTxt.text = arg_17_1)

def var_0_0.UpdateView(arg_18_0):
	local var_18_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

	for iter_18_0, iter_18_1 in pairs(arg_18_0.Buildings):
		arg_18_0.Respones[iter_18_1] = var_18_0.data1KeyValueList[2][iter_18_0] or 1
		arg_18_0.Respones[iter_18_1 .. "Tip"] = arg_18_0.UpdateBuildingTip(var_18_0, iter_18_0)

	local var_18_1 = _.all(_.keys(arg_18_0.Buildings), function(arg_19_0)
		local var_19_0 = var_18_0.data1KeyValueList[2][arg_19_0] or 1
		local var_19_1 = pg.activity_event_building[arg_19_0]

		return var_19_1 and var_19_0 >= #var_19_1.buff)

	setActive(arg_18_0.map_Decoration, var_18_1)

	local var_18_2 = next(var_18_0.data1KeyValueList[1])

	arg_18_0.Respones.materialCount = var_18_0.data1KeyValueList[1][var_18_2] or 0

	local function var_18_3()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_CAKEMAKING)

	arg_18_0.Respones.cakeshopTip = tobool(var_18_3())

	local var_18_4 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_CAKEMAKING)
	local var_18_5 = getProxy(MiniGameProxy).GetHubByHubId(var_18_4.getConfig("config_id"))

	arg_18_0.UpdateHubData(var_18_5)

	local function var_18_6()
		if PLATFORM_CODE != PLATFORM_JP:
			return

		local var_21_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_21_0)

	arg_18_0.Respones.shujvhuiguTip = tobool(var_18_6())

def var_0_0.UpdateHubData(arg_22_0, arg_22_1):
	arg_22_0.Respones.hubData.count = arg_22_1.count
	arg_22_0.Respones.hubData.usedtime = arg_22_1.usedtime
	arg_22_0.Respones.hubData.id = arg_22_1.id

	arg_22_0.Respones.PropertyChange("hubData")

def var_0_0.IsShowMainTip(arg_23_0):
	local function var_23_0()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_CAKEMAKING)

	local function var_23_1()
		local var_25_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

		return Activity.IsActivityReady(var_25_0)

	local function var_23_2()
		if PLATFORM_CODE != PLATFORM_JP:
			return

		local var_26_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_26_0)

	return var_23_0() or var_23_1() or var_23_2()

def var_0_0.willExit(arg_27_0):
	arg_27_0.clearStudents()
	var_0_0.super.willExit(arg_27_0)

return var_0_0

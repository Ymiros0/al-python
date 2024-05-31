local var_0_0 = class("AmusementParkScene2", import("..TemplateMV.BackHillTemplate"))

var_0_0.UIName = "AmusementParkUI2"
var_0_0.edge2area = {
	default = "map_middle"
}
var_0_0.Buildings = {
	[13] = "jiujiuchonglang",
	[15] = "huahuashijie",
	[16] = "jiujiupubu",
	[14] = "jiujiutiaoshui"
}

local var_0_1 = 23

def var_0_0.init(arg_1_0):
	arg_1_0.top = arg_1_0.findTF("Top")
	arg_1_0._map = arg_1_0.findTF("map")

	for iter_1_0 = 0, arg_1_0._map.childCount - 1:
		local var_1_0 = arg_1_0._map.GetChild(iter_1_0)
		local var_1_1 = go(var_1_0).name

		arg_1_0["map_" .. var_1_1] = var_1_0

	arg_1_0._shipTpl = arg_1_0._map.Find("ship")
	arg_1_0.containers = {
		arg_1_0.map_middle
	}
	arg_1_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.AmusementParkGraph2"))
	arg_1_0._upper = arg_1_0.findTF("upper")

	for iter_1_1 = 0, arg_1_0._upper.childCount - 1:
		local var_1_2 = arg_1_0._upper.GetChild(iter_1_1)
		local var_1_3 = go(var_1_2).name

		arg_1_0["upper_" .. var_1_3] = var_1_2

	arg_1_0.gameCountTxt = arg_1_0.top.Find("GameCount/text").GetComponent(typeof(Text))
	arg_1_0.materialTxt = arg_1_0.top.Find("MaterialCount/text").GetComponent(typeof(Text))

	if PLATFORM_CODE != PLATFORM_JP:
		setActive(arg_1_0.upper_jinianchengbao, False)

		GetOrAddComponent(arg_1_0.map_jinianchengbao, typeof(Button)).enabled = False

	arg_1_0.RegisterDataResponse()

	arg_1_0.loader = AutoLoader.New()

def var_0_0.RegisterDataResponse(arg_2_0):
	arg_2_0.Respones = ResponsableTree.CreateShell({})

	arg_2_0.Respones.SetRawData("view", arg_2_0)

	local var_2_0 = _.values(arg_2_0.Buildings)

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		arg_2_0.Respones.AddRawListener({
			"view",
			iter_2_1
		}, function(arg_3_0, arg_3_1)
			if not arg_3_1:
				return

			arg_3_0.loader.GetSpriteQuiet("ui/AmusementParkUI2_atlas", "entrance_" .. iter_2_1 .. arg_3_1, arg_3_0["map_" .. iter_2_1])

			local var_3_0 = arg_3_0["upper_" .. iter_2_1]

			if not var_3_0 or IsNil(var_3_0.Find("Level")):
				return

			setText(var_3_0.Find("Level"), "LV." .. arg_3_1))

	local var_2_1 = {
		"jiujiudalaotuan"
	}

	table.insertto(var_2_1, var_2_0)

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
			helps = pg.gametip.activity_event_building.tip
		}))
	onButton(arg_7_0, arg_7_0.top.Find("Invitation"), function()
		local var_11_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.JP_CEREMONY_INVITATION_ID)

		if var_11_0 and not var_11_0.isEnd():
			arg_7_0.emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ACTIVITY, {
				id = var_11_0.id
			}))

	for iter_7_0, iter_7_1 in pairs(arg_7_0.Buildings):
		arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, iter_7_1, function()
			arg_7_0.emit(BackHillMediatorTemplate.GO_SUBLAYER, Context.New({
				mediator = BuildingUpgradeMediator,
				viewComponent = BuildingUpgradeLayer,
				data = {
					buildingID = iter_7_0
				}
			})))

	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "jiujiudalaotuan", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 30))
	arg_7_0.InitFacilityCross(arg_7_0._map, arg_7_0._upper, "jinianchengbao", function()
		arg_7_0.emit(AmusementParkMediator.GO_SCENE, SCENE.SUMMARY))
	arg_7_0.BindItemSkinShop()
	arg_7_0.BindItemBuildShip()

	local var_7_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)

	arg_7_0.InitStudents(var_7_0 and var_7_0.id, 3, 4)
	arg_7_0.UpdateView()

def var_0_0.UpdateActivity(arg_15_0, arg_15_1):
	arg_15_0.activity = arg_15_1

	for iter_15_0, iter_15_1 in pairs(arg_15_0.Buildings):
		arg_15_0.Respones[iter_15_1] = arg_15_1.data1KeyValueList[2][iter_15_0] or 1

	local var_15_0 = next(arg_15_1.data1KeyValueList[1])

	arg_15_0.Respones.materialCount = arg_15_1.data1KeyValueList[1][var_15_0] or 0

	arg_15_0.UpdateView()

def var_0_0.UpdateView(arg_16_0):
	local var_16_0

	for iter_16_0, iter_16_1 in pairs(arg_16_0.Buildings):
		arg_16_0.Respones[iter_16_1 .. "Tip"] = arg_16_0.UpdateBuildingTip(arg_16_0.activity, iter_16_0)

	local var_16_1 = getProxy(MiniGameProxy).GetHubByHubId(var_0_1)
	local var_16_2 = var_16_1.count > 0

	arg_16_0.Respones.jiujiudalaotuanTip = var_16_2

	arg_16_0.UpdateHubData(var_16_1)

def var_0_0.UpdateHubData(arg_17_0, arg_17_1):
	arg_17_0.Respones.hubData.count = arg_17_1.count
	arg_17_0.Respones.hubData.usedtime = arg_17_1.usedtime
	arg_17_0.Respones.hubData.id = arg_17_1.id

	arg_17_0.Respones.PropertyChange("hubData")

def var_0_0.willExit(arg_18_0):
	arg_18_0.clearStudents()
	var_0_0.super.willExit(arg_18_0)

return var_0_0

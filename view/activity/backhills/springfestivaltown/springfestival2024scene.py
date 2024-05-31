local var_0_0 = class("SpringFestival2024Scene", import("view.activity.BackHills.TemplateMV.BackHillTemplate"))

def var_0_0.getUIName(arg_1_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return "SpringFestival2024TWUI"
	else
		return "SpringFestival2024UI"

var_0_0.edge2area = {
	default = "_SDPlace"
}
var_0_0.EffectPoolCnt = 3
var_0_0.Id2EffectName = {
	[70177] = "yanhua_hongbao",
	[70176] = "yanhua_Azurlane",
	[70175] = "yanhua_2024",
	[70174] = "yanhua_xiaojiajia",
	[70173] = "yanhua_xinxin",
	[70172] = "yanhua_jiezhi",
	[70171] = "yanhua_huangji",
	[70170] = "yanhua_chuanmao",
	[70169] = "yanhua_long",
	[70168] = "yanhua_mofang",
	[70167] = "yanhua_maomao",
	[70166] = "yanhua_02",
	[70165] = "yanhua_01",
	[70178] = "yanhua_denglong"
}
var_0_0.FireworkRange = Vector2(300, 300)
var_0_0.EffectPosLimit = {
	limitX = {
		-700,
		700
	},
	limitY = {
		250,
		500
	}
}
var_0_0.EffectInterval = 1
var_0_0.DelayPop = 2.5
var_0_0.SFX_LIST = {
	"event./ui/firework1",
	"event./ui/firework2",
	"event./ui/firework3",
	"event./ui/firework4"
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

	arg_2_0.tipTfs = _.map(_.range(arg_2_0._upper.childCount), function(arg_3_0)
		local var_3_0 = arg_2_0._upper.GetChild(arg_3_0 - 1)

		return {
			name = var_3_0.name,
			trans = var_3_0.Find("Tip")
		})
	arg_2_0._SDPlace = arg_2_0._tf.Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0._shipTpl = arg_2_0._map.Find("ship")
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.SpringFestival2024Graph"))
	arg_2_0.fireworksTF = arg_2_0.findTF("play_fireworks")

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0.findTF("top/Back"), function()
		arg_4_0.emit(var_0_0.ON_BACK))
	onButton(arg_4_0, arg_4_0.findTF("top/Home"), function()
		arg_4_0.emit(var_0_0.ON_HOME))
	onButton(arg_4_0, arg_4_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_chunjie2024.tip
		}))
	onButton(arg_4_0, arg_4_0.findTF("top/firework_btn"), function()
		arg_4_0.OpenFireworkLayer())
	arg_4_0.BindItemSkinShop()
	arg_4_0.BindItemBuildShip()

	local var_4_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_SPRING_FESTIVAL_2024)

	arg_4_0.InitStudents(var_4_0 and var_4_0.id, 4, 4)

	if PLATFORM_CODE == PLATFORM_CHT:
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "feicaiyingxinchuntw", function()
			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = ActivityConst.FIREWORK_PT_2024_ID
			}))
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "aomeiyingchun", function()
			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = ActivityConst.ACTIVITY_COUPLET
			}))
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "huazhongshijie", function()
			local var_11_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ACTIVITY_HUAZHONGSHIJIE)

			if not var_11_0 or var_11_0.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

				return

			local var_11_1 = var_11_0.getConfig("config_client").linkActID

			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = var_11_1
			}))
	else
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "feicaiyingxinchun", function()
			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = ActivityConst.FIREWORK_PT_2024_ID
			}))
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "meiyiyannian", function()
			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = ActivityConst.TAIYUAN_ALERT_TASK
			}))
		arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "xinchunmaoxianwang", function()
			arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.ACTIVITY, {
				id = ActivityConst.FEIYUEN_LOGIN
			}))

	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "fushundamaoxian", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 37))
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "jiujiudajiulou", function()
		arg_4_0.emit(SpringFestival2024Mediator.GO_SUBLAYER, Context.New({
			mediator = RedPacketMediator,
			viewComponent = RedPacketLayer,
			def onRemoved:()
				arg_4_0.PlayBGM()
		})))
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "huituriji", function()
		arg_4_0.emit(SpringFestival2024Mediator.GO_SCENE, SCENE.COLORING))
	arg_4_0.UpdateView()

	arg_4_0.firePools = {}

	if arg_4_0.contextData.openFireworkLayer:
		arg_4_0.contextData.openFireworkLayer = None

		arg_4_0.OpenFireworkLayer()
	else
		arg_4_0.PlayFireworks()

	if arg_4_0.contextData.isOpenRedPacket:
		arg_4_0.contextData.isOpenRedPacket = None

		arg_4_0.emit(SpringFestival2024Mediator.GO_SUBLAYER, Context.New({
			mediator = RedPacketMediator,
			viewComponent = RedPacketLayer,
			def onRemoved:()
				arg_4_0.PlayBGM()
		}))

def var_0_0.UpdateActivity(arg_20_0, arg_20_1):
	arg_20_0.UpdateView()

def var_0_0.UpdateView(arg_21_0):
	_.each(arg_21_0.tipTfs, function(arg_22_0)
		if arg_22_0.trans:
			setActive(arg_22_0.trans, tobool(var_0_0.CheckTip(arg_22_0.name))))

def var_0_0.OpenFireworkLayer(arg_23_0):
	arg_23_0.emit(SpringFestival2024Mediator.GO_SUBLAYER, Context.New({
		mediator = FireworkPanel2024Mediator,
		viewComponent = FireworkPanel2024Layer,
		data = {
			def onExit:()
				arg_23_0.PlayFireworks()
		}
	}))

def var_0_0.PlayFireworks(arg_25_0):
	local var_25_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FIREWORK)

	assert(var_25_0 and not var_25_0.isEnd(), "烟花活动(type92)已结束")

	local var_25_1 = getProxy(PlayerProxy).getData().id
	local var_25_2 = pg.activity_template[var_25_0.id].config_data[3]

	arg_25_0.fireworks = {}

	for iter_25_0 = 1, #var_25_2:
		local var_25_3 = PlayerPrefs.GetInt("fireworks_" .. var_25_0.id .. "_" .. var_25_1 .. "_pos_" .. iter_25_0)

		if var_25_3 != 0:
			table.insert(arg_25_0.fireworks, var_25_3)

	if #arg_25_0.fireworks == 0:
		return

	eachChild(arg_25_0.fireworksTF, function(arg_26_0)
		setActive(arg_26_0, False))
	setActive(arg_25_0.fireworksTF, True)
	arg_25_0.StopFireworksTimer()

	arg_25_0.index = 1
	arg_25_0.fireworksTimer = Timer.New(function()
		arg_25_0.PlayerOneFirework(), var_0_0.EffectInterval, #arg_25_0.fireworks)

	arg_25_0.fireworksTimer.Start()

def var_0_0.PlayerOneFirework(arg_28_0):
	if arg_28_0.index == #arg_28_0.fireworks:
		arg_28_0.managedTween(LeanTween.delayedCall, function()
			arg_28_0.StopPlayFireworks()
			arg_28_0.PlayFireworks(), var_0_0.DelayPop, None)

	local var_28_0 = arg_28_0.fireworks[arg_28_0.index]
	local var_28_1 = math.random(#var_0_0.SFX_LIST)

	if arg_28_0.firePools[var_28_0] and #arg_28_0.firePools[var_28_0] >= var_0_0.EffectPoolCnt:
		local var_28_2 = arg_28_0.firePools[var_28_0][var_0_0.EffectPoolCnt]

		setLocalPosition(var_28_2, arg_28_0.GetFireworkPos())
		setActive(var_28_2, False)
		setActive(var_28_2, True)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_0.SFX_LIST[var_28_1])
		table.removebyvalue(arg_28_0.firePools[var_28_0], var_28_2)
		table.insert(arg_28_0.firePools[var_28_0], var_28_2)
	else
		arg_28_0.loader.GetPrefab("ui/" .. var_0_0.Id2EffectName[var_28_0], "", function(arg_30_0)
			pg.ViewUtils.SetSortingOrder(arg_30_0, 1)
			setParent(arg_30_0, arg_28_0.fireworksTF)
			setLocalPosition(arg_30_0, arg_28_0.GetFireworkPos())
			setActive(arg_30_0, True)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_0.SFX_LIST[var_28_1])

			if not arg_28_0.firePools[var_28_0]:
				arg_28_0.firePools[var_28_0] = {}

			table.insert(arg_28_0.firePools[var_28_0], arg_30_0))

	arg_28_0.index = arg_28_0.index + 1

def var_0_0.GetFireworkPos(arg_31_0):
	local var_31_0 = Vector2(0, 0)

	if arg_31_0.lastPos:
		local var_31_1 = Vector2(arg_31_0.lastPos.x, arg_31_0.lastPos.y)
		local var_31_2 = math.abs(var_31_1.x - arg_31_0.lastPos.x)
		local var_31_3 = math.abs(var_31_1.y - arg_31_0.lastPos.y)

		while var_31_2 < var_0_0.FireworkRange.x / 2 and var_31_3 < var_0_0.FireworkRange.y or var_31_3 < var_0_0.FireworkRange.y / 2 and var_31_2 < var_0_0.FireworkRange.x:
			var_31_1.x = math.random(var_0_0.EffectPosLimit.limitX[1], var_0_0.EffectPosLimit.limitX[2])
			var_31_1.y = math.random(var_0_0.EffectPosLimit.limitY[1], var_0_0.EffectPosLimit.limitY[2])
			var_31_2 = math.abs(var_31_1.x - arg_31_0.lastPos.x)
			var_31_3 = math.abs(var_31_1.y - arg_31_0.lastPos.y)

		var_31_0 = var_31_1
	else
		var_31_0.x = math.random(var_0_0.EffectPosLimit.limitX[1], var_0_0.EffectPosLimit.limitX[2])
		var_31_0.y = math.random(var_0_0.EffectPosLimit.limitY[1], var_0_0.EffectPosLimit.limitY[2])

	arg_31_0.lastPos = var_31_0

	return var_31_0

def var_0_0.StopFireworksTimer(arg_32_0):
	if arg_32_0.fireworksTimer:
		arg_32_0.fireworksTimer.Stop()

		arg_32_0.fireworksTimer = None

def var_0_0.StopPlayFireworks(arg_33_0):
	arg_33_0.StopFireworksTimer()

	arg_33_0.fireworks = None
	arg_33_0.index = None

	setActive(arg_33_0.fireworksTF, False)

def var_0_0.willExit(arg_34_0):
	arg_34_0.StopPlayFireworks()
	arg_34_0.clearStudents()
	var_0_0.super.willExit(arg_34_0)

def var_0_0.CheckTip(arg_35_0):
	return switch(arg_35_0, {
		def fushundamaoxian:()
			return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_SPRING_FESTIVAL_2024),
		def huituriji:()
			return getProxy(ColoringProxy).CheckTodayTip(),
		def jiujiudajiulou:()
			return RedPacketLayer.isShowRedPoint(),
		def xinchunmaoxianwang:()
			local var_39_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEIYUEN_LOGIN)

			return Activity.IsActivityReady(var_39_0),
		def meiyiyannian:()
			local var_40_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.TAIYUAN_ALERT_TASK)

			return Activity.IsActivityReady(var_40_0),
		def feicaiyingxinchun:()
			local var_41_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FIREWORK_PT_2024_ID)

			return Activity.IsActivityReady(var_41_0),
		def feicaiyingxinchuntw:()
			local var_42_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FIREWORK_PT_2024_ID)

			return Activity.IsActivityReady(var_42_0),
		def aomeiyingchun:()
			local var_43_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ACTIVITY_COUPLET)

			return Activity.IsActivityReady(var_43_0),
		def huazhongshijie:()
			local var_44_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ACTIVITY_HUAZHONGSHIJIE)

			return Activity.IsActivityReady(var_44_0)
	}, function()
		return False)

def var_0_0.IsShowMainTip(arg_46_0):
	local var_46_0 = {
		"fushundamaoxian",
		"huituriji",
		"jiujiudajiulou",
		"xinchunmaoxianwang",
		"meiyiyannian",
		"feicaiyingxinchun"
	}

	if PLATFORM_CODE == PLATFORM_CHT:
		var_46_0 = {
			"fushundamaoxian",
			"huituriji",
			"jiujiudajiulou",
			"aomeiyingchun",
			"huazhongshijie",
			"feicaiyingxinchuntw"
		}

	return _.any(var_46_0, function(arg_47_0)
		return tobool(var_0_0.CheckTip(arg_47_0)))

return var_0_0

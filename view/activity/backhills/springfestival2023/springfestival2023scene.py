local var_0_0 = class("SpringFestival2023Scene", import("..TemplateMV.BackHillTemplate"))

var_0_0.Id2EffectName = {
	[70114] = "yanhua_xiaojiajia",
	[70113] = "yanhua_xinxin",
	[70112] = "yanhua_jiezhi",
	[70111] = "yanhua_huangji",
	[70110] = "yanhua_chuanmao",
	[70109] = "yanhua_tutu",
	[70108] = "yanhua_mofang",
	[70107] = "yanhua_maomao",
	[70106] = "yanhua_02",
	[70105] = "yanhua_01",
	[70118] = "yanhua_denglong",
	[70117] = "yanhua_hongbao",
	[70116] = "yanhua_Azurlane",
	[70115] = "yanhua_2023"
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

def var_0_0.getUIName(arg_1_0):
	return "SpringFestival2023UI"

var_0_0.edge2area = {
	default = "map_middle"
}

def var_0_0.init(arg_2_0):
	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0._map = arg_2_0.findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1:
		local var_2_0 = arg_2_0._map.GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0

	arg_2_0._shipTpl = arg_2_0._map.Find("ship")
	arg_2_0._upper = arg_2_0.findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1:
		local var_2_2 = arg_2_0._upper.GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2

	arg_2_0.tipTfs = _.map(_.range(arg_2_0._upper.childCount), function(arg_3_0)
		local var_3_0 = arg_2_0._upper.GetChild(arg_3_0 - 1)

		return {
			name = var_3_0.name,
			trans = var_3_0.Find("tip")
		})
	arg_2_0.fireworksTF = arg_2_0.findTF("play_fireworks")
	arg_2_0.containers = {
		arg_2_0.map_front,
		arg_2_0.map_middle
	}
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.SpringFestival2023Graph"))
	arg_2_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_4_0):
	if arg_4_0.contextData.openFireworkLayer:
		arg_4_0.contextData.openFireworkLayer = None

		arg_4_0.OpenFireworkLayer()

	onButton(arg_4_0, arg_4_0.findTF("top/return_btn"), function()
		arg_4_0.emit(var_0_0.ON_BACK))
	onButton(arg_4_0, arg_4_0.findTF("top/return_main_btn"), function()
		arg_4_0.emit(var_0_0.ON_HOME))
	onButton(arg_4_0, arg_4_0.findTF("top/help_btn"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_chunjie2023.tip
		}))
	onButton(arg_4_0, arg_4_0.findTF("top/firework_btn"), function()
		arg_4_0.OpenFireworkLayer())
	onButton(arg_4_0, arg_4_0.fireworksTF, function()
		arg_4_0.StopPlayFireworks())
	arg_4_0.BindItemSkinShop()
	arg_4_0.BindItemBuildShip()

	local var_4_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_SPRING_FESTIVAL_2023)

	arg_4_0.InitStudents(var_4_0 and var_4_0.id, 2, 3)
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "xiaoyouxi", function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 48))

	local var_4_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.FIREWORK_PT_ID)

	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "yanhua", function()
		arg_4_0.emit(SpringFestival2023Mediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_4_1 and var_4_1.id
		}))

	local var_4_2 = getProxy(ActivityProxy).getActivityById(ActivityConst.ACTIVITY_COUPLET)

	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "duilian", function()
		arg_4_0.emit(SpringFestival2023Mediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_4_2 and var_4_2.id
		}))
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "jiulou", function()
		arg_4_0.emit(NewYearFestivalMediator.GO_SUBLAYER, Context.New({
			mediator = RedPacketMediator,
			viewComponent = RedPacketLayer,
			def onRemoved:()
				arg_4_0.PlayBGM()
		})))
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "huituriji", function()
		arg_4_0.emit(SpringFestival2023Mediator.GO_SCENE, SCENE.COLORING))
	arg_4_0.InitFacilityCross(arg_4_0._map, arg_4_0._upper, "huazhongshijie", function()
		local var_16_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

		if not var_16_0 or var_16_0.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		local var_16_1 = var_16_0.getConfig("config_client").linkActID

		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = var_16_1
		}))
	arg_4_0.UpdateView()
	arg_4_0.AutoFitScreen()

def var_0_0.OpenFireworkLayer(arg_17_0):
	arg_17_0.emit(SpringFestival2023Mediator.GO_SUBLAYER, Context.New({
		mediator = FireworkPanelMediator,
		viewComponent = FireworkPanelLayer
	}))

def var_0_0.PlayFireworks(arg_18_0, arg_18_1):
	if not arg_18_1 or #arg_18_1 == 0:
		return

	setActive(arg_18_0._upper, False)
	setActive(arg_18_0.top, False)
	eachChild(arg_18_0.fireworksTF, function(arg_19_0)
		setActive(arg_19_0, False))
	setActive(arg_18_0.fireworksTF, True)
	arg_18_0.StopFireworksTimer()

	arg_18_0.fireworks = arg_18_1
	arg_18_0.index = 1

	arg_18_0.PlayerOneFirework()

	if #arg_18_1 > 1:
		arg_18_0.fireworksTimer = Timer.New(function()
			arg_18_0.PlayerOneFirework(), var_0_0.EffectInterval, #arg_18_1 - 1)

		arg_18_0.fireworksTimer.Start()

def var_0_0.PlayerOneFirework(arg_21_0):
	if arg_21_0.index == #arg_21_0.fireworks:
		arg_21_0.managedTween(LeanTween.delayedCall, function()
			arg_21_0.StopPlayFireworks(), var_0_0.DelayPop, None)

	local var_21_0 = arg_21_0.fireworks[arg_21_0.index]
	local var_21_1 = arg_21_0.fireworksTF.Find(tostring(var_21_0))
	local var_21_2 = math.random(#var_0_0.SFX_LIST)

	if var_21_1:
		setLocalPosition(var_21_1, arg_21_0.GetFireworkPos())
		setActive(var_21_1, True)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_0.SFX_LIST[var_21_2])
	else
		arg_21_0.loader.GetPrefab("ui/" .. var_0_0.Id2EffectName[var_21_0], "", function(arg_23_0)
			pg.ViewUtils.SetSortingOrder(arg_23_0, 1)

			arg_23_0.name = var_21_0

			setParent(arg_23_0, arg_21_0.fireworksTF)
			setLocalPosition(arg_23_0, arg_21_0.GetFireworkPos())
			setActive(arg_23_0, True)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_0.SFX_LIST[var_21_2]))

	arg_21_0.index = arg_21_0.index + 1

def var_0_0.GetFireworkPos(arg_24_0):
	local var_24_0 = Vector2(0, 0)

	if arg_24_0.lastPos:
		local var_24_1 = Vector2(arg_24_0.lastPos.x, arg_24_0.lastPos.y)
		local var_24_2 = math.abs(var_24_1.x - arg_24_0.lastPos.x)
		local var_24_3 = math.abs(var_24_1.y - arg_24_0.lastPos.y)

		while var_24_2 < var_0_0.FireworkRange.x / 2 and var_24_3 < var_0_0.FireworkRange.y or var_24_3 < var_0_0.FireworkRange.y / 2 and var_24_2 < var_0_0.FireworkRange.x:
			var_24_1.x = math.random(var_0_0.EffectPosLimit.limitX[1], var_0_0.EffectPosLimit.limitX[2])
			var_24_1.y = math.random(var_0_0.EffectPosLimit.limitY[1], var_0_0.EffectPosLimit.limitY[2])
			var_24_2 = math.abs(var_24_1.x - arg_24_0.lastPos.x)
			var_24_3 = math.abs(var_24_1.y - arg_24_0.lastPos.y)

		var_24_0 = var_24_1
	else
		var_24_0.x = math.random(var_0_0.EffectPosLimit.limitX[1], var_0_0.EffectPosLimit.limitX[2])
		var_24_0.y = math.random(var_0_0.EffectPosLimit.limitY[1], var_0_0.EffectPosLimit.limitY[2])

	arg_24_0.lastPos = var_24_0

	return var_24_0

def var_0_0.StopFireworksTimer(arg_25_0):
	if arg_25_0.fireworksTimer:
		arg_25_0.fireworksTimer.Stop()

		arg_25_0.fireworksTimer = None

def var_0_0.StopPlayFireworks(arg_26_0):
	arg_26_0.StopFireworksTimer()

	arg_26_0.fireworks = None
	arg_26_0.index = None

	setActive(arg_26_0._upper, True)
	setActive(arg_26_0.top, True)
	setActive(arg_26_0.fireworksTF, False)
	arg_26_0.OpenFireworkLayer()

def var_0_0.UpdateView(arg_27_0):
	_.each(arg_27_0.tipTfs, function(arg_28_0)
		if arg_28_0.trans:
			setActive(arg_28_0.trans, tobool(var_0_0.CheckTip(arg_28_0.name))))

def var_0_0.willExit(arg_29_0):
	arg_29_0.clearStudents()
	arg_29_0.StopFireworksTimer()
	arg_29_0.cleanManagedTween()
	arg_29_0.loader.Clear()

def var_0_0.CheckTip(arg_30_0):
	local var_30_0 = getProxy(ActivityProxy)

	return switch(arg_30_0, {
		def xiaoyouxi:()
			return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_SPRING_FESTIVAL_2023),
		def huituriji:()
			return getProxy(ColoringProxy).CheckTodayTip(),
		def huazhongshijie:()
			local var_33_0 = var_30_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

			return Activity.IsActivityReady(var_33_0),
		def jiulou:()
			return RedPacketLayer.isShowRedPoint(),
		def yanhua:()
			local var_35_0 = var_30_0.getActivityById(ActivityConst.FIREWORK_PT_ID)

			return Activity.IsActivityReady(var_35_0),
		def duilian:()
			local var_36_0 = var_30_0.getActivityById(ActivityConst.ACTIVITY_COUPLET)

			return Activity.IsActivityReady(var_36_0)
	}, function()
		return False)

def var_0_0.IsShowMainTip(arg_38_0):
	local var_38_0 = {
		"xiaoyouxi",
		"huituriji",
		"huazhongshijie",
		"jiulou",
		"yanhua",
		"duilian"
	}

	return _.any(var_38_0, function(arg_39_0)
		return tobool(var_0_0.CheckTip(arg_39_0)))

return var_0_0

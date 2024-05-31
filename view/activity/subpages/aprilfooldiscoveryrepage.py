local var_0_0 = class("AprilFoolDiscoveryRePage", import(".AprilFoolDiscoveryPage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.bulin = arg_1_0.bg.Find("bulin")
	arg_1_0.bulinAnim = arg_1_0.bulin.Find("bulin").GetComponent("SpineAnimUI")

	setText(arg_1_0.bulin.Find("Text"), i18n("super_bulin_tip"))
	setActive(arg_1_0.bulin, False)

	arg_1_0._funcsLink = {}

def var_0_0.AddFunc(arg_2_0, arg_2_1):
	table.insert(arg_2_0._funcsLink, arg_2_1)

	if #arg_2_0._funcsLink > 1:
		return

	arg_2_0.PlayFuncsLink()

def var_0_0.PlayFuncsLink(arg_3_0):
	local var_3_0 = False
	local var_3_1

	local function var_3_2(...)
		if var_3_0:
			table.remove(arg_3_0._funcsLink, 1)

		var_3_0 = True

		local var_4_0 = arg_3_0._funcsLink[1]

		if var_4_0:
			var_4_0(var_3_2, ...)

	var_3_2()

def var_0_0.OnDataSetting(arg_5_0):
	local var_5_0 = var_0_0.super.OnDataSetting(arg_5_0)

	local function var_5_1()
		if arg_5_0.activity.data1 == 1 and arg_5_0.activity.data3 == 1:
			arg_5_0.activity.data3 = 0

			pg.m02.sendNotification(GAME.PUZZLE_PIECE_OP, {
				cmd = 4,
				actId = arg_5_0.activity.id
			})

			return True

	var_5_0 = var_5_0 or var_5_1()

	return var_5_0

def var_0_0.OnFirstFlush(arg_7_0):
	local var_7_0 = pg.activity_event_picturepuzzle[arg_7_0.activity.id]

	assert(var_7_0, "Can't Find activity_event_picturepuzzle 's ID . " .. arg_7_0.activity.id)

	arg_7_0.puzzleConfig = var_7_0
	arg_7_0.keyList = Clone(var_7_0.pickup_picturepuzzle)

	table.insertto(arg_7_0.keyList, var_7_0.drop_picturepuzzle)
	assert(#arg_7_0.keyList == #arg_7_0.items, string.format("keyList has {0}, but items has 9", #arg_7_0.keyList))
	table.sort(arg_7_0.keyList)
	onButton(arg_7_0, arg_7_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.bulin_help.tip
		}), SFX_PANEL)

	local var_7_1 = arg_7_0.activity.id

	onButton(arg_7_0, arg_7_0.btnBattle, function()
		if #arg_7_0.activity.data2_list < #arg_7_0.keyList:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_not_start"))

			return

		arg_7_0.emit(ActivityMediator.ON_SIMULATION_COMBAT, {
			warnMsg = "bulin_tip_other3",
			stageId = arg_7_0.puzzleConfig.chapter
		}, function()
			local var_10_0 = getProxy(ActivityProxy)
			local var_10_1 = var_10_0.getActivityById(var_7_1)

			if var_10_1.data1 == 1:
				return

			var_10_1.data3 = 1

			var_10_0.updateActivity(var_10_1)), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.bulin, function()
		if arg_7_0.activity.data1 >= 1:
			seriesAsync({
				function(arg_12_0)
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("super_bulin"),
						onYes = arg_12_0
					}),
				function(arg_13_0)
					arg_7_0.emit(ActivityMediator.ON_SIMULATION_COMBAT, {
						warnMsg = "bulin_tip_other3",
						stageId = arg_7_0.GetLinkStage()
					}, function()
						local var_14_0 = getProxy(ActivityProxy)
						local var_14_1 = var_14_0.getActivityById(var_7_1)

						if var_14_1.data1 == 2:
							return

						var_14_1.data3 = 1

						var_14_0.updateActivity(var_14_1))
			}))

	local var_7_2 = arg_7_0.activity.getConfig("config_client").guideName

	arg_7_0.AddFunc(function(arg_15_0)
		pg.SystemGuideMgr.GetInstance().PlayByGuideId(var_7_2, None, arg_15_0))

local var_0_1 = {
	"lock",
	"hint",
	"unlock"
}

def var_0_0.OnUpdateFlush(arg_16_0):
	local var_16_0 = arg_16_0.activity.data1 >= 1
	local var_16_1 = #arg_16_0.activity.data2_list == #arg_16_0.keyList
	local var_16_2 = var_16_0 and "activity_bg_aprilfool_final" or "activity_bg_aprilfool_discovery"

	if var_16_2 != arg_16_0.bgName:
		setImageSprite(arg_16_0.bg, LoadSprite("ui/activityuipage/AprilFoolDiscoveryRePage_atlas", var_16_2))

		arg_16_0.bg.GetComponent(typeof(Image)).enabled = True
		arg_16_0.bgName = var_16_2

	local var_16_3 = arg_16_0.activity.data2_list
	local var_16_4 = arg_16_0.activity.data3_list

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.items):
		local var_16_5 = arg_16_0.keyList[iter_16_0]
		local var_16_6 = table.contains(var_16_3, var_16_5) and 3 or table.contains(var_16_4, var_16_5) and 2 or 1

		onButton(arg_16_0, iter_16_1, function()
			if var_16_6 >= 3:
				return

			if var_16_6 == 2:
				arg_16_0.selectIndex = iter_16_0

				arg_16_0.UpdateSelection()

				return
			elif var_16_6 == 1:
				if pg.TimeMgr.GetInstance().GetServerTime() < arg_16_0.activity.data2:
					pg.TipsMgr.GetInstance().ShowTips(i18n("bulin_tip_other2"))

					return

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("bulin_tip_other1"),
					def onYes:()
						pg.m02.sendNotification(GAME.PUZZLE_PIECE_OP, {
							cmd = 3,
							actId = arg_16_0.activity.id,
							id = var_16_5
						})

						arg_16_0.selectIndex = iter_16_0
				}))
		arg_16_0.loader.GetSprite("UI/ActivityUIPage/AprilFoolDiscoveryRePage_atlas", var_0_1[var_16_6], iter_16_1.Find("state"))
		setActive(iter_16_1.Find("character"), var_16_6 == 3)

	setActive(arg_16_0.btnBattle, var_16_1)
	setActive(arg_16_0.btnIncomplete, not var_16_1)
	arg_16_0.UpdateSelection()
	setActive(arg_16_0.bulin, var_16_0)

	if arg_16_0.activity.data1 == 1:
		local var_16_7 = arg_16_0.activity.getConfig("config_client").popStory

		arg_16_0.AddFunc(function(arg_19_0)
			pg.NewStoryMgr.GetInstance().Play(var_16_7, arg_19_0))
		arg_16_0.AddFunc(function(arg_20_0)
			local var_20_0 = getProxy(PlayerProxy).getRawData()

			if PlayerPrefs.GetInt("SuperBurinPopUp_" .. var_20_0.id, 0) == 0:
				LoadContextCommand.LoadLayerOnTopContext(Context.New({
					mediator = SuperBulinPopMediator,
					viewComponent = SuperBulinPopView,
					data = {
						stageId = arg_16_0.GetLinkStage(),
						actId = arg_16_0.activity.id,
						onRemoved = arg_20_0
					}
				}))
				PlayerPrefs.SetInt("SuperBurinPopUp_" .. var_20_0.id, 1))

def var_0_0.OnDestroy(arg_21_0):
	var_0_0.super.OnDestroy(arg_21_0)

def var_0_0.GetLinkStage(arg_22_0):
	return arg_22_0.activity.getConfig("config_client").lastChapter

return var_0_0

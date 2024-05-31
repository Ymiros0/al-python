local var_0_0 = class("AprilFoolDiscoveryPage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.bgName = None
	arg_1_0.itemList = arg_1_0.findTF("AD/list")
	arg_1_0.items = CustomIndexLayer.Clone2Full(arg_1_0.itemList, 9)
	arg_1_0.selectIndex = 0
	arg_1_0.btnHelp = arg_1_0.bg.Find("help_btn")
	arg_1_0.btnBattle = arg_1_0.bg.Find("battle_btn")
	arg_1_0.btnIncomplete = arg_1_0.bg.Find("incomplete_btn")
	arg_1_0.tip = arg_1_0.bg.Find("tip")
	arg_1_0.slider = arg_1_0.bg.Find("slider")
	arg_1_0.leftTime = arg_1_0.slider.Find("time")
	arg_1_0.loader = AutoLoader.New()

def var_0_0.OnDataSetting(arg_2_0):
	if arg_2_0.activity.data1 == 0 and arg_2_0.activity.data3 == 1:
		arg_2_0.activity.data3 = 0

		pg.m02.sendNotification(GAME.PUZZLE_PIECE_OP, {
			cmd = 1,
			actId = arg_2_0.activity.id
		})

		return True

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.activity.data1_list):
		if not table.contains(arg_2_0.activity.data2_list, iter_2_1):
			pg.m02.sendNotification(GAME.MEMORYBOOK_UNLOCK, {
				id = iter_2_1,
				actId = arg_2_0.activity.id
			})

			return True

def var_0_0.OnFirstFlush(arg_3_0):
	local var_3_0 = pg.activity_event_picturepuzzle[arg_3_0.activity.id]

	assert(var_3_0, "Can't Find activity_event_picturepuzzle 's ID . " .. arg_3_0.activity.id)

	arg_3_0.puzzleConfig = var_3_0
	arg_3_0.keyList = Clone(var_3_0.pickup_picturepuzzle)

	table.insertto(arg_3_0.keyList, var_3_0.drop_picturepuzzle)
	assert(#arg_3_0.keyList == #arg_3_0.items, string.format("keyList has {0}, but items has 9", #arg_3_0.keyList))
	table.sort(arg_3_0.keyList)
	onButton(arg_3_0, arg_3_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.bulin_help.tip
		}), SFX_PANEL)

	local var_3_1 = arg_3_0.activity.id

	onButton(arg_3_0, arg_3_0.btnBattle, function()
		if #arg_3_0.activity.data2_list < #arg_3_0.keyList:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_not_start"))

			return

		arg_3_0.emit(ActivityMediator.ON_SIMULATION_COMBAT, {
			warnMsg = "bulin_tip_other3",
			stageId = arg_3_0.puzzleConfig.chapter
		}, function()
			local var_6_0 = getProxy(ActivityProxy)
			local var_6_1 = var_6_0.getActivityById(var_3_1)

			if var_6_1.data1 == 1:
				return

			var_6_1.data3 = 1

			var_6_0.updateActivity(var_6_1)), SFX_PANEL)

	local var_3_2 = arg_3_0.activity.getConfig("config_client")

	pg.SystemGuideMgr.GetInstance().PlayByGuideId(var_3_2.guideName)

local var_0_1 = {
	"lock",
	"hint",
	"unlock"
}

def var_0_0.OnUpdateFlush(arg_7_0):
	var_0_0.super.OnUpdateFlush(arg_7_0)

	local var_7_0 = arg_7_0.activity.data1 > 0
	local var_7_1 = #arg_7_0.activity.data2_list == #arg_7_0.keyList
	local var_7_2 = var_7_0 and "activity_bg_aprilfool_final" or "activity_bg_aprilfool_discovery"

	if var_7_2 != arg_7_0.bgName:
		setImageSprite(arg_7_0.bg, LoadSprite("ui/activityuipage/AprilFoolDiscoveryPage_atlas", var_7_2))

		arg_7_0.bg.GetComponent(typeof(Image)).enabled = True
		arg_7_0.bgName = var_7_2

	local var_7_3 = arg_7_0.activity.data2_list
	local var_7_4 = arg_7_0.activity.data3_list

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.items):
		local var_7_5 = arg_7_0.keyList[iter_7_0]
		local var_7_6 = table.contains(var_7_3, var_7_5) and 3 or table.contains(var_7_4, var_7_5) and 2 or 1

		onButton(arg_7_0, iter_7_1, function()
			if var_7_6 >= 3:
				return

			if var_7_6 == 2:
				arg_7_0.selectIndex = iter_7_0

				arg_7_0.UpdateSelection()

				return
			elif var_7_6 == 1:
				if pg.TimeMgr.GetInstance().GetServerTime() < arg_7_0.activity.data2:
					pg.TipsMgr.GetInstance().ShowTips(i18n("bulin_tip_other2"))

					return

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("bulin_tip_other1"),
					def onYes:()
						pg.m02.sendNotification(GAME.PUZZLE_PIECE_OP, {
							cmd = 3,
							actId = arg_7_0.activity.id,
							id = var_7_5
						})

						arg_7_0.selectIndex = iter_7_0
				}))
		arg_7_0.loader.GetSprite("UI/ActivityUIPage/AprilFoolDiscoveryPage_atlas", var_0_1[var_7_6], iter_7_1.Find("state"))
		setActive(iter_7_1.Find("character"), var_7_6 == 3)

	setActive(arg_7_0.btnBattle, var_7_1)
	setActive(arg_7_0.btnIncomplete, not var_7_1)
	arg_7_0.UpdateSelection()

def var_0_0.UpdateSelection(arg_10_0):
	local var_10_0 = arg_10_0.keyList[arg_10_0.selectIndex]
	local var_10_1 = table.contains(arg_10_0.activity.data3_list, var_10_0)

	setText(arg_10_0.tip, var_10_1 and i18n("bulin_tip" .. arg_10_0.selectIndex) or "")
	arg_10_0.CreateCDTimer()

def var_0_0.CreateCDTimer(arg_11_0):
	if arg_11_0.CDTimer:
		return

	if #arg_11_0.activity.data2_list == #arg_11_0.keyList or pg.TimeMgr.GetInstance().GetServerTime() >= arg_11_0.activity.data2:
		setActive(arg_11_0.slider, False)
		arg_11_0.RemoveCDTimer()

		return

	setActive(arg_11_0.slider, True)

	arg_11_0.CDTimer = Timer.New(function()
		local var_12_0 = arg_11_0.activity.data2
		local var_12_1 = pg.TimeMgr.GetInstance().GetServerTime()

		if var_12_0 <= var_12_1:
			setActive(arg_11_0.slider, False)
			arg_11_0.RemoveCDTimer()

			return

		local var_12_2 = var_12_0 - var_12_1
		local var_12_3 = math.floor(var_12_2 / 60)
		local var_12_4 = var_12_2 % 60

		setText(arg_11_0.leftTime, string.format("%d.%02d", var_12_3, var_12_4))

		local var_12_5 = arg_11_0.puzzleConfig.cd

		setSlider(arg_11_0.slider, 0, 1, var_12_2 / var_12_5), 1, -1)

	arg_11_0.CDTimer.Start()
	arg_11_0.CDTimer.func()

def var_0_0.RemoveCDTimer(arg_13_0):
	if arg_13_0.CDTimer:
		arg_13_0.CDTimer.Stop()

		arg_13_0.CDTimer = None

def var_0_0.OnDestroy(arg_14_0):
	arg_14_0.loader.Clear()
	arg_14_0.RemoveCDTimer()
	var_0_0.super.OnDestroy(arg_14_0)

return var_0_0

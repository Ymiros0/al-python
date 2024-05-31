local var_0_0 = class("ShrineView", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "Shrine"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initData()
	arg_3_0.spineAnim.SetAction("normal", 0)
	arg_3_0.updateView()
	arg_3_0.updateBuff()
	arg_3_0.updateWitchImg()

def var_0_0.onBackPressed(arg_4_0):
	if arg_4_0.shrineBuffView.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.shrineBuffView.Destroy()
	elif arg_4_0.shrineResultView.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.shrineResultView.Destroy()
	else
		arg_4_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.OnSendMiniGameOPDone(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.argList
	local var_5_1 = var_5_0[1]
	local var_5_2 = var_5_0[2]

	if var_5_1 == arg_5_0.miniGameId:
		if var_5_2 == 1:
			arg_5_0.updateView()
			arg_5_0.updateWitchImg()
		elif var_5_2 == 2:
			local var_5_3 = getProxy(PlayerProxy).getData()

			var_5_3.consume({
				gold = arg_5_0.GetMGData().getConfig("config_data")[1]
			})
			getProxy(PlayerProxy).updatePlayer(var_5_3)

			local var_5_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SHRINE)

			if var_5_4 and not var_5_4.isEnd():
				var_5_4.data2 = var_5_4.data2 + 1

				getProxy(ActivityProxy).updateActivity(var_5_4)

			local var_5_5 = var_5_0[3]
			local var_5_6 = pg.benefit_buff_template[var_5_5].name
			local var_5_7 = table.indexof(arg_5_0.GetMGData().getConfig("config_data")[2], var_5_5, 1)
			local var_5_8 = i18n("tips_shrine_buff")

			arg_5_0.playAnime(var_5_8, var_5_7)
			arg_5_0.updateView()
			arg_5_0.updateWitchImg()
		elif var_5_2 == 3:
			local var_5_9 = getProxy(PlayerProxy).getData()

			var_5_9.consume({
				gold = arg_5_0.GetMGData().getConfig("config_data")[1]
			})
			getProxy(PlayerProxy).updatePlayer(var_5_9)

			local var_5_10 = i18n("tips_shrine_nobuff")

			arg_5_0.playAnime(var_5_10)
			arg_5_0.updateView()
			arg_5_0.updateWitchImg()

def var_0_0.OnModifyMiniGameDataDone(arg_6_0, arg_6_1):
	arg_6_0.updateView()

def var_0_0.willExit(arg_7_0):
	if arg_7_0.shrineBuffView.CheckState(BaseSubView.STATES.INITED):
		arg_7_0.shrineBuffView.Destroy()

	if arg_7_0.shrineResultView.CheckState(BaseSubView.STATES.INITED):
		arg_7_0.shrineResultView.Destroy()

	arg_7_0.spineAnim = None

	if arg_7_0._buffTextTimer:
		arg_7_0._buffTextTimer.Stop()

	if arg_7_0._buffTimeCountDownTimer:
		arg_7_0._buffTimeCountDownTimer.Stop()

	if arg_7_0.ringSE:
		arg_7_0.ringSE.Stop(True)

def var_0_0.initData(arg_8_0):
	arg_8_0.miniGameId = arg_8_0.contextData.miniGameId

	local var_8_0 = getProxy(MiniGameProxy).GetHubByGameId(arg_8_0.miniGameId)

	if not arg_8_0.isInitedMiniGameData():
		arg_8_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
			arg_8_0.miniGameId,
			1
		})

	local var_8_1 = {
		def onSelect:(arg_9_0)
			local var_9_0 = getProxy(PlayerProxy).getData()

			if arg_8_0.GetMGData().getConfig("config_data")[1] > var_9_0.gold:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

				return

			if arg_8_0.GetMGData().GetRuntimeData("count") <= 0:
				arg_8_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
					arg_8_0.miniGameId,
					3
				})
			else
				local var_9_1 = arg_8_0.GetMGData().getConfig("config_data")[2][arg_9_0]

				arg_8_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
					arg_8_0.miniGameId,
					2,
					var_9_1
				}),
		def onClose:()
			arg_8_0.buffEffectAni.enabled = False
			arg_8_0.bgImg.color = Color.New(1, 1, 1)

			setActive(arg_8_0.noAdaptPanel, True)
			setActive(arg_8_0.cloudTF, True)
			setActive(arg_8_0.witchImg, arg_8_0.activityWitch)
	}

	arg_8_0.shrineBuffView = ShrineBuffView.New(arg_8_0._tf.parent, arg_8_0.event, var_8_1)
	arg_8_0.shrineResultView = ShrineResultView.New(arg_8_0._tf, arg_8_0.event)

def var_0_0.findUI(arg_11_0):
	arg_11_0.noAdaptPanel = arg_11_0.findTF("noAdaptPanel")
	arg_11_0.buffTF = arg_11_0.findTF("Buff", arg_11_0.noAdaptPanel)
	arg_11_0.buffImg = arg_11_0.findTF("BuffTypeImg", arg_11_0.buffTF)
	arg_11_0.buffEffectAni = GetComponent(arg_11_0.buffImg, "Animator")
	arg_11_0.buffText = arg_11_0.findTF("BuffText", arg_11_0.buffTF)
	arg_11_0.buffDftAniEvent = GetComponent(arg_11_0.buffImg, "DftAniEvent")
	arg_11_0.bgImg = arg_11_0.findTF("BGImg").GetComponent(typeof(Image))
	arg_11_0.bgImg.color = Color.New(1, 1, 1)
	arg_11_0.cloudTF = arg_11_0.findTF("BG/cloud")

	local var_11_0 = arg_11_0.findTF("Top", arg_11_0.noAdaptPanel)

	arg_11_0.topTF = var_11_0
	arg_11_0.backBtn = arg_11_0.findTF("BackBtn", var_11_0)
	arg_11_0.helpBtn = arg_11_0.findTF("HelpBtn", var_11_0)
	arg_11_0.timesText = arg_11_0.findTF("Times/Text", var_11_0)
	arg_11_0.goldText = arg_11_0.findTF("Gold/Text", var_11_0)

	local var_11_1 = arg_11_0.findTF("Main")

	arg_11_0.witchImg = arg_11_0.findTF("Witch", var_11_1)
	arg_11_0.rope = arg_11_0.findTF("Rope", var_11_1)
	arg_11_0.spineAnim = GetComponent(arg_11_0.rope, "SpineAnimUI")
	arg_11_0.press = GetComponent(arg_11_0.rope, "EventTriggerListener")

def var_0_0.addListener(arg_12_0):
	onButton(arg_12_0, arg_12_0.backBtn, function()
		arg_12_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_12_0, arg_12_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_newyear_shrine.tip
		}), SFX_PANEL)
	onButton(arg_12_0, arg_12_0.rope, function()
		arg_12_0.bgImg.color = Color.New(0, 0, 0)

		setActive(arg_12_0.noAdaptPanel, False)
		setActive(arg_12_0.cloudTF, False)
		setActive(arg_12_0.witchImg, False)
		arg_12_0.shrineBuffView.Reset()
		arg_12_0.shrineBuffView.Load())
	onButton(arg_12_0, arg_12_0.buffImg, function()
		arg_12_0.updateBuffDesc(), SFX_PANEL)
	arg_12_0.buffDftAniEvent.SetStartEvent(function()
		setButtonEnabled(arg_12_0.rope, False))
	arg_12_0.buffDftAniEvent.SetEndEvent(function()
		setButtonEnabled(arg_12_0.rope, True))

def var_0_0.playAnime(arg_19_0, arg_19_1, arg_19_2):
	setButtonEnabled(arg_19_0.rope, False)

	arg_19_0.ringSE = pg.CriMgr.GetInstance().PlaySE_V3("ui-shensheling")

	if arg_19_0.spineAnim:
		arg_19_0.spineAnim.SetAction("action", 0)
		arg_19_0.spineAnim.SetActionCallBack(function(arg_20_0)
			if arg_20_0 == "finish":
				arg_19_0.spineAnim.SetActionCallBack(None)

				if arg_19_0.ringSE:
					arg_19_0.ringSE.Stop(True)

				arg_19_0.shrineResultView.Reset()
				arg_19_0.shrineResultView.Load()
				arg_19_0.shrineResultView.ActionInvoke("updateView", arg_19_1, arg_19_2)
				arg_19_0.shrineResultView.ActionInvoke("setCloseFunc", function()
					if arg_19_2:
						arg_19_0.updateBuff()

						arg_19_0.buffEffectAni.enabled = True

					setButtonEnabled(arg_19_0.rope, True))
				arg_19_0.spineAnim.SetAction("normal", 0))

def var_0_0.updateView(arg_22_0):
	if not arg_22_0.isInitedMiniGameData():
		return

	local var_22_0 = arg_22_0.GetMGData().GetRuntimeData("count")

	setText(arg_22_0.timesText, var_22_0)

	local var_22_1 = getProxy(PlayerProxy).getData().gold

	setText(arg_22_0.goldText, var_22_1)

def var_0_0.updateBuff(arg_23_0, arg_23_1):
	if arg_23_1:
		setImageSprite(arg_23_0.buffImg, GetSpriteFromAtlas("ui/shrineui_atlas", "buff_type_" .. arg_23_1))
		setActive(arg_23_0.buffImg, True)
	else
		local var_23_0 = getProxy(PlayerProxy).getData()
		local var_23_1 = arg_23_0.GetMGData().getConfig("config_data")[2]
		local var_23_2

		for iter_23_0, iter_23_1 in ipairs(var_23_0.buff_list):
			var_23_2 = table.indexof(var_23_1, iter_23_1.id, 1)

			if var_23_2:
				if pg.TimeMgr.GetInstance().GetServerTime() < iter_23_1.timestamp:
					setImageSprite(arg_23_0.buffImg, GetSpriteFromAtlas("ui/shrineui_atlas", "buff_type_" .. var_23_2))
					setActive(arg_23_0.buffImg, True)

					break

				var_23_2 = None

				break

		if not var_23_2:
			setActive(arg_23_0.buffImg, False)

def var_0_0.updateBuffDesc(arg_24_0):
	local var_24_0
	local var_24_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)

	if var_24_1 and not var_24_1.isEnd():
		local var_24_2 = arg_24_0.GetMGData().getConfig("config_data")[2]
		local var_24_3 = getProxy(PlayerProxy).getData()

		for iter_24_0, iter_24_1 in pairs(var_24_3.buff_list):
			if table.contains(var_24_2, iter_24_1.id):
				var_24_0 = ActivityBuff.New(var_24_1.id, iter_24_1.id, iter_24_1.timestamp)

				break

	if arg_24_0._buffTimeCountDownTimer:
		arg_24_0._buffTimeCountDownTimer.Stop()

	if arg_24_0._buffTextTimer:
		arg_24_0._buffTextTimer.Stop()

	local var_24_4 = var_24_0.getConfig("desc")

	if var_24_0.getConfig("max_time") > 0:
		local var_24_5 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_24_6 = var_24_0.timestamp

		if var_24_6:
			local var_24_7 = var_24_6 - var_24_5
			local var_24_8 = pg.TimeMgr.GetInstance().DescCDTime(var_24_7)

			setText(arg_24_0.buffText.Find("Text"), string.gsub(var_24_4, "$" .. 1, var_24_8))

			arg_24_0._buffTimeCountDownTimer = Timer.New(function()
				if var_24_7 > 0:
					var_24_7 = var_24_7 - 1

					local var_25_0 = pg.TimeMgr.GetInstance().DescCDTime(var_24_7)

					setText(arg_24_0.buffText.Find("Text"), string.gsub(var_24_4, "$" .. 1, var_25_0))
				else
					arg_24_0._buffTimeCountDownTimer.Stop()
					setActive(arg_24_0.buffText, False)
					setActive(arg_24_0.buffImg, False), 1, -1)

			setActive(arg_24_0.buffText, True)
			arg_24_0._buffTimeCountDownTimer.Start()

	arg_24_0._buffTextTimer = Timer.New(function()
		setActive(arg_24_0.buffText, False)
		arg_24_0._buffTimeCountDownTimer.Stop(), 7, 1)

	arg_24_0._buffTextTimer.Start()

def var_0_0.updateWitchImg(arg_27_0):
	arg_27_0.activityWitch = False

	if not arg_27_0.isInitedMiniGameData():
		return

	if arg_27_0.GetMGData().GetRuntimeData("serverGold") >= arg_27_0.GetMGData().getConfig("simple_config_data").target:
		arg_27_0.activityWitch = True

		setActive(arg_27_0.witchImg, True)

def var_0_0.isInitedMiniGameData(arg_28_0):
	if not arg_28_0.GetMGData().GetRuntimeData("isInited"):
		return False
	else
		return True

return var_0_0

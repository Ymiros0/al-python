local var_0_0 = class("HoloLiveLinkLinkSelectScene", import("view.base.BaseUI"))

var_0_0.HOLOLIVE_LINKGAME_HUB_ID = 3
var_0_0.HOLOLIVE_LINKGAME_ID = 7

def var_0_0.getUIName(arg_1_0):
	return "HoloLiveLinkGameSelectUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.initUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateProgressBar()
	arg_3_0.updateAwardPanel()
	arg_3_0.updateEntranceList()

def var_0_0.willExit(arg_4_0):
	return

def var_0_0.initData(arg_5_0):
	arg_5_0.lightPointTFList = {}
	arg_5_0.lightLineTFList = {}
	arg_5_0.entranceTFList = {}

	arg_5_0.updateData()

def var_0_0.findUI(arg_6_0):
	arg_6_0.forNotchPanel = arg_6_0.findTF("ForNotchPanel")
	arg_6_0.backBtn = arg_6_0.findTF("BackBtn", arg_6_0.forNotchPanel)
	arg_6_0.helpBtn = arg_6_0.findTF("HelpBtn", arg_6_0.forNotchPanel)
	arg_6_0.awardMask = arg_6_0.findTF("AwardImg/Mask", arg_6_0.forNotchPanel)
	arg_6_0.progressText = arg_6_0.findTF("AwardImg/ProgressText", arg_6_0.forNotchPanel)
	arg_6_0.getAwardBtn = arg_6_0.findTF("AwardImg/GetBtn", arg_6_0.forNotchPanel)
	arg_6_0.gotAwardBtn = arg_6_0.findTF("AwardImg/GotBtn", arg_6_0.forNotchPanel)
	arg_6_0.progressPanel = arg_6_0.findTF("Progress", arg_6_0.forNotchPanel)
	arg_6_0.lightPointContainer = arg_6_0.findTF("Light", arg_6_0.progressPanel)
	arg_6_0.lightLineContainer = arg_6_0.findTF("LightLine", arg_6_0.progressPanel)
	arg_6_0.entranceContainer = arg_6_0.findTF("EntranceContainer")

def var_0_0.initUI(arg_7_0):
	setActive(arg_7_0.getAwardBtn, False)
	setActive(arg_7_0.gotAwardBtn, False)
	eachChild(arg_7_0.lightPointContainer, function(arg_8_0)
		table.insert(arg_7_0.lightPointTFList, 1, arg_8_0)

		local var_8_0 = arg_7_0.findTF("Point", arg_8_0)

		setActive(arg_8_0, False)
		setActive(var_8_0, False))
	eachChild(arg_7_0.lightLineContainer, function(arg_9_0)
		table.insert(arg_7_0.lightLineTFList, 1, arg_9_0)
		setActive(arg_9_0, False))

	for iter_7_0 = 0, 7:
		local var_7_0 = arg_7_0.entranceContainer.GetChild(iter_7_0)

		table.insert(arg_7_0.entranceTFList, var_7_0)

		local var_7_1 = arg_7_0.findTF("Mask", var_7_0)
		local var_7_2 = arg_7_0.findTF("GotImg", var_7_0)
		local var_7_3 = arg_7_0.findTF("LockText", var_7_0)

		setActive(var_7_1, True)
		setActive(var_7_2, False)
		setActive(var_7_3, True)

def var_0_0.addListener(arg_10_0):
	onButton(arg_10_0, arg_10_0.backBtn, function()
		arg_10_0.closeView(), SFX_CANCEL)
	onButton(arg_10_0, arg_10_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.hololive_lianliankan.tip
		}), SFX_PANEL)

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.entranceTFList):
		local var_10_0 = arg_10_0.findTF("EntranceBtn", iter_10_1)

		onButton(arg_10_0, var_10_0, function()
			arg_10_0.linkGameData.SetRuntimeData("curLinkGameID", iter_10_0)
			pg.m02.sendNotification(GAME.GO_MINI_GAME, var_0_0.HOLOLIVE_LINKGAME_ID), SFX_PANEL)

def var_0_0.updateProgressBar(arg_14_0):
	local var_14_0 = arg_14_0.linkGameHub.usedtime
	local var_14_1 = math.min(var_14_0, 7)

	if var_14_1 > 0:
		for iter_14_0 = 1, var_14_1:
			local var_14_2 = arg_14_0.lightPointTFList[iter_14_0]

			setActive(var_14_2, True)

		local var_14_3 = arg_14_0.lightPointTFList[var_14_1]
		local var_14_4 = arg_14_0.findTF("Point", var_14_3)

		setActive(var_14_4, True)

	if var_14_1 > 1:
		local var_14_5 = var_14_1 - 1

		for iter_14_1 = 1, var_14_5:
			local var_14_6 = arg_14_0.lightLineTFList[iter_14_1]

			setActive(var_14_6, True)

def var_0_0.updateAwardPanel(arg_15_0):
	local var_15_0 = arg_15_0.linkGameHub.usedtime

	setText(arg_15_0.progressText, var_15_0 > 7 and 7 or var_15_0)

	if arg_15_0.linkGameHub.ultimate > 0:
		setActive(arg_15_0.getAwardBtn, False)
		setActive(arg_15_0.gotAwardBtn, True)
		setActive(arg_15_0.awardMask, True)
	elif var_15_0 >= arg_15_0.linkGameHub.getConfig("reward_need"):
		setActive(arg_15_0.getAwardBtn, True)
		setActive(arg_15_0.gotAwardBtn, False)
		setActive(arg_15_0.awardMask, True)
		onButton(arg_15_0, arg_15_0.getAwardBtn, function()
			pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = arg_15_0.linkGameHub.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			}), SFX_PANEL)
	else
		setActive(arg_15_0.getAwardBtn, False)
		setActive(arg_15_0.gotAwardBtn, False)
		setActive(arg_15_0.awardMask, False)

def var_0_0.updateEntranceList(arg_17_0):
	local var_17_0 = arg_17_0.linkGameHub.usedtime

	for iter_17_0 = 1, 8:
		local var_17_1 = arg_17_0.entranceTFList[iter_17_0]
		local var_17_2 = arg_17_0.findTF("Mask", var_17_1)
		local var_17_3 = arg_17_0.findTF("GotImg", var_17_1)
		local var_17_4 = arg_17_0.findTF("LockText", var_17_1)
		local var_17_5 = arg_17_0.linkGameData.GetConfigCsvLine(iter_17_0).unlock_txt

		setText(var_17_4, var_17_5)

		if iter_17_0 <= var_17_0:
			setActive(var_17_2, False)
			setActive(var_17_3, True)
			setActive(var_17_4, False)
		elif iter_17_0 == var_17_0 + 1:
			local var_17_6 = arg_17_0.linkGameHub.count

			if var_17_6 == 0:
				setActive(var_17_2, True)
				setActive(var_17_3, False)
				setActive(var_17_4, True)
			elif var_17_6 > 0:
				setActive(var_17_2, False)
				setActive(var_17_3, False)
				setActive(var_17_4, False)
		elif iter_17_0 > var_17_0 + 1:
			setActive(var_17_2, True)
			setActive(var_17_3, False)
			setActive(var_17_4, True)

def var_0_0.updateData(arg_18_0):
	arg_18_0.miniGameProxy = getProxy(MiniGameProxy)
	arg_18_0.linkGameHub = arg_18_0.miniGameProxy.GetHubByHubId(var_0_0.HOLOLIVE_LINKGAME_HUB_ID)
	arg_18_0.linkGameData = arg_18_0.miniGameProxy.GetMiniGameData(var_0_0.HOLOLIVE_LINKGAME_ID)

def var_0_0.updateUI(arg_19_0):
	arg_19_0.updateProgressBar()
	arg_19_0.updateAwardPanel()
	arg_19_0.updateEntranceList()

def var_0_0.isTip():
	local var_20_0 = getProxy(MiniGameProxy).GetHubByHubId(var_0_0.HOLOLIVE_LINKGAME_HUB_ID)

	if var_20_0.ultimate == 0 and var_20_0.usedtime >= 7:
		return True
	elif var_20_0.count > 0:
		return True

return var_0_0

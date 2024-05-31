local var_0_0 = class("Shrine2022View", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "Shrine2022UI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initData()
	arg_3_0.updateDataView()
	arg_3_0.updateCardList()
	arg_3_0.updateCardBuffTag()
	arg_3_0.updateCommanderBuff()

def var_0_0.onBackPressed(arg_4_0):
	if arg_4_0.shrineSelectShipView and arg_4_0.shrineSelectShipView.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.shrineSelectShipView.closeSelf()
	elif arg_4_0.shrineSelectBuffView and arg_4_0.shrineSelectBuffView.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.shrineSelectBuffView.closeMySelf()
	elif arg_4_0.shrineShipWordView and arg_4_0.shrineShipWordView.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.shrineShipWordView.closeMySelf()
	else
		arg_4_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.OnSendMiniGameOPDone(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.argList
	local var_5_1 = var_5_0[1]
	local var_5_2 = var_5_0[2]

	arg_5_0.PrintLog("后端返回,游戏ID,操作类型", var_5_1, var_5_2)

	if var_5_1 == arg_5_0.commanderGameID:
		if var_5_2 == 1:
			arg_5_0.updateDataView()
			arg_5_0.updateCommanderBuff()
		elif var_5_2 == 2:
			local var_5_3 = arg_5_0.playerProxy.getData()

			var_5_3.consume({
				gold = arg_5_0.GetMGData().getConfig("config_data")[1]
			})
			arg_5_0.playerProxy.updatePlayer(var_5_3)
			arg_5_0.updateDataView()
			arg_5_0.updateCommanderBuff(True)
		elif var_5_2 == 3:
			local var_5_4 = arg_5_0.playerProxy.getData()

			var_5_4.consume({
				gold = arg_5_0.GetMGData().getConfig("config_data")[1]
			})
			arg_5_0.playerProxy.updatePlayer(var_5_4)
	elif var_5_1 == arg_5_0.shipGameID:
		if var_5_2 == 1:
			arg_5_0.updateDataView()
			arg_5_0.updateCommanderBuff()
		elif var_5_2 == 2:
			local var_5_5 = arg_5_0.playerProxy.getData()

			var_5_5.consume({
				gold = arg_5_0.getShipGameData().getConfig("config_data")[1]
			})
			arg_5_0.playerProxy.updatePlayer(var_5_5)

			local var_5_6 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SHRINE)

			if var_5_6 and not var_5_6.isEnd():
				var_5_6.data2 = var_5_6.data2 + 1

				getProxy(ActivityProxy).updateActivity(var_5_6)

			arg_5_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
				arg_5_0.commanderGameID,
				1
			})
			arg_5_0.updateCardList()
			arg_5_0.updateCardBuffTag()
			arg_5_0.openFakeDrop(function()
				local var_6_0 = var_5_0[5]

				arg_5_0.openShipWordView(var_6_0))

def var_0_0.OnModifyMiniGameDataDone(arg_7_0, arg_7_1):
	return

def var_0_0.willExit(arg_8_0):
	if arg_8_0.shrineSelectShipView and arg_8_0.shrineSelectShipView.CheckState(BaseSubView.STATES.INITED):
		arg_8_0.shrineSelectShipView.Destroy()
	elif arg_8_0.shrineSelectBuffView and arg_8_0.shrineSelectBuffView.CheckState(BaseSubView.STATES.INITED):
		arg_8_0.shrineSelectBuffView.Destroy()
	elif arg_8_0.shrineShipWordView and arg_8_0.shrineShipWordView.CheckState(BaseSubView.STATES.INITED):
		arg_8_0.shrineShipWordView.Destroy()

	arg_8_0.cleanManagedTween()

def var_0_0.initData(arg_9_0):
	arg_9_0.playerProxy = getProxy(PlayerProxy)
	arg_9_0.miniGameProxy = getProxy(MiniGameProxy)
	arg_9_0.commanderGameID = arg_9_0.contextData.miniGameId
	arg_9_0.shipGameID = pg.mini_game[arg_9_0.commanderGameID].simple_config_data.shipGameID
	arg_9_0.cardPosList = {
		{
			x = -447,
			y = 205
		},
		{
			x = -154,
			y = 205
		},
		{
			x = 145,
			y = 205
		},
		{
			x = 445,
			y = 205
		},
		{
			x = -299,
			y = -160
		},
		{
			x = 0,
			y = -160
		},
		{
			x = 302,
			y = -160
		}
	}

	if not arg_9_0.isInitedShipGameData():
		arg_9_0.PrintLog("请求舰娘游戏数据", arg_9_0.shipGameID)
		arg_9_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
			arg_9_0.shipGameID,
			1
		})

	if not arg_9_0.isInitedCommanderGameData():
		arg_9_0.PrintLog("请求指挥官游戏数据", arg_9_0.commanderGameID)
		arg_9_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
			arg_9_0.commanderGameID,
			1
		})

def var_0_0.findUI(arg_10_0):
	local var_10_0 = arg_10_0.findTF("Res")
	local var_10_1 = getImageSprite(arg_10_0.findTF("CurBuff1", var_10_0))
	local var_10_2 = getImageSprite(arg_10_0.findTF("CurBuff2", var_10_0))
	local var_10_3 = getImageSprite(arg_10_0.findTF("CurBuff3", var_10_0))

	arg_10_0.curBuffSpriteList = {
		var_10_1,
		var_10_2,
		var_10_3
	}

	local var_10_4 = arg_10_0.findTF("Adapt")

	arg_10_0.tipGoldTF = arg_10_0.findTF("TipGold", var_10_4)
	arg_10_0.backBtn = arg_10_0.findTF("BackBtn", var_10_4)
	arg_10_0.helpBtn = arg_10_0.findTF("HelpBtn", var_10_4)

	local var_10_5 = arg_10_0.findTF("Data")

	arg_10_0.countText = arg_10_0.findTF("Count", var_10_5)
	arg_10_0.goldText = arg_10_0.findTF("Gold", var_10_5)
	arg_10_0.countText2 = arg_10_0.findTF("Count2", var_10_5)
	arg_10_0.cardTpl = arg_10_0.findTF("CardTpl")
	arg_10_0.cardContainer = arg_10_0.findTF("CardContainer")
	arg_10_0.cardUIItemList = UIItemList.New(arg_10_0.cardContainer, arg_10_0.cardTpl)
	arg_10_0.selectBuffBtn = arg_10_0.findTF("SelectBuffBtn")
	arg_10_0.selectBuffLight = arg_10_0.findTF("SelectBuffLight")
	arg_10_0.curBuffTF = arg_10_0.findTF("CurBuff")
	arg_10_0.curBuffImg = arg_10_0.findTF("BuffImg", arg_10_0.curBuffTF)

def var_0_0.addListener(arg_11_0):
	onButton(arg_11_0, arg_11_0.backBtn, function()
		arg_11_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.Pray_activity_tips1.tip
		}), SFX_PANEL)
	onButton(arg_11_0, arg_11_0.selectBuffBtn, function()
		arg_11_0.openSelectBuffView(), SFX_PANEL)

def var_0_0.updateDataView(arg_15_0):
	if not arg_15_0.isInitedCommanderGameData():
		arg_15_0.PrintLog("无指挥官数据,返回")

		return

	arg_15_0.PrintLog("刷新指挥官次数与金币")

	local var_15_0 = arg_15_0.GetMGData().GetRuntimeData("count")

	setText(arg_15_0.countText, var_15_0)

	local var_15_1 = arg_15_0.getShipGameData().GetRuntimeData("count")

	setText(arg_15_0.countText2, var_15_1)

	local var_15_2 = arg_15_0.playerProxy.getData().gold

	setText(arg_15_0.goldText, var_15_2)

	local var_15_3 = arg_15_0.isHaveCommanderBuff()

	setActive(arg_15_0.selectBuffLight, var_15_0 > 0 and not var_15_3)

def var_0_0.updateCardList(arg_16_0):
	if not arg_16_0.isInitedShipGameData():
		arg_16_0.PrintLog("无舰娘数据,返回")

		return

	arg_16_0.PrintLog("刷新舰娘显示")

	arg_16_0.cardTFList = {}

	arg_16_0.cardUIItemList.make(function(arg_17_0, arg_17_1, arg_17_2)
		if arg_17_0 == UIItemList.EventUpdate:
			local var_17_0 = arg_17_1 + 1

			arg_16_0.cardTFList[var_17_0] = arg_17_2

			arg_16_0.updateCardImg(var_17_0)
			setLocalPosition(arg_17_2, arg_16_0.cardPosList[var_17_0])

			local var_17_1 = arg_16_0.findTF("Empty", arg_17_2)

			onButton(arg_16_0, var_17_1, function()
				arg_16_0.openSelectShipView(var_17_0), SFX_PANEL)

			local var_17_2 = arg_16_0.findTF("Ship", arg_17_2)

			onButton(arg_16_0, var_17_2, function()
				local var_19_0 = arg_16_0.getSelectedShipByCardIndex(var_17_0)

				arg_16_0.openShipWordView(var_19_0), SFX_PANEL))

	local var_16_0 = arg_16_0.getShipGameData().GetRuntimeData("count")
	local var_16_1 = arg_16_0.getSelectedShipCount()
	local var_16_2 = #arg_16_0.getShipGameData().getConfig("config_data")[2]
	local var_16_3 = var_16_2 < var_16_0 + var_16_1 and var_16_2 or var_16_0 + var_16_1

	arg_16_0.PrintLog("舰娘次数相关", var_16_0, var_16_1, var_16_3)
	arg_16_0.cardUIItemList.align(var_16_3)

def var_0_0.updateCardImg(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0.cardTFList[arg_20_1]
	local var_20_1 = arg_20_0.findTF("Empty", var_20_0)
	local var_20_2 = arg_20_0.findTF("Ship", var_20_0)
	local var_20_3 = arg_20_0.getSelectedShipByCardIndex(arg_20_1)

	if var_20_3 > 0:
		local var_20_4 = "shipcard_" .. var_20_3
		local var_20_5 = "Shrine2022/" .. var_20_4

		setImageSprite(var_20_2, LoadSprite(var_20_5, var_20_4), True)

	setActive(var_20_1, var_20_3 == 0)
	setActive(var_20_2, var_20_3 > 0)

def var_0_0.updateCardSelecting(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = arg_21_0.cardTFList[arg_21_1]
	local var_21_1 = arg_21_0.findTF("Selecting", var_21_0)

	setActive(var_21_1, arg_21_2)

def var_0_0.updateCardBuffTag(arg_22_0):
	if not arg_22_0.isInitedShipGameData():
		arg_22_0.PrintLog("无舰娘数据,返回")

		return

	arg_22_0.PrintLog("刷新舰娘BuffTtag")

	for iter_22_0, iter_22_1 in ipairs(arg_22_0.cardTFList):
		local var_22_0 = arg_22_0.findTF("Ship/Buff", iter_22_1)

		setActive(var_22_0, False)

	local var_22_1 = arg_22_0.playerProxy.getData().buff_list
	local var_22_2 = arg_22_0.getShipGameData().getConfig("config_data")[2]
	local var_22_3

	for iter_22_2, iter_22_3 in ipairs(var_22_1):
		local var_22_4 = table.indexof(var_22_2, iter_22_3.id, 1)

		if var_22_4:
			if pg.TimeMgr.GetInstance().GetServerTime() < iter_22_3.timestamp:
				local var_22_5 = arg_22_0.getCardIndexByShip(var_22_4)
				local var_22_6 = arg_22_0.cardTFList[var_22_5]
				local var_22_7 = arg_22_0.findTF("Ship/Buff", var_22_6)

				setActive(var_22_7, True)

				break

			local var_22_8

			break

def var_0_0.updateCommanderBuff(arg_23_0, arg_23_1):
	if not arg_23_0.isInitedCommanderGameData():
		arg_23_0.PrintLog("无指挥官数据,返回")

		return

	arg_23_0.PrintLog("刷新指挥官Buff")

	local var_23_0 = arg_23_0.playerProxy.getData().buff_list
	local var_23_1 = arg_23_0.GetMGData().getConfig("config_data")[2]
	local var_23_2

	for iter_23_0, iter_23_1 in ipairs(var_23_0):
		var_23_2 = table.indexof(var_23_1, iter_23_1.id, 1)

		if var_23_2:
			if pg.TimeMgr.GetInstance().GetServerTime() < iter_23_1.timestamp:
				setImageSprite(arg_23_0.curBuffImg, arg_23_0.curBuffSpriteList[var_23_2])
				setActive(arg_23_0.curBuffTF, True)

				break

			var_23_2 = None

			break

	if not var_23_2:
		setActive(arg_23_0.curBuffTF, False)
	elif arg_23_1:
		local var_23_3 = 160
		local var_23_4 = -70
		local var_23_5 = 0.5
		local var_23_6 = {
			x = rtf(arg_23_0.curBuffTF).localPosition.x,
			y = var_23_3
		}

		setLocalPosition(arg_23_0.curBuffTF, var_23_6)
		arg_23_0.managedTween(LeanTween.value, None, go(arg_23_0.curBuffTF), 0, 1, var_23_5).setEase(LeanTweenType.easeOutBack).setOnUpdate(System.Action_float(function(arg_24_0)
			local var_24_0 = var_23_3 + (var_23_4 - var_23_3) * arg_24_0

			var_23_6.y = var_24_0

			setAnchoredPosition(arg_23_0.curBuffTF, var_23_6)))

def var_0_0.openSelectShipView(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.playerProxy.getData()

	if arg_25_0.getShipGameData().getConfig("config_data")[1] > var_25_0.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	arg_25_0.updateCardSelecting(arg_25_1, True)
	setActive(arg_25_0.tipGoldTF, False)

	local var_25_1 = {
		shipGameID = arg_25_0.shipGameID,
		selectingCardIndex = arg_25_1,
		def onClose:()
			arg_25_0.updateCardSelecting(arg_25_1, False)
			setActive(arg_25_0.tipGoldTF, True)

			local var_26_0 = arg_25_0.cardTFList[arg_25_1]
			local var_26_1 = arg_25_0.findTF("Empty", var_26_0)
			local var_26_2 = arg_25_0.findTF("Ship", var_26_0)

			setActive(var_26_1, True)
			setActive(var_26_2, False),
		def onSelect:(arg_27_0)
			local var_27_0 = arg_25_0.cardTFList[arg_25_1]
			local var_27_1 = arg_25_0.findTF("Empty", var_27_0)
			local var_27_2 = arg_25_0.findTF("Ship", var_27_0)
			local var_27_3 = "shipcard_" .. arg_27_0
			local var_27_4 = "Shrine2022/" .. var_27_3

			setImageSprite(var_27_2, LoadSprite(var_27_4, var_27_3), True)
			setActive(var_27_1, False)
			setActive(var_27_2, True),
		def onConfirm:(arg_28_0)
			local var_28_0 = arg_25_0.getShipGameData()

			if var_28_0.GetRuntimeData("count") <= 0:
				arg_25_0.PrintLog("Error, count <= 0")
			else
				local var_28_1 = var_28_0.getConfig("config_data")[2][arg_28_0]

				arg_25_0.PrintLog("发送选船操作", arg_25_0.shipGameID, 2, var_28_1, arg_25_1, arg_28_0)
				arg_25_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
					arg_25_0.shipGameID,
					2,
					var_28_1,
					arg_25_1,
					arg_28_0
				})
	}

	arg_25_0.shrineSelectShipView = Shrine2022SelectShipView.New(arg_25_0._tf.parent, arg_25_0.event, var_25_1)

	arg_25_0.shrineSelectShipView.Reset()
	arg_25_0.shrineSelectShipView.Load()

def var_0_0.openSelectBuffView(arg_29_0):
	local var_29_0 = arg_29_0.playerProxy.getData()

	if arg_29_0.GetMGData().getConfig("config_data")[1] > var_29_0.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	if arg_29_0.GetMGData().GetRuntimeData("count") <= 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("pray_cant_tips"))

		return

	local var_29_1 = {
		def onClose:()
			return,
		def onSelect:(arg_31_0)
			local var_31_0 = arg_29_0.GetMGData()

			if var_31_0.GetRuntimeData("count") <= 0:
				arg_29_0.PrintLog("Error, count <= 0")
			else
				local var_31_1 = var_31_0.getConfig("config_data")[2][arg_31_0]

				arg_29_0.PrintLog("发送选Buff操作", arg_29_0.commanderGameID, 2, var_31_1)
				arg_29_0.SendOperator(MiniGameOPCommand.CMD_SPECIAL_GAME, {
					arg_29_0.commanderGameID,
					2,
					var_31_1
				})
	}

	arg_29_0.shrineSelectBuffView = Shrine2022SelectBuffView.New(arg_29_0._tf.parent, arg_29_0.event, var_29_1)

	arg_29_0.shrineSelectBuffView.Reset()
	arg_29_0.shrineSelectBuffView.Load()

def var_0_0.openShipWordView(arg_32_0, arg_32_1):
	local var_32_0 = {
		curSelectShip = arg_32_1
	}

	arg_32_0.shrineShipWordView = Shrine2022ShipWordView.New(arg_32_0._tf, arg_32_0.event, var_32_0)

	arg_32_0.shrineShipWordView.Reset()
	arg_32_0.shrineShipWordView.Load()

def var_0_0.openFakeDrop(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.getShipGameData().getConfig("simple_config_data")
	local var_33_1 = {
		type = var_33_0[1],
		id = var_33_0[2],
		count = var_33_0[3]
	}

	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = AwardInfoMediator,
		viewComponent = AwardInfoLayer,
		data = {
			items = {
				var_33_1
			}
		},
		def onRemoved:()
			if arg_33_1:
				arg_33_1()
	}))

def var_0_0.isInitedCommanderGameData(arg_35_0):
	if not arg_35_0.GetMGData().GetRuntimeData("isInited"):
		return False
	else
		return True

def var_0_0.isInitedShipGameData(arg_36_0):
	if not arg_36_0.getShipGameData().GetRuntimeData("isInited"):
		return False
	else
		return True

def var_0_0.isHaveCommanderBuff(arg_37_0):
	local var_37_0 = arg_37_0.playerProxy.getData().buff_list
	local var_37_1 = arg_37_0.GetMGData().getConfig("config_data")[2]
	local var_37_2

	for iter_37_0, iter_37_1 in ipairs(var_37_0):
		var_37_2 = table.indexof(var_37_1, iter_37_1.id, 1)

		if var_37_2:
			if pg.TimeMgr.GetInstance().GetServerTime() < iter_37_1.timestamp:
				return var_37_2
			else
				return None

	return var_37_2

def var_0_0.getSelectedShipByCardIndex(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.getShipGameData().GetRuntimeData("kvpElements")[1]

	for iter_38_0, iter_38_1 in ipairs(var_38_0):
		if iter_38_1.key == arg_38_1:
			return iter_38_1.value

	return 0

def var_0_0.getCardIndexByShip(arg_39_0, arg_39_1):
	local var_39_0 = arg_39_0.getShipGameData().GetRuntimeData("kvpElements")[1]

	for iter_39_0, iter_39_1 in ipairs(var_39_0):
		if iter_39_1.value == arg_39_1:
			return iter_39_1.key

	return 0

def var_0_0.getSelectedShipCount(arg_40_0):
	local var_40_0 = 0

	return #arg_40_0.getShipGameData().GetRuntimeData("kvpElements")[1]

def var_0_0.getShipGameData(arg_41_0):
	return arg_41_0.miniGameProxy.GetMiniGameData(arg_41_0.shipGameID)

def var_0_0.PrintLog(arg_42_0, ...):
	if IsUnityEditor:
		print(...)

def var_0_0.IsNeedShowTipWithoutActivityFinalReward():
	local var_43_0 = False
	local var_43_1 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_3)

	if var_43_1:
		var_43_0 = (var_43_1.GetRuntimeData("count") or 0) > 0

	local var_43_2
	local var_43_3 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_3)

	if var_43_3:
		local var_43_4 = getProxy(PlayerProxy).getData()
		local var_43_5 = var_43_3.getConfig("config_data")[2]

		for iter_43_0, iter_43_1 in ipairs(var_43_4.buff_list):
			var_43_2 = table.indexof(var_43_5, iter_43_1.id, 1)

			if var_43_2:
				if pg.TimeMgr.GetInstance().GetServerTime() > iter_43_1.timestamp:
					var_43_2 = None

				break

	if var_43_2:
		var_43_0 = False

	local var_43_6 = False
	local var_43_7 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_5)

	if var_43_7:
		var_43_6 = (var_43_7.GetRuntimeData("count") or 0) > 0

	local var_43_8
	local var_43_9 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_5)

	if var_43_9:
		local var_43_10 = getProxy(PlayerProxy).getData()
		local var_43_11 = var_43_9.getConfig("config_data")[2]

		for iter_43_2, iter_43_3 in ipairs(var_43_10.buff_list):
			var_43_8 = table.indexof(var_43_11, iter_43_3.id, 1)

			if var_43_8:
				if pg.TimeMgr.GetInstance().GetServerTime() > iter_43_3.timestamp:
					var_43_8 = None

				break

	if var_43_8:
		var_43_6 = False

	return var_43_0 or var_43_6

return var_0_0

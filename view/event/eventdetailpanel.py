EventConst = require("view/event/EventConst")

local var_0_0 = class("EventDetailPanel")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.go = arg_1_1
	arg_1_0.tr = arg_1_1.transform
	arg_1_0.dispatch = arg_1_2
	arg_1_0.btn = arg_1_0.findTF("btn").gameObject

	setText(findTF(arg_1_0.tr, "btn_recommend/text"), pg.gametip.event_ui_recommend.tip)
	setText(findTF(arg_1_0.tr, "btn_recommend_disable/text"), pg.gametip.event_ui_recommend.tip)
	setText(findTF(arg_1_0.tr, "consume/label"), pg.gametip.event_ui_consume.tip)
	setText(findTF(arg_1_0.tr, "btn/start/text"), pg.gametip.event_ui_start.tip)
	setText(findTF(arg_1_0.tr, "btn_disable/text"), pg.gametip.event_ui_start.tip)
	setText(findTF(arg_1_0.tr, "btn/giveup/text"), pg.gametip.event_ui_giveup.tip)
	setText(findTF(arg_1_0.tr, "btn/finish/text"), pg.gametip.event_ui_finish.tip)

	arg_1_0.conditions = findTF(arg_1_0.tr, "conditions")
	arg_1_0.condition1 = findTF(arg_1_0.conditions, "condition_1/mask/Text")
	arg_1_0.condition2 = findTF(arg_1_0.conditions, "condition_2/mask/Text")
	arg_1_0.condition3 = findTF(arg_1_0.conditions, "condition_3/mask/Text")
	arg_1_0.consume = arg_1_0.findTF("consume/Text")
	arg_1_0.leftShips = arg_1_0.findTF("frame/ship_contain_left")
	arg_1_0.rightShips = arg_1_0.findTF("frame/ship_contain_right")
	arg_1_0.disabeleBtn = arg_1_0.findTF("btn_disable").gameObject
	arg_1_0.recommentBtn = arg_1_0.findTF("btn_recommend")
	arg_1_0.recommentDisable = arg_1_0.findTF("btn_recommend_disable")
	arg_1_0.usePrevFormationBtn = arg_1_0.findTF("use_prev_formation")
	arg_1_0.shipItems = {}

	eachChild(arg_1_0.leftShips, function(arg_2_0)
		table.insert(arg_1_0.shipItems, 1, arg_2_0))
	eachChild(arg_1_0.rightShips, function(arg_3_0)
		table.insert(arg_1_0.shipItems, 4, arg_3_0))
	onButton(arg_1_0, arg_1_0.btn, function()
		arg_1_0.onFuncClick(), SFX_PANEL)
	onButton(arg_1_0, arg_1_0.recommentBtn, function()
		local var_5_0 = getProxy(BayProxy)
		local var_5_1 = var_5_0.getDelegationRecommendShips(arg_1_0.event)
		local var_5_2 = var_5_0.getDelegationRecommendShipsLV1(arg_1_0.event)

		if #var_5_1 == 0 and #var_5_2 > 0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("event_recommend_level1"),
				def onYes:()
					arg_1_0.dispatch(EventConst.EVENT_RECOMMEND_LEVEL1, arg_1_0.event)
			})
		else
			arg_1_0.dispatch(EventConst.EVENT_RECOMMEND, arg_1_0.event))
	onButton(arg_1_0, arg_1_0.usePrevFormationBtn, function()
		arg_1_0.UsePrevFormation(), SFX_PANEL)

def var_0_0.Update(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.index = arg_8_1
	arg_8_0.event = arg_8_2

	arg_8_0.Flush()

def var_0_0.UsePrevFormation(arg_9_0):
	if arg_9_0.event and arg_9_0.event.ExistPrevFormation():
		local var_9_0 = arg_9_0.event.GetPrevFormation()

		arg_9_0.dispatch(EventConst.EVEN_USE_PREV_FORMATION, arg_9_0.event, var_9_0)

def var_0_0.Flush(arg_10_0):
	setActive(arg_10_0.usePrevFormationBtn, arg_10_0.event.ExistPrevFormation() and arg_10_0.event.state == EventInfo.StateNone and arg_10_0.event.CanRecordPrevFormation())
	eachChild(arg_10_0.btn, function(arg_11_0)
		if arg_10_0.event.state == EventInfo.StateNone and arg_11_0.name == "start":
			SetActive(arg_11_0, True)
		elif arg_10_0.event.state == EventInfo.StateActive and arg_11_0.name == "giveup":
			SetActive(arg_11_0, True)
		elif arg_10_0.event.state == EventInfo.StateFinish and arg_11_0.name == "finish":
			SetActive(arg_11_0, True)
		else
			SetActive(arg_11_0, False))

	local var_10_0 = arg_10_0.event.reachLevel()
	local var_10_1 = arg_10_0.event.reachNum()
	local var_10_2 = arg_10_0.event.reachTypes()

	SetActive(arg_10_0.disabeleBtn, not var_10_0 or not var_10_1 or not var_10_2)

	local var_10_3 = arg_10_0.event.ships
	local var_10_4 = arg_10_0.event.template
	local var_10_5 = arg_10_0.setConditionStr(i18n("event_condition_ship_level", var_10_4.ship_lv), var_10_0)

	setScrollText(arg_10_0.condition1, var_10_5)
	setActive(findTF(arg_10_0.conditions, "condition_1/mark"), var_10_0)
	setActive(findTF(arg_10_0.conditions, "condition_1/mark1"), not var_10_0)

	local var_10_6 = arg_10_0.setConditionStr(i18n("event_condition_ship_count", var_10_4.ship_num), var_10_1)

	setScrollText(arg_10_0.condition2, var_10_6)
	setActive(findTF(arg_10_0.conditions, "condition_2/mark"), var_10_1)
	setActive(findTF(arg_10_0.conditions, "condition_2/mark1"), not var_10_1)

	local var_10_7 = arg_10_0.event.getTypesStr()
	local var_10_8 = arg_10_0.setConditionStr(var_10_7, var_10_2)

	setScrollText(arg_10_0.condition3, var_10_8)
	setActive(findTF(arg_10_0.conditions, "condition_3/mark"), var_10_2)
	setActive(findTF(arg_10_0.conditions, "condition_3/mark1"), not var_10_2)
	setText(arg_10_0.consume, arg_10_0.event.getOilConsume())

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.shipItems):
		local var_10_9 = iter_10_1.Find("shiptpl")
		local var_10_10 = iter_10_1.Find("emptytpl")
		local var_10_11 = iter_10_0 <= #var_10_3

		SetActive(var_10_9, var_10_11)
		SetActive(var_10_10, not var_10_11)

		if var_10_11:
			updateShip(var_10_9, var_10_3[iter_10_0], {
				initStar = True
			})
			setText(findTF(var_10_9, "icon_bg/lv/Text"), var_10_3[iter_10_0].level)
			onButton(arg_10_0, var_10_9.Find("icon_bg"), function()
				arg_10_0.onRemoveClick(iter_10_0), SFX_PANEL)
		else
			onButton(arg_10_0, var_10_10, function()
				arg_10_0.onChangeClick())

	if arg_10_0.event.state == EventInfo.StateNone:
		SetActive(arg_10_0.recommentBtn, True)
		SetActive(arg_10_0.recommentDisable, False)
	else
		SetActive(arg_10_0.recommentBtn, False)
		SetActive(arg_10_0.recommentDisable, True)

def var_0_0.setConditionStr(arg_14_0, arg_14_1, arg_14_2):
	return arg_14_2 and setColorStr(arg_14_1, COLOR_YELLOW) or setColorStr(arg_14_1, "#F35842FF")

def var_0_0.Clear(arg_15_0):
	pg.DelegateInfo.Dispose(arg_15_0)

def var_0_0.onChangeClick(arg_16_0):
	if arg_16_0.event.state == EventInfo.StateNone:
		arg_16_0.dispatch(EventConst.EVENT_OPEN_DOCK, arg_16_0.event)

def var_0_0.onRemoveClick(arg_17_0, arg_17_1):
	if arg_17_0.event.state == EventInfo.StateNone:
		table.remove(arg_17_0.event.shipIds, arg_17_1)
		table.remove(arg_17_0.event.ships, arg_17_1)
		arg_17_0.Flush()

def var_0_0.onFuncClick(arg_18_0):
	if arg_18_0.event.state == EventInfo.StateNone:
		arg_18_0.dispatch(EventConst.EVENT_START, arg_18_0.event)
	elif arg_18_0.event.state == EventInfo.StateActive:
		arg_18_0.dispatch(EventConst.EVENT_GIVEUP, arg_18_0.event)
	elif arg_18_0.event.state == EventInfo.StateFinish:
		arg_18_0.dispatch(EventConst.EVENT_FINISH, arg_18_0.event)

def var_0_0.findTF(arg_19_0, arg_19_1):
	return findTF(arg_19_0.tr, arg_19_1)

return var_0_0

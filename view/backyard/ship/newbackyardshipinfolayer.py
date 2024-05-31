local var_0_0 = class("NewBackYardShipInfoLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "NewBackYardShipInfoUI"

def var_0_0.init(arg_2_0):
	arg_2_0.descTxt = arg_2_0.findTF("frame/desc").GetComponent(typeof(Text))
	arg_2_0.counterTxt = arg_2_0.findTF("frame/top/value/Text").GetComponent(typeof(Text))
	arg_2_0.cardContainer = arg_2_0.findTF("frame/panel")
	arg_2_0.closeBtn = arg_2_0.findTF("frame/top/close")
	arg_2_0.mainPanel = arg_2_0.findTF("frame")
	arg_2_0.toggles = {
		[Ship.STATE_REST] = arg_2_0.findTF("frame/top/rest"),
		[Ship.STATE_TRAIN] = arg_2_0.findTF("frame/top/train")
	}
	arg_2_0.animations = {
		[Ship.STATE_REST] = arg_2_0.findTF("frame/top/rest").GetComponent(typeof(Animation)),
		[Ship.STATE_TRAIN] = arg_2_0.findTF("frame/top/train").GetComponent(typeof(Animation))
	}
	arg_2_0.animationName = {
		[Ship.STATE_REST] = {
			"anim_backyard_shipinfo_rest_Select",
			"anim_backyard_shipinfo_rest_unSelect"
		},
		[Ship.STATE_TRAIN] = {
			"anim_backyard_shipinfo_train_Select",
			"anim_backyard_shipinfo_train_unSelect"
		}
	}
	arg_2_0.addShipTpl = arg_2_0.cardContainer.Find("AddShipTpl")
	arg_2_0.extendShipTpl = arg_2_0.cardContainer.Find("ExtendShipTpl")
	arg_2_0.shipCardTpl = arg_2_0.cardContainer.Find("ShipCardTpl")
	arg_2_0.cards = {
		{},
		{},
		{}
	}

	table.insert(arg_2_0.cards[1], BackYardShipCard.New(arg_2_0.shipCardTpl, arg_2_0.event))
	table.insert(arg_2_0.cards[2], BackYardEmptyCard.New(arg_2_0.addShipTpl, arg_2_0.event))
	table.insert(arg_2_0.cards[3], BackYardExtendCard.New(arg_2_0.extendShipTpl, arg_2_0.event))
	setText(arg_2_0.findTF("frame/desc1"), i18n("backyard_longpress_ship_tip"))
	setText(arg_2_0.findTF("frame/top/rest/Text"), i18n("courtyard_label_rest"))
	setText(arg_2_0.findTF("frame/top/train/Text"), i18n("courtyard_label_train"))
	setText(arg_2_0.findTF("frame/top/rest/Text_un"), i18n("courtyard_label_rest"))
	setText(arg_2_0.findTF("frame/top/train/Text_un"), i18n("courtyard_label_train"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.emit(var_0_0.ON_CLOSE), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.emit(var_0_0.ON_CLOSE), SFX_PANEL)

	local var_3_0 = Color.New(0.2235294, 0.227451, 0.2352941, 1)
	local var_3_1 = Color.New(0.5137255, 0.5137255, 0.5137255, 1)

	for iter_3_0, iter_3_1 in pairs(arg_3_0.toggles):
		onToggle(arg_3_0, iter_3_1, function(arg_6_0)
			if arg_6_0:
				arg_3_0.SwitchToPage(iter_3_0)

			iter_3_1.Find("icon").GetComponent(typeof(Image)).color = arg_6_0 and var_3_0 or var_3_1

			local var_6_0 = arg_3_0.animations[iter_3_0]
			local var_6_1 = arg_3_0.animationName[iter_3_0]
			local var_6_2 = arg_6_0 and 1 or 2

			var_6_0.Play(var_6_1[var_6_2])
			print(var_6_1[var_6_2]), SFX_PANEL)

	local var_3_2 = getProxy(DormProxy).getRawData()

	setActive(arg_3_0.toggles[2], var_3_2.isUnlockFloor(2))
	onNextTick(function()
		if arg_3_0.exited:
			return

		local var_7_0 = arg_3_0.contextData.type or Ship.STATE_TRAIN
		local var_7_1 = {
			Ship.STATE_TRAIN,
			Ship.STATE_REST
		}

		for iter_7_0, iter_7_1 in ipairs(var_7_1):
			triggerToggle(arg_3_0.toggles[iter_7_1], iter_7_1 == var_7_0))

def var_0_0.GetCardTypeCnt(arg_8_0, arg_8_1):
	local var_8_0 = getProxy(DormProxy).getRawData()
	local var_8_1 = 0
	local var_8_2 = 0
	local var_8_3 = 0

	if arg_8_1 == Ship.STATE_TRAIN:
		var_8_1 = var_8_0.exp_pos
		var_8_2 = var_8_0.getConfig("training_ship_number")
	elif arg_8_1 == Ship.STATE_REST:
		var_8_1 = var_8_0.rest_pos
		var_8_2 = var_8_0.getConfig("fix_ship_number")

	local var_8_4 = var_8_0.GetStateShipCnt(arg_8_1)
	local var_8_5 = var_8_1 - var_8_4
	local var_8_6 = var_8_2 - var_8_1

	return {
		var_8_4,
		var_8_5,
		var_8_6
	}

def var_0_0.SwitchToPage(arg_9_0, arg_9_1):
	if arg_9_0.type == arg_9_1:
		return

	arg_9_0.type = arg_9_1

	arg_9_0.UpdateSlots()

	if arg_9_1 == Ship.STATE_TRAIN:
		arg_9_0.descTxt.text = i18n("backyard_traning_tip")
	elif arg_9_1 == Ship.STATE_REST:
		arg_9_0.descTxt.text = i18n("backyard_rest_tip")

def var_0_0.UpdateSlots(arg_10_0):
	local var_10_0 = arg_10_0.type
	local var_10_1 = arg_10_0.GetCardTypeCnt(var_10_0)
	local var_10_2 = getProxy(DormProxy).getRawData().GetStateShips(var_10_0)
	local var_10_3 = 0
	local var_10_4 = {}

	for iter_10_0, iter_10_1 in ipairs(var_10_1):
		local var_10_5 = arg_10_0.GetTypeCards(iter_10_0, iter_10_1)

		for iter_10_2, iter_10_3 in ipairs(var_10_5):
			var_10_3 = var_10_3 + 1

			iter_10_3.Flush(var_10_0, var_10_2[iter_10_2])
			iter_10_3.SetSiblingIndex(var_10_3)

	arg_10_0.counterTxt.text = var_10_1[1] .. "/" .. var_10_1[2] + var_10_1[1]

def var_0_0.GetTypeCards(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.cards[arg_11_1]

	for iter_11_0 = #var_11_0, arg_11_2 - 1:
		table.insert(var_11_0, var_11_0[1].Clone())

	for iter_11_1 = #var_11_0, arg_11_2 + 1, -1:
		var_11_0[iter_11_1].Disable()

	local var_11_1 = {}

	for iter_11_2 = 1, arg_11_2:
		local var_11_2 = var_11_0[iter_11_2]

		var_11_2.Enable()

		var_11_1[iter_11_2] = var_11_2

	return var_11_1

def var_0_0.willExit(arg_12_0):
	for iter_12_0, iter_12_1 in ipairs(arg_12_0.cards):
		for iter_12_2, iter_12_3 in ipairs(iter_12_1):
			iter_12_3.Dispose()

return var_0_0

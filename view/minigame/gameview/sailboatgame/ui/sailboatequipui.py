local var_0_0 = class("SailBoatEquipUI")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	var_0_1 = SailBoatGameVo
	arg_1_0._equipUI = findTF(arg_1_0._tf, "ui/equipUI")
	arg_1_0.btnBack = findTF(arg_1_0._equipUI, "back")
	arg_1_0.btnBack1 = findTF(arg_1_0._equipUI, "back_1")
	arg_1_0.btnStart = findTF(arg_1_0._equipUI, "btnStart")

	onButton(arg_1_0._event, arg_1_0.btnBack1, function()
		arg_1_0.show(False)
		arg_1_0._event.emit(SailBoatGameView.BACK_MENU), SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnStart, function()
		arg_1_0._event.emit(SailBoatGameView.READY_START), SFX_CONFIRM)

	arg_1_0.selectTpl = findTF(arg_1_0._equipUI, "selectItem")
	arg_1_0.equipTpl = findTF(arg_1_0._equipUI, "equipItem")
	arg_1_0.selectContent = findTF(arg_1_0._equipUI, "select/ad/list")
	arg_1_0.equipContent = findTF(arg_1_0._equipUI, "equip/list")
	arg_1_0.unEquipFlag = False
	arg_1_0.baseHp = SailBoatGameConst.game_char[var_0_1.char_id].hp
	arg_1_0.baseSpeed = SailBoatGameConst.game_char[var_0_1.char_id].speed.x
	arg_1_0.speedTf = findTF(arg_1_0._equipUI, "equip/speed")
	arg_1_0.hpTf = findTF(arg_1_0._equipUI, "equip/hp")
	arg_1_0.btnUnEquip = findTF(arg_1_0._equipUI, "btnUnEquip")

	onButton(arg_1_0._event, arg_1_0.btnUnEquip, function()
		if arg_1_0.curSelectItem:
			arg_1_0.unEquipFlag = True
		else
			arg_1_0.unEquipFlag = not arg_1_0.unEquipFlag

		if arg_1_0.unEquipFlag:
			arg_1_0.curSelectData = None
			arg_1_0.curSelectItem = None

		arg_1_0.updateUI())

	arg_1_0.selects = {}

	for iter_1_0 = 1, #SailBoatGameConst.equip_data:
		local var_1_0 = SailBoatGameConst.equip_data[iter_1_0]
		local var_1_1 = tf(instantiate(arg_1_0.selectTpl))

		onButton(arg_1_0._event, var_1_1, function()
			if arg_1_0.curSelectItem == var_1_1:
				arg_1_0.curSelectItem = None
				arg_1_0.curSelectData = None
			else
				arg_1_0.curSelectItem = var_1_1
				arg_1_0.curSelectData = var_1_0

				if arg_1_0.unEquipFlag:
					arg_1_0.unEquipFlag = False

			arg_1_0.updateUI(), SFX_CANCEL)

		local var_1_2 = GetComponent(findTF(var_1_1, "icon"), typeof(Image))

		var_1_2.sprite = var_0_1.GetEquipIcon(var_1_0.icon)

		var_1_2.SetNativeSize()
		SetParent(var_1_1, arg_1_0.selectContent)
		table.insert(arg_1_0.selects, var_1_1)

	arg_1_0.equips = {}
	arg_1_0.equipItems = {}

	for iter_1_1 = 1, SailBoatGameConst.max_equip_count:
		table.insert(arg_1_0.equips, 0)

	for iter_1_2 = 1, SailBoatGameConst.max_equip_count:
		local var_1_3 = iter_1_2
		local var_1_4 = tf(instantiate(arg_1_0.equipTpl))
		local var_1_5 = arg_1_0.equips[iter_1_2]

		onButton(arg_1_0._event, var_1_4, function()
			local var_6_0 = var_0_1.GetGameUseTimes()

			if var_0_1.GetGameTimes() > 0:
				var_6_0 = var_6_0 + 1

			if SailBoatGameConst.game_round[var_6_0].equip_count >= var_1_3:
				if arg_1_0.curSelectData:
					if not arg_1_0.checkEquipAble(arg_1_0.curSelectData.id):
						return

					arg_1_0.equips[iter_1_2] = arg_1_0.curSelectData.id
				elif arg_1_0.unEquipFlag:
					arg_1_0.equips[iter_1_2] = 0

				arg_1_0.updateUI(), SFX_CANCEL)
		SetParent(var_1_4, arg_1_0.equipContent)
		table.insert(arg_1_0.equipItems, var_1_4)

	arg_1_0.descTf = findTF(arg_1_0._equipUI, "desc")
	arg_1_0.descTextTf = findTF(arg_1_0._equipUI, "desc/bg/desc")
	arg_1_0.curSelectItem = None
	arg_1_0.curSelectData = None

	arg_1_0.showUI()
	arg_1_0.updateUI()

def var_0_0.show(arg_7_0, arg_7_1):
	setActive(arg_7_0._equipUI, arg_7_1)
	arg_7_0.showUI()
	arg_7_0.updateUI()

def var_0_0.showUI(arg_8_0):
	local var_8_0 = var_0_1.GetGameUseTimes()

	if var_0_1.GetGameTimes() > 0:
		var_8_0 = var_8_0 + 1

	arg_8_0.roundEquipData = SailBoatGameConst.game_equip_round[var_8_0]

	for iter_8_0 = 1, #arg_8_0.selects:
		if arg_8_0.roundEquipData[iter_8_0][2] == 0:
			setActive(arg_8_0.selects[iter_8_0], False)
		else
			setActive(arg_8_0.selects[iter_8_0], True)

def var_0_0.checkEquipAble(arg_9_0, arg_9_1):
	local var_9_0 = 0
	local var_9_1 = var_0_1.GetGameUseTimes()

	if var_0_1.GetGameTimes() > 0:
		var_9_1 = var_9_1 + 1

	local var_9_2 = SailBoatGameConst.game_equip_round[var_9_1]

	for iter_9_0 = 1, #var_9_2:
		if var_9_2[iter_9_0][1] == arg_9_1:
			var_9_0 = var_9_2[iter_9_0][2]

	if var_9_0 == 0:
		return False, 0, 0

	local var_9_3 = 0

	for iter_9_1 = 1, #arg_9_0.equips:
		if arg_9_0.equips[iter_9_1] == arg_9_1:
			var_9_3 = var_9_3 + 1

	if var_9_0 <= var_9_3:
		return False, var_9_3, var_9_0

	return True, var_9_3, var_9_0

def var_0_0.updateUI(arg_10_0):
	for iter_10_0 = 1, #arg_10_0.selects:
		local var_10_0 = arg_10_0.selects[iter_10_0]

		setActive(findTF(var_10_0, "select"), arg_10_0.curSelectItem == var_10_0)

		local var_10_1, var_10_2, var_10_3 = arg_10_0.checkEquipAble(iter_10_0)

		setText(findTF(var_10_0, "amount"), var_10_3 - var_10_2)

	setActive(arg_10_0.descTf, arg_10_0.curSelectItem != None)

	if arg_10_0.curSelectItem:
		arg_10_0.descTf.anchoredPosition = arg_10_0._equipUI.InverseTransformPoint(arg_10_0.curSelectItem.position)

		setText(arg_10_0.descTextTf, i18n(arg_10_0.curSelectData.desc))

	local var_10_4 = var_0_1.GetGameUseTimes()

	if var_0_1.GetGameTimes() > 0:
		var_10_4 = var_10_4 + 1

	local var_10_5 = SailBoatGameConst.game_round[var_10_4].equip_count

	for iter_10_1 = 1, SailBoatGameConst.max_equip_count:
		local var_10_6 = iter_10_1
		local var_10_7 = arg_10_0.equips[iter_10_1]
		local var_10_8 = arg_10_0.equipItems[iter_10_1]

		setActive(findTF(var_10_8, "lock"), var_10_5 < iter_10_1)
		setActive(findTF(var_10_8, "empty"), False)
		setActive(findTF(var_10_8, "bg"), False)
		setActive(findTF(var_10_8, "icon"), False)
		setActive(findTF(var_10_8, "unEquip"), False)
		setActive(findTF(var_10_8, "add"), False)
		setActive(findTF(var_10_8, "add_2"), False)

		local var_10_9 = True

		if var_10_7 != 0:
			local var_10_10 = SailBoatGameConst.equip_data[var_10_7]
			local var_10_11 = GetComponent(findTF(var_10_8, "icon"), typeof(Image))

			var_10_11.sprite = var_0_1.GetEquipIcon(var_10_10.icon)

			var_10_11.SetNativeSize()
			setActive(findTF(var_10_8, "bg"), True)
			setActive(findTF(var_10_8, "icon"), True)

			if arg_10_0.unEquipFlag:
				setActive(findTF(var_10_8, "unEquip"), True)

			var_10_9 = False
		else
			setActive(findTF(var_10_8, "empty"), True)

		if arg_10_0.curSelectItem and iter_10_1 <= var_10_5:
			if var_10_9:
				setActive(findTF(var_10_8, "add"), True)
			else
				setActive(findTF(var_10_8, "add_2"), True)

	local var_10_12 = arg_10_0.baseHp
	local var_10_13 = arg_10_0.baseSpeed

	for iter_10_2 = 1, #arg_10_0.equips:
		local var_10_14 = arg_10_0.equips[iter_10_2]

		if var_10_14 != 0:
			local var_10_15 = SailBoatGameConst.equip_data[var_10_14]

			var_10_12 = var_10_12 + var_10_15.hp
			var_10_13 = var_10_13 + var_10_15.speed

	setText(arg_10_0.speedTf, tostring(var_10_13))
	setText(arg_10_0.hpTf, tostring(var_10_12))

	var_0_1.equips = arg_10_0.equips

return var_0_0

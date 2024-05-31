local var_0_0 = class("OtherWorldTempleChars")
local var_0_1 = "other_world_temple_char"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2

	onButton(arg_1_0._event, findTF(arg_1_0._tf, "ad/btnClose"), function()
		arg_1_0.setActive(False), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0._tf, "ad/clickClose"), function()
		arg_1_0.setActive(False), SFX_CANCEL)

	arg_1_0._charTpl = findTF(arg_1_0._tf, "ad/chars/content/charTpl")

	setText(findTF(arg_1_0._charTpl, "got/img/text"), i18n("word_got"))
	setActive(arg_1_0._charTpl, False)

	arg_1_0._charItems = {}
	arg_1_0._charContent = findTF(arg_1_0._tf, "ad/chars/content")

def var_0_0.setData(arg_4_0, arg_4_1):
	arg_4_0.charIds = arg_4_1

def var_0_0.updateActivityPool(arg_5_0, arg_5_1):
	arg_5_0.activityPools = arg_5_1

def var_0_0.updateSelect(arg_6_0):
	arg_6_0.updateItemsCount(#arg_6_0.charIds)

	for iter_6_0 = 1, #arg_6_0._charItems:
		local var_6_0 = arg_6_0._charItems[iter_6_0]

		setActive(var_6_0, False)

		if iter_6_0 <= #arg_6_0.charIds:
			setActive(var_6_0, True)
			arg_6_0.setItemData(var_6_0, arg_6_0.charIds[iter_6_0])

	setText(findTF(arg_6_0._tf, "ad/title/text"), i18n(var_0_1))

def var_0_0.setItemData(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = pg.guardian_template[arg_7_2]
	local var_7_1 = arg_7_0.activityPools[var_7_0.guardian_gain_pool]
	local var_7_2 = ""
	local var_7_3 = var_7_1.getGuardianGot(arg_7_2)

	if var_7_0.type == 1:
		var_7_2 = string.gsub(var_7_0.guardian_gain_desc, "$1", math.min(var_7_1.getFetchCount(), var_7_0.guardian_gain[2]))
	elif var_7_0.type == 2:
		if var_7_3:
			var_7_2 = var_7_0.guardian_gain_desc
		else
			var_7_2 = "???"

	if var_7_0.type == 2:
		setText(findTF(arg_7_1, "desc/text"), var_7_3 and var_7_0.guardian_desc or "???")
		setText(findTF(arg_7_1, "name/text"), var_7_3 and var_7_0.guardian_name or "???")
	else
		setText(findTF(arg_7_1, "name/text"), var_7_0.guardian_name)
		setText(findTF(arg_7_1, "desc/text"), var_7_0.guardian_desc)

	if PLATFORM_CODE != PLATFORM_CH:
		GetComponent(findTF(arg_7_1, "name/text"), typeof(Text)).fontSize = 30
		GetComponent(findTF(arg_7_1, "desc/text"), typeof(Text)).fontSize = 24

	if var_7_0.type == 2:
		setActive(findTF(arg_7_1, "icon/mask/img"), var_7_3)

	LoadImageSpriteAsync("shipyardicon/" .. var_7_0.guardian_painting, findTF(arg_7_1, "icon/mask/img"), True)
	setText(findTF(arg_7_1, "tip/text"), var_7_2)
	setActive(findTF(arg_7_1, "icon/lock"), not var_7_3)
	setActive(findTF(arg_7_1, "got"), var_7_3)

def var_0_0.updateItemsCount(arg_8_0, arg_8_1):
	local var_8_0 = 0

	if arg_8_1 > #arg_8_0._charItems:
		var_8_0 = arg_8_1 - #arg_8_0._charItems

	for iter_8_0 = 1, var_8_0:
		local var_8_1 = tf(instantiate(arg_8_0._charTpl))

		SetParent(var_8_1, arg_8_0._charContent)
		table.insert(arg_8_0._charItems, var_8_1)

def var_0_0.setActive(arg_9_0, arg_9_1):
	setActive(arg_9_0._tf, arg_9_1)

return var_0_0

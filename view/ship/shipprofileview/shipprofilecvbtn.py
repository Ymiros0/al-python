local var_0_0 = class("ShipProfileCvBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0._go = go(arg_1_1)
	arg_1_0.nameTxt = arg_1_0._tf.Find("Text").GetComponent(typeof(Text))

	setActive(arg_1_0._tf.Find("tag_common"), True)

	arg_1_0.tagDiff = arg_1_0._tf.Find("tag_diff")
	arg_1_0.playIcon = arg_1_0._tf.Find("play_icon")

def var_0_0.Init(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0.shipGroup = arg_2_1
	arg_2_0.isLive2d = arg_2_3
	arg_2_0.skin = arg_2_2
	arg_2_0.voice = arg_2_4
	arg_2_0.words = pg.ship_skin_words[arg_2_0.skin.id]

	local var_2_0 = arg_2_0.voice.key
	local var_2_1 = arg_2_1.getIntimacyName(var_2_0)

	if var_2_1:
		arg_2_0.voice = setmetatable({
			voice_name = var_2_1
		}, {
			__index = arg_2_4
		})

	local var_2_2
	local var_2_3
	local var_2_4
	local var_2_5
	local var_2_6
	local var_2_7
	local var_2_8 = arg_2_4.key

	if string.find(var_2_8, ShipWordHelper.WORD_TYPE_MAIN):
		local var_2_9 = string.gsub(var_2_8, ShipWordHelper.WORD_TYPE_MAIN, "")

		var_2_5 = tonumber(var_2_9)
		var_2_2, var_2_3, var_2_4 = ShipWordHelper.GetWordAndCV(arg_2_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_2_5)

		if arg_2_0.isLive2d:
			var_2_6 = ShipWordHelper.GetL2dCvCalibrate(arg_2_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_2_5)
			var_2_7 = ShipWordHelper.GetL2dSoundEffect(arg_2_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_2_5)
	else
		var_2_2, var_2_3, var_2_4 = ShipWordHelper.GetWordAndCV(arg_2_0.skin.id, var_2_8)

		if arg_2_0.isLive2d:
			var_2_6 = ShipWordHelper.GetL2dCvCalibrate(arg_2_0.skin.id, var_2_8)
			var_2_7 = ShipWordHelper.GetL2dSoundEffect(arg_2_0.skin.id, var_2_8)

	arg_2_0.l2dEventFlag = var_2_6 == -1
	var_2_6 = arg_2_0.l2dEventFlag and 0 or var_2_6
	arg_2_0.wordData = {
		maxfavor = 0,
		cvKey = var_2_2,
		cvPath = var_2_3,
		textContent = var_2_4,
		mainIndex = var_2_5,
		voiceCalibrate = var_2_6,
		se = var_2_7
	}

def var_0_0.Update(arg_3_0):
	local var_3_0 = arg_3_0.voice
	local var_3_1 = var_3_0.unlock_condition[1] < 0
	local var_3_2 = arg_3_0.wordData.textContent == None or arg_3_0.wordData.textContent == "None" or arg_3_0.wordData.textContent == ""

	if not arg_3_0.isLive2d:
		var_3_1 = var_3_1 or var_3_2
	else
		local var_3_3 = var_3_0.l2d_action.match("^" .. ShipWordHelper.WORD_TYPE_MAIN .. "_")

		var_3_1 = var_3_1 or var_3_2 and var_3_3

	setActive(arg_3_0._tf, not var_3_1)

	if not var_3_1:
		arg_3_0.UpdateCvBtn()
		arg_3_0.UpdateIcon()

def var_0_0.UpdateCvBtn(arg_4_0):
	local var_4_0 = arg_4_0.voice
	local var_4_1, var_4_2 = arg_4_0.shipGroup.VoiceReplayCodition(var_4_0)
	local var_4_3 = var_4_1 and var_4_0.voice_name or "???"

	arg_4_0.nameTxt.text = var_4_3

	local var_4_4 = ShipWordHelper.ExistDifferentWord(arg_4_0.skin.id, var_4_0.key, arg_4_0.wordData.mainIndex)

	setActive(arg_4_0.tagDiff, var_4_4)

	if not var_4_1:
		onButton(None, arg_4_0._tf, function()
			pg.TipsMgr.GetInstance().ShowTips(var_4_2), SFX_PANEL)

def var_0_0.UpdateIcon(arg_6_0):
	local var_6_0 = arg_6_0.voice.key == "unlock" and checkABExist("ui/skinunlockanim/star_level_unlock_anim_" .. arg_6_0.skin.id)

	setActive(arg_6_0.playIcon, var_6_0)

def var_0_0.L2dHasEvent(arg_7_0):
	return arg_7_0.l2dEventFlag

def var_0_0.isEx(arg_8_0):
	return False

def var_0_0.Destroy(arg_9_0):
	Destroy(arg_9_0._go)
	removeOnButton(arg_9_0._tf)

return var_0_0

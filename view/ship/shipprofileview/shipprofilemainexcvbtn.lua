local var_0_0 = class("ShipProfileMainExCvBtn", import(".ShipProfileCvBtn"))

function var_0_0.Init(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	arg_1_0.shipGroup = arg_1_1
	arg_1_0.isLive2d = arg_1_3
	arg_1_0.skin = arg_1_2

	local var_1_0 = "main" .. arg_1_4
	local var_1_1 = pg.character_voice[var_1_0]
	local var_1_2 = i18n("word_cv_key_main") .. arg_1_4 .. "Ex"

	if var_1_1 then
		arg_1_0.voice = Clone(var_1_1)
		arg_1_0.voice.voice_name = var_1_2
	else
		arg_1_0.voice = {
			profile_index = 5,
			spine_action = "normal",
			l2d_action = "main_3",
			key = var_1_0,
			voice_name = var_1_2,
			resource_key = "main_" .. arg_1_4,
			unlock_condition = {
				0,
				0
			}
		}
	end

	local var_1_3 = arg_1_0.voice

	arg_1_0.words = pg.ship_skin_words[arg_1_0.skin.id]

	local var_1_4
	local var_1_5
	local var_1_6
	local var_1_7
	local var_1_8
	local var_1_9
	local var_1_10 = var_1_3.key
	local var_1_11 = arg_1_0.shipGroup:GetMaxIntimacy()

	if string.find(var_1_10, ShipWordHelper.WORD_TYPE_MAIN) then
		local var_1_12 = string.gsub(var_1_10, ShipWordHelper.WORD_TYPE_MAIN, "")

		var_1_7 = tonumber(var_1_12)
		var_1_4, var_1_5, var_1_6 = ShipWordHelper.GetWordAndCV(arg_1_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_1_7, nil, var_1_11)

		if arg_1_0.isLive2d then
			var_1_8 = ShipWordHelper.GetL2dCvCalibrate(arg_1_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_1_7)
			var_1_9 = ShipWordHelper.GetL2dSoundEffect(arg_1_0.skin.id, ShipWordHelper.WORD_TYPE_MAIN, var_1_7)
		end
	else
		var_1_4, var_1_5, var_1_6 = ShipWordHelper.GetWordAndCV(arg_1_0.skin.id, var_1_10)

		if arg_1_0.isLive2d then
			var_1_8 = ShipWordHelper.GetL2dCvCalibrate(arg_1_0.skin.id, var_1_10)
			var_1_9 = ShipWordHelper.GetL2dSoundEffect(arg_1_0.skin.id, var_1_10)
		end
	end

	arg_1_0.wordData = {
		cvKey = var_1_4,
		cvPath = var_1_5,
		textContent = var_1_6,
		mainIndex = var_1_7,
		voiceCalibrate = var_1_8,
		se = var_1_9,
		maxfavor = var_1_11
	}
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.voice
	local var_2_1 = var_2_0.unlock_condition[1] < 0
	local var_2_2 = arg_2_0.wordData.textContent == nil or arg_2_0.wordData.textContent == "nil" or arg_2_0.wordData.textContent == ""

	if not arg_2_0.isLive2d then
		var_2_1 = var_2_1 or var_2_2
	else
		local var_2_3 = var_2_0.l2d_action:match("^" .. ShipWordHelper.WORD_TYPE_MAIN .. "_")

		var_2_1 = var_2_1 or var_2_2 and var_2_3
	end

	setActive(arg_2_0._tf, not var_2_1)

	if not var_2_1 then
		arg_2_0:UpdateCvBtn()
		arg_2_0:UpdateIcon()
	end
end

function var_0_0.UpdateCvBtn(arg_3_0)
	local var_3_0 = arg_3_0.voice
	local var_3_1 = arg_3_0.shipGroup
	local var_3_2 = true
	local var_3_3
	local var_3_4 = var_3_2 and var_3_0.voice_name or "???"

	arg_3_0.nameTxt.text = var_3_4

	local var_3_5 = arg_3_0.shipGroup:GetMaxIntimacy()
	local var_3_6 = ShipWordHelper.ExistDifferentMainExWord(arg_3_0.skin.id, var_3_0.key, arg_3_0.wordData.mainIndex, var_3_5)

	setActive(arg_3_0.tagDiff, var_3_6)
end

return var_0_0

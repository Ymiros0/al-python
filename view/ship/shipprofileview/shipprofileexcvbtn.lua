local var_0_0 = class("ShipProfileExCvBtn", import(".ShipProfileCvBtn"))

function var_0_0.Init(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5)
	var_0_0.super.Init(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)

	arg_1_0.favor = arg_1_5

	local var_1_0 = arg_1_4.key
	local var_1_1
	local var_1_2

	if string.find(var_1_0, ShipWordHelper.WORD_TYPE_MAIN) then
		local var_1_3 = string.gsub(var_1_0, ShipWordHelper.WORD_TYPE_MAIN, "")

		mainIndex = tonumber(var_1_3)
		var_1_1, var_1_2 = ShipWordHelper.ExistExCv(arg_1_2.id, ShipWordHelper.WORD_TYPE_MAIN, mainIndex, arg_1_5)
	else
		var_1_1, var_1_2 = ShipWordHelper.ExistExCv(arg_1_2.id, var_1_0, nil, arg_1_5)
	end

	if arg_1_0.wordData.cvPath and var_1_2 then
		arg_1_0.wordData.cvPath = arg_1_0.wordData.cvPath .. "_ex" .. var_1_2
	end

	arg_1_0.wordData.matchFavor = var_1_2
	arg_1_0.wordData.textContent = var_1_1
	arg_1_0.wordData.maxfavor = arg_1_5
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.voice.unlock_condition[1] < 0
	local var_2_1 = arg_2_0.wordData.textContent == nil or arg_2_0.wordData.textContent == "nil" or arg_2_0.wordData.textContent == ""

	var_2_0 = var_2_0 or var_2_1

	setActive(arg_2_0._tf, not var_2_0)

	if not var_2_0 then
		arg_2_0:UpdateCvBtn()
		arg_2_0:UpdateIcon()
	end
end

function var_0_0.UpdateCvBtn(arg_3_0)
	local var_3_0 = arg_3_0.voice
	local var_3_1, var_3_2 = arg_3_0.shipGroup:VoiceReplayCodition(var_3_0)
	local var_3_3 = var_3_1 and var_3_0.voice_name .. "Ex" or "???"

	arg_3_0.nameTxt.text = var_3_3

	local var_3_4 = ShipWordHelper.ExistDifferentExWord(arg_3_0.skin.id, var_3_0.key, arg_3_0.wordData.mainIndex, arg_3_0.favor)

	setActive(arg_3_0.tagDiff, var_3_4)

	if not var_3_1 then
		onButton(nil, arg_3_0._tf, function()
			pg.TipsMgr.GetInstance():ShowTips(var_3_2)
		end, SFX_PANEL)
	end
end

function var_0_0.isEx(arg_5_0)
	return arg_5_0.shipGroup:VoiceReplayCodition(arg_5_0.voice)
end

return var_0_0

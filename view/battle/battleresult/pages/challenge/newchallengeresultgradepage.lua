local var_0_0 = class("NewChallengeResultGradePage", import("..NewBattleResultGradePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.challenge = getProxy(ChallengeProxy):getUserChallengeInfo(arg_1_0.contextData.mode)
	arg_1_0.challengeExpire = getProxy(ChallengeProxy):userSeaonExpire(arg_1_0.contextData.mode)
end

function var_0_0.isTotalClear(arg_2_0)
	return arg_2_0.challenge:getMode() == ChallengeProxy.MODE_CASUAL and arg_2_0.challenge:IsFinish() or arg_2_0:isFail()
end

function var_0_0.isFail(arg_3_0)
	return arg_3_0.contextData.score < ys.Battle.BattleConst.BattleScore.S
end

function var_0_0.GetGetObjectives(arg_4_0)
	local var_4_0 = arg_4_0.contextData
	local var_4_1 = getProxy(ChallengeProxy):getUserChallengeInfo(var_4_0.mode)

	if var_4_1:getMode() == ChallengeProxy.MODE_INFINITE then
		return {}
	else
		local var_4_2 = {}
		local var_4_3 = i18n("challenge_combat_score", var_4_1:getLastScore())
		local var_4_4, var_4_5 = NewBattleResultUtil.ColorObjective(true)

		table.insert(var_4_2, {
			text = setColorStr(var_4_3, var_4_5),
			icon = var_4_4
		})

		local var_4_6 = i18n("challenge_current_score", var_4_1:getScore())

		table.insert(var_4_2, {
			text = setColorStr(var_4_6, var_4_5),
			icon = var_4_4
		})

		return var_4_2
	end
end

function var_0_0.UpdateChapterName(arg_5_0)
	local var_5_0 = arg_5_0.contextData

	if getProxy(ChallengeProxy):getUserChallengeInfo(var_5_0.mode) == ChallengeProxy.MODE_INFINITE then
		local var_5_1 = pg.expedition_data_template[var_5_0.stageId].name .. " - ROUND " .. getProxy(ChallengeProxy):getUserChallengeInfo(var_5_0.mode):getLevel()

		setText(arg_5_0.gradeChapterName, var_5_1)
	else
		var_0_0.super.UpdateChapterName(arg_5_0)
	end
end

function var_0_0.LoadChallengeRes(arg_6_0, arg_6_1)
	setActive(arg_6_0.bgTr:Find("ResultEffect/Tips"), false)
	ResourceMgr.Inst:getAssetAsync("BattleResultItems/Challenge", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_7_0)
		if arg_6_0.exited or IsNil(arg_7_0) then
			if arg_6_1 then
				arg_6_1()
			end

			return
		end

		arg_6_0:UpdateChallengeInfo(Object.Instantiate(arg_7_0, arg_6_0._tf).transform)

		if arg_6_1 then
			arg_6_1()
		end
	end), true, true)
end

function var_0_0.UpdateChallengeInfo(arg_8_0, arg_8_1)
	setText(arg_8_1:Find("expire"), arg_8_0.challengeExpire and i18n("challenge_expire_warn") or "")
	setText(findTF(arg_8_1, "continue_btn/text"), i18n("battle_result_continue_battle"))
	setText(findTF(arg_8_1, "quit_btn/text"), i18n("battle_result_quit_battle"))
	setText(findTF(arg_8_1, "share_btn/text"), i18n("battle_result_share_battle"))

	arg_8_0.continueBtn = findTF(arg_8_1, "continue_btn")
	arg_8_0.quitBtn = findTF(arg_8_1, "quit_btn")
	arg_8_0.shareBtn = findTF(arg_8_1, "share_btn")

	local var_8_0 = arg_8_0:isTotalClear()

	SetActive(arg_8_0.continueBtn, not var_8_0)
	SetActive(arg_8_0.quitBtn, not var_8_0)
	SetActive(arg_8_0.shareBtn, var_8_0)
end

function var_0_0.RegisterEvent(arg_9_0, arg_9_1)
	seriesAsync({
		function(arg_10_0)
			var_0_0.super.RegisterEvent(arg_9_0, arg_10_0)
		end,
		function(arg_11_0)
			removeOnButton(arg_9_0._tf)
			arg_9_0:LoadChallengeRes(arg_11_0)
		end,
		function(arg_12_0)
			arg_9_0:RegisterChallengeEvent(arg_9_1)
		end
	})
end

function var_0_0.RegisterChallengeEvent(arg_13_0, arg_13_1)
	if arg_13_0:isTotalClear() then
		onButton(arg_13_0, arg_13_0.shareBtn, function()
			arg_13_0:emit(NewBattleResultMediator.CHALLENGE_SHARE)
		end, SFX_CONFIRM)
		onButton(arg_13_0, arg_13_0._tf, arg_13_1, SFX_CONFIRM)
	else
		onButton(arg_13_0, arg_13_0.continueBtn, function()
			arg_13_0:OnContinue(arg_13_1)
		end, SFX_CONFIRM)
		onButton(arg_13_0, arg_13_0.quitBtn, function()
			arg_13_0:OnQuit(arg_13_1)
		end, SFX_CONFIRM)
	end
end

function var_0_0.OnContinue(arg_17_0, arg_17_1)
	if arg_17_0:isFail() then
		arg_17_1()
	else
		arg_17_0.contextData.goToNext = true

		arg_17_0:emit(NewBattleResultMediator.CHALLENGE_DEFEAT_SCENE, {
			callback = arg_17_1
		})
	end
end

function var_0_0.OnQuit(arg_18_0, arg_18_1)
	if arg_18_0:isFail() then
		arg_18_1()
	else
		arg_18_0:emit(NewBattleResultMediator.CHALLENGE_DEFEAT_SCENE, {
			callback = arg_18_1
		})
	end
end

return var_0_0

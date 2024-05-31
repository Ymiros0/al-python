local var_0_0 = class("NewWorldBossResultStatisticsPage", import("..NewBattleResultStatisticsPage"))

function var_0_0.UpdateGrade(arg_1_0)
	local var_1_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_1_0, arg_1_0.gradeTxt, false)
	setActive(arg_1_0.gradeIcon, false)
	setActive(arg_1_0.topPanel:Find("grade/label"), false)
end

function var_0_0.LoadBG(arg_2_0, arg_2_1)
	local var_2_0 = "CommonBg"

	ResourceMgr.Inst:getAssetAsync("BattleResultItems/" .. var_2_0, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
		if arg_2_0.exited or IsNil(arg_3_0) then
			if arg_2_1 then
				arg_2_1()
			end

			return
		end

		local var_3_0 = Object.Instantiate(arg_3_0, arg_2_0._tf)

		var_3_0.transform:SetAsFirstSibling()

		arg_2_0.effectTr = var_3_0.transform

		if arg_2_1 then
			arg_2_1()
		end
	end), true, true)
end

function var_0_0.UpdateOutput(arg_4_0, arg_4_1)
	setText(arg_4_1:Find("Text"), arg_4_0.contextData.statistics.specificDamage)
end

function var_0_0.UpdateCommanders(arg_5_0, arg_5_1)
	ResourceMgr.Inst:getAssetAsync("BattleResultItems/Worldboss", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_6_0)
		if arg_5_0.exited or IsNil(arg_6_0) then
			arg_5_1()

			return
		end

		local var_6_0 = Object.Instantiate(arg_6_0, arg_5_0.topPanel)

		arg_5_0:UpdateOutput(var_6_0.transform)
		arg_5_1()
	end), true, true)
end

function var_0_0.UpdatePlayer(arg_7_0)
	setActive(arg_7_0.topPanel:Find("exp"), false)
end

function var_0_0.RegisterEvent(arg_8_0, arg_8_1)
	var_0_0.super.RegisterEvent(arg_8_0, arg_8_1)
	triggerButton(arg_8_0.statisticsBtn)
	setActive(arg_8_0.statisticsBtn, false)
end

function var_0_0.UpdatePainting(arg_9_0, arg_9_1)
	arg_9_0:UpdatePaintingPosition()
	arg_9_0:UpdateMvpPainting(arg_9_1)
end

function var_0_0.UpdateChapterName(arg_10_0)
	arg_10_0.chapterName.text = ""

	setActive(arg_10_0.opBonus, false)
end

return var_0_0

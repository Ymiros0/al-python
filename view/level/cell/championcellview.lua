﻿local var_0_0 = import(".EnemyCellView")
local var_0_1 = import(".SpineCellView")
local var_0_2 = class("ChampionCellView", DecorateClass(var_0_0, var_0_1))

function var_0_2.Ctor(arg_1_0)
	var_0_0.Ctor(arg_1_0)
	var_0_1.Ctor(arg_1_0)

	arg_1_0.autoLoader = AutoLoader.New()
end

function var_0_2.InitChampionCellTransform(arg_2_0)
	var_0_1.InitCellTransform(arg_2_0)

	arg_2_0.tfEffectFound = arg_2_0.tf:Find("effect_found")
	arg_2_0.tfFighting = arg_2_0.tf:Find("fighting")

	setText(findTF(arg_2_0.tfFighting, "Text"), i18n("ui_word_levelui2_inevent"))

	arg_2_0.tfDamageCount = arg_2_0.tf:Find("damage_count")
	arg_2_0.tfBufficons = arg_2_0.tf:Find("random_buff_container")
end

function var_0_2.UpdateChampionCell(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = arg_3_2.trait ~= ChapterConst.TraitLurk and arg_3_2.flag == ChapterConst.CellFlagActive and not arg_3_1:existFleet(FleetType.Transport, arg_3_2.row, arg_3_2.column)
	local var_3_1 = arg_3_1:existEnemy(ChapterConst.SubjectChampion, arg_3_2.row, arg_3_2.column)

	setActive(arg_3_0.tfFighting, var_3_0 and var_3_1)
	setActive(arg_3_0.tfEffectFound, var_3_0 and arg_3_2.trait == ChapterConst.TraitVirgin)
	setActive(arg_3_0.tfDamageCount, var_3_0 and arg_3_2.data > 0)
	setActive(arg_3_0.tf:Find("huoqiubaozha"), false)

	if arg_3_2.trait == ChapterConst.TraitVirgin then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)
	end

	arg_3_0.tfShadow.localEulerAngles = Vector3(arg_3_1.theme.angle, 0, 0)

	if var_3_0 then
		var_0_0.RefreshEnemyTplIcons(arg_3_0, arg_3_2:getConfigTable(), arg_3_1)
	end

	arg_3_0:SetActive(var_3_0)
	existCall(arg_3_3)
end

function var_0_2.LoadSpine(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
	var_0_1.LoadSpine(arg_4_0, arg_4_1, arg_4_2, nil, function()
		existCall(arg_4_4)
		arg_4_0.LoadExtraEffects(arg_4_0, arg_4_3)
	end)
end

function var_0_2.LoadExtraEffects(arg_6_0, arg_6_1)
	if arg_6_1 and #arg_6_1 > 0 then
		local var_6_0 = "effect/" .. arg_6_1

		arg_6_0.autoLoader:LoadPrefab(var_6_0, arg_6_1, function(arg_7_0)
			arg_6_0._extraEffectList[var_6_0] = arg_7_0

			local var_7_0 = arg_7_0.transform.localScale

			setParent(arg_7_0, arg_6_0.tf, false)

			arg_7_0.transform.localScale = var_7_0

			arg_6_0:ResetCanvasOrder()
		end)
	end
end

function var_0_2.Clear(arg_8_0)
	var_0_1.ClearSpine(arg_8_0)
	var_0_0.Clear(arg_8_0)

	if arg_8_0.autoLoader then
		arg_8_0.autoLoader:ClearRequests()
	end
end

return var_0_2

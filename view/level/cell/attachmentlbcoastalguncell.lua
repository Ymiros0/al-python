local var_0_0 = class("AttachmentLBCoastalGunCell", import("view.level.cell.StaticCellView"))

var_0_0.StateLive = 1
var_0_0.StateDead = 2

function var_0_0.GetOrder(arg_1_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go) then
		arg_2_0:PrepareBase("landbase_" .. var_2_0.attachmentId)
	end

	local var_2_1 = arg_2_0.state

	if var_2_0.flag == ChapterConst.CellFlagActive and arg_2_0.state ~= var_0_0.StateLive then
		arg_2_0.state = var_0_0.StateLive
		arg_2_0.dead = nil

		arg_2_0:ClearLoader()

		local var_2_2 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_2, "land_based_template not exist: " .. var_2_0.attachmentId)
		arg_2_0:GetLoader():GetPrefab("leveluiview/Tpl_Enemy", "Tpl_Enemy", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition = Vector2(0, 10)

			arg_2_0:GetLoader():GetSprite("enemies/" .. var_2_2.prefab, "", findTF(arg_3_0, "icon"))
			setActive(findTF(arg_3_0, "lv"), false)
			setActive(findTF(arg_3_0, "titleContain/bg_boss"), false)
			setActive(findTF(arg_3_0, "damage_count"), false)
			setActive(findTF(arg_3_0, "fighting"), false)

			arg_2_0.enemy = arg_3_0

			arg_2_0:Update()
		end)
	elseif var_2_0.flag == ChapterConst.CellFlagDisabled and arg_2_0.state ~= var_0_0.StateDead then
		arg_2_0.state = var_0_0.StateDead

		if not IsNil(arg_2_0.enemy) then
			local var_2_3 = arg_2_0.enemy

			setActive(findTF(var_2_3, "lv"), true)
			setActive(findTF(var_2_3, "titleContain"), true)
			setActive(findTF(var_2_3, "damage_count"), true)
			setActive(findTF(var_2_3, "fighting"), true)
		end

		arg_2_0.enemy = nil

		arg_2_0:ClearLoader()

		local var_2_4 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_4, "land_based_template not exist: " .. var_2_0.attachmentId)
		arg_2_0:GetLoader():GetPrefab("leveluiview/Tpl_Dead", "Tpl_Dead", function(arg_4_0)
			setParent(arg_4_0, arg_2_0.tf)

			tf(arg_4_0).anchoredPosition = Vector2(0, 10)

			arg_2_0:GetLoader():GetSprite("enemies/" .. var_2_4.prefab .. "_d_blue", "", findTF(arg_4_0, "icon"))
			setActive(findTF(arg_4_0, "effect_not_open"), false)
			setActive(findTF(arg_4_0, "effect_open"), false)
			setActive(findTF(arg_4_0, "huoqiubaozha"), var_2_1 == var_0_0.StateLive)

			arg_2_0.dead = arg_4_0

			arg_2_0:ResetCanvasOrder()
			arg_2_0:Update()
		end)
	end

	if var_2_0.flag == ChapterConst.CellFlagActive and arg_2_0.enemy then
		setActive(findTF(arg_2_0.enemy, "effect_found"), var_2_0.trait == ChapterConst.TraitVirgin)

		if var_2_0.trait == ChapterConst.TraitVirgin then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)
		end
	end
end

function var_0_0.DestroyGO(arg_5_0)
	if not IsNil(arg_5_0.enemy) then
		local var_5_0 = arg_5_0.enemy

		setActive(findTF(var_5_0, "lv"), true)
		setActive(findTF(var_5_0, "titleContain"), true)
		setActive(findTF(var_5_0, "damage_count"), true)
		setActive(findTF(var_5_0, "fighting"), true)
	end

	var_0_0.super.DestroyGO(arg_5_0)
end

return var_0_0

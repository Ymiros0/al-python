local var_0_0 = class("AttachmentLBCoastalGunCell", import("view.level.cell.StaticCellView"))

var_0_0.StateLive = 1
var_0_0.StateDead = 2

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("landbase_" .. var_2_0.attachmentId)

	local var_2_1 = arg_2_0.state

	if var_2_0.flag == ChapterConst.CellFlagActive and arg_2_0.state != var_0_0.StateLive:
		arg_2_0.state = var_0_0.StateLive
		arg_2_0.dead = None

		arg_2_0.ClearLoader()

		local var_2_2 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_2, "land_based_template not exist. " .. var_2_0.attachmentId)
		arg_2_0.GetLoader().GetPrefab("leveluiview/Tpl_Enemy", "Tpl_Enemy", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition = Vector2(0, 10)

			arg_2_0.GetLoader().GetSprite("enemies/" .. var_2_2.prefab, "", findTF(arg_3_0, "icon"))
			setActive(findTF(arg_3_0, "lv"), False)
			setActive(findTF(arg_3_0, "titleContain/bg_boss"), False)
			setActive(findTF(arg_3_0, "damage_count"), False)
			setActive(findTF(arg_3_0, "fighting"), False)

			arg_2_0.enemy = arg_3_0

			arg_2_0.Update())
	elif var_2_0.flag == ChapterConst.CellFlagDisabled and arg_2_0.state != var_0_0.StateDead:
		arg_2_0.state = var_0_0.StateDead

		if not IsNil(arg_2_0.enemy):
			local var_2_3 = arg_2_0.enemy

			setActive(findTF(var_2_3, "lv"), True)
			setActive(findTF(var_2_3, "titleContain"), True)
			setActive(findTF(var_2_3, "damage_count"), True)
			setActive(findTF(var_2_3, "fighting"), True)

		arg_2_0.enemy = None

		arg_2_0.ClearLoader()

		local var_2_4 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_4, "land_based_template not exist. " .. var_2_0.attachmentId)
		arg_2_0.GetLoader().GetPrefab("leveluiview/Tpl_Dead", "Tpl_Dead", function(arg_4_0)
			setParent(arg_4_0, arg_2_0.tf)

			tf(arg_4_0).anchoredPosition = Vector2(0, 10)

			arg_2_0.GetLoader().GetSprite("enemies/" .. var_2_4.prefab .. "_d_blue", "", findTF(arg_4_0, "icon"))
			setActive(findTF(arg_4_0, "effect_not_open"), False)
			setActive(findTF(arg_4_0, "effect_open"), False)
			setActive(findTF(arg_4_0, "huoqiubaozha"), var_2_1 == var_0_0.StateLive)

			arg_2_0.dead = arg_4_0

			arg_2_0.ResetCanvasOrder()
			arg_2_0.Update())

	if var_2_0.flag == ChapterConst.CellFlagActive and arg_2_0.enemy:
		setActive(findTF(arg_2_0.enemy, "effect_found"), var_2_0.trait == ChapterConst.TraitVirgin)

		if var_2_0.trait == ChapterConst.TraitVirgin:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

def var_0_0.DestroyGO(arg_5_0):
	if not IsNil(arg_5_0.enemy):
		local var_5_0 = arg_5_0.enemy

		setActive(findTF(var_5_0, "lv"), True)
		setActive(findTF(var_5_0, "titleContain"), True)
		setActive(findTF(var_5_0, "damage_count"), True)
		setActive(findTF(var_5_0, "fighting"), True)

	var_0_0.super.DestroyGO(arg_5_0)

return var_0_0

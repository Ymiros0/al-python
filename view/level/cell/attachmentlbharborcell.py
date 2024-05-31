local var_0_0 = class("AttachmentLBHarborCell", import("view.level.cell.StaticCellView"))

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("box_gangkou")
		arg_2_0.GetLoader().GetPrefab("leveluiview/Tpl_Box", "Tpl_Box", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition3D = Vector3(0, 30, 0)

			arg_2_0.GetLoader().GetPrefab("boxprefab/gangkou", "gangkou", function(arg_4_0)
				tf(arg_4_0).SetParent(tf(arg_3_0).Find("icon"), False))

			arg_2_0.box = arg_3_0

			arg_2_0.Update())

	if arg_2_0.box:
		setActive(findTF(arg_2_0.box, "effect_found"), var_2_0.trait == ChapterConst.TraitVirgin)

		if var_2_0.trait == ChapterConst.TraitVirgin:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)

return var_0_0

local var_0_0 = class("EnemyDeadCellView", import("view.level.cell.StaticCellView"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.config = None
	arg_1_0.chapter = None
	arg_1_0._live2death = None

def var_0_0.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityLittle

def var_0_0.Update(arg_3_0):
	local var_3_0 = arg_3_0.info
	local var_3_1 = arg_3_0.config

	if IsNil(arg_3_0.go):
		arg_3_0.GetLoader().GetPrefab("leveluiview/Tpl_Dead", "Tpl_Dead", function(arg_4_0)
			arg_4_0.name = "enemy_" .. var_3_0.attachmentId
			arg_3_0.go = arg_4_0
			arg_3_0.tf = tf(arg_4_0)

			setParent(arg_4_0, arg_3_0.parent)
			arg_3_0.OverrideCanvas()
			arg_3_0.ResetCanvasOrder()
			setAnchoredPosition(arg_3_0.tf, Vector2.zero)

			if var_3_1.icon_type == 1:
				setAnchoredPosition(arg_3_0.tf, Vector2(0, 10))
				arg_3_0.GetLoader().LoadSprite("enemies/" .. var_3_1.icon .. "_d_blue", "", tf(arg_4_0).Find("icon"))

			setActive(findTF(arg_3_0.tf, "effect_not_open"), False)
			setActive(findTF(arg_3_0.tf, "effect_open"), False)
			setActive(findTF(arg_3_0.tf, "huoqiubaozha"), False)
			arg_3_0.Update(), "Main")

		return

	setActive(findTF(arg_3_0.tf, "huoqiubaozha"), arg_3_0._live2death)

def var_0_0.Clear(arg_5_0):
	arg_5_0._live2death = None
	arg_5_0.chapter = None

	var_0_0.super.Clear(arg_5_0)

return var_0_0

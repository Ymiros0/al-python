local var_0_0 = class("FushunEliteBeastChar", import(".FushunBeastChar"))

def var_0_0.Hurt(arg_1_0, arg_1_1):
	if arg_1_0.IsDeath() or arg_1_0.IsEscape():
		return

	arg_1_0.animatorEvent.SetEndEvent(None)
	arg_1_0.animatorEvent.SetEndEvent(function()
		arg_1_0.Unfreeze())
	arg_1_0.Freeze()
	arg_1_0.UpdateHp(arg_1_0.hp - arg_1_1)
	arg_1_0.animator.SetTrigger("damage")

def var_0_0.UpdateHp(arg_3_0, arg_3_1):
	var_0_0.super.UpdateHp(arg_3_0, arg_3_1)
	arg_3_0.animator.SetInteger("hp", arg_3_0.hp)

return var_0_0

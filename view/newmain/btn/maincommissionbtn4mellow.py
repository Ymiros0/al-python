local var_0_0 = class("MainCommissionBtn4Mellow", import(".MainCommissionBtn"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, 0)

	arg_1_0.animationPlayer = arg_1_1.GetComponent(typeof(Animation))

def var_0_0.OnClick(arg_2_0):
	arg_2_0.animationPlayer.Play("anim_newmain_extend_show")
	arg_2_0.emit(NewMainMediator.OPEN_COMMISION)

def var_0_0.ResetCommissionBtn(arg_3_0):
	arg_3_0.animationPlayer.Play("anim_newmain_extend_hide")

def var_0_0.Flush(arg_4_0, arg_4_1):
	local var_4_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(CommissionInfoMediator)

	if not arg_4_1 and not var_4_0:
		arg_4_0.ResetCommissionBtn()

return var_0_0

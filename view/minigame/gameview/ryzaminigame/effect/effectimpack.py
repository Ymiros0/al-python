local var_0_0 = class("EffectImpack", import("view.miniGame.gameView.RyzaMiniGame.effect.TargetEffect"))

def var_0_0.InitUI(arg_1_0, arg_1_1):
	arg_1_0._tf.Find("Lockon").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		setActive(arg_1_0._tf.Find("Lockon"), False)
		setActive(arg_1_0._tf.Find("impack"), True))

	local var_1_0 = arg_1_0._tf.Find("impack").GetComponent(typeof(DftAniEvent))

	var_1_0.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function()
		if arg_1_0.responder.CollideRyza(arg_1_0):
			arg_1_0.Calling("hit", {
				1,
				arg_1_0.realPos
			}, MoveRyza))
	var_1_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_1_0.Destroy())

return var_0_0

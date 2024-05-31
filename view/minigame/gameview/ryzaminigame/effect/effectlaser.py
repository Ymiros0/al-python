local var_0_0 = class("EffectLaser", import("view.miniGame.gameView.RyzaMiniGame.effect.TargetEffect"))

def var_0_0.GetBaseOrder(arg_1_0):
	if arg_1_0.mark == "N":
		return var_0_0.super.GetBaseOrder(arg_1_0)
	else
		return 500

def var_0_0.InitUI(arg_2_0, arg_2_1):
	arg_2_0.mark = arg_2_1.mark

	arg_2_0.UpdatePos(arg_2_0.pos)

	local var_2_0 = arg_2_0._tf.Find("scale/" .. arg_2_0.mark)

	setActive(var_2_0, True)
	var_2_0.Find("base").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_2_0.Destroy())

	if arg_2_0.responder.CollideRyza(arg_2_0):
		arg_2_0.Calling("hit", {
			1,
			arg_2_0.realPos
		}, MoveRyza)

def var_0_0.GetCollideRange(arg_4_0):
	local var_4_0

	switch(arg_4_0.mark, {
		def N:()
			var_4_0 = {
				{
					-0.5,
					0.5
				},
				{
					-25,
					-0.5
				}
			},
		def S:()
			var_4_0 = {
				{
					-0.5,
					0.5
				},
				{
					0.5,
					25
				}
			},
		def W:()
			var_4_0 = {
				{
					-25,
					-0.5
				},
				{
					-0.5,
					0.5
				}
			},
		def E:()
			var_4_0 = {
				{
					0.5,
					25
				},
				{
					-0.5,
					0.5
				}
			}
	})

	return {
		var_4_0
	}

return var_0_0

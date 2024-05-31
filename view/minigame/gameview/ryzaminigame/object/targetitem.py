local var_0_0 = class("TargetItem", import("view.miniGame.gameView.RyzaMiniGame.Reactor"))
local var_0_1 = {
	hp1 = "4",
	speed = "3",
	power = "2",
	spirit = "6",
	bomb = "1",
	hp2 = "5"
}

def var_0_0.InitUI(arg_1_0, arg_1_1):
	arg_1_0.type = arg_1_1.type

	arg_1_0._tf.Find("Image").GetComponent(typeof(Animator)).Play(var_0_1[arg_1_0.type])
	setActive(arg_1_0._tf.Find("Burn"), False)
	arg_1_0._tf.Find("Burn").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_1_0.Destroy(False))
	eachChild(arg_1_0._tf.Find("front"), function(arg_3_0)
		arg_3_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_3_0, False))
		setActive(arg_3_0, arg_3_0.name == arg_1_1.drop))

def var_0_0.InitRegister(arg_5_0, arg_5_1):
	arg_5_0.Register("move", function(arg_6_0)
		if isa(arg_6_0, MoveRyza):
			arg_6_0.AddItem(arg_5_0.type)
			arg_5_0.Destroy()
		else
			arg_5_0.Destroy(False), {
		{
			0,
			0
		}
	})
	arg_5_0.Register("burn", function()
		arg_5_0.DeregisterAll()
		setActive(arg_5_0._tf.Find("Image"), False)
		setActive(arg_5_0._tf.Find("Burn"), True), {
		{
			0,
			0
		}
	})

return var_0_0

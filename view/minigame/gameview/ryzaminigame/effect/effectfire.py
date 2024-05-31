local var_0_0 = class("EffectFire", import("view.miniGame.gameView.RyzaMiniGame.effect.TargetEffect"))

def var_0_0.GetBaseOrder(arg_1_0):
	return "floor"

local var_0_1 = {
	"S",
	"E",
	"N",
	"W"
}

def var_0_0.InitUI(arg_2_0, arg_2_1):
	arg_2_0.power = arg_2_1.power

	eachChild(arg_2_0._tf, function(arg_3_0)
		setActive(arg_3_0, arg_3_0.name == "C"))

	local var_2_0 = arg_2_0._tf.Find("C/Image").GetComponent(typeof(DftAniEvent))

	var_2_0.SetTriggerEvent(function()
		arg_2_0.triggerCount = defaultValue(arg_2_0.triggerCount, 0) + 1

		switch(arg_2_0.triggerCount, {
			function()
				local var_5_0, var_5_1, var_5_2 = arg_2_0.responder.GetCrossFire(arg_2_0.pos, arg_2_0.power)

				for iter_5_0, iter_5_1 in ipairs(var_5_0):
					local var_5_3 = arg_2_0._tf.Find(var_0_1[iter_5_0])

					for iter_5_2 = var_5_3.childCount + 1, iter_5_1:
						local var_5_4 = cloneTplTo(var_5_3.Find("7"), var_5_3, iter_5_2)

						if iter_5_0 < 3:
							var_5_4.SetAsLastSibling()

					local var_5_5 = var_5_3.childCount

					for iter_5_3 = 1, var_5_5:
						setActive(var_5_3.Find(iter_5_3), iter_5_3 <= iter_5_1)

					setActive(var_5_3, True)

				arg_2_0.Calling("burn", {}, var_5_1)

				arg_2_0.lenList = var_5_0

				arg_2_0.Register("move", function(arg_6_0)
					arg_2_0.Calling("burn", {}, arg_6_0), var_5_1)

				for iter_5_4, iter_5_5 in pairs(var_5_2):
					arg_2_0.Calling("block", {
						iter_5_5[2]
					}, iter_5_5[1]),
			function()
				arg_2_0.lenList = None

				arg_2_0.Deregister("move")
		}))
	var_2_0.SetEndEvent(function()
		arg_2_0.Destroy())
	pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-ryza-minigame-bomb")

def var_0_0.GetCollideRange(arg_9_0):
	if arg_9_0.lenList:
		return {
			{
				{
					-0.5 - arg_9_0.lenList[4],
					0.5 + arg_9_0.lenList[2]
				},
				{
					-0.5,
					0.5
				}
			},
			{
				{
					-0.5,
					0.5
				},
				{
					-0.5 - arg_9_0.lenList[3],
					0.5 + arg_9_0.lenList[1]
				}
			}
		}
	else
		return {}

return var_0_0

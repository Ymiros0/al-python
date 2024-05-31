local var_0_0 = class("MainSpineIcon", import(".MainBaseIcon"))

def var_0_0.Resume(arg_1_0):
	if arg_1_0.spineAnim:
		arg_1_0.spineAnim.Resume()

def var_0_0.Pause(arg_2_0):
	if not IsNil(arg_2_0.spineAnim):
		arg_2_0.spineAnim.Pause()

def var_0_0.Load(arg_3_0, arg_3_1):
	arg_3_0.loading = True

	PoolMgr.GetInstance().GetSpineChar(arg_3_1, True, function(arg_4_0)
		if arg_3_0.exited:
			return

		LeanTween.cancel(arg_4_0)

		arg_3_0.loading = False
		arg_3_0.shipModel = arg_4_0
		tf(arg_4_0).localScale = Vector3(0.75, 0.75, 1)

		local var_4_0 = pg.ship_spine_shift[arg_3_1]
		local var_4_1 = var_4_0 and var_4_0.mainui_shift[1] or 0
		local var_4_2 = -130 + (var_4_0 and var_4_0.mainui_shift[2] or 0)

		setParent(arg_4_0, arg_3_0._tf)

		tf(arg_4_0).localPosition = Vector3(var_4_1, var_4_2, 0)

		local var_4_3 = arg_4_0.GetComponent("SpineAnimUI")

		var_4_3.SetAction("normal", 0)

		arg_3_0.spineAnim = var_4_3

		onNextTick(function()
			if arg_3_0.spineAnim:
				arg_3_0.spineAnim.Resume()))

	arg_3_0.name = arg_3_1

def var_0_0.Unload(arg_6_0):
	if arg_6_0.name and arg_6_0.shipModel:
		PoolMgr.GetInstance().ReturnSpineChar(arg_6_0.name, arg_6_0.shipModel)

		arg_6_0.spineAnim = None
		arg_6_0.name = None

return var_0_0

local var_0_0 = class("ObjectBush", import("view.miniGame.gameView.RyzaMiniGame.object.TargetObject"))

def var_0_0.GetBaseOrder(arg_1_0):
	return 3

def var_0_0.CellPassability(arg_2_0):
	return True

def var_0_0.FirePassability(arg_3_0):
	return 0

def var_0_0.InitUI(arg_4_0, arg_4_1):
	arg_4_0.hideCount = 0

def var_0_0.InitRegister(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0._tf.Find("Image").GetComponent(typeof(Animator))

	arg_5_0.Register("burn", function()
		var_5_0.Play("New State")
		var_5_0.Play("Burn_A"), {
		{
			0,
			0
		}
	})
	arg_5_0.Register("move", function(arg_7_0)
		var_5_0.Play("New State")
		var_5_0.Play("Sway")
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-ryza-minigame-grass")
		arg_7_0.SetHide(True)

		if not isa(arg_7_0, MoveEnemy):
			arg_5_0.ChangeHide(True), {
		{
			0,
			0
		}
	})
	arg_5_0.Register("leave", function(arg_8_0)
		var_5_0.Play("New State")
		var_5_0.Play("Sway")
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-ryza-minigame-grass")
		arg_8_0.SetHide(False)

		if not isa(arg_8_0, MoveEnemy):
			arg_5_0.ChangeHide(False), {
		{
			0,
			0
		}
	})

def var_0_0.ChangeHide(arg_9_0, arg_9_1):
	arg_9_0.hideCount = arg_9_0.hideCount + (arg_9_1 and 1 or -1)
	GetOrAddComponent(arg_9_0._tf, typeof(CanvasGroup)).alpha = arg_9_0.hideCount > 0 and 0.5 or 1

return var_0_0

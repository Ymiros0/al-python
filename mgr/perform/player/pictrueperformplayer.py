local var_0_0 = class("StoryPerformPlayer", import(".BasePerformPlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.bgTF = arg_1_0.findTF("bg", arg_1_0._tf)
	arg_1_0.nameTF = arg_1_0.findTF("name", arg_1_0.bgTF)
	arg_1_0.imageCom = arg_1_0.findTF("picture", arg_1_0.bgTF).GetComponent(typeof(Image))

def var_0_0.Play(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.Show()

	if arg_2_0._anim:
		arg_2_0._anim.Play()

	if arg_2_3:
		setText(arg_2_0.nameTF, arg_2_3)

	local var_2_0 = arg_2_1.param[1] or ""
	local var_2_1 = arg_2_1.param[2] or 3

	setActive(arg_2_0.bgTF, False)
	ResourceMgr.Inst.getAssetAsync("educatepicture/" .. var_2_0, "", typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
		arg_2_0.imageCom.sprite = arg_3_0

		setActive(arg_2_0.bgTF, True)

		arg_2_0.timer = Timer.New(function()
			if arg_2_2:
				arg_2_2(), var_2_1)

		arg_2_0.timer.Start()), True, True)

def var_0_0.Clear(arg_5_0):
	arg_5_0.imageCom.sprite = None

	if arg_5_0.timer != None:
		arg_5_0.timer.Stop()

		arg_5_0.timer = None

	setText(arg_5_0.nameTF, "")
	arg_5_0.Hide()

return var_0_0

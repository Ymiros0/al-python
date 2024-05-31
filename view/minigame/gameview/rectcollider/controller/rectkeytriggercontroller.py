local var_0_0 = class("RectKeyTriggerController")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._keyInfo = arg_1_1

	if not arg_1_0.handle:
		arg_1_0.handle = UpdateBeat.CreateListener(arg_1_0.Update, arg_1_0)

	UpdateBeat.AddListener(arg_1_0.handle)

def var_0_0.Update(arg_2_0):
	if Application.isEditor:
		if Input.GetKeyDown(KeyCode.A):
			arg_2_0._keyInfo.setKeyPress(KeyCode.A, True)

		if Input.GetKeyDown(KeyCode.D):
			arg_2_0._keyInfo.setKeyPress(KeyCode.D, True)

		if Input.GetKeyUp(KeyCode.A):
			arg_2_0._keyInfo.setKeyPress(KeyCode.A, False)

		if Input.GetKeyUp(KeyCode.D):
			arg_2_0._keyInfo.setKeyPress(KeyCode.D, False)

		if Input.GetKeyDown(KeyCode.Space):
			arg_2_0._keyInfo.setKeyPress(KeyCode.Space, True)

		if Input.GetKeyUp(KeyCode.Space):
			arg_2_0._keyInfo.setKeyPress(KeyCode.Space, False)

		if Input.GetKeyDown(KeyCode.J):
			arg_2_0._keyInfo.setKeyPress(KeyCode.J, True)

		if Input.GetKeyUp(KeyCode.J):
			arg_2_0._keyInfo.setKeyPress(KeyCode.J, False)

def var_0_0.destroy(arg_3_0):
	if arg_3_0.handle:
		UpdateBeat.RemoveListener(arg_3_0.handle)

		arg_3_0.handle = None

return var_0_0

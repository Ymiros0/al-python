local var_0_0 = class("SettingsRedDotNode", import(".RedDotNode"))

var_0_0.CVChecked = False
var_0_0.CanUpdateCV = False

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.CheckCV()

def var_0_0.CheckCV(arg_2_0):
	if var_0_0.CVChecked:
		return

	var_0_0.CVChecked = True

	local var_2_0 = BundleWizard.Inst.GetGroupMgr("CV")

	var_2_0.CheckD()

	local var_2_1

	var_2_1 = Timer.New(function()
		if var_2_0.state == DownloadState.CheckToUpdate:
			var_0_0.CanUpdateCV = True

			arg_2_0.SetData(False)

		if var_2_0.state != DownloadState.None:
			var_2_1.Stop(), 0.5, -1)

	var_2_1.Start()

def var_0_0.SetData(arg_4_0, arg_4_1):
	if IsNil(arg_4_0.gameObject):
		return

	setActive(arg_4_0.gameObject, arg_4_1 or var_0_0.CanUpdateCV)

return var_0_0

local var_0_0 = class("SettingsRedDotNode", import(".RedDotNode"))

var_0_0.CVChecked = false
var_0_0.CanUpdateCV = false

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0:CheckCV()
end

function var_0_0.CheckCV(arg_2_0)
	if var_0_0.CVChecked then
		return
	end

	var_0_0.CVChecked = true

	local var_2_0 = BundleWizard.Inst:GetGroupMgr("CV")

	var_2_0:CheckD()

	local var_2_1

	var_2_1 = Timer.New(function()
		if var_2_0.state == DownloadState.CheckToUpdate then
			var_0_0.CanUpdateCV = true

			arg_2_0:SetData(false)
		end

		if var_2_0.state ~= DownloadState.None then
			var_2_1:Stop()
		end
	end, 0.5, -1)

	var_2_1:Start()
end

function var_0_0.SetData(arg_4_0, arg_4_1)
	if IsNil(arg_4_0.gameObject) then
		return
	end

	setActive(arg_4_0.gameObject, arg_4_1 or var_0_0.CanUpdateCV)
end

return var_0_0

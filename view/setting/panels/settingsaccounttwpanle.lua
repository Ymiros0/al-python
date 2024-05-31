local var_0_0 = class("SettingsAccountTwPanle", import(".SettingsBasePanel"))

function var_0_0.GetUIName(arg_1_0)
	return "SettingsAccountTW"
end

function var_0_0.InitTitle(arg_2_0)
	return
end

function var_0_0.OnInit(arg_3_0)
	arg_3_0.googleBtn = arg_3_0._tf:Find("page1/bind_google")
	arg_3_0.gamecenterBtn = arg_3_0._tf:Find("page1/bind_gamecenter")
	arg_3_0.faceBookBtn = arg_3_0._tf:Find("page1/bind_facebook")
	arg_3_0.phoneBtn = arg_3_0._tf:Find("page1/bind_phone")
	arg_3_0.appleBtn = arg_3_0._tf:Find("page1/bind_apple")

	setActive(arg_3_0.appleBtn, true)

	local var_3_0 = {
		arg_3_0.faceBookBtn,
		arg_3_0.googleBtn,
		arg_3_0.phoneBtn,
		arg_3_0.gamecenterBtn,
		arg_3_0.appleBtn
	}
	local var_3_1 = pg.SdkMgr.GetInstance()
	local var_3_2 = var_3_1:IsBindFaceBook()
	local var_3_3 = var_3_1:IsBindGoogle()
	local var_3_4 = var_3_1:IsBindPhone()
	local var_3_5 = var_3_1:IsBindGameCenter()
	local var_3_6 = var_3_1:IsBindApple()
	local var_3_7 = {
		var_3_2,
		var_3_3,
		var_3_4,
		var_3_5,
		var_3_6
	}

	for iter_3_0, iter_3_1 in ipairs(var_3_0) do
		local var_3_8 = var_3_7[iter_3_0]

		setActive(iter_3_1:Find("unbind"), not var_3_8)
		setActive(iter_3_1:Find("bind"), var_3_8)
		onButton(arg_3_0, iter_3_1, function()
			if not var_3_8 then
				var_3_1:BindSocial(iter_3_0)
			end
		end, SFX_PANEL)
	end
end

function var_0_0.OnUpdate(arg_5_0)
	if PLATFORM == PLATFORM_ANDROID then
		setActive(arg_5_0.googleBtn, true)
		setActive(arg_5_0.gamecenterBtn, false)
	else
		setActive(arg_5_0.googleBtn, true)
		setActive(arg_5_0.gamecenterBtn, false)
	end
end

return var_0_0

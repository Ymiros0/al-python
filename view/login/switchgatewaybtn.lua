local var_0_0 = class("SwitchGatewayBtn")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tr = arg_1_1
	arg_1_0._go = arg_1_1.gameObject

	setActive(arg_1_0._go, false)
end

function var_0_0.Flush(arg_2_0)
	local var_2_0 = getProxy(UserProxy):ShowGatewaySwitcher()

	setActive(arg_2_0._go, var_2_0)

	if var_2_0 then
		arg_2_0:RegistSwicher()
	end
end

function var_0_0.RegistSwicher(arg_3_0)
	local var_3_0 = getProxy(UserProxy)
	local var_3_1 = var_3_0:getLastLoginUser()

	onButton(nil, arg_3_0._go, function()
		pg.m02:sendNotification(GAME.SERVER_INTERCOMMECTION, {
			user = var_3_1,
			platform = var_3_0:GetReversePlatform()
		})
	end, SFX_PANEL)

	arg_3_0.isRegist = true
end

function var_0_0.Dispose(arg_5_0)
	if arg_5_0.isRegist then
		removeOnButton(arg_5_0._go)

		arg_5_0.isRegist = nil
	end
end

return var_0_0

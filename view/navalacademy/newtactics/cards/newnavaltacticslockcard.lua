local var_0_0 = class("NewNavalTacticsLockCard", import(".NewNavalTacticsBaseCard"))

function var_0_0.UnlockCnt2ShopId(arg_1_0, arg_1_1)
	return ({
		21,
		22
	})[arg_1_1 - 1]
end

function var_0_0.OnInit(arg_2_0)
	onButton(arg_2_0, arg_2_0._tf, function()
		local var_3_0 = getProxy(NavalAcademyProxy):getSkillClassNum()
		local var_3_1 = arg_2_0:UnlockCnt2ShopId(var_3_0)

		arg_2_0:emit(NewNavalTacticsLayer.ON_UNLOCK, var_3_1)
	end, SFX_PANEL)
end

return var_0_0

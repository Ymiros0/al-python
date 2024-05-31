local var_0_0 = class("NewNavalTacticsEmptyCard", import(".NewNavalTacticsBaseCard"))

function var_0_0.OnInit(arg_1_0)
	onButton(arg_1_0, arg_1_0._tf, function()
		arg_1_0:emit(NewNavalTacticsLayer.ON_ADD_STUDENT, arg_1_0.index)
	end, SFX_PANEL)
end

return var_0_0

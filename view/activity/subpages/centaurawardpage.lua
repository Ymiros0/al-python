local var_0_0 = class("CentaurAwardPage", import(".TemplatePage.SkinTemplatePage"))

function var_0_0.OnUpdateFlush(arg_1_0)
	var_0_0.super.OnUpdateFlush(arg_1_0)
	setText(arg_1_0.dayTF, arg_1_0.nday .. "/" .. #arg_1_0.taskGroup)
	eachChild(arg_1_0.items, function(arg_2_0)
		local var_2_0 = arg_1_0:findTF("get_btn", arg_2_0)
		local var_2_1 = arg_1_0:findTF("got_btn", arg_2_0)
		local var_2_2 = isActive(var_2_1)

		setButtonEnabled(var_2_1, false)
		setButtonEnabled(var_2_0, not var_2_2)

		if var_2_2 then
			setActive(var_2_0, true)
		end
	end)
end

return var_0_0

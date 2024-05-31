local var_0_0 = class("MainReplaceFoodSequence")

function var_0_0.Execute(arg_1_0, arg_1_1)
	local var_1_0 = getProxy(ActivityProxy):getActiveBannerByType(GAMEUI_BANNER_10)

	if var_1_0 then
		arg_1_0:Repalce(var_1_0, arg_1_1)
	else
		arg_1_0:Revert()
		arg_1_1()
	end
end

function var_0_0.Repalce(arg_2_0, arg_2_1, arg_2_2)
	if var_0_0.backUp then
		arg_2_2()

		return
	end

	local var_2_0

	var_2_0 = coroutine.wrap(function()
		onNextTick(var_2_0)
		coroutine.yield()

		local var_3_0 = pg.item_data_statistics[50004]

		var_0_0.backUp = {
			icon = var_3_0.icon,
			name = var_3_0.name,
			display = var_3_0.display
		}

		onNextTick(var_2_0)
		coroutine.yield()

		var_3_0.icon = "Props/" .. arg_2_1.pic

		local var_3_1 = string.split(arg_2_1.param, "|")

		var_3_0.name = var_3_1[1]
		var_3_0.display = var_3_1[2]
		pg.benefit_buff_template[1].icon = "Props/" .. arg_2_1.pic

		arg_2_2()
	end)

	var_2_0()
end

function var_0_0.Revert(arg_4_0)
	if var_0_0.backUp then
		local var_4_0 = pg.item_data_statistics[50004]

		var_4_0.icon = var_0_0.backUp.icon
		var_4_0.name = var_0_0.backUp.name
		var_4_0.display = var_0_0.backUp.display
		pg.benefit_buff_template[1].icon = var_0_0.backUp.icon
		var_0_0.backUp = nil
	end
end

return var_0_0

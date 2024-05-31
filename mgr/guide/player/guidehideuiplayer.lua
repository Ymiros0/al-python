local var_0_0 = class("GuideHideUIPlayer", import(".GuidePlayer"))

function var_0_0.OnExecution(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_1:GetHideNodes()
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0) do
		table.insert(var_1_1, function(arg_2_0)
			arg_1_0:SearchWithoutDelay(iter_1_1, function(arg_3_0)
				if not arg_3_0 then
					pg.NewGuideMgr.GetInstance():Stop()

					return
				end

				setActive(arg_3_0, not iter_1_1.hideFlag)
				arg_2_0()
			end)
		end)
	end

	parallelAsync(var_1_1, arg_1_2)
end

function var_0_0.RegisterEvent(arg_4_0, arg_4_1, arg_4_2)
	arg_4_2()
end

return var_0_0

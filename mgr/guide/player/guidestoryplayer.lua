local var_0_0 = class("GuideStoryPlayer", import(".GuidePlayer"))

function var_0_0.OnExecution(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_1:GetStories()
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0) do
		table.insert(var_1_1, function(arg_2_0)
			pg.NewStoryMgr.GetInstance():Play(iter_1_1, arg_2_0, true)
		end)
	end

	table.insert(var_1_1, function(arg_3_0)
		pg.m02:sendNotification(GAME.START_GUIDE)
		arg_3_0()
	end)
	seriesAsync(var_1_1, arg_1_2)
end

return var_0_0

pg = pg or {}
pg.ConfigTablePreloadMgr = singletonClass("ConfigTablePreloadMgr")

function pg.ConfigTablePreloadMgr.Init(arg_1_0, arg_1_1)
	local var_1_0 = {
		"furniture_data_template",
		"ship_data_statistics",
		"task_data_template",
		"ship_skin_template_column_time"
	}
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0) do
		table.insert(var_1_1, function(arg_2_0)
			local var_2_0 = pg[iter_1_1]

			onNextTick(arg_2_0)
		end)
	end

	seriesAsync(var_1_1, arg_1_1)
end

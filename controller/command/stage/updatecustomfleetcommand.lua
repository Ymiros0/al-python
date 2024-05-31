local var_0_0 = class("UpdateCustomFleetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().chapterId
	local var_1_1 = getProxy(BayProxy):getRawData()
	local var_1_2 = getProxy(ChapterProxy):getChapterById(var_1_0)
	local var_1_3 = var_1_2:getConfig("formation")
	local var_1_4 = var_1_2:getEliteFleetList()
	local var_1_5 = var_1_2:getEliteFleetCommanders()
	local var_1_6 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_4) do
		local var_1_7 = {}
		local var_1_8 = {}
		local var_1_9 = {}

		for iter_1_2, iter_1_3 in ipairs(iter_1_1) do
			var_1_8[#var_1_8 + 1] = iter_1_3
		end

		local var_1_10 = var_1_5[iter_1_0]

		for iter_1_4, iter_1_5 in pairs(var_1_10) do
			table.insert(var_1_9, {
				pos = iter_1_4,
				id = iter_1_5
			})
		end

		var_1_7.map_id = var_1_3
		var_1_7.main_id = var_1_8
		var_1_7.commanders = var_1_9
		var_1_6[#var_1_6 + 1] = var_1_7
	end

	local var_1_11 = var_1_2:getSupportFleet()
	local var_1_12 = var_1_2:getConfig("map")
	local var_1_13 = {}
	local var_1_14 = {}

	for iter_1_6, iter_1_7 in ipairs(var_1_11) do
		var_1_14[#var_1_14 + 1] = iter_1_7
	end

	var_1_13.map_id = var_1_12
	var_1_13.main_id = var_1_14
	var_1_13.commanders = {}
	var_1_6[#var_1_6 + 1] = var_1_13

	pg.ConnectionMgr.GetInstance():Send(13107, {
		id = var_1_3,
		elite_fleet_list = var_1_6
	}, 13108, function(arg_2_0)
		if arg_2_0.result == 0 then
			-- block empty
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("update_custom_fleet", arg_2_0.result))
		end
	end)
end

return var_0_0

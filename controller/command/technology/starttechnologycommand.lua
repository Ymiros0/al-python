local var_0_0 = class("StartTechnologyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.pool_id
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3:getTechnologyById(var_1_1)

	if not var_1_4 then
		return
	end

	if tobool(var_1_3:getActivateTechnology()) then
		return
	end

	local var_1_5, var_1_6 = var_1_4:hasResToStart()

	if not var_1_5 then
		pg.TipsMgr.GetInstance():ShowTips(var_1_6)

		return
	end

	pg.ConnectionMgr.GetInstance():Send(63001, {
		tech_id = var_1_1,
		refresh_id = var_1_2
	}, 63002, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = var_1_4:getConfig("consume")

			for iter_2_0, iter_2_1 in ipairs(var_2_0) do
				arg_1_0:sendNotification(GAME.CONSUME_ITEM, Drop.Create(iter_2_1))
			end

			var_1_4:start(arg_2_0.time)
			var_1_3:updateTechnology(var_1_4)
			arg_1_0:sendNotification(GAME.START_TECHNOLOGY_DONE, {
				technologyId = var_1_4.id
			})
			pg.TipsMgr.GetInstance():ShowTips(i18n("technology_start_up"))
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("technology_start_erro") .. arg_2_0.result)
		end
	end)
end

return var_0_0

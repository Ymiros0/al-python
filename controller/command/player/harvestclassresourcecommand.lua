local var_0_0 = class("HarvestClassResourceCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(NavalAcademyProxy):GetClassVO()
	local var_1_2 = var_1_1:GetCanGetResCnt()

	if var_1_2 <= 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("player_harvestResource_error_fullBag"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(22009, {
		type = 0
	}, 22010, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = var_1_1:GetTarget()
			local var_2_1 = var_1_1:GetResourceType()
			local var_2_2 = Drop.New({
				type = DROP_TYPE_ITEM,
				id = var_2_1,
				count = var_1_2
			})

			arg_1_0:sendNotification(GAME.ADD_ITEM, var_2_2)

			local var_2_3 = var_1_2 * var_2_0
			local var_2_4 = getProxy(PlayerProxy):getData()

			var_2_4:consume({
				[id2res(PlayerConst.ResClassField)] = var_2_3
			})
			getProxy(PlayerProxy):updatePlayer(var_2_4)

			local var_2_5 = var_2_2:getConfig("name")

			pg.TipsMgr.GetInstance():ShowTips(i18n("commission_get_award", var_2_5, var_1_2))
			getProxy(NavalAcademyProxy):getCourse():SetProficiency(arg_2_0.exp_in_well)
			arg_1_0:sendNotification(GAME.HARVEST_CLASS_RES_DONE, {
				award = var_2_2,
				value = var_1_2
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0

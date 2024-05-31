local var_0_0 = class("ApartmentReplaceFurnitureCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1.body
	local var_1_1 = var_1_0.shipGroupId
	local var_1_2 = var_1_0.furnitures
	local var_1_3 = _.map(var_1_2, function(arg_2_0)
		return {
			slot_id = arg_2_0.slotId,
			furniture_id = arg_2_0.furnitureId
		}
	end)

	pg.ConnectionMgr.GetInstance():Send(28007, {
		ship_group = var_1_1,
		furnitures = var_1_3
	}, 28008, function(arg_3_0)
		if arg_3_0.result ~= 0 then
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_3_0.result))
			arg_1_0:sendNotification(GAME.APARTMENT_REPLACE_FURNITURE_ERROR)

			return
		end

		local var_3_0 = getProxy(ApartmentProxy):getApartment(var_1_1)

		var_3_0:ReplaceFurnitures(var_1_2)
		getProxy(ApartmentProxy):updateApartment(var_3_0)
		pg.TipsMgr.GetInstance():ShowTips(i18n("dorm3d_replace_furniture_sucess"))
		arg_1_0:sendNotification(GAME.APARTMENT_REPLACE_FURNITURE_DONE)
	end)
end

return var_0_0

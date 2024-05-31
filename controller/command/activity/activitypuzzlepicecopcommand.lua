﻿local var_0_0 = class("ActivityPuzzlePicecOPCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id or 0
	local var_1_2 = var_1_0.cmd
	local var_1_3 = var_1_0.actId
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(ActivityProxy)
	local var_1_6 = getProxy(ActivityProxy):getActivityById(var_1_3)

	if not var_1_6 or var_1_6:isEnd() then
		return
	end

	local var_1_7 = pg.activity_event_picturepuzzle[var_1_3]

	if not var_1_7 then
		return
	end

	if var_1_2 == 1 then
		if #var_1_6.data2_list > #var_1_7.pickup_picturepuzzle + #var_1_7.drop_picturepuzzle then
			return
		end

		if var_1_6.data1 ~= 0 then
			return
		end

		arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = var_1_3
		})

		return
	elseif var_1_2 == 2 then
		if not var_1_0.isPickUp and not table.contains(var_1_6.data1_list, var_1_1) then
			return
		end

		if table.contains(var_1_6.data2_list, var_1_1) then
			return
		end
	elseif var_1_2 == 3 then
		if table.contains(var_1_6.data3_list, var_1_1) then
			return
		end

		if pg.TimeMgr.GetInstance():GetServerTime() < var_1_6.data2 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("bulin_tip_other2"))

			return
		end
	elseif var_1_2 == 4 then
		if var_1_6.data1 ~= 1 then
			return
		end

		arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 4,
			activity_id = var_1_3
		})

		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		arg2 = 0,
		activity_id = var_1_3,
		cmd = var_1_2,
		arg1 = var_1_1,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_6 = getProxy(ActivityProxy):getActivityById(var_1_3)

			if var_1_2 == 1 then
				var_1_6.data1 = 1
			elseif var_1_2 == 2 then
				table.insert(var_1_6.data2_list, var_1_1)
			elseif var_1_2 == 3 then
				table.insert(var_1_6.data3_list, var_1_1)

				var_1_6.data2 = pg.TimeMgr.GetInstance():GetServerTime() + var_1_7.cd
			elseif var_1_2 == 4 then
				var_1_6.data1 = 2
			end

			var_1_5:updateActivity(var_1_6)

			if var_1_4 then
				var_1_4()
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0

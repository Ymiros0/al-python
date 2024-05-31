﻿local var_0_0 = class("MainCheckShipNumSequence")

function var_0_0.Execute(arg_1_0, arg_1_1)
	local function var_1_0(arg_2_0)
		if arg_1_0:Check(arg_2_0) then
			arg_1_1()
		end
	end

	pg.m02:sendNotification(GAME.GET_SHIP_CNT, {
		callback = var_1_0
	})
end

function var_0_0.Check(arg_3_0, arg_3_1)
	local var_3_0 = getProxy(BayProxy):getRawShipCount()
	local var_3_1 = arg_3_1 <= var_3_0

	if not var_3_1 then
		originalPrint(arg_3_1, var_3_0)
		arg_3_0:ShowTip()
	end

	return var_3_1
end

function var_0_0.ShowTip(arg_4_0)
	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		modal = true,
		hideNo = true,
		hideClose = true,
		content = i18n("dockyard_data_loss_detected"),
		onYes = function()
			pg.m02:sendNotification(GAME.LOGOUT, {
				code = 0
			})
		end
	})
end

return var_0_0

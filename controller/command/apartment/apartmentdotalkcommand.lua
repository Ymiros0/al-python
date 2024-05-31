﻿local var_0_0 = class("ApartmentDoTalkCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.talkId
	local var_1_2 = var_1_0.callback
	local var_1_3 = pg.dorm3d_dialogue_group[var_1_1].char_id
	local var_1_4 = getProxy(ApartmentProxy)
	local var_1_5 = var_1_4:getApartment(var_1_3)

	if var_1_5.talkDic[var_1_1] then
		existCall(var_1_2)
		arg_1_0:sendNotification(GAME.APARTMENT_DO_TALK_DONE, {
			talkId = var_1_1
		})

		return
	end

	pg.ConnectionMgr.GetInstance():Send(28015, {
		dialog_id = var_1_1
	}, 28016, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_5.talkDic[var_1_1] = true

			var_1_4:updateApartment(var_1_5)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)

			existCall(var_1_2, var_2_0)
			arg_1_0:sendNotification(GAME.APARTMENT_DO_TALK_DONE, {
				talkId = var_1_1,
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0

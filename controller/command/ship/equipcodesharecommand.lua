local var_0_0 = class("EquipCodeShareCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.code

	pg.ConnectionMgr.GetInstance():Send(17603, {
		shipgroup = var_1_1,
		eqcode = var_1_2
	}, 17604, function(arg_2_0)
		if arg_2_0.result == 0 then
			pg.m02:sendNotification(GAME.EQUIP_CODE_SHARE_DONE)
			pg.TipsMgr.GetInstance():ShowTips(i18n("equipcode_share_success"))
		elseif arg_2_0.result == 7 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("equipcode_share_errorcode7"))
		elseif arg_2_0.result == 44 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("equipcode_share_errorcode44"))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0

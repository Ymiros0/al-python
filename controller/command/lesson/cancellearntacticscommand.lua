﻿local var_0_0 = class("CancelLearnTacticsCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.type
	local var_1_3 = getProxy(NavalAcademyProxy)

	if not var_1_3:ExistStudent(var_1_1) then
		return
	end

	local var_1_4 = var_1_3:getStudentById(var_1_1)
	local var_1_5 = var_1_0.callback
	local var_1_6 = var_1_0.onConfirm

	if not var_1_4 then
		existCall(var_1_5)

		return
	end

	local var_1_7 = getProxy(BayProxy)
	local var_1_8 = var_1_7:getShipById(var_1_4.shipId)
	local var_1_9 = var_1_4:getSkillId(var_1_8)

	if not var_1_8.skills[var_1_9] then
		pg.TipsMgr.GetInstance():ShowTips(i18n("tactics_noskill_erro"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(22203, {
		room_id = var_1_1,
		type = var_1_2
	}, 22204, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = Clone(var_1_8.skills[var_1_9])

			var_1_8:addSkillExp(var_2_0.id, arg_2_0.exp)
			var_1_7:updateShip(var_1_8)
			var_1_3:deleteStudent(var_1_1)
			var_1_3:SaveRecentShip(var_1_4.shipId)
			arg_1_0:sendNotification(GAME.CANCEL_LEARN_TACTICS_DONE, {
				id = var_1_1,
				shipId = var_1_4.shipId,
				totalExp = arg_2_0.exp,
				oldSkill = var_2_0,
				newSkill = var_1_8.skills[var_1_9],
				onConfirm = var_1_6,
				newShipVO = var_1_8
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("lesson_endToLearn", arg_2_0.result))
		end

		if var_1_5 ~= nil then
			var_1_5()
		end
	end)
end

return var_0_0

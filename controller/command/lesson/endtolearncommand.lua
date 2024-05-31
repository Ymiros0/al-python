﻿local var_0_0 = class("EndToLearnCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	pg.ConnectionMgr.GetInstance():Send(22004, {
		type = 0
	}, 22005, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(NavalAcademyProxy)
			local var_2_1 = getProxy(BayProxy)
			local var_2_2 = var_2_0:getCourse()
			local var_2_3 = var_2_2:getConfig("name_show")
			local var_2_4 = var_2_2.proficiency
			local var_2_5 = math.max(var_2_4 - arg_2_0.proficiency, 0)

			var_2_2.proficiency = var_2_5

			local var_2_6 = {}
			local var_2_7 = {}

			_.each(arg_2_0.awards, function(arg_3_0)
				var_2_6[arg_3_0.ship_id] = arg_3_0.exp
				var_2_7[arg_3_0.ship_id] = arg_3_0.energy
			end)

			local var_2_8 = _.map(var_2_2.students, function(arg_4_0)
				return var_2_1:getShipById(arg_4_0)
			end)
			local var_2_9 = Clone(var_2_8)

			_.each(var_2_9, function(arg_5_0)
				arg_5_0:addExp(var_2_6[arg_5_0.id] or 0)
				arg_5_0:cosumeEnergy(var_2_7[arg_5_0.id] or 0)
				var_2_1:updateShip(arg_5_0)
			end)

			var_2_2.students = {}
			var_2_2.timestamp = 0

			var_2_0:setCourse(var_2_2)
			arg_1_0:sendNotification(GAME.CLASS_STOP_COURSE_DONE, {
				title = var_2_3,
				oldProficiency = var_2_4,
				newProficiency = var_2_5,
				oldStudents = var_2_8,
				newStudents = var_2_9
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("lesson_endToLearn", arg_2_0.result))
		end
	end)
end

return var_0_0

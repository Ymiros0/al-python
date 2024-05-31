local var_0_0 = class("StartLearnTacticsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.lessonId
	local var_1_3 = var_1_0.skillPos
	local var_1_4 = var_1_0.roomId
	local var_1_5 = getProxy(BagProxy)
	local var_1_6 = var_1_5.getItemById(var_1_2)

	if not var_1_6 or var_1_6.count == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("buyProp_noResource_error", var_1_6.getConfig("name")))

		return

	pg.ConnectionMgr.GetInstance().Send(22201, {
		room_id = var_1_4,
		ship_id = var_1_1,
		skill_pos = var_1_3,
		item_id = var_1_2
	}, 22202, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(NavalAcademyProxy)
			local var_2_1 = Item.getConfigData(var_1_2).usage_arg[1]
			local var_2_2 = Student.New(arg_2_0.class_info)

			var_2_2.setTime(var_2_1)
			var_2_2.setLesson(var_1_2)
			var_2_0.addStudent(var_2_2)
			var_1_5.removeItemById(var_1_6.id, 1)
			arg_1_0.sendNotification(GAME.START_TO_LEARN_TACTICS_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("lesson_endToLearn", arg_2_0.result)))

return var_0_0

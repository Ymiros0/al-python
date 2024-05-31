local var_0_0 = class("ReturnerActivity", import(".Activity"))

var_0_0.TYPE_INVITER = 1
var_0_0.TYPE_RETURNER = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.roleType = arg_1_0.data1

def var_0_0.IsPush(arg_2_0):
	return arg_2_0.data2_list[1] == 1

def var_0_0.IsInviter(arg_3_0):
	return arg_3_0.roleType == var_0_0.TYPE_INVITER

def var_0_0.IsReturner(arg_4_0):
	return arg_4_0.roleType == var_0_0.TYPE_RETURNER

def var_0_0.ShouldAcceptTasks(arg_5_0):
	if arg_5_0.IsInviter():
		return arg_5_0.ShouldAcceptTasksIfInviter()
	elif arg_5_0.IsReturner():
		return arg_5_0.ShouldAcceptTasksIfReturner()

def var_0_0.ShouldAcceptTasksIfInviter(arg_6_0):
	if arg_6_0.IsPush():
		local var_6_0 = arg_6_0.getDataConfigTable("tasklist")
		local var_6_1 = arg_6_0.getDayIndex()
		local var_6_2 = getProxy(TaskProxy)
		local var_6_3 = 0

		for iter_6_0 = #var_6_0, 1, -1:
			if arg_6_0.GetTask(var_6_0[iter_6_0]):
				var_6_3 = iter_6_0

				break

		local var_6_4 = arg_6_0.GetTask(var_6_0[var_6_3])

		if (not var_6_4 or var_6_4.isReceive()) and var_6_3 < var_6_1 and (var_6_3 != #var_6_0 or not var_6_4 or not var_6_4.isReceive()):
			return True

	return False

def var_0_0.GetTask(arg_7_0, arg_7_1):
	local var_7_0 = getProxy(TaskProxy)

	return var_7_0.getTaskById(arg_7_1) or var_7_0.getFinishTaskById(arg_7_1)

def var_0_0.ShouldAcceptTasksIfReturner(arg_8_0):
	local var_8_0 = arg_8_0.data4

	if arg_8_0.data2 == 0:
		return False

	if var_8_0 == 0:
		return True

	local var_8_1 = arg_8_0.getDataConfigTable("task_list")
	local var_8_2 = getProxy(TaskProxy)
	local var_8_3 = _.all(var_8_1[var_8_0], function(arg_9_0)
		return var_8_2.getFinishTaskById(arg_9_0) != None)
	local var_8_4 = _.all(var_8_1[var_8_0], function(arg_10_0)
		return var_8_2.getTaskById(arg_10_0) == None and var_8_2.getFinishTaskById(arg_10_0) == None)
	local var_8_5 = var_8_0 == #var_8_1

	local function var_8_6()
		local var_11_0 = pg.TimeMgr.GetInstance().GetServerTime()

		return pg.TimeMgr.GetInstance().DiffDay(arg_8_0.getStartTime(), var_11_0) + 1 > var_8_0

	return var_8_4 or var_8_3 and not var_8_5 and var_8_6()

def var_0_0.getDataConfigTable(arg_12_0, arg_12_1):
	if arg_12_0.IsInviter():
		return pg.activity_template_headhunting[arg_12_0.id][arg_12_1]
	elif arg_12_0.IsReturner():
		return pg.activity_template_returnner[arg_12_0.id][arg_12_1]

return var_0_0

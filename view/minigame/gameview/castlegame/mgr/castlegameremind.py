local var_0_0 = class("CastleGameRemind")

var_0_0.remind_type_1 = "remind_type_1"
var_0_0.remind_type_2 = "remind_type_2"
var_0_0.remind_type_3 = "remind_type_3"
var_0_0.remind_type_4 = "remind_type_4"

local var_0_1 = {
	{
		tpl = "remind_1",
		type = var_0_0.remind_type_1
	},
	{
		tpl = "remind_2",
		type = var_0_0.remind_type_2
	},
	{
		tpl = "remind_3",
		type = var_0_0.remind_type_3
	},
	{
		tpl = "remind_4",
		type = var_0_0.remind_type_4
	}
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tplContent = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.remindPool = {}
	arg_1_0.reminds = {}

def var_0_0.setContent(arg_2_0, arg_2_1):
	if not arg_2_1:
		print("地板的容器不能为None")

		return

	arg_2_0._content = arg_2_1

def var_0_0.start(arg_3_0):
	for iter_3_0 = #arg_3_0.reminds, 1, -1:
		local var_3_0 = table.remove(arg_3_0.reminds, iter_3_0)

		arg_3_0.returnRemind(var_3_0)

def var_0_0.step(arg_4_0):
	for iter_4_0 = #arg_4_0.reminds, 1, -1:
		local var_4_0 = arg_4_0.reminds[iter_4_0]

		if var_4_0.removeTime and var_4_0.removeTime > 0:
			var_4_0.removeTime = var_4_0.removeTime - CastleGameVo.deltaTime

			if var_4_0.removeTime <= 0:
				var_4_0.removeTime = None

				local var_4_1 = table.remove(arg_4_0.reminds, iter_4_0)

				arg_4_0.returnRemind(var_4_1)

def var_0_0.addRemind(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = arg_5_0.getRemindByType(arg_5_3)

	var_5_0.removeTime = CastleGameVo.item_ready_time

	local var_5_1 = CastleGameVo.GetRotationPosByWH(arg_5_1, arg_5_2)

	setActive(var_5_0.tf, False)
	setActive(var_5_0.tf, True)

	var_5_0.tf.anchoredPosition = var_5_1

	table.insert(arg_5_0.reminds, var_5_0)

def var_0_0.getRemindByType(arg_6_0, arg_6_1):
	local var_6_0

	for iter_6_0 = 1, #arg_6_0.remindPool:
		if arg_6_0.remindPool[iter_6_0].type == arg_6_1:
			var_6_0 = table.remove(arg_6_0.remindPool, iter_6_0)

			return var_6_0

	if not var_6_0:
		for iter_6_1 = 1, #var_0_1:
			if arg_6_1 == var_0_1[iter_6_1].type:
				local var_6_1 = tf(instantiate(findTF(arg_6_0._tplContent, var_0_1[iter_6_1].tpl)))

				setParent(var_6_1, arg_6_0._content)

				local var_6_2 = GetComponent(findTF(var_6_1, "zPos"), typeof(DftAniEvent))

				return {
					tf = var_6_1,
					dft = var_6_2,
					type = arg_6_1
				}

def var_0_0.returnRemind(arg_7_0, arg_7_1):
	setActive(arg_7_1.tf, False)

	arg_7_1.removeTime = None

	table.insert(arg_7_0.remindPool, arg_7_1)

def var_0_0.clear(arg_8_0):
	return

return var_0_0

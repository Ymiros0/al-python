local var_0_0 = class("Fushun3SceneController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._sceneTf = arg_1_2
	arg_1_0._followTf = arg_1_3
	arg_1_0._sceneBackTf = arg_1_1
	arg_1_0._backGrouds = {}

	for iter_1_0 = 1, #Fushun3GameConst.backgroud_data:
		local var_1_0 = Fushun3GameConst.backgroud_data[iter_1_0]
		local var_1_1 = findTF(arg_1_0._sceneBackTf, var_1_0.name)

		table.insert(arg_1_0._backGrouds, {
			tf = var_1_1,
			data = var_1_0
		})

def var_0_0.start(arg_2_0):
	arg_2_0._sceneTf.anchoredPosition = Vector2(0, 0)

	for iter_2_0 = 1, #arg_2_0._backGrouds:
		arg_2_0._backGrouds[iter_2_0].tf.anchoredPosition = Vector2(0, 0)

def var_0_0.step(arg_3_0):
	local var_3_0 = arg_3_0._sceneTf.anchoredPosition
	local var_3_1 = arg_3_0._followTf.anchoredPosition.x + var_3_0.x
	local var_3_2 = 0

	if var_3_1 > 350:
		var_3_2 = (var_3_1 - Fushun3GameConst.follow_bound_mid) * Fushun3GameConst.follow_spring * -1
	elif var_3_1 < 250:
		var_3_2 = math.abs(var_3_1 - Fushun3GameConst.follow_bound_mid) * Fushun3GameConst.follow_spring

	if var_3_2 != 0:
		if math.abs(var_3_2) < 1:
			var_3_2 = 1 * math.sign(var_3_2)

		var_3_0.x = var_3_0.x + var_3_2
		arg_3_0._sceneTf.anchoredPosition = var_3_0

		for iter_3_0 = 1, #arg_3_0._backGrouds:
			local var_3_3 = arg_3_0._backGrouds[iter_3_0]
			local var_3_4 = var_3_3.tf.anchoredPosition

			var_3_4.x = var_3_0.x * var_3_3.data.rate
			var_3_4.y = var_3_0.y * var_3_3.data.rate
			var_3_3.tf.anchoredPosition = var_3_4

def var_0_0.dispose(arg_4_0):
	return

return var_0_0

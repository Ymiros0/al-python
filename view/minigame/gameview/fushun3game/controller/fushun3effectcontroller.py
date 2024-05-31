local var_0_0 = class("Fushun3EffectController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._effectTpl = arg_1_1
	arg_1_0._effectPos = arg_1_2
	arg_1_0._event = arg_1_3
	arg_1_0._effects = {}
	arg_1_0._effectPool = {}

def var_0_0.start(arg_2_0):
	for iter_2_0 = #arg_2_0._effects, 1, -1:
		arg_2_0.returnEffectToPool(table.remove(arg_2_0._effects, iter_2_0))

def var_0_0.step(arg_3_0):
	return

def var_0_0.returnEffectToPool(arg_4_0, arg_4_1):
	setActive(arg_4_1.tf, False)
	table.insert(arg_4_0._effectPool, arg_4_1)

def var_0_0.addEffectByName(arg_5_0, arg_5_1, arg_5_2):
	if not arg_5_1:
		return

	local var_5_0 = arg_5_0.getOrCreateEffect(None, arg_5_1)

	if var_5_0:
		arg_5_0.addEffectToTarget(var_5_0, arg_5_2)
		table.insert(arg_5_0._effects, var_5_0)

def var_0_0.addEffectByAnim(arg_6_0, arg_6_1, arg_6_2):
	if not arg_6_1:
		return

	local var_6_0 = arg_6_0.getOrCreateEffect(arg_6_1)

	if var_6_0:
		arg_6_0.addEffectToTarget(var_6_0, arg_6_2)
		table.insert(arg_6_0._effects, var_6_0)

def var_0_0.addEffectToTarget(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_1.data.parent:
		SetParent(arg_7_1.tf, arg_7_2)

		arg_7_1.tf.localScale = arg_7_2.localScale
		arg_7_1.tf.anchoredPosition = Vector2(0, 0)

		setActive(arg_7_1.tf, True)
		table.insert(arg_7_0._effects, arg_7_1)
	else
		setParent(arg_7_1.tf, arg_7_0._effectPos)

		arg_7_1.tf.localScale = Fushun3GameConst.game_scale_v3
		arg_7_1.tf.position = arg_7_2.position

		setActive(arg_7_1.tf, True)

def var_0_0.getOrCreateEffect(arg_8_0, arg_8_1, arg_8_2):
	for iter_8_0 = 1, #arg_8_0._effectPool:
		if arg_8_1 and arg_8_0._effectPool[iter_8_0].data.trigger == arg_8_1 or arg_8_2 and arg_8_0._effectPool[iter_8_0].data.name == arg_8_2:
			return table.remove(arg_8_0._effectPool, iter_8_0)

	local var_8_0 = arg_8_0.getEffectData(arg_8_1, arg_8_2)

	return arg_8_0.instiateEffect(var_8_0)

def var_0_0.instiateEffect(arg_9_0, arg_9_1):
	if arg_9_1:
		local var_9_0 = tf(instantiate(findTF(arg_9_0._effectTpl, arg_9_1.name)))
		local var_9_1 = {
			tf = var_9_0,
			data = arg_9_1
		}

		GetOrAddComponent(findTF(var_9_0, "efAnim"), typeof(DftAniEvent)).SetEndEvent(function()
			arg_9_0.removeEffect(var_9_1))

		return var_9_1

def var_0_0.removeEffect(arg_11_0, arg_11_1):
	for iter_11_0 = #arg_11_0._effects, 1, -1:
		if arg_11_0._effects[iter_11_0] == arg_11_1:
			setActive(arg_11_0._effects[iter_11_0].tf, False)
			arg_11_0.returnEffectToPool(table.remove(arg_11_0._effects, iter_11_0))

def var_0_0.getEffectData(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_1:
		for iter_12_0 = 1, #Fushun3GameConst.effect_data:
			if Fushun3GameConst.effect_data[iter_12_0].trigger == arg_12_1:
				return Clone(Fushun3GameConst.effect_data[iter_12_0])
	elif arg_12_2:
		for iter_12_1 = 1, #Fushun3GameConst.effect_data:
			if Fushun3GameConst.effect_data[iter_12_1].name == arg_12_2:
				return Clone(Fushun3GameConst.effect_data[iter_12_1])

return var_0_0

local var_0_0 = class("SailBoatEffectControl")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._content = findTF(arg_1_0._tf, "scene_front/content")
	arg_1_0._effects = {}
	arg_1_0._effectPool = {}

def var_0_0.start(arg_2_0):
	for iter_2_0 = #arg_2_0._effects, 1, -1:
		local var_2_0 = table.remove(arg_2_0._effects, iter_2_0)

		setActive(var_2_0.tf, False)
		table.insert(arg_2_0._effectPool, var_2_0)

def var_0_0.step(arg_3_0, arg_3_1):
	return

def var_0_0.getEffect(arg_4_0, arg_4_1):
	if #arg_4_0._effectPool > 0:
		for iter_4_0 = 1, #arg_4_0._effectPool:
			if #arg_4_0._effectPool[iter_4_0].name == arg_4_1:
				return (table.remove(arg_4_0._effectPool, iter_4_0))

	local var_4_0 = var_0_1.GetGameEffectTf(arg_4_1)
	local var_4_1 = {
		tf = var_4_0,
		name = arg_4_1
	}

	GetComponent(findTF(var_4_0, "img"), typeof(DftAniEvent)).SetEndEvent(function()
		arg_4_0.effectEnd(var_4_1))

	return var_4_1

def var_0_0.onEventCall(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_1 == SailBoatGameEvent.CREATE_EFFECT:
		local var_6_0 = arg_6_2.effect
		local var_6_1 = arg_6_2.direct
		local var_6_2 = arg_6_2.position
		local var_6_3 = arg_6_2.content

		arg_6_0.createEffect(var_6_0, var_6_1, var_6_2, var_6_3)

def var_0_0.createEffect(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	local var_7_0 = arg_7_0.getEffect(arg_7_1)

	if arg_7_2:
		var_7_0.tf.localScale = arg_7_2

	if arg_7_3:
		var_7_0.tf.anchoredPosition = arg_7_3

	if arg_7_4:
		SetParent(var_7_0.tf, arg_7_4)
	else
		SetParent(var_7_0.tf, arg_7_0._content)

	setActive(var_7_0.tf, True)
	table.insert(arg_7_0._effects, var_7_0)

def var_0_0.effectEnd(arg_8_0, arg_8_1):
	for iter_8_0 = 1, #arg_8_0._effects:
		if arg_8_0._effects[iter_8_0] == arg_8_1:
			local var_8_0 = table.remove(arg_8_0._effects, iter_8_0)

			setActive(var_8_0.tf, False)
			table.insert(arg_8_0._effectPool, var_8_0)

			return

def var_0_0.dispose(arg_9_0):
	return

def var_0_0.clear(arg_10_0):
	return

return var_0_0

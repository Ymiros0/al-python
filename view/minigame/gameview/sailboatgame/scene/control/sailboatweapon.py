local var_0_0 = class("SailBoatWeapon")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_1 = SailBoatGameVo
	arg_1_0._data = arg_1_1
	arg_1_0._fireTime = None

def var_0_0.start(arg_2_0):
	arg_2_0._fireTime = arg_2_0.getConfig("cd")

def var_0_0.step(arg_3_0, arg_3_1):
	if arg_3_0._fireTime and arg_3_0._fireTime > 0:
		arg_3_0._fireTime = arg_3_0._fireTime - arg_3_1

		if arg_3_0._fireTime < 0:
			arg_3_0._fireTime = 0
	else
		arg_3_0._fireTime = 0

def var_0_0.skillStep(arg_4_0, arg_4_1):
	arg_4_0._fireTime = arg_4_0._fireTime - arg_4_1

def var_0_0.getFireAble(arg_5_0):
	if arg_5_0._fireTime and arg_5_0._fireTime > 0:
		return False

	return True

def var_0_0.fire(arg_6_0):
	if not arg_6_0.getFireAble():
		return None

	arg_6_0._fireTime = arg_6_0.getConfig("cd")

	return arg_6_0.getFireData()

def var_0_0.getFireTime(arg_7_0):
	return arg_7_0._fireTime or 0

def var_0_0.getFireData(arg_8_0):
	return Clone(arg_8_0._data)

def var_0_0.getAngel(arg_9_0):
	return arg_9_0.getConfig("angel")

def var_0_0.getDistance(arg_10_0):
	return arg_10_0.getConfig("distance")

def var_0_0.getDamage(arg_11_0):
	return arg_11_0.getConfig("damage")

def var_0_0.getFireFlag(arg_12_0):
	return arg_12_0._fireTime == 0

def var_0_0.getConfig(arg_13_0, arg_13_1):
	return arg_13_0._data[arg_13_1]

def var_0_0.clear(arg_14_0):
	arg_14_0._data = None

return var_0_0

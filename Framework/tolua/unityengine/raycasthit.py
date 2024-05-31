local var_0_0 = rawget
local var_0_1 = setmetatable

RaycastBits = {
	ALL = 31,
	Collider = 1,
	Point = 4,
	Transform = 16,
	Normal = 2,
	Rigidbody = 8
}

local var_0_2 = RaycastBits
local var_0_3 = {}
local var_0_4 = tolua.initget(var_0_3)

def var_0_3.__index(arg_1_0, arg_1_1):
	local var_1_0 = var_0_0(var_0_3, arg_1_1)

	if var_1_0 == None:
		var_1_0 = var_0_0(var_0_4, arg_1_1)

		if var_1_0 != None:
			return var_1_0(arg_1_0)

	return var_1_0

def var_0_3.New(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5):
	local var_2_0 = {
		collider = arg_2_0,
		distance = arg_2_1,
		normal = arg_2_2,
		point = arg_2_3,
		rigidbody = arg_2_4,
		transform = arg_2_5
	}

	var_0_1(var_2_0, var_0_3)

	return var_2_0

def var_0_3.Init(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, arg_3_6):
	arg_3_0.collider = arg_3_1
	arg_3_0.distance = arg_3_2
	arg_3_0.normal = arg_3_3
	arg_3_0.point = arg_3_4
	arg_3_0.rigidbody = arg_3_5
	arg_3_0.transform = arg_3_6

def var_0_3.Get(arg_4_0):
	return arg_4_0.collider, arg_4_0.distance, arg_4_0.normal, arg_4_0.point, arg_4_0.rigidbody, arg_4_0.transform

def var_0_3.Destroy(arg_5_0):
	arg_5_0.collider = None
	arg_5_0.rigidbody = None
	arg_5_0.transform = None

def var_0_3.GetMask(...):
	local var_6_0 = {
		...
	}
	local var_6_1 = 0

	for iter_6_0 = 1, #var_6_0:
		local var_6_2 = var_0_2[var_6_0[iter_6_0]] or 0

		if var_6_2 != 0:
			var_6_1 = var_6_1 + var_6_2

	if var_6_1 == 0:
		var_6_1 = var_0_2.all

	return var_6_1

UnityEngine.RaycastHit = var_0_3

var_0_1(var_0_3, var_0_3)

return var_0_3

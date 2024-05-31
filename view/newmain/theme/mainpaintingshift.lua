﻿local var_0_0 = class("MainPaintingShift")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.meshImageShift = Vector3(arg_1_1[1], arg_1_1[2], 0) + (arg_1_2 or Vector3.zero)
	arg_1_0.l2dShift = Vector3(arg_1_1[3], arg_1_1[4], 0)
	arg_1_0.spineShift = Vector3(arg_1_1[5], arg_1_1[6], 0)
	arg_1_0.scale = Vector3(arg_1_1[7], arg_1_1[7], 1)
	arg_1_0.l2dScale = Vector3(arg_1_1[8], arg_1_1[8], 1)
	arg_1_0.spineScale = Vector3(arg_1_1[9], arg_1_1[9], 1)
end

function var_0_0.GetMeshImageShift(arg_2_0)
	return arg_2_0.meshImageShift, arg_2_0.scale
end

function var_0_0.GetL2dShift(arg_3_0)
	return arg_3_0.l2dShift, arg_3_0.l2dScale
end

function var_0_0.GetSpineShift(arg_4_0)
	return arg_4_0.spineShift, arg_4_0.spineScale
end

return var_0_0

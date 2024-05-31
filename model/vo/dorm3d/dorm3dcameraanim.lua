local var_0_0 = class("Dorm3dCameraAnim", import("model.vo.BaseVO"))

function var_0_0.bindConfigTable(arg_1_0)
	return pg.dorm3d_camera_anim_template
end

function var_0_0.GetName(arg_2_0)
	return arg_2_0:getConfig("desc")
end

function var_0_0.GetStateName(arg_3_0)
	return arg_3_0:getConfig("state")
end

function var_0_0.GetAnimTime(arg_4_0)
	return arg_4_0:getConfig("anim_time")
end

function var_0_0.GetPreAnimID(arg_5_0)
	return arg_5_0:getConfig("pre_anim")
end

function var_0_0.GetFinishAnimID(arg_6_0)
	return arg_6_0:getConfig("finish_anim")
end

function var_0_0.GetUnlockRequirment(arg_7_0)
	return arg_7_0:getConfig("unlock")
end

function var_0_0.GetFurnitureID(arg_8_0)
	return arg_8_0:getConfig("furniture_id")
end

return var_0_0

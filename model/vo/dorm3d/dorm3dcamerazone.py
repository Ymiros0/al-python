local var_0_0 = class("Dorm3dCameraZone", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.dorm3d_camera_zone_template

def var_0_0.Ctor(arg_2_0, arg_2_1):
	var_0_0.super.Ctor(arg_2_0, arg_2_1)

	arg_2_0.regulaAnims = _.map(arg_2_0.GetRegularAnimIDList(), function(arg_3_0)
		return Dorm3dCameraAnim.New({
			configId = arg_3_0
		}))
	arg_2_0.specialAnims = _.map(arg_2_0.GetSpecialFurnitureIDList(), function(arg_4_0)
		local var_4_0 = arg_4_0[1]

		return {
			furnitureId = var_4_0,
			slotId = arg_4_0[2],
			anims = _.map(arg_2_0.GetSpecialAnimIDListByFurnitureID(var_4_0), function(arg_5_0)
				return Dorm3dCameraAnim.New({
					configId = arg_5_0
				}))
		})

def var_0_0.GetName(arg_6_0):
	return arg_6_0.getConfig("name")

def var_0_0.GetShipGroupId(arg_7_0):
	return arg_7_0.getConfig("char_id")

def var_0_0.GetWatchCameraName(arg_8_0):
	return arg_8_0.getConfig("watch_camera")

def var_0_0.GetRegularAnimIDList(arg_9_0):
	return arg_9_0.getConfig("regular_anim") or {}

def var_0_0.GetRegularAnims(arg_10_0):
	return arg_10_0.regulaAnims

def var_0_0.GetSpecialFurnitureIDList(arg_11_0):
	return arg_11_0.getConfig("special_furniture") or {}

def var_0_0.GetSpecialAnimIDListByFurnitureID(arg_12_0, arg_12_1):
	return pg.dorm3d_camera_anim_template.get_id_list_by_furniture_id[arg_12_1] or {}

def var_0_0.GetSpecialAnims(arg_13_0):
	return arg_13_0.specialAnims

def var_0_0.GetAnimSpeeds(arg_14_0):
	return arg_14_0.getConfig("anim_speeds")

def var_0_0.Get(arg_15_0):
	return arg_15_0.getConfig("")

def var_0_0.GetRecordTime(arg_16_0):
	return arg_16_0.getConfig("record_time")

def var_0_0.GetFocusDistanceRange(arg_17_0):
	return arg_17_0.getConfig("focus_distance")

def var_0_0.GetDepthOfFieldBlurRange(arg_18_0):
	return arg_18_0.getConfig("blur_strength")

def var_0_0.GetExposureRange(arg_19_0):
	return arg_19_0.getConfig("exposure")

def var_0_0.GetContrastRange(arg_20_0):
	return arg_20_0.getConfig("contrast")

def var_0_0.GetSaturationRange(arg_21_0):
	return arg_21_0.getConfig("saturation")

return var_0_0

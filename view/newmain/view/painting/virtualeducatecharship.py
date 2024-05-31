local var_0_0 = class("VirtualEducateCharShip", import("model.vo.Ship"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.educateCharId = arg_1_1

	var_0_0.super.Ctor(arg_1_0, {
		id = 99999999,
		configId = 999024
	})

	arg_1_0.templateConfig = pg.secretary_special_ship[arg_1_1]

def var_0_0.getPainting(arg_2_0):
	return arg_2_0.templateConfig.prefab or "tbniang"

def var_0_0.getName(arg_3_0):
	return arg_3_0.templateConfig.name or ""

def var_0_0.getPrefab(arg_4_0):
	return arg_4_0.templateConfig.head

def var_0_0.GetRecordPosKey(arg_5_0):
	return arg_5_0.educateCharId .. "" .. arg_5_0.id

return var_0_0

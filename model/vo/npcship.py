local var_0_0 = class("NpcShip", import(".Ship"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	local var_1_0 = pg.ship_data_template[arg_1_0.configId]

	for iter_1_0 = 1, 3:
		if not arg_1_0.equipments[iter_1_0]:
			local var_1_1 = var_1_0["equip_id_" .. iter_1_0]

			arg_1_0.equipments[iter_1_0] = var_1_1 > 0 and Equipment.New({
				id = var_1_1
			}) or False

	arg_1_0.isNpc = True

def var_0_0.getExp(arg_2_0):
	return 0

def var_0_0.addExp(arg_3_0, arg_3_1, arg_3_2):
	return

def var_0_0.getIntimacy(arg_4_0):
	return pg.intimacy_template[arg_4_0.getIntimacyLevel()].lower_bound

def var_0_0.getIntimacyLevel(arg_5_0):
	return 2

def var_0_0.setIntimacy(arg_6_0, arg_6_1):
	return

def var_0_0.getEnergy(arg_7_0):
	return pg.ship_data_template[arg_7_0.configId].energy

def var_0_0.setEnergy(arg_8_0, arg_8_1):
	return

return var_0_0

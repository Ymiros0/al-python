local var_0_0 = class("EquipmentsDict")

def var_0_0.Ctor(arg_1_0):
	local var_1_0 = {}
	local var_1_1 = getProxy(EquipmentProxy).GetEquipmentsRaw()

	for iter_1_0, iter_1_1 in pairs(var_1_1):
		var_1_0[iter_1_1.id] = var_1_0[iter_1_1.id] or {}

		table.insert(var_1_0[iter_1_1.id], CreateShell(iter_1_1))

	for iter_1_2, iter_1_3 in pairs(getProxy(BayProxy).GetEquipsInShipsRaw()):
		var_1_0[iter_1_3.id] = var_1_0[iter_1_3.id] or {}

		table.insert(var_1_0[iter_1_3.id], iter_1_3)

	arg_1_0.data = var_1_0

def var_0_0.GetSameTypeInEquips(arg_2_0, arg_2_1):
	local var_2_0 = {}
	local var_2_1 = arg_2_0.data
	local var_2_2 = Equipment.getConfigData(arg_2_1)

	while var_2_2:
		if var_2_1[var_2_2.id]:
			table.insertto(var_2_0, var_2_1[var_2_2.id])

		var_2_2 = var_2_2.next and Equipment.getConfigData(var_2_2.next)

	return var_2_0

def var_0_0.GetEquipmentTransformCandicates(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.GetSameTypeInEquips(arg_3_1)
	local var_3_1 = _.map(var_3_0, function(arg_4_0)
		return {
			type = DROP_TYPE_EQUIP,
			id = arg_4_0.id,
			template = arg_4_0
		})
	local var_3_2 = Equipment.GetEquipComposeCfgStatic({
		equip_id = arg_3_1
	})

	if var_3_2:
		local var_3_3 = getProxy(BagProxy).getItemById(var_3_2.material_id) or Item.New({
			count = 0,
			id = var_3_2.material_id
		})

		table.insert(var_3_1, 1, {
			type = DROP_TYPE_ITEM,
			id = var_3_2.material_id,
			template = var_3_3,
			composeCfg = var_3_2
		})

	return var_3_1

def var_0_0.GetEquipTraceBack(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = arg_5_0.data

	arg_5_2 = arg_5_2 or {
		arg_5_1
	}
	arg_5_3 = arg_5_3 or {}

	local var_5_1 = EquipmentProxy.GetTransformSources(arg_5_1)

	if #var_5_1 == 0:
		table.insert(arg_5_3, arg_5_2)

	for iter_5_0, iter_5_1 in ipairs(var_5_1):
		local var_5_2 = pg.equip_upgrade_data[iter_5_1].upgrade_from
		local var_5_3 = iter_5_0 == #var_5_1 and arg_5_2 or Clone(arg_5_2)

		table.insert(var_5_3, var_5_2)

		var_5_3.formulas = var_5_3.formulas or {}

		table.insert(var_5_3.formulas, 1, iter_5_1)

		local var_5_4 = arg_5_0.GetEquipmentTransformCandicates(var_5_2)

		if _.any(var_5_4, function(arg_6_0)
			if arg_6_0.type == DROP_TYPE_ITEM:
				return arg_6_0.template.count >= arg_6_0.composeCfg.material_num
			elif arg_6_0.type == DROP_TYPE_EQUIP:
				return arg_6_0.template.count > 0):
			var_5_3.candicates = var_5_4

			table.insert(arg_5_3, var_5_3)
		elif var_5_2 == 0:
			assert(False, "ERROR Source Equip ID 0")

			var_5_3.candicates = {
				setmetatable({
					id = 0
				}, Equipment)
			}

			table.insert(arg_5_3, var_5_3)
		else
			arg_5_0.GetEquipTraceBack(var_5_2, var_5_3, arg_5_3)

	return arg_5_3

def var_0_0.GetSortedEquipTraceBack(arg_7_0, ...):
	local var_7_0 = arg_7_0.GetEquipTraceBack(...)

	table.sort(var_7_0, function(arg_8_0, arg_8_1)
		if #arg_8_0 != #arg_8_1:
			return #arg_8_0 < #arg_8_1
		else
			for iter_8_0 = 1, #arg_8_0:
				if arg_8_0[iter_8_0] != arg_8_1[iter_8_0]:
					return arg_8_0[iter_8_0] < arg_8_1[iter_8_0]

			return False)

	return var_7_0

def var_0_0.FindTheEquip(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.data

	if not arg_9_1 or not var_9_0[arg_9_1.id]:
		return

	for iter_9_0, iter_9_1 in ipairs(var_9_0[arg_9_1.id]):
		if EquipmentProxy.SameEquip(arg_9_1, iter_9_1):
			return iter_9_0, iter_9_1

def var_0_0.AddEquipment(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.data

	var_10_0[arg_10_1.id] = var_10_0[arg_10_1.id] or {}

	local var_10_1 = arg_10_0.FindTheEquip(arg_10_1) or #var_10_0[arg_10_1.id] + 1

	var_10_0[arg_10_1.id][var_10_1] = arg_10_1

def var_0_0.RemoveEquipment(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.data

	if not arg_11_1 or not var_11_0[arg_11_1.id]:
		return

	local var_11_1 = arg_11_0.FindTheEquip(arg_11_1)

	if not var_11_1:
		return

	table.remove(var_11_0[arg_11_1.id], var_11_1)

def var_0_0.UpdateEquipment(arg_12_0, arg_12_1):
	if arg_12_1.count == 0:
		arg_12_0.RemoveEquipment(arg_12_1)
	else
		arg_12_0.AddEquipment(arg_12_1)

return var_0_0

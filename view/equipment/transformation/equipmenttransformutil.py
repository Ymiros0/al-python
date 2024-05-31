local var_0_0 = {}

var_0_0.__name = "EquipmentTransformUtil"

def var_0_0.SameDrop(arg_1_0, arg_1_1):
	if arg_1_0.type != arg_1_1.type:
		return False

	if arg_1_0.type == DROP_TYPE_EQUIP:
		return EquipmentProxy.SameEquip(arg_1_0.template, arg_1_1.template)
	else
		return arg_1_0.id == arg_1_1.id

def var_0_0.CheckEquipmentFormulasSucceed(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(PlayerProxy)
	local var_2_1 = getProxy(BagProxy)
	local var_2_2 = {}
	local var_2_3 = arg_2_1

	for iter_2_0, iter_2_1 in ipairs(arg_2_0):
		local var_2_4 = pg.equip_upgrade_data[iter_2_1]
		local var_2_5 = Equipment.GetRevertRewardsStatic(var_2_3)

		assert(Equipment.CanInBag(var_2_3), "Missing equip_data_template ID. " .. (var_2_3 or "NIL"))

		local var_2_6 = Equipment.CanInBag(var_2_3) and Equipment.getConfigData(var_2_3).destory_gold or 0

		var_2_3 = Equipment.GetEquipRootStatic(var_2_3)

		assert(var_2_4 and var_2_4.upgrade_from == var_2_3, "Transform a non formula equipment, formula " .. (iter_2_1 or -1) .. " equipment " .. (var_2_3 or -1))

		local var_2_7 = var_2_4.material_consume

		for iter_2_2, iter_2_3 in ipairs(var_2_7):
			local var_2_8 = iter_2_3[1]
			local var_2_9 = iter_2_3[2]

			var_2_2[var_2_8] = (var_2_2[var_2_8] or var_2_1.getItemCountById(var_2_8) or 0) - var_2_9

			if var_2_2[var_2_8] < 0:
				local var_2_10 = Item.getConfigData(var_2_8)

				return False, var_2_10 and var_2_10.name

		var_2_2.gold = (var_2_2.gold or var_2_0.getRawData().gold or 0) - var_2_4.coin_consume

		if var_2_2.gold < 0:
			return False, Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResGold
			}).getName()

		for iter_2_4, iter_2_5 in pairs(var_2_5):
			if iter_2_4 != "gold":
				var_2_2[iter_2_4] = (var_2_2[iter_2_4] or 0) + iter_2_5

		var_2_2.gold = (var_2_2.gold or 0) + var_2_6
		var_2_3 = var_2_4.target_id

	return True

def var_0_0.CheckTransformFormulasSucceed(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(PlayerProxy)
	local var_3_1 = getProxy(BagProxy)
	local var_3_2 = {
		gold = var_3_0.getRawData().gold or 0
	}
	local var_3_3

	if arg_3_1.type == DROP_TYPE_EQUIP:
		var_3_3 = arg_3_1.id

		if not arg_3_1.template.shipId:
			local var_3_4 = getProxy(EquipmentProxy).getEquipmentById(var_3_3)

			if not var_3_4 or var_3_4.count <= 0:
				return False, Equipment.getConfigData(var_3_3).name
	elif arg_3_1.type == DROP_TYPE_ITEM:
		if var_3_2.gold < arg_3_1.composeCfg.gold_num:
			return False, Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResGold
			}).getName()
		elif (var_3_1.getItemCountById(arg_3_1.composeCfg.material_id) or 0) < arg_3_1.composeCfg.material_num:
			return False, Item.getConfigData(arg_3_1.composeCfg.material_id).name

		var_3_2.gold = var_3_2.gold - arg_3_1.composeCfg.gold_num
		var_3_3 = arg_3_1.composeCfg.equip_id

	assert(var_3_3)

	local var_3_5 = var_3_3

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		local var_3_6 = pg.equip_upgrade_data[iter_3_1]
		local var_3_7 = Equipment.GetRevertRewardsStatic(var_3_5)

		assert(Equipment.CanInBag(var_3_5), "Missing equip_data_template ID. " .. (var_3_5 or "NIL"))

		local var_3_8 = Equipment.CanInBag(var_3_5) and Equipment.getConfigData(var_3_5).destory_gold or 0

		var_3_5 = Equipment.GetEquipRootStatic(var_3_5)

		assert(var_3_6 and var_3_6.upgrade_from == var_3_5, "Transform a non formula equipment, formula " .. (iter_3_1 or -1) .. " equipment " .. (var_3_5 or -1))

		local var_3_9 = var_3_6.material_consume

		for iter_3_2, iter_3_3 in ipairs(var_3_9):
			local var_3_10 = iter_3_3[1]
			local var_3_11 = iter_3_3[2]

			var_3_2[var_3_10] = (var_3_2[var_3_10] or var_3_1.getItemCountById(var_3_10) or 0) - var_3_11

			if var_3_2[var_3_10] < 0:
				local var_3_12 = Item.getConfigData(var_3_10)

				return False, var_3_12 and var_3_12.name

		var_3_2.gold = var_3_2.gold - var_3_6.coin_consume

		if var_3_2.gold < 0:
			return False, Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResGold
			}).getName()

		for iter_3_4, iter_3_5 in pairs(var_3_7):
			if iter_3_4 != "gold":
				var_3_2[iter_3_4] = (var_3_2[iter_3_4] or var_3_1.getItemCountById(iter_3_4)) + iter_3_5

		var_3_2.gold = (var_3_2.gold or 0) + var_3_8
		var_3_5 = var_3_6.target_id

	return True

def var_0_0.CheckTransformEnoughGold(arg_4_0, arg_4_1):
	local var_4_0 = getProxy(PlayerProxy)
	local var_4_1 = getProxy(BagProxy)
	local var_4_2 = var_4_0.getRawData().gold or 0
	local var_4_3 = 0
	local var_4_4 = 0
	local var_4_5 = True
	local var_4_6

	if arg_4_1.type == DROP_TYPE_EQUIP:
		var_4_6 = arg_4_1.id
	elif arg_4_1.type == DROP_TYPE_ITEM:
		var_4_2 = var_4_2 - arg_4_1.composeCfg.gold_num
		var_4_4 = var_4_4 + arg_4_1.composeCfg.gold_num
		var_4_5 = var_4_5 and var_4_2 >= 0
		var_4_6 = arg_4_1.composeCfg.equip_id

	assert(var_4_6)

	local var_4_7 = var_4_6

	for iter_4_0, iter_4_1 in ipairs(arg_4_0):
		local var_4_8 = pg.equip_upgrade_data[iter_4_1]
		local var_4_9 = Equipment.GetRevertRewardsStatic(var_4_7)

		assert(Equipment.CanInBag(var_4_7), "Missing equip_data_template ID. " .. (var_4_7 or "NIL"))

		local var_4_10 = Equipment.CanInBag(var_4_7) and Equipment.getConfigData(var_4_7).destory_gold or 0

		var_4_7 = Equipment.GetEquipRootStatic(var_4_7)

		assert(var_4_8 and var_4_8.upgrade_from == var_4_7, "Transform a non formula equipment, formula " .. (iter_4_1 or -1) .. " equipment " .. (var_4_7 or -1))

		var_4_2 = var_4_2 - var_4_8.coin_consume
		var_4_3 = var_4_3 + var_4_8.coin_consume
		var_4_5 = var_4_5 and var_4_2 >= 0

		for iter_4_2, iter_4_3 in pairs(var_4_9):
			if iter_4_2 != "gold":
				var_4_2 = var_4_2 + iter_4_3

		var_4_2 = var_4_2 + var_4_10
		var_4_7 = var_4_8.target_id

	return var_4_5, var_4_3, var_4_4

local function var_0_1(arg_5_0, arg_5_1)
	local var_5_0 = {
		{
			"icon_bg/slv"
		},
		{
			"icon_bg/frame/IconColorful(Clone)"
		},
		{
			"icon_bg/frame/Item_duang5(Clone)"
		},
		{
			"icon_bg/frame/specialFrame"
		},
		{
			"ship_type"
		},
		{
			"icon_bg/new"
		},
		{
			"icon_bg/npc"
		}
	}

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		local var_5_1 = arg_5_0.Find(iter_5_1[1])

		if type != iter_5_1[2] and not IsNil(var_5_1):
			setActive(var_5_1, False)

	arg_5_0.Find("icon_bg/frame").GetComponent(typeof(Image)).enabled = True

return var_0_0

local var_0_0 = class("RecordShipEquipmentCommand", pm.SimpleCommand)
local var_0_1 = {
	"#FFFFFF",
	"#60a9ff",
	"#966af6",
	"#fff157",
	"#EE799F"
}

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.index
	local var_1_3 = var_1_0.type

	if not var_1_3:
		return

	if not var_1_1:
		return

	if not var_1_2:
		return

	local var_1_4 = getProxy(PlayerProxy).getData()
	local var_1_5 = getProxy(BayProxy)
	local var_1_6 = var_1_5.getShipById(var_1_1)

	var_1_6.getEquipmentRecord(var_1_4.id)

	local var_1_7 = Clone(var_1_6.equipments)
	local var_1_8 = var_1_6.GetSpWeaponRecord(var_1_4.id)

	if var_1_3 == 1:
		for iter_1_0, iter_1_1 in ipairs(var_1_7):
			var_1_6.equipmentRecords[var_1_2][iter_1_0] = iter_1_1 and iter_1_1.id or -1

		var_1_6.setEquipmentRecord(var_1_4.id, var_1_6.equipmentRecords)

		if not LOCK_SP_WEAPON:
			var_1_8[var_1_2] = var_1_6.GetSpWeapon()

			var_1_6.SetSpWeaponRecord(var_1_4.id, var_1_8)

		var_1_5.updateShip(var_1_6)
	elif var_1_3 == 2:
		local var_1_9 = getProxy(EquipmentProxy)
		local var_1_10 = Clone(var_1_6.equipmentRecords[var_1_2])
		local var_1_11 = var_1_8[var_1_2]

		if #var_1_10 == 0 or _.all(var_1_10, function(arg_2_0)
			return arg_2_0 == -1) and var_1_11 == None:
			return

		local function var_1_12(arg_3_0, arg_3_1)
			if var_1_7[arg_3_0] and var_1_7[arg_3_0].id == arg_3_1:
				return True

			return False

		local var_1_13 = {}

		for iter_1_2, iter_1_3 in ipairs(var_1_10):
			if iter_1_3 != -1:
				local var_1_14 = var_1_9.getEquipmentById(iter_1_3)

				if (not var_1_14 or var_1_14.count <= 0) and not var_1_12(iter_1_2, iter_1_3):
					local var_1_15 = Equipment.New({
						id = iter_1_3
					})

					var_1_10[iter_1_2] = var_1_9.getSameTypeEquipmentId(var_1_15) or 0

					local var_1_16 = var_0_1[var_1_15.config.rarity - 1]
					local var_1_17 = string.format("<color=%s>%s+%s</color>", var_1_16, var_1_15.config.name, var_1_15.config.level - 1)

					table.insert(var_1_13, var_1_17)

		local var_1_18 = var_1_11

		if var_1_11 and (not var_1_11.IsReal() or var_1_11.GetShipId() != None and var_1_11.GetShipId() != var_1_6.id):
			local var_1_19 = var_0_1[var_1_11.GetRarity()]
			local var_1_20 = string.format("<color=%s>%s+%s</color>", var_1_19, var_1_11.GetName(), var_1_11.GetLevel() - 1)

			table.insert(var_1_13, var_1_20)

			var_1_18 = var_1_9.GetSameTypeSpWeapon(var_1_11)

		local function var_1_21(arg_4_0)
			local var_4_0 = {}

			for iter_4_0, iter_4_1 in ipairs(arg_4_0):
				if not var_1_7[iter_4_0] or var_1_7[iter_4_0].id != iter_4_1:
					if iter_4_1 == 0:
						pg.TipsMgr.GetInstance().ShowTips(i18n("ship_quick_change_noequip"))
					elif iter_4_1 == -1 and var_1_7[iter_4_0]:
						table.insert(var_4_0, function(arg_5_0)
							arg_1_0.sendNotification(GAME.UNEQUIP_FROM_SHIP, {
								shipId = var_1_1,
								pos = iter_4_0,
								callback = arg_5_0
							}))
					elif iter_4_1 != -1:
						table.insert(var_4_0, function(arg_6_0)
							arg_1_0.sendNotification(GAME.EQUIP_TO_SHIP, {
								equipmentId = iter_4_1,
								shipId = var_1_1,
								pos = iter_4_0,
								callback = arg_6_0
							}))

			if not LOCK_SP_WEAPON:
				table.insert(var_4_0, function(arg_7_0)
					local var_7_0 = var_1_6.GetSpWeapon()

					if var_1_11:
						if not var_1_18:
							pg.TipsMgr.GetInstance().ShowTips(i18n("ship_quick_change_noequip"))

							return
						elif not var_7_0 or var_7_0.GetUID() != var_1_18.GetUID():
							arg_1_0.sendNotification(GAME.EQUIP_SPWEAPON_TO_SHIP, {
								spWeaponUid = var_1_18.GetUID(),
								shipId = var_1_1,
								callback = arg_7_0
							})

							return
					elif var_7_0:
						arg_1_0.sendNotification(GAME.EQUIP_SPWEAPON_TO_SHIP, {
							shipId = var_1_1,
							callback = arg_7_0
						})

						return

					arg_7_0())

			seriesAsync(var_4_0)

		if #var_1_13 > 0:
			local var_1_22 = ""

			if #var_1_13 > 2:
				var_1_22 = table.concat(_.slice(var_1_13, 1, 2), "、") .. i18n("word_wait")
			else
				var_1_22 = table.concat(var_1_13, "、")

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("no_found_record_equipment", var_1_22),
				def onYes:()
					var_1_21(var_1_10)
			})
		else
			var_1_21(var_1_10)

	arg_1_0.sendNotification(GAME.RECORD_SHIP_EQUIPMENT_DONE, {
		shipId = var_1_1,
		index = var_1_2,
		type = var_1_3
	})

return var_0_0

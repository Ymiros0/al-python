local var_0_0 = class("ModBluePrintCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.count
	local var_1_2 = var_1_0.id
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3.getBluePrintById(var_1_2)

	if not var_1_4:
		return

	if not var_1_4.isUnlock():
		return

	local var_1_5 = var_1_4.getConfig("strengthen_item")

	if var_1_1 > getProxy(BagProxy).getItemCountById(var_1_5):
		return

	if var_1_1 == 0:
		return

	if var_1_4.isMaxLevel() and var_1_4.isMaxFateLevel():
		pg.TipsMgr.GetInstance().ShowTips(i18n("blueprint_max_level_tip"))

		return

	local var_1_6 = var_1_1 * var_1_4.getItemExp()
	local var_1_7 = Clone(var_1_4)

	var_1_7.addExp(var_1_6)

	local var_1_8 = getProxy(BayProxy)
	local var_1_9 = var_1_8.getShipById(var_1_4.shipId)
	local var_1_10 = var_1_7.fateLevel > 0 and var_1_7.getFateStrengthenConfig(var_1_7.fateLevel) or var_1_7.getStrengthenConfig(math.max(var_1_7.level, 1))

	if var_1_9.level < var_1_10.need_lv:
		pg.TipsMgr.GetInstance().ShowTips(i18n("buleprint_need_level_tip", var_1_10.need_lv))

		return

	pg.ConnectionMgr.GetInstance().Send(63204, {
		ship_id = var_1_4.shipId,
		count = var_1_1
	}, 63205, function(arg_2_0)
		if arg_2_0.result == 0:
			arg_1_0.sendNotification(GAME.CONSUME_ITEM, Drop.New({
				type = DROP_TYPE_ITEM,
				count = var_1_1,
				id = var_1_5
			}))

			local var_2_0 = Clone(var_1_4)
			local var_2_1 = var_1_4.getItemExp()

			var_1_4.addExp(var_2_1 * var_1_1)

			if var_1_4.level > var_2_0.level:
				for iter_2_0 = var_2_0.level + 1, var_1_4.level:
					local var_2_2 = var_1_4.getStrengthenConfig(iter_2_0)

					if var_2_2.special == 1 and type(var_2_2.special_effect) == "table":
						local var_2_3 = var_2_2.special_effect

						for iter_2_1, iter_2_2 in ipairs(var_2_3):
							local var_2_4 = iter_2_2[1]

							if var_2_4 == ShipBluePrint.STRENGTHEN_TYPE_SKILL:
								local var_2_5 = iter_2_2[2]
								local var_2_6 = getProxy(BayProxy)
								local var_2_7 = var_2_6.getShipById(var_1_4.shipId)

								for iter_2_3, iter_2_4 in ipairs(var_2_5):
									var_2_7.skills[var_1_2] = {
										exp = 0,
										level = 1,
										id = iter_2_4
									}

									pg.TipsMgr.GetInstance().ShowTips(iter_2_2[3])

								var_2_6.updateShip(var_2_7)
							elif var_2_4 == ShipBluePrint.STRENGTHEN_TYPE_SKIN:
								getProxy(ShipSkinProxy).addSkin(ShipSkin.New({
									id = iter_2_2[2]
								}))

								local var_2_8 = pg.ship_skin_template[iter_2_2[2]].name

								pg.TipsMgr.GetInstance().ShowTips(iter_2_2[3])
							elif var_2_4 == ShipBluePrint.STRENGTHEN_TYPE_BREAKOUT:
								local var_2_9 = getProxy(BayProxy).getShipById(var_1_4.shipId)

								arg_1_0.upgradeStar(var_2_9)
			elif var_1_4.fateLevel > var_2_0.fateLevel:
				for iter_2_5 = var_2_0.fateLevel + 1, var_1_4.fateLevel:
					local var_2_10 = var_1_4.getFateStrengthenConfig(iter_2_5)

					if var_2_10.special == 1 and type(var_2_10.special_effect) == "table":
						local var_2_11 = var_2_10.special_effect

						for iter_2_6, iter_2_7 in ipairs(var_2_11):
							if iter_2_7[1] == ShipBluePrint.STRENGTHEN_TYPE_CHANGE_SKILL:
								local var_2_12 = getProxy(BayProxy)
								local var_2_13 = var_2_12.getShipById(var_1_4.shipId)
								local var_2_14 = iter_2_7[2][1]
								local var_2_15 = iter_2_7[2][2]
								local var_2_16 = Clone(var_2_13.skills[var_2_14])

								assert(var_2_16, "shipVO without this skill" .. var_2_14)

								var_2_16.id = var_2_15
								var_2_13.skills[var_2_14] = None
								var_2_13.skills[var_2_15] = var_2_16

								pg.TipsMgr.GetInstance().ShowTips(iter_2_7[3])
								var_2_12.updateShip(var_2_13)

								local var_2_17 = getProxy(NavalAcademyProxy)
								local var_2_18 = var_2_17.getStudentByShipId(var_2_13.id)

								if var_2_18 and var_2_18.skillId == var_2_14:
									var_2_18.skillId = var_2_15

									var_2_17.updateStudent(var_2_18)

			local var_2_19 = var_1_8.getShipById(var_1_4.shipId)

			var_2_19.strengthList = {}

			table.insert(var_2_19.strengthList, {
				level = var_1_4.level + math.max(var_1_4.fateLevel, 0),
				exp = var_1_4.exp
			})
			var_1_8.updateShip(var_2_19)
			arg_1_0.sendNotification(GAME.MOD_BLUEPRINT_ANIM_LOCK)
			var_1_3.updateBluePrint(var_1_4)
			arg_1_0.sendNotification(GAME.MOD_BLUEPRINT_DONE, {
				oldBluePrint = var_2_0,
				newBluePrint = var_1_4
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("blueprint_mod_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("blueprint_mod_erro") .. arg_2_0.result))

def var_0_0.upgradeStar(arg_3_0, arg_3_1):
	local var_3_0 = Clone(arg_3_1)
	local var_3_1 = getProxy(CollectionProxy).getShipGroup(var_3_0.groupId)
	local var_3_2 = pg.ship_data_breakout[arg_3_1.configId]

	if var_3_2.breakout_id != 0:
		arg_3_1.configId = var_3_2.breakout_id

		local var_3_3 = pg.ship_data_template[arg_3_1.configId]

		for iter_3_0, iter_3_1 in ipairs(var_3_3.buff_list):
			if not arg_3_1.skills[iter_3_1]:
				arg_3_1.skills[iter_3_1] = {
					exp = 0,
					level = 1,
					id = iter_3_1
				}

		arg_3_1.updateMaxLevel(var_3_3.max_level)

		local var_3_4 = pg.ship_data_template[var_3_0.configId].buff_list

		for iter_3_2, iter_3_3 in ipairs(var_3_4):
			if not table.contains(var_3_3.buff_list, iter_3_3):
				arg_3_1.skills[iter_3_3] = None

		getProxy(BayProxy).updateShip(arg_3_1)

return var_0_0

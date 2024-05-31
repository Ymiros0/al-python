local var_0_0 = class("PursuingBluePrintCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.count
	local var_1_2 = var_1_0.id

	if var_1_1 == 0 then
		return
	end

	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3:getBluePrintById(var_1_2)

	if not var_1_4 then
		return
	end

	if not var_1_4:isUnlock() then
		return
	end

	local var_1_5 = getProxy(PlayerProxy):getRawData():getResource(PlayerConst.ResGold)
	local var_1_6 = var_1_3:calcPursuingCost(var_1_4, var_1_1)

	if var_1_5 < var_1_6 then
		return
	end

	if var_1_4:isMaxLevel() and var_1_4:isMaxFateLevel() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("blueprint_max_level_tip"))

		return
	end

	local var_1_7 = var_1_1 * var_1_4:getItemExp()
	local var_1_8 = Clone(var_1_4)

	var_1_8:addExp(var_1_7)

	local var_1_9 = var_1_8:getStrengthenConfig(math.max(var_1_8.level, 1))
	local var_1_10 = getProxy(BayProxy)

	if var_1_10:getShipById(var_1_4.shipId).level < var_1_9.need_lv then
		pg.TipsMgr.GetInstance():ShowTips(i18n("buleprint_need_level_tip", var_1_9.need_lv))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(63212, {
		ship_id = var_1_4.shipId,
		count = var_1_1
	}, 63213, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(PlayerProxy)
			local var_2_1 = var_2_0:getData()

			var_2_1:consume({
				gold = var_1_6
			})
			var_2_0:updatePlayer(var_2_1)
			var_1_3:addPursuingTimes(var_1_1, var_1_4:isRarityUR())

			local var_2_2 = Clone(var_1_4)
			local var_2_3 = var_1_4:getItemExp()

			var_1_4:addExp(var_2_3 * var_1_1)

			if var_1_4.level > var_2_2.level then
				for iter_2_0 = var_2_2.level + 1, var_1_4.level do
					local var_2_4 = var_1_4:getStrengthenConfig(iter_2_0)

					if var_2_4.special == 1 and type(var_2_4.special_effect) == "table" then
						local var_2_5 = var_2_4.special_effect

						for iter_2_1, iter_2_2 in ipairs(var_2_5) do
							local var_2_6 = iter_2_2[1]

							if var_2_6 == ShipBluePrint.STRENGTHEN_TYPE_SKILL then
								local var_2_7 = iter_2_2[2]
								local var_2_8 = getProxy(BayProxy)
								local var_2_9 = var_2_8:getShipById(var_1_4.shipId)

								for iter_2_3, iter_2_4 in ipairs(var_2_7) do
									var_2_9.skills[var_1_2] = {
										exp = 0,
										level = 1,
										id = iter_2_4
									}

									pg.TipsMgr.GetInstance():ShowTips(iter_2_2[3])
								end

								var_2_8:updateShip(var_2_9)
							elseif var_2_6 == ShipBluePrint.STRENGTHEN_TYPE_SKIN then
								getProxy(ShipSkinProxy):addSkin(ShipSkin.New({
									id = iter_2_2[2]
								}))

								local var_2_10 = pg.ship_skin_template[iter_2_2[2]].name

								pg.TipsMgr.GetInstance():ShowTips(iter_2_2[3])
							elseif var_2_6 == ShipBluePrint.STRENGTHEN_TYPE_BREAKOUT then
								local var_2_11 = getProxy(BayProxy):getShipById(var_1_4.shipId)

								arg_1_0:upgradeStar(var_2_11)
							end
						end
					end
				end
			elseif var_1_4.fateLevel > var_2_2.fateLevel then
				for iter_2_5 = var_2_2.fateLevel + 1, var_1_4.fateLevel do
					local var_2_12 = var_1_4:getFateStrengthenConfig(iter_2_5)

					if var_2_12.special == 1 and type(var_2_12.special_effect) == "table" then
						local var_2_13 = var_2_12.special_effect

						for iter_2_6, iter_2_7 in ipairs(var_2_13) do
							if iter_2_7[1] == ShipBluePrint.STRENGTHEN_TYPE_CHANGE_SKILL then
								local var_2_14 = getProxy(BayProxy)
								local var_2_15 = var_2_14:getShipById(var_1_4.shipId)
								local var_2_16 = iter_2_7[2][1]
								local var_2_17 = iter_2_7[2][2]
								local var_2_18 = Clone(var_2_15.skills[var_2_16])

								assert(var_2_18, "shipVO without this skill" .. var_2_16)

								var_2_18.id = var_2_17
								var_2_15.skills[var_2_16] = nil
								var_2_15.skills[var_2_17] = var_2_18

								pg.TipsMgr.GetInstance():ShowTips(iter_2_7[3])
								var_2_14:updateShip(var_2_15)

								local var_2_19 = getProxy(NavalAcademyProxy)
								local var_2_20 = var_2_19:getStudentByShipId(var_2_15.id)

								if var_2_20 and var_2_20.skillId == var_2_16 then
									var_2_20.skillId = var_2_17

									var_2_19:updateStudent(var_2_20)
								end
							end
						end
					end
				end
			end

			local var_2_21 = var_1_10:getShipById(var_1_4.shipId)

			var_2_21.strengthList = {}

			table.insert(var_2_21.strengthList, {
				level = var_1_4.level + math.max(var_1_4.fateLevel, 0),
				exp = var_1_4.exp
			})
			var_1_10:updateShip(var_2_21)
			arg_1_0:sendNotification(GAME.MOD_BLUEPRINT_ANIM_LOCK)
			var_1_3:updateBluePrint(var_1_4)
			arg_1_0:sendNotification(GAME.MOD_BLUEPRINT_DONE, {
				oldBluePrint = var_2_2,
				newBluePrint = var_1_4
			})
			pg.TipsMgr.GetInstance():ShowTips(i18n("blueprint_mod_success"))
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("blueprint_mod_erro") .. arg_2_0.result)
		end
	end)
end

function var_0_0.upgradeStar(arg_3_0, arg_3_1)
	local var_3_0 = Clone(arg_3_1)
	local var_3_1 = getProxy(CollectionProxy):getShipGroup(var_3_0.groupId)
	local var_3_2 = pg.ship_data_breakout[arg_3_1.configId]

	if var_3_2.breakout_id ~= 0 then
		arg_3_1.configId = var_3_2.breakout_id

		local var_3_3 = pg.ship_data_template[arg_3_1.configId]

		for iter_3_0, iter_3_1 in ipairs(var_3_3.buff_list) do
			if not arg_3_1.skills[iter_3_1] then
				arg_3_1.skills[iter_3_1] = {
					exp = 0,
					level = 1,
					id = iter_3_1
				}
			end
		end

		arg_3_1:updateMaxLevel(var_3_3.max_level)

		local var_3_4 = pg.ship_data_template[var_3_0.configId].buff_list

		for iter_3_2, iter_3_3 in ipairs(var_3_4) do
			if not table.contains(var_3_3.buff_list, iter_3_3) then
				arg_3_1.skills[iter_3_3] = nil
			end
		end

		getProxy(BayProxy):updateShip(arg_3_1)
	end
end

return var_0_0

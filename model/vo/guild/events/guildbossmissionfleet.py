local var_0_0 = class("GuildBossMissionFleet", import("...BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.fleet_id
	arg_1_0.userShips = {}
	arg_1_0.commanders = {}
	arg_1_0.invaildShips = {}
	arg_1_0.invaildCommanders = {}

	if arg_1_1.ships:
		arg_1_0.Flush(arg_1_1)

def var_0_0.Flush(arg_2_0, arg_2_1):
	arg_2_0.userShips = {}
	arg_2_0.invaildShips = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.ships):
		local var_2_0 = {
			uid = iter_2_1.user_id,
			id = iter_2_1.ship_id
		}

		if arg_2_0.IsVaildShip(var_2_0):
			table.insert(arg_2_0.userShips, var_2_0)
		else
			table.insert(arg_2_0.invaildShips, var_2_0)

	local var_2_1 = getProxy(CommanderProxy).getData()
	local var_2_2 = {}

	for iter_2_2, iter_2_3 in pairs(arg_2_1.commanders):
		local var_2_3 = var_2_1[iter_2_3.id]

		if var_2_3 and iter_2_3.pos:
			var_2_2[iter_2_3.pos] = var_2_3
		else
			table.insert(arg_2_0.invaildCommanders, iter_2_3.id)

	arg_2_0.UpdateCommander(var_2_2)

def var_0_0.GetName(arg_3_0):
	if arg_3_0.IsMainFleet():
		return i18n("ship_formationUI_fleetName11")
	else
		return i18n("ship_formationUI_fleetName1")

def var_0_0.ExistMember(arg_4_0, arg_4_1):
	local var_4_0 = getProxy(GuildProxy).getRawData()

	return var_4_0 and var_4_0.getMemberById(arg_4_1)

def var_0_0.IsVaildShip(arg_5_0, arg_5_1):
	local function var_5_0(arg_6_0)
		local var_6_0 = getProxy(GuildProxy).getRawData()

		if getProxy(PlayerProxy).getRawData().id == arg_6_0.uid:
			return getProxy(BayProxy).getShipById(arg_6_0.id) != None

		local var_6_1 = var_6_0.getMemberById(arg_6_0.uid).GetAssaultFleet()
		local var_6_2 = GuildAssaultFleet.GetVirtualId(arg_6_0.uid, arg_6_0.id)

		return (var_6_1.ExistShip(var_6_2))

	local function var_5_1(arg_7_0)
		return pg.ShipFlagMgr.GetInstance().GetShipFlag(arg_7_0.id, "inEvent")

	return arg_5_0.ExistMember(arg_5_1.uid) and var_5_0(arg_5_1) and not var_5_1(arg_5_1)

def var_0_0.ExistInvailShips(arg_8_0):
	if #arg_8_0.invaildShips > 0:
		return True

	if _.any(arg_8_0.userShips, function(arg_9_0)
		return not arg_8_0.IsVaildShip(arg_9_0)):
		return True

	return False

def var_0_0.ClearInvaildShip(arg_10_0):
	arg_10_0.invaildShips = {}

	for iter_10_0 = #arg_10_0.userShips, 1, -1:
		local var_10_0 = arg_10_0.userShips[iter_10_0]

		if not arg_10_0.IsVaildShip(var_10_0):
			table.remove(arg_10_0.userShips, iter_10_0)

def var_0_0.GetMyShipIds(arg_11_0):
	local var_11_0 = {}
	local var_11_1 = getProxy(PlayerProxy).getRawData().id

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.userShips):
		if iter_11_1.uid == var_11_1:
			table.insert(var_11_0, iter_11_1.id)

	return var_11_0

def var_0_0.GetShipIds(arg_12_0):
	return arg_12_0.userShips

def var_0_0.GetShips(arg_13_0):
	local var_13_0 = getProxy(PlayerProxy).getData()
	local var_13_1 = getProxy(GuildProxy).getData()
	local var_13_2 = getProxy(BayProxy)
	local var_13_3 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.userShips):
		if var_13_0.id == iter_13_1.uid:
			local var_13_4 = var_13_2.getShipById(iter_13_1.id)

			if var_13_4:
				var_13_4.id = GuildAssaultFleet.GetVirtualId(var_13_0.id, var_13_4.id)

				local var_13_5 = GuildBossMissionShip.New(var_13_4)

				table.insert(var_13_3, {
					member = var_13_0,
					ship = var_13_5
				})
		else
			local var_13_6 = var_13_1.getMemberById(iter_13_1.uid)
			local var_13_7 = var_13_6 and var_13_6.GetAssaultFleet()
			local var_13_8 = var_13_7 and var_13_7.GetShipByRealId(iter_13_1.uid, iter_13_1.id)

			if var_13_8:
				local var_13_9 = GuildBossMissionShip.New(var_13_8)

				table.insert(var_13_3, {
					member = var_13_6,
					ship = var_13_9
				})

	return var_13_3

def var_0_0.GetDownloadResShips(arg_14_0):
	local var_14_0 = getProxy(PlayerProxy).getRawData()
	local var_14_1 = arg_14_0.GetShips()
	local var_14_2 = {}

	for iter_14_0, iter_14_1 in pairs(var_14_1):
		if iter_14_1.member.id != var_14_0.id:
			table.insert(var_14_2, iter_14_1.ship.getPainting())

	return var_14_2

def var_0_0.GetTeamTypeShips(arg_15_0, arg_15_1):
	local var_15_0 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.GetShips()):
		local var_15_1 = iter_15_1.ship

		if var_15_1.getTeamType() == arg_15_1:
			table.insert(var_15_0, var_15_1)

	return var_15_0

def var_0_0.ExistSubShip(arg_16_0):
	return #arg_16_0.GetTeamTypeShips(TeamType.Submarine) > 0

def var_0_0.RemoveAll(arg_17_0):
	arg_17_0.userShips = {}

def var_0_0.IsMainFleet(arg_18_0):
	return arg_18_0.id == 1

def var_0_0.ExistUserShip(arg_19_0, arg_19_1):
	return _.any(arg_19_0.userShips, function(arg_20_0)
		return arg_20_0.uid == arg_19_1)

def var_0_0.ContainShip(arg_21_0, arg_21_1, arg_21_2):
	return _.any(arg_21_0.userShips, function(arg_22_0)
		return arg_22_0.uid == arg_21_1 and arg_22_0.id == arg_21_2)

def var_0_0.RemoveUserShip(arg_23_0, arg_23_1, arg_23_2):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.userShips):
		if iter_23_1.uid == arg_23_1 and iter_23_1.id == arg_23_2:
			table.remove(arg_23_0.userShips, iter_23_0)

			return iter_23_0

def var_0_0.AddUserShip(arg_24_0, arg_24_1, arg_24_2, arg_24_3):
	if arg_24_3:
		table.insert(arg_24_0.userShips, arg_24_3, {
			uid = arg_24_1,
			id = arg_24_2
		})
	else
		table.insert(arg_24_0.userShips, {
			uid = arg_24_1,
			id = arg_24_2
		})

def var_0_0.GetOtherMemberShipCnt(arg_25_0, arg_25_1):
	local var_25_0 = 0

	for iter_25_0, iter_25_1 in ipairs(arg_25_0.userShips):
		if iter_25_1.uid != arg_25_1:
			var_25_0 = var_25_0 + 1

	return var_25_0

def var_0_0.ExistSameKindShip(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_0.GetShips()

	for iter_26_0, iter_26_1 in pairs(var_26_0):
		if iter_26_1.ship.isSameKind(arg_26_1):
			return True

	return False

def var_0_0.IsLegal(arg_27_0):
	local var_27_0 = arg_27_0.GetShips()
	local var_27_1 = 0
	local var_27_2 = 0
	local var_27_3 = 0
	local var_27_4 = 0
	local var_27_5 = 0
	local var_27_6 = 0
	local var_27_7 = getProxy(PlayerProxy).getRawData().id

	for iter_27_0, iter_27_1 in ipairs(var_27_0):
		if iter_27_1 and iter_27_1.ship.getTeamType() == TeamType.Main:
			var_27_1 = var_27_1 + 1

			if iter_27_1.member.id == var_27_7:
				var_27_4 = var_27_4 + 1
		elif iter_27_1 and iter_27_1.ship.getTeamType() == TeamType.Vanguard:
			var_27_2 = var_27_2 + 1

			if iter_27_1.member.id == var_27_7:
				var_27_5 = var_27_5 + 1
		elif iter_27_1 and iter_27_1.ship.getTeamType() == TeamType.Submarine:
			var_27_3 = var_27_3 + 1

			if iter_27_1.member.id == var_27_7:
				var_27_6 = var_27_6 + 1

		local var_27_8 = GuildAssaultFleet.GetRealId(iter_27_1.ship.id)

		if pg.ShipFlagMgr.GetInstance().GetShipFlag(var_27_8, "inEvent"):
			return False, i18n("guild_boss_formation_exist_event_ship", iter_27_1.ship.getConfig("name"))

	if var_27_1 > 3 or var_27_2 > 3 or var_27_3 > 3:
		return False, i18n("guild_boss_fleet_cnt_invaild")

	local var_27_9 = var_27_5 > 0 and var_27_4 > 0
	local var_27_10

	if var_27_1 > 0 and var_27_2 > 0 and not var_27_9:
		var_27_10 = i18n("guild_boss_formation_not_exist_self_ship")
	else
		var_27_10 = i18n("guild_fleet_is_legal")

	if arg_27_0.IsMainFleet():
		return var_27_1 > 0 and var_27_2 > 0 and var_27_9, var_27_10
	else
		return True

def var_0_0.ResortShips(arg_28_0, arg_28_1):
	local function var_28_0(arg_29_0)
		local var_29_0 = GuildAssaultFleet.GetVirtualId(arg_29_0.uid, arg_29_0.id)

		for iter_29_0, iter_29_1 in ipairs(arg_28_1):
			if var_29_0 == iter_29_1.shipId:
				return iter_29_0

		return 0

	table.sort(arg_28_0.userShips, function(arg_30_0, arg_30_1)
		return var_28_0(arg_30_0) < var_28_0(arg_30_1))

def var_0_0.UpdateCommander(arg_31_0, arg_31_1):
	arg_31_0.commanders = arg_31_1
	arg_31_0.skills = {}

	arg_31_0.updateCommanderSkills()

def var_0_0.ClearCommanders(arg_32_0):
	for iter_32_0, iter_32_1 in pairs(arg_32_0.commanders):
		arg_32_0.RemoveCommander(iter_32_0)

def var_0_0.getCommanders(arg_33_0):
	return arg_33_0.commanders

def var_0_0.AddCommander(arg_34_0, arg_34_1, arg_34_2):
	arg_34_0.commanders[arg_34_1] = arg_34_2
	arg_34_0.skills = {}

	arg_34_0.updateCommanderSkills()

def var_0_0.RemoveCommander(arg_35_0, arg_35_1):
	arg_35_0.commanders[arg_35_1] = None
	arg_35_0.skills = {}

	arg_35_0.updateCommanderSkills()

def var_0_0.GetCommanderPos(arg_36_0, arg_36_1):
	for iter_36_0, iter_36_1 in pairs(arg_36_0.commanders):
		if iter_36_1.id == arg_36_1:
			return iter_36_0

	return False

def var_0_0.updateCommanderSkills(arg_37_0):
	local var_37_0 = #arg_37_0.skills

	while var_37_0 > 0:
		local var_37_1 = arg_37_0.skills[var_37_0]

		if not arg_37_0.findCommanderBySkillId(var_37_1.id) and var_37_1.GetSystem() == FleetSkill.SystemCommanderNeko:
			table.remove(arg_37_0.skills, var_37_0)

		var_37_0 = var_37_0 - 1

	local var_37_2 = arg_37_0.getCommanders()

	for iter_37_0, iter_37_1 in pairs(var_37_2):
		for iter_37_2, iter_37_3 in ipairs(iter_37_1.getSkills()):
			for iter_37_4, iter_37_5 in ipairs(iter_37_3.getTacticSkill()):
				table.insert(arg_37_0.skills, FleetSkill.New(FleetSkill.SystemCommanderNeko, iter_37_5))

def var_0_0.findSkills(arg_38_0, arg_38_1):
	return _.filter(arg_38_0.getSkills(), function(arg_39_0)
		return arg_39_0.GetType() == arg_38_1)

def var_0_0.findCommanderBySkillId(arg_40_0, arg_40_1):
	local var_40_0 = arg_40_0.getCommanders()

	for iter_40_0, iter_40_1 in pairs(var_40_0):
		if _.any(iter_40_1.getSkills(), function(arg_41_0)
			return _.any(arg_41_0.getTacticSkill(), function(arg_42_0)
				return arg_42_0 == arg_40_1)):
			return iter_40_1

def var_0_0.getSkills(arg_43_0):
	return arg_43_0.skills or {}

def var_0_0.getFleetType(arg_44_0):
	if arg_44_0.id == GuildBossMission.MAIN_FLEET_ID:
		return FleetType.Normal
	elif arg_44_0.id == GuildBossMission.SUB_FLEET_ID:
		return FleetType.Submarine

	assert(False, arg_44_0.id)

def var_0_0.BuildBattleBuffList(arg_45_0):
	local var_45_0 = {}
	local var_45_1, var_45_2 = FleetSkill.GuildBossTriggerSkill(arg_45_0, FleetSkill.TypeBattleBuff)

	if var_45_1 and #var_45_1 > 0:
		local var_45_3 = {}

		for iter_45_0, iter_45_1 in ipairs(var_45_1):
			local var_45_4 = var_45_2[iter_45_0]
			local var_45_5 = arg_45_0.findCommanderBySkillId(var_45_4.id)

			var_45_3[var_45_5] = var_45_3[var_45_5] or {}

			table.insert(var_45_3[var_45_5], iter_45_1)

		for iter_45_2, iter_45_3 in pairs(var_45_3):
			table.insert(var_45_0, {
				iter_45_2,
				iter_45_3
			})

	local var_45_6 = arg_45_0.getCommanders()

	for iter_45_4, iter_45_5 in pairs(var_45_6):
		local var_45_7 = iter_45_5.getTalents()

		for iter_45_6, iter_45_7 in ipairs(var_45_7):
			local var_45_8 = iter_45_7.getBuffsAddition()

			if #var_45_8 > 0:
				local var_45_9

				for iter_45_8, iter_45_9 in ipairs(var_45_0):
					if iter_45_9[1] == iter_45_5:
						var_45_9 = iter_45_9[2]

						break

				if not var_45_9:
					var_45_9 = {}

					table.insert(var_45_0, {
						iter_45_5,
						var_45_9
					})

				for iter_45_10, iter_45_11 in ipairs(var_45_8):
					table.insert(var_45_9, iter_45_11)

	return var_45_0

def var_0_0.ExistCommander(arg_46_0, arg_46_1):
	local var_46_0 = arg_46_0.getCommanders()

	for iter_46_0, iter_46_1 in pairs(var_46_0):
		if iter_46_1.id == arg_46_1:
			return True

	return False

def var_0_0.ExistInvaildCommanders(arg_47_0):
	if #arg_47_0.invaildCommanders > 0:
		return True

	local var_47_0 = arg_47_0.getCommanders()
	local var_47_1 = getProxy(CommanderProxy)

	for iter_47_0, iter_47_1 in pairs(var_47_0):
		if not var_47_1.getCommanderById(iter_47_1.id):
			return True

	return False

def var_0_0.RemoveInvaildCommanders(arg_48_0):
	local var_48_0 = arg_48_0.getCommanders()
	local var_48_1 = getProxy(CommanderProxy)

	for iter_48_0, iter_48_1 in pairs(var_48_0):
		if not var_48_1.getCommanderById(iter_48_1.id):
			arg_48_0.RemoveCommander(iter_48_0)

	arg_48_0.invaildCommanders = {}

def var_0_0.getCommandersAddition(arg_49_0):
	local var_49_0 = {}

	for iter_49_0, iter_49_1 in pairs(CommanderConst.PROPERTIES):
		local var_49_1 = 0

		for iter_49_2, iter_49_3 in pairs(arg_49_0.getCommanders()):
			var_49_1 = var_49_1 + iter_49_3.getAbilitysAddition()[iter_49_1]

		if var_49_1 > 0:
			table.insert(var_49_0, {
				attrName = iter_49_1,
				value = var_49_1
			})

	return var_49_0

def var_0_0.getCommandersTalentDesc(arg_50_0):
	local var_50_0 = {}

	for iter_50_0, iter_50_1 in pairs(arg_50_0.getCommanders()):
		local var_50_1 = iter_50_1.getTalentsDesc()

		for iter_50_2, iter_50_3 in pairs(var_50_1):
			if var_50_0[iter_50_2]:
				var_50_0[iter_50_2].value = var_50_0[iter_50_2].value + iter_50_3.value
			else
				var_50_0[iter_50_2] = {
					name = iter_50_2,
					value = iter_50_3.value,
					type = iter_50_3.type
				}

	return var_50_0

def var_0_0.ExistAnyCommander(arg_51_0):
	local var_51_0 = arg_51_0.getCommanders()

	return table.getCount(var_51_0) != 0

return var_0_0

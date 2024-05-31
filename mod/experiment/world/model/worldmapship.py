local var_0_0 = class("WorldMapShip", import("...BaseEntity"))

var_0_0.Fields = {
	fleetId = "number",
	buffs = "table",
	triggers = "table",
	id = "number",
	hpRant = "number"
}
var_0_0.EventHpRantChange = "WorldMapShip.EventHpRantChange"
var_0_0.EventUpdateBuff = "WorldMapShip.EventUpdateBuff"
var_0_0.EventUpdateBroken = "WorldMapShip.EventUpdateBroken"

def var_0_0.Build(arg_1_0):
	arg_1_0.id = None
	arg_1_0.hpRant = 10000
	arg_1_0.buffs = {}
	arg_1_0.triggers = {}

def var_0_0.Setup(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.hpRant = arg_2_1.hp_rant
	arg_2_0.buffs = WorldConst.ParsingBuffs(arg_2_1.buff_list)

def var_0_0.Dispose(arg_3_0):
	arg_3_0.Clear()

def var_0_0.GetImportWorldShipVO(arg_4_0):
	return setmetatable({
		triggers = arg_4_0.triggers,
		isBroken = arg_4_0.IsBroken(),
		def IsBenefitSkillActive:(arg_5_0, arg_5_1)
			local var_5_0 = False

			if arg_5_1.type == Ship.BENEFIT_SKILL:
				if not arg_5_0.isBroken and (not arg_5_1.limit[1] or arg_5_1.limit[1] == arg_5_0.triggers.TeamNumbers):
					var_5_0 = True
			elif arg_5_1.type == Ship.BENEFIT_EQUIP:
				local var_5_1 = arg_5_1.limit
				local var_5_2 = arg_5_0.getAllEquipments()

				for iter_5_0, iter_5_1 in ipairs(var_5_2):
					if iter_5_1 and table.contains(var_5_1, iter_5_1.getConfig("id")):
						var_5_0 = True

						break
			elif arg_5_1.type == Ship.BENEFIT_MAP_AURA:
				var_5_0 = not arg_5_0.isBroken
			elif arg_5_1.type == Ship.BENEFIT_AID:
				var_5_0 = not arg_5_0.isBroken

			return var_5_0,
		def GetStaminaDiscount:(arg_6_0, arg_6_1)
			local var_6_0 = 0

			if arg_6_1 == WorldConst.OpReqSub:
				for iter_6_0, iter_6_1 in pairs(arg_6_0.getAllSkills()):
					local var_6_1 = tonumber(iter_6_0 .. string.format("%.2d", iter_6_1.level))
					local var_6_2 = pg.skill_benefit_template[var_6_1]

					if var_6_2 and arg_6_0.IsBenefitSkillActive(var_6_2) and (var_6_2.type == Ship.BENEFIT_EQUIP or var_6_2.type == Ship.BENEFIT_SKILL):
						var_6_0 = var_6_0 + defaultValue(var_6_2.world_extra_effect[1], 0)

			return var_6_0
	}, {
		__index = WorldConst.FetchRawShipVO(arg_4_0.id)
	})

def var_0_0.UpdateHpRant(arg_7_0, arg_7_1):
	if arg_7_0.hpRant != arg_7_1:
		arg_7_0.hpRant = arg_7_1

		arg_7_0.DispatchEvent(var_0_0.EventHpRantChange)

def var_0_0.IsValid(arg_8_0):
	return tobool(WorldConst.FetchRawShipVO(arg_8_0.id))

def var_0_0.IsAlive(arg_9_0):
	return arg_9_0.hpRant > 0

def var_0_0.IsHpFull(arg_10_0):
	return arg_10_0.hpRant == 10000

def var_0_0.IsHpSafe(arg_11_0):
	return arg_11_0.hpRant >= 3000

def var_0_0.GetBuffList(arg_12_0):
	local var_12_0 = underscore.filter(underscore.values(arg_12_0.buffs), function(arg_13_0)
		return arg_13_0.GetFloor() > 0)
	local var_12_1 = arg_12_0.fleetId and nowWorld().GetFleet(arg_12_0.fleetId).GetDamageBuff()

	if var_12_1:
		table.insert(var_12_0, var_12_1)

	return var_12_0

def var_0_0.GetBuff(arg_14_0, arg_14_1):
	if not arg_14_0.buffs[arg_14_1]:
		arg_14_0.buffs[arg_14_1] = WorldBuff.New()

		arg_14_0.buffs[arg_14_1].Setup({
			floor = 0,
			id = arg_14_1
		})

	return arg_14_0.buffs[arg_14_1]

def var_0_0.AddBuff(arg_15_0, arg_15_1, arg_15_2):
	assert(arg_15_1 and arg_15_2)
	arg_15_0.GetBuff(arg_15_1).AddFloor(arg_15_2)

	if arg_15_1 == WorldConst.BrokenBuffId:
		arg_15_0.DispatchEvent(var_0_0.EventUpdateBroken)

	arg_15_0.DispatchEvent(var_0_0.EventUpdateBuff)

def var_0_0.RemoveBuff(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = arg_16_0.GetBuff(arg_16_1)

	if arg_16_2:
		var_16_0.AddFloor(arg_16_2 * -1)
	else
		arg_16_0.buffs[arg_16_1] = None

	if arg_16_1 == WorldConst.BrokenBuffId:
		arg_16_0.DispatchEvent(var_0_0.EventUpdateBroken)

	arg_16_0.DispatchEvent(var_0_0.EventUpdateBuff)

def var_0_0.IsBuffMax(arg_17_0, arg_17_1):
	return arg_17_0.GetBuff(arg_17_1).GetFloor() >= WorldBuff.GetTemplate(arg_17_1).buff_maxfloor

def var_0_0.Rebirth(arg_18_0):
	assert(arg_18_0.hpRant <= 0)

	local var_18_0 = pg.gameset.world_death_hpfix.key_value

	arg_18_0.UpdateHpRant(var_18_0)
	arg_18_0.AddBuff(WorldConst.BrokenBuffId, 1)

def var_0_0.Repair(arg_19_0):
	arg_19_0.UpdateHpRant(10000)
	arg_19_0.RemoveBuff(WorldConst.BrokenBuffId)

def var_0_0.Regenerate(arg_20_0, arg_20_1):
	local var_20_0 = math.min(10000, arg_20_0.hpRant + arg_20_1)

	arg_20_0.UpdateHpRant(var_20_0)

def var_0_0.RegenerateValue(arg_21_0, arg_21_1):
	local var_21_0 = math.floor(arg_21_1 / WorldConst.FetchShipVO(arg_21_0.id).getProperties(None, True, False)[AttributeType.Durability] * 10000)
	local var_21_1 = math.min(10000, arg_21_0.hpRant + var_21_0)

	arg_21_0.UpdateHpRant(var_21_1)

def var_0_0.IsBroken(arg_22_0):
	return arg_22_0.GetBuff(WorldConst.BrokenBuffId).GetFloor() > 0

def var_0_0.GetShipBuffProperties(arg_23_0):
	local var_23_0 = {}
	local var_23_1 = {}
	local var_23_2 = arg_23_0.fleetId and nowWorld().GetFleet(arg_23_0.fleetId).GetBuffList() or {}

	WorldConst.AppendPropertiesFromBuffList(var_23_0, var_23_1, var_23_2)

	return var_23_0, var_23_1

def var_0_0.GetShipPowerBuffProperties(arg_24_0):
	local var_24_0 = {}
	local var_24_1 = arg_24_0.GetBuffList()

	WorldConst.ExtendPropertiesRatesFromBuffList(var_24_0, var_24_1)

	return var_24_0

return var_0_0

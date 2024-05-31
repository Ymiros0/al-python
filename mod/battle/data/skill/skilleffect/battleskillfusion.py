ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr
local var_0_2 = var_0_0.Battle.BattleTargetChoise

var_0_0.Battle.BattleSkillFusion = class("BattleSkillFusion", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillFusion.__name = "BattleSkillFusion"

local var_0_3 = var_0_0.Battle.BattleSkillFusion

var_0_3.FREEZE_POS = {
	Vector3(-10000, 0, 58),
	[-1] = Vector3(10000, 0, 58)
}

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._fusionUnitTempID = arg_1_0._tempData.arg_list.fusion_id
	arg_1_0._fusionUnitSkinID = arg_1_0._tempData.arg_list.ship_skin_id
	arg_1_0._elementTagList = arg_1_0._tempData.arg_list.element_tag_list
	arg_1_0._attrInheritList = arg_1_0._tempData.arg_list.attr_inherit_list
	arg_1_0._fusionUnitEquipmentList = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0._tempData.arg_list.weapon_id_list):
		table.insert(arg_1_0._fusionUnitEquipmentList, {
			id = iter_1_1,
			equipment = {
				weapon_id = {
					iter_1_1
				}
			}
		})

	arg_1_0._fusionUnitSkillList = {}

	for iter_1_2, iter_1_3 in ipairs(arg_1_0._tempData.arg_list.buff_list):
		table.insert(arg_1_0._fusionUnitSkillList, {
			id = iter_1_3,
			level = arg_1_0._level
		})

	arg_1_0._duration = arg_1_0._tempData.arg_list.duration

def var_0_3.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.doFusion(arg_2_1)

def var_0_3.DoDataEffectWithoutTarget(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.doFusion(arg_3_1)

def var_0_3.doFusion(arg_4_0, arg_4_1):
	local var_4_0 = var_0_2.TargetAllHelp(arg_4_1)
	local var_4_1 = var_0_2.TargetShipTag(arg_4_1, {
		ship_tag_list = arg_4_0._elementTagList
	}, var_4_0)
	local var_4_2 = {}

	for iter_4_0, iter_4_1 in ipairs(Ship.PROPERTIES):
		var_4_2[iter_4_1] = 1

	local var_4_3 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_4_4 = {
		name = "123",
		shipGS = 1,
		id = arg_4_1.id,
		tmpID = arg_4_0._fusionUnitTempID,
		skinId = arg_4_0._fusionUnitSkinID,
		level = var_0_1.GetCurrent(arg_4_1, "formulaLevel"),
		equipment = arg_4_0._fusionUnitEquipmentList,
		properties = var_4_2,
		baseProperties = var_4_2,
		proficiency = {
			1,
			1,
			1
		},
		rarity = arg_4_1.GetRarity(),
		intimacy = arg_4_1.GetIntimacy(),
		skills = arg_4_0._fusionUnitSkillList,
		baseList = {
			1,
			1,
			1
		},
		preloasList = {
			0,
			0,
			0
		}
	}
	local var_4_5 = var_4_3.SpawnFusionUnit(arg_4_1, var_4_4, var_4_1, arg_4_0._attrInheritList)
	local var_4_6 = var_4_5.GetHP()
	local var_4_7 = {}

	for iter_4_2, iter_4_3 in ipairs(var_4_1):
		if iter_4_3.IsMainFleetUnit():
			var_4_7[iter_4_3] = Clone(iter_4_3.GetPosition())

		var_4_3.FreezeUnit(iter_4_3)
		iter_4_3.SetPosition(var_0_3.FREEZE_POS[iter_4_3.GetIFF()])

	if arg_4_1.IsMainFleetUnit():
		var_4_7[arg_4_1] = Clone(arg_4_1.GetPosition())

	var_4_3.FreezeUnit(arg_4_1)
	arg_4_1.SetPosition(var_0_3.FREEZE_POS[arg_4_1.GetIFF()])

	arg_4_0._fusionTimer = None

	local function var_4_8()
		local var_5_0, var_5_1 = var_4_5.GetHP()
		local var_5_2 = var_5_1 - var_5_0
		local var_5_3 = 0
		local var_5_4 = var_4_5.GetPosition()
		local var_5_5 = var_4_5.GetAttrByName("hpProvideRate")

		if arg_4_1.IsMainFleetUnit():
			arg_4_1.SetPosition(var_4_7[arg_4_1])
		else
			arg_4_1.SetPosition(Clone(var_5_4))

		local var_5_6 = math.floor(var_5_2 * var_5_5[arg_4_1.GetAttrByName("id")])

		var_4_3.HandleDirectDamage(arg_4_1, var_5_6)
		var_4_3.ActiveFreezeUnit(arg_4_1)

		for iter_5_0, iter_5_1 in ipairs(var_4_1):
			if iter_5_1.IsMainFleetUnit():
				iter_5_1.SetPosition(var_4_7[iter_5_1])
			else
				iter_5_1.SetPosition(Clone(var_5_4))

			local var_5_7 = math.floor(var_5_2 * var_5_5[iter_5_1.GetAttrByName("id")])

			var_4_3.HandleDirectDamage(iter_5_1, var_5_7)
			var_4_3.ActiveFreezeUnit(iter_5_1)

		var_4_3.DefusionUnit(var_4_5)
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_4_0._fusionTimer)

	arg_4_0._fusionTimer = pg.TimeMgr.GetInstance().AddBattleTimer("fusionSkillTimer", 0, arg_4_0._duration, var_4_8, True)

def var_0_3.Clear(arg_6_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_6_0._fusionTimer)
	var_0_3.super.Clear(arg_6_0)

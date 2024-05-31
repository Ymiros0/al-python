ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleFormulas

var_0_0.Battle.BattleDataFunction = var_0_0.Battle.BattleDataFunction or {}

local var_0_3 = var_0_0.Battle.BattleDataFunction
local var_0_4 = pg.puzzle_card_template
local var_0_5 = pg.puzzle_ship_template
local var_0_6 = pg.puzzle_combat_template
local var_0_7 = pg.puzzle_card_affix

def var_0_3.GetDungeonTmpDataByID(arg_1_0):
	return require("GameCfg.dungeon." .. arg_1_0)

def var_0_3.ClearDungeonCfg(arg_2_0):
	package.loaded["GameCfg.dungeon." .. arg_2_0] = None

def var_0_3.GetSkillTemplate(arg_3_0, arg_3_1):
	arg_3_1 = arg_3_1 or 1

	local var_3_0 = "skill_" .. arg_3_0
	local var_3_1 = pg.ConvertedSkill[var_3_0]
	local var_3_2 = var_3_1[arg_3_1] or var_3_1[0]

	var_3_2.name = getSkillName(arg_3_0)

	return var_3_2

def var_0_3.ConvertSkillTemplate():
	pg.ConvertedSkill = {}

	setmetatable(pg.ConvertedSkill, {
		def __index:(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_1
			local var_5_1 = pg.skillCfg[arg_5_1]

			if var_5_1:
				local var_5_2 = {}
				local var_5_3 = {}

				for iter_5_0, iter_5_1 in pairs(var_5_1):
					var_5_3[iter_5_0] = Clone(iter_5_1)

				var_5_2[0] = var_5_3

				for iter_5_2, iter_5_3 in ipairs(var_5_1):
					local var_5_4 = Clone(var_5_3)

					for iter_5_4, iter_5_5 in pairs(iter_5_3):
						var_5_4[iter_5_4] = iter_5_5

					var_5_2[iter_5_2] = var_5_4

				pg.ConvertedSkill[var_5_0] = var_5_2

				return var_5_2
	})

def var_0_3.GetBuffTemplate(arg_6_0, arg_6_1):
	arg_6_1 = arg_6_1 or 1

	local var_6_0 = "buff_" .. arg_6_0
	local var_6_1 = pg.ConvertedBuff[var_6_0]

	return var_6_1[arg_6_1] or var_6_1[0]

def var_0_3.ConvertBuffTemplate():
	pg.ConvertedBuff = {}

	setmetatable(pg.ConvertedBuff, {
		def __index:(arg_8_0, arg_8_1)
			local var_8_0 = arg_8_1
			local var_8_1 = pg.buffCfg[arg_8_1]

			if var_8_1:
				local var_8_2 = {}
				local var_8_3 = {}

				for iter_8_0, iter_8_1 in pairs(var_8_1):
					var_8_3[iter_8_0] = Clone(iter_8_1)

				var_8_2[0] = var_8_3

				for iter_8_2, iter_8_3 in ipairs(var_8_1):
					local var_8_4 = Clone(var_8_3)

					for iter_8_4, iter_8_5 in pairs(iter_8_3):
						var_8_4[iter_8_4] = iter_8_5

					var_8_2[iter_8_2] = var_8_4

				pg.ConvertedBuff[var_8_0] = var_8_2

				return var_8_2
	})

def var_0_3.GetBuffBulletRes(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	local var_9_0 = {}
	local var_9_1 = {}

	arg_9_1 = arg_9_1 or {}

	local var_9_2 = var_0_3.GetPlayerShipModelFromID(arg_9_0)

	local function var_9_3(arg_10_0)
		for iter_10_0, iter_10_1 in ipairs(arg_10_0):
			local var_10_0

			if arg_9_1[iter_10_1]:
				var_10_0 = arg_9_1[iter_10_1].level
			else
				var_10_0 = 1

			iter_10_1 = arg_9_4 and arg_9_4.RemapSkillId(iter_10_1) or iter_10_1

			local var_10_1 = var_0_3.SkillTranform(arg_9_2, iter_10_1)
			local var_10_2 = var_0_3.GetResFromBuff(var_10_1, var_10_0, var_9_1, arg_9_3)

			for iter_10_2, iter_10_3 in ipairs(var_10_2):
				var_9_0[#var_9_0 + 1] = iter_10_3

	var_9_3(var_9_2.buff_list)
	var_9_3(var_9_2.hide_buff_list)

	local var_9_4 = var_9_2.airassist_time

	for iter_9_0, iter_9_1 in ipairs(var_9_4):
		local var_9_5 = var_0_3.GetResFromSkill(iter_9_1, 1, None, arg_9_3)

		for iter_9_2, iter_9_3 in ipairs(var_9_5):
			var_9_0[#var_9_0 + 1] = iter_9_3

	local var_9_6 = var_0_3.GetShipTransformDataTemplate(arg_9_0)

	if var_9_6 and var_9_6.skill_id != 0 and pg.transform_data_template[var_9_6.skill_id].skill_id != 0:
		local var_9_7 = pg.transform_data_template[var_9_6.skill_id].skill_id
		local var_9_8

		if arg_9_1[var_9_7]:
			var_9_8 = arg_9_1[var_9_7].level
		else
			var_9_8 = 1

		local var_9_9 = var_0_3.GetResFromBuff(var_9_7, var_9_8, var_9_1, arg_9_3)

		for iter_9_4, iter_9_5 in ipairs(var_9_9):
			var_9_0[#var_9_0 + 1] = iter_9_5

	if var_0_3.GetShipMetaFromDataTemplate(arg_9_0):
		var_9_3(var_9_2.buff_list_display)

	return var_9_0

def var_0_3.getWeaponResource(arg_11_0, arg_11_1):
	local var_11_0 = var_0_0.Battle.BattleResourceManager.GetWeaponResource(arg_11_0)

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		arg_11_1[#arg_11_1 + 1] = iter_11_1

def var_0_3.GetResFromBuff(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	local var_12_0 = {}
	local var_12_1 = arg_12_0 .. "_" .. arg_12_1

	if arg_12_2[var_12_1]:
		return var_12_0
	else
		arg_12_2[var_12_1] = True

	local var_12_2 = var_0_3.GetBuffTemplate(arg_12_0, arg_12_1)

	if var_12_2.init_effect and var_12_2.init_effect != "":
		local var_12_3 = var_12_2.init_effect

		if var_12_2.skin_adapt:
			var_12_3 = var_0_3.SkinAdaptFXID(var_12_3, arg_12_3)

		var_12_0[#var_12_0 + 1] = var_0_0.Battle.BattleResourceManager.GetFXPath(var_12_3)

	if var_12_2.last_effect and var_12_2.last_effect != "":
		local var_12_4 = type(var_12_2.last_effect) == "table" and var_12_2.last_effect or {
			var_12_2.last_effect
		}

		for iter_12_0, iter_12_1 in ipairs(var_12_4):
			var_12_0[#var_12_0 + 1] = var_0_0.Battle.BattleResourceManager.GetFXPath(iter_12_1)

	for iter_12_2, iter_12_3 in ipairs(var_12_2.effect_list):
		local var_12_5 = iter_12_3.arg_list.skill_id

		if var_12_5 != None:
			local var_12_6 = var_0_3.GetResFromSkill(var_12_5, arg_12_1, arg_12_2, arg_12_3)

			for iter_12_4, iter_12_5 in ipairs(var_12_6):
				var_12_0[#var_12_0 + 1] = iter_12_5

		local var_12_7 = iter_12_3.arg_list.skill_id_list

		if var_12_7 != None:
			for iter_12_6, iter_12_7 in ipairs(var_12_7):
				local var_12_8 = var_0_3.GetResFromSkill(iter_12_7, arg_12_1, arg_12_2, arg_12_3)

				for iter_12_8, iter_12_9 in ipairs(var_12_8):
					var_12_0[#var_12_0 + 1] = iter_12_9

		local var_12_9 = iter_12_3.arg_list.damage_attr_list

		if var_12_9 != None:
			for iter_12_10, iter_12_11 in pairs(var_12_9):
				local var_12_10 = var_0_3.GetResFromSkill(iter_12_11, arg_12_1, arg_12_2, arg_12_3)

				for iter_12_12, iter_12_13 in ipairs(var_12_10):
					var_12_0[#var_12_0 + 1] = iter_12_13

		local var_12_11 = iter_12_3.arg_list.bullet_id

		if var_12_11:
			local var_12_12 = var_0_0.Battle.BattleResourceManager.GetBulletResource(var_12_11)

			for iter_12_14, iter_12_15 in ipairs(var_12_12):
				var_12_0[#var_12_0 + 1] = iter_12_15

		local var_12_13 = iter_12_3.arg_list.weapon_id

		if var_12_13:
			var_0_3.getWeaponResource(var_12_13, var_12_0)

		local var_12_14 = iter_12_3.arg_list.skin_id

		if var_12_14:
			local var_12_15 = var_0_0.Battle.BattleResourceManager.GetEquipSkinBulletRes(var_12_14)

			for iter_12_16, iter_12_17 in ipairs(var_12_15):
				var_12_0[#var_12_0 + 1] = iter_12_17

		local var_12_16 = iter_12_3.arg_list.ship_skin_id

		if var_12_16:
			local var_12_17 = var_0_3.GetPlayerShipSkinDataFromID(var_12_16)

			var_12_0[#var_12_0 + 1] = var_0_0.Battle.BattleResourceManager.GetCharacterPath(var_12_17.prefab)

		local var_12_18 = iter_12_3.arg_list.buff_id

		if var_12_18:
			local var_12_19 = var_0_3.GetResFromBuff(var_12_18, arg_12_1, arg_12_2, arg_12_3)

			for iter_12_18, iter_12_19 in ipairs(var_12_19):
				if type(iter_12_19) == "string":
					var_12_0[#var_12_0 + 1] = iter_12_19
				elif type(iter_12_19) == "table":
					for iter_12_20, iter_12_21 in ipairs(iter_12_19):
						var_12_0[#var_12_0 + 1] = iter_12_21

		local var_12_20 = iter_12_3.arg_list.buff_skin_id

		if var_12_20:
			local var_12_21 = var_0_3.GetResFromBuff(var_12_20, arg_12_1, arg_12_2, arg_12_3)

			for iter_12_22, iter_12_23 in ipairs(var_12_21):
				if type(iter_12_23) == "string":
					var_12_0[#var_12_0 + 1] = iter_12_23
				elif type(iter_12_23) == "table":
					for iter_12_24, iter_12_25 in ipairs(iter_12_23):
						var_12_0[#var_12_0 + 1] = iter_12_25

		local var_12_22 = iter_12_3.arg_list.effect

		if var_12_22:
			var_12_0[#var_12_0 + 1] = var_0_0.Battle.BattleResourceManager.GetFXPath(var_12_22)

	return var_12_0

def var_0_3.GetBuffListRes(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = {}
	local var_13_1 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0):
		local var_13_2 = iter_13_1.id
		local var_13_3 = iter_13_1.level

		for iter_13_2, iter_13_3 in ipairs(var_0_3.GetResFromBuff(var_13_2, var_13_3, var_13_1, arg_13_2)):
			var_13_0[#var_13_0 + 1] = iter_13_3

	return var_13_0

def var_0_3.GetResFromSkill(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	arg_14_1 = arg_14_1 or 1

	local var_14_0 = {}
	local var_14_1 = var_0_3.GetSkillTemplate(arg_14_0, arg_14_1)

	local function var_14_2(arg_15_0)
		for iter_15_0, iter_15_1 in ipairs(arg_15_0):
			if iter_15_1.type == var_0_0.Battle.BattleSkillGridmanFloat.__name:
				table.insert(var_14_0, "UI/combatgridmanskillfloat")

			if iter_15_1.type == var_0_0.Battle.BattleSkillFusion.__name:
				local var_15_0 = iter_15_1.arg_list
				local var_15_1 = var_0_0.Battle.BattleResourceManager.GetShipResource(var_15_0.fusion_id, var_15_0.ship_skin_id)

				for iter_15_2, iter_15_3 in ipairs(var_15_1):
					table.insert(var_14_0, iter_15_3)

				local var_15_2 = var_15_0.weapon_id_list

				for iter_15_4, iter_15_5 in ipairs(var_15_2):
					var_0_3.getWeaponResource(iter_15_5, var_14_0)

				local var_15_3 = var_15_0.buff_list

				for iter_15_6, iter_15_7 in ipairs(var_15_3):
					local var_15_4 = var_0_3.GetResFromBuff(iter_15_7, arg_14_1, arg_14_2)

					for iter_15_8, iter_15_9 in ipairs(var_15_4):
						var_14_0[#var_14_0 + 1] = iter_15_9

			local var_15_5 = iter_15_1.arg_list.weapon_id

			if var_15_5 != None:
				var_0_3.getWeaponResource(var_15_5, var_14_0)

			local var_15_6 = iter_15_1.arg_list.buff_id

			if var_15_6:
				local var_15_7 = var_0_3.GetResFromBuff(var_15_6, arg_14_1, arg_14_2)

				for iter_15_10, iter_15_11 in ipairs(var_15_7):
					var_14_0[#var_14_0 + 1] = iter_15_11

			local var_15_8 = iter_15_1.arg_list.damage_buff_id

			if var_15_8:
				local var_15_9 = iter_15_1.arg_list.damage_buff_lv or 1
				local var_15_10 = var_0_3.GetResFromBuff(var_15_8, var_15_9, arg_14_2)

				for iter_15_12, iter_15_13 in ipairs(var_15_10):
					var_14_0[#var_14_0 + 1] = iter_15_13

			local var_15_11 = iter_15_1.arg_list.effect

			if var_15_11:
				var_14_0[#var_14_0 + 1] = var_0_0.Battle.BattleResourceManager.GetFXPath(var_15_11)

			local var_15_12 = iter_15_1.arg_list.finale_effect

			if var_15_12:
				var_14_0[#var_14_0 + 1] = var_0_0.Battle.BattleResourceManager.GetFXPath(var_15_12)

			local var_15_13 = iter_15_1.arg_list.spawnData

			if var_15_13:
				local var_15_14 = var_0_0.Battle.BattleResourceManager.GetMonsterRes(var_15_13)

				for iter_15_14, iter_15_15 in ipairs(var_15_14):
					var_14_0[#var_14_0 + 1] = iter_15_15

	if type(var_14_1.painting) == "string":
		var_14_0[#var_14_0 + 1] = var_0_0.Battle.BattleResourceManager.GetHrzIcon(var_14_1.painting)

	if type(var_14_1.castCV) == "table":
		var_0_0.Battle.BattleResourceManager.GetInstance().AddPreloadCV(var_14_1.castCV.skinID)

	if var_14_1.focus_duration:
		if var_14_1.cutin_cover:
			var_14_0[#var_14_0 + 1] = var_0_0.Battle.BattleResourceManager.GetInstance().GetPaintingPath(var_14_1.cutin_cover)
		elif arg_14_3:
			local var_14_3 = var_0_3.GetPlayerShipSkinDataFromID(arg_14_3).painting

			var_14_0[#var_14_0 + 1] = var_0_0.Battle.BattleResourceManager.GetInstance().GetPaintingPath(var_14_3)

	var_14_2(var_14_1.effect_list)

	for iter_14_0, iter_14_1 in ipairs(var_14_1):
		var_14_2(iter_14_1.effect_list)

	return var_14_0

def var_0_3.GetShipSkillTriggerCount(arg_16_0, arg_16_1):
	local function var_16_0(arg_17_0)
		local var_17_0 = 0

		for iter_17_0, iter_17_1 in pairs(arg_17_0):
			local var_17_1 = var_0_3.GetBuffTemplate(iter_17_1.id).effect_list

			for iter_17_2, iter_17_3 in ipairs(var_17_1):
				local var_17_2 = iter_17_3.trigger

				for iter_17_4, iter_17_5 in ipairs(var_17_2):
					if table.contains(arg_16_1, iter_17_5):
						var_17_0 = var_17_0 + 1

		return var_17_0

	local var_16_1 = 0
	local var_16_2 = arg_16_0.skills or {}
	local var_16_3 = var_16_1 + var_16_0(var_16_2)
	local var_16_4 = var_0_3.GetEquipSkill(arg_16_0.equipment)
	local var_16_5 = {}

	for iter_16_0, iter_16_1 in ipairs(var_16_4):
		table.insert(var_16_5, {
			id = iter_16_1
		})

	return var_16_3 + var_16_0(var_16_5)

def var_0_3.GetSongList(arg_18_0):
	local var_18_0 = {
		initList = {},
		otherList = {}
	}

	for iter_18_0, iter_18_1 in pairs(arg_18_0):
		local var_18_1 = var_0_3.GetBuffTemplate(iter_18_0, 1)

		for iter_18_2, iter_18_3 in ipairs(var_18_1.effect_list):
			if iter_18_3.type == var_0_0.Battle.BattleBuffDiva.__name:
				if table.contains(iter_18_3.trigger, "onInitGame"):
					for iter_18_4, iter_18_5 in ipairs(iter_18_3.arg_list.bgm_list):
						var_18_0.initList[iter_18_5] = True

				if not table.contains(iter_18_3.trigger, "onInitGame") or #iter_18_3.trigger > 1:
					for iter_18_6, iter_18_7 in ipairs(iter_18_3.arg_list.bgm_list):
						var_18_0.otherList[iter_18_7] = True

	return var_18_0

def var_0_3.GetCardRes(arg_19_0):
	local var_19_0 = {}
	local var_19_1 = var_0_0.Battle.BattleCardPuzzleCard.GetCardEffectConfig(arg_19_0)

	for iter_19_0, iter_19_1 in ipairs(var_19_1.effect_list):
		local var_19_2 = var_0_3.GetCardFXRes(iter_19_1)

		for iter_19_2, iter_19_3 in ipairs(var_19_2):
			table.insert(var_19_0, iter_19_3)

	for iter_19_4, iter_19_5 in pairs(var_19_1.effect_list):
		local var_19_3 = var_0_3.GetCardFXRes(iter_19_5)

		for iter_19_6, iter_19_7 in ipairs(var_19_3):
			table.insert(var_19_0, iter_19_7)

	return var_19_0

def var_0_3.GetCardFXRes(arg_20_0):
	local var_20_0 = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_0):
		if iter_20_1.type == "BattleCardPuzzleSkillCreateCard":
			local var_20_1 = var_0_3.GetCardRes(iter_20_1.arg_list.card_id)

			for iter_20_2, iter_20_3 in ipairs(var_20_1):
				table.insert(var_20_0, iter_20_3)
		elif iter_20_1.type == "BattleCardPuzzleSkillFire":
			local var_20_2 = var_0_0.Battle.BattleResourceManager.GetWeaponResource(iter_20_1.arg_list.weapon_id)

			for iter_20_4, iter_20_5 in ipairs(var_20_2):
				table.insert(var_20_0, iter_20_5)
		elif iter_20_1.type == "BattleCardPuzzleSkillAddBuff":
			local var_20_3 = var_0_3.GetResFromBuff(iter_20_1.arg_list.buff_id, 1, {})

			for iter_20_6, iter_20_7 in ipairs(var_20_3):
				table.insert(var_20_0, iter_20_7)

	return var_20_0

def var_0_3.NeedSkillPainting(arg_21_0):
	local var_21_0 = False

	if var_0_3.GetSkillTemplate(arg_21_0).focus_duration:
		var_21_0 = True

	return var_21_0

def var_0_3.SkinAdaptFXID(arg_22_0, arg_22_1):
	return arg_22_0 .. "_" .. arg_22_1

def var_0_3.GetFleetReload(arg_23_0):
	return var_0_2.GetFleetReload(arg_23_0)

def var_0_3.GetFleetTorpedoPower(arg_24_0):
	return var_0_2.GetFleetTorpedoPower(arg_24_0)

def var_0_3.SortFleetList(arg_25_0, arg_25_1):
	local var_25_0 = {}

	for iter_25_0, iter_25_1 in ipairs(arg_25_0):
		var_25_0[#var_25_0 + 1] = arg_25_1[iter_25_1]

		var_25_0[iter_25_0].SetFormationIndex(iter_25_0)

	return var_25_0

def var_0_3.GetLimitAttributeRange(arg_26_0, arg_26_1):
	if pg.battle_attribute_range[arg_26_0]:
		return math.clamp(arg_26_1, pg.battle_attribute_range[arg_26_0].min / 10000, pg.battle_attribute_range[arg_26_0].max / 10000)

	return arg_26_1

def var_0_3.GetPuzzleCardDataTemplate(arg_27_0):
	assert(var_0_4[arg_27_0] != None, ">>puzzle_card_template<< 找不到卡牌配置：" .. arg_27_0)

	return var_0_4[arg_27_0]

def var_0_3.GetPuzzleShipDataTemplate(arg_28_0):
	assert(var_0_5[arg_28_0] != None, ">>puzzle_ship_template<< 找不到卡牌舰船配置：" .. arg_28_0)

	return var_0_5[arg_28_0]

def var_0_3.GetPuzzleDungeonTemplate(arg_29_0):
	assert(var_0_6[arg_29_0] != None, ">>puzzle_combat_template<< 找不到卡牌关卡配置：" .. arg_29_0)

	return var_0_6[arg_29_0]

def var_0_3.GetPuzzleCardAffixDataTemplate(arg_30_0):
	assert(var_0_7[arg_30_0] != None, ">>puzzle_card_affix<< 找不到卡牌关卡配置：" .. arg_30_0)

	return var_0_7[arg_30_0]

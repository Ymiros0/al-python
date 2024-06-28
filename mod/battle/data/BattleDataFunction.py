from luatable import table, setmetatable
from alsupport import math
from support.helpers.M02 import getSkillName

var_0_1 = ys.Battle.BattleConst
var_0_2 = ys.Battle.BattleFormulas



var_0_4 = pg.puzzle_card_template
var_0_5 = pg.puzzle_ship_template
var_0_6 = pg.puzzle_combat_template
var_0_7 = pg.puzzle_card_affix

class BattleDataFunction:
	def GetDungeonTmpDataByID(arg_1_0):
		#Just use the json tbh
		return getattr(__import__("gamecfg.dungeon", fromlist=[arg_1_0 + '.data']), arg_1_0 + '.data')

	def ClearDungeonCfg(arg_2_0):
		#Maybe implement sth for the api to reduce memory usage?
		#package.loaded["GameCfg.dungeon." + arg_2_0] = None
		pass

	def GetSkillTemplate(arg_3_0, arg_3_1):
		arg_3_1 = arg_3_1 or 1

		var_3_0 = "skill_" + arg_3_0
		var_3_1 = pg.ConvertedSkill[var_3_0]
		var_3_2 = var_3_1[arg_3_1] or var_3_1[0]

		var_3_2.name = getSkillName(arg_3_0)

		return var_3_2

	def ConvertSkillTemplate():
		pg.ConvertedSkill = table()
		def index_func(arg_5_0, arg_5_1):
			var_5_0 = arg_5_1
			var_5_1 = pg.skillCfg[arg_5_1]

			if var_5_1:
				var_5_2 = table()
				var_5_3 = table()

				for iter_5_0, iter_5_1 in table.pairs(var_5_1):
					var_5_3[iter_5_0] = table.Clone(iter_5_1)

				var_5_2[0] = var_5_3

				for iter_5_2, iter_5_3 in table.ipairs(var_5_1):
					var_5_4 = table.Clone(var_5_3)

					for iter_5_4, iter_5_5 in table.pairs(iter_5_3):
						var_5_4[iter_5_4] = iter_5_5

					var_5_2[iter_5_2] = var_5_4

				pg.ConvertedSkill[var_5_0] = var_5_2

				return var_5_2
		setmetatable(pg.ConvertedSkill, table(
			__index = index_func
		))

	def GetBuffTemplate(arg_6_0, arg_6_1):
		arg_6_1 = arg_6_1 or 1

		var_6_0 = "buff_" + arg_6_0
		var_6_1 = pg.ConvertedBuff[var_6_0]

		return var_6_1[arg_6_1] or var_6_1[0]

	def ConvertBuffTemplate():
		pg.ConvertedBuff = table()
		def index_func(arg_8_0, arg_8_1):
			var_8_0 = arg_8_1
			var_8_1 = pg.buffCfg[arg_8_1]

			if var_8_1:
				var_8_2 = table()
				var_8_3 = table()

				for iter_8_0, iter_8_1 in table.pairs(var_8_1):
					var_8_3[iter_8_0] = table.Clone(iter_8_1)

				var_8_2[0] = var_8_3

				for iter_8_2, iter_8_3 in table.ipairs(var_8_1):
					var_8_4 = table.Clone(var_8_3)

					for iter_8_4, iter_8_5 in table.pairs(iter_8_3):
						var_8_4[iter_8_4] = iter_8_5

					var_8_2[iter_8_2] = var_8_4

				pg.ConvertedBuff[var_8_0] = var_8_2

				return var_8_2
		setmetatable(pg.ConvertedBuff, table(
			__index = index_func
		))

	def GetBuffBulletRes(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
		var_9_0 = table()
		var_9_1 = table()

		arg_9_1 = arg_9_1 or table()

		var_9_2 = BattleDataFunction.GetPlayerShipModelFromID(arg_9_0)

		def var_9_3(arg_10_0):
			for iter_10_0, iter_10_1 in table.ipairs(arg_10_0):
				var_10_0

				if arg_9_1[iter_10_1]:
					var_10_0 = arg_9_1[iter_10_1].level
				else:
					var_10_0 = 1

				iter_10_1 = arg_9_4 and arg_9_4.RemapSkillId(iter_10_1) or iter_10_1

				var_10_1 = BattleDataFunction.SkillTranform(arg_9_2, iter_10_1)
				var_10_2 = BattleDataFunction.GetResFromBuff(var_10_1, var_10_0, var_9_1, arg_9_3)

				for iter_10_2, iter_10_3 in table.ipairs(var_10_2):
					var_9_0.append(iter_10_3)

		var_9_3(var_9_2.buff_list)
		var_9_3(var_9_2.hide_buff_list)

		var_9_4 = var_9_2.airassist_time

		for iter_9_0, iter_9_1 in table.ipairs(var_9_4):
			var_9_5 = BattleDataFunction.GetResFromSkill(iter_9_1, 1, None, arg_9_3)

			for iter_9_2, iter_9_3 in table.ipairs(var_9_5):
				var_9_0.append(iter_9_3)

		var_9_6 = BattleDataFunction.GetShipTransformDataTemplate(arg_9_0)

		if var_9_6 and var_9_6.skill_id != 0 and pg.transform_data_template[var_9_6.skill_id].skill_id != 0:
			var_9_7 = pg.transform_data_template[var_9_6.skill_id].skill_id
			var_9_8

			if arg_9_1[var_9_7]:
				var_9_8 = arg_9_1[var_9_7].level
			else:
				var_9_8 = 1

			var_9_9 = BattleDataFunction.GetResFromBuff(var_9_7, var_9_8, var_9_1, arg_9_3)

			for iter_9_4, iter_9_5 in table.ipairs(var_9_9):
				var_9_0.append(iter_9_5)

		if BattleDataFunction.GetShipMetaFromDataTemplate(arg_9_0):
			var_9_3(var_9_2.buff_list_display)

		return var_9_0

	def getWeaponResource(arg_11_0, arg_11_1):
		var_11_0 = ys.Battle.BattleResourceManager.GetWeaponResource(arg_11_0)

		for iter_11_0, iter_11_1 in table.ipairs(var_11_0):
			arg_11_1.append(iter_11_1)

	def GetResFromBuff(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
		var_12_0 = table()
		var_12_1 = arg_12_0 + "_" + arg_12_1

		if arg_12_2[var_12_1]:
			return var_12_0
		else:
			arg_12_2[var_12_1] = True

		var_12_2 = BattleDataFunction.GetBuffTemplate(arg_12_0, arg_12_1)

		if var_12_2.init_effect and var_12_2.init_effect != "":
			var_12_3 = var_12_2.init_effect

			if var_12_2.skin_adapt:
				var_12_3 = BattleDataFunction.SkinAdaptFXID(var_12_3, arg_12_3)

			var_12_0.append(ys.Battle.BattleResourceManager.GetFXPath(var_12_3))

		if var_12_2.last_effect and var_12_2.last_effect != "":
			var_12_4 = type(var_12_2.last_effect) == "table" and var_12_2.last_effect or table(
				var_12_2.last_effect
			)

			for iter_12_0, iter_12_1 in table.ipairs(var_12_4):
				var_12_0.append(ys.Battle.BattleResourceManager.GetFXPath(iter_12_1))

		for iter_12_2, iter_12_3 in table.ipairs(var_12_2.effect_list):
			var_12_5 = iter_12_3.arg_list.skill_id

			if var_12_5 != None:
				var_12_6 = BattleDataFunction.GetResFromSkill(var_12_5, arg_12_1, arg_12_2, arg_12_3)

				for iter_12_4, iter_12_5 in table.ipairs(var_12_6):
					var_12_0.append(iter_12_5)

			var_12_7 = iter_12_3.arg_list.skill_id_list

			if var_12_7 != None:
				for iter_12_6, iter_12_7 in table.ipairs(var_12_7):
					var_12_8 = BattleDataFunction.GetResFromSkill(iter_12_7, arg_12_1, arg_12_2, arg_12_3)

					for iter_12_8, iter_12_9 in table.ipairs(var_12_8):
						var_12_0.append(iter_12_9)

			var_12_9 = iter_12_3.arg_list.damage_attr_list

			if var_12_9 != None:
				for iter_12_10, iter_12_11 in table.pairs(var_12_9):
					var_12_10 = BattleDataFunction.GetResFromSkill(iter_12_11, arg_12_1, arg_12_2, arg_12_3)

					for iter_12_12, iter_12_13 in table.ipairs(var_12_10):
						var_12_0.append(iter_12_13)

			var_12_11 = iter_12_3.arg_list.bullet_id

			if var_12_11:
				var_12_12 = ys.Battle.BattleResourceManager.GetBulletResource(var_12_11)

				for iter_12_14, iter_12_15 in table.ipairs(var_12_12):
					var_12_0.append(iter_12_15)

			var_12_13 = iter_12_3.arg_list.weapon_id

			if var_12_13:
				BattleDataFunction.getWeaponResource(var_12_13, var_12_0)

			var_12_14 = iter_12_3.arg_list.skin_id

			if var_12_14:
				var_12_15 = ys.Battle.BattleResourceManager.GetEquipSkinBulletRes(var_12_14)

				for iter_12_16, iter_12_17 in table.ipairs(var_12_15):
					var_12_0.append(iter_12_17)

			var_12_16 = iter_12_3.arg_list.ship_skin_id

			if var_12_16:
				var_12_17 = BattleDataFunction.GetPlayerShipSkinDataFromID(var_12_16)

				var_12_0.append(ys.Battle.BattleResourceManager.GetCharacterPath(var_12_17.prefab))

			var_12_18 = iter_12_3.arg_list.buff_id

			if var_12_18:
				var_12_19 = BattleDataFunction.GetResFromBuff(var_12_18, arg_12_1, arg_12_2, arg_12_3)

				for iter_12_18, iter_12_19 in table.ipairs(var_12_19):
					if type(iter_12_19) == str:
						var_12_0.append(iter_12_19)
					elif type(iter_12_19) == table:
						for iter_12_20, iter_12_21 in table.ipairs(iter_12_19):
							var_12_0.append(iter_12_21)

			var_12_20 = iter_12_3.arg_list.buff_skin_id

			if var_12_20:
				var_12_21 = BattleDataFunction.GetResFromBuff(var_12_20, arg_12_1, arg_12_2, arg_12_3)

				for iter_12_22, iter_12_23 in table.ipairs(var_12_21):
					if type(iter_12_23) == str:
						var_12_0.append(iter_12_23)
					elif type(iter_12_23) == table:
						for iter_12_24, iter_12_25 in table.ipairs(iter_12_23):
							var_12_0.append(iter_12_25)

			var_12_22 = iter_12_3.arg_list.effect

			if var_12_22:
				var_12_0.append(ys.Battle.BattleResourceManager.GetFXPath(var_12_22))

		return var_12_0

	def GetBuffListRes(arg_13_0, arg_13_1, arg_13_2):
		var_13_0 = table()
		var_13_1 = table()

		for iter_13_0, iter_13_1 in table.ipairs(arg_13_0):
			var_13_2 = iter_13_1.id
			var_13_3 = iter_13_1.level

			for iter_13_2, iter_13_3 in table.ipairs(BattleDataFunction.GetResFromBuff(var_13_2, var_13_3, var_13_1, arg_13_2)):
				var_13_0.append(iter_13_3)

		return var_13_0

	def GetResFromSkill(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
		arg_14_1 = arg_14_1 or 1

		var_14_0 = table()
		var_14_1 = BattleDataFunction.GetSkillTemplate(arg_14_0, arg_14_1)

		def var_14_2(arg_15_0):
			for iter_15_0, iter_15_1 in table.ipairs(arg_15_0):
				if iter_15_1.type == ys.Battle.BattleSkillGridmanFloat.__name:
					table.insert(var_14_0, "UI/combatgridmanskillfloat")

				if iter_15_1.type == ys.Battle.BattleSkillFusion.__name:
					var_15_0 = iter_15_1.arg_list
					var_15_1 = ys.Battle.BattleResourceManager.GetShipResource(var_15_0.fusion_id, var_15_0.ship_skin_id)

					for iter_15_2, iter_15_3 in table.ipairs(var_15_1):
						table.insert(var_14_0, iter_15_3)

					var_15_2 = var_15_0.weapon_id_list

					for iter_15_4, iter_15_5 in table.ipairs(var_15_2):
						BattleDataFunction.getWeaponResource(iter_15_5, var_14_0)

					var_15_3 = var_15_0.buff_list

					for iter_15_6, iter_15_7 in table.ipairs(var_15_3):
						var_15_4 = BattleDataFunction.GetResFromBuff(iter_15_7, arg_14_1, arg_14_2)

						for iter_15_8, iter_15_9 in table.ipairs(var_15_4):
							var_14_0.append(iter_15_9)

				var_15_5 = iter_15_1.arg_list.weapon_id

				if var_15_5 != None:
					BattleDataFunction.getWeaponResource(var_15_5, var_14_0)

				var_15_6 = iter_15_1.arg_list.buff_id

				if var_15_6:
					var_15_7 = BattleDataFunction.GetResFromBuff(var_15_6, arg_14_1, arg_14_2)

					for iter_15_10, iter_15_11 in table.ipairs(var_15_7):
						var_14_0.append(iter_15_11)

				var_15_8 = iter_15_1.arg_list.damage_buff_id

				if var_15_8:
					var_15_9 = iter_15_1.arg_list.damage_buff_lv or 1
					var_15_10 = BattleDataFunction.GetResFromBuff(var_15_8, var_15_9, arg_14_2)

					for iter_15_12, iter_15_13 in table.ipairs(var_15_10):
						var_14_0.append(iter_15_13)

				var_15_11 = iter_15_1.arg_list.effect

				if var_15_11:
					var_14_0.append(ys.Battle.BattleResourceManager.GetFXPath(var_15_11))

				var_15_12 = iter_15_1.arg_list.finale_effect

				if var_15_12:
					var_14_0.append(ys.Battle.BattleResourceManager.GetFXPath(var_15_12))

				var_15_13 = iter_15_1.arg_list.spawnData

				if var_15_13:
					var_15_14 = ys.Battle.BattleResourceManager.GetMonsterRes(var_15_13)

					for iter_15_14, iter_15_15 in table.ipairs(var_15_14):
						var_14_0.append(iter_15_15)

		if type(var_14_1.painting) == str:
			var_14_0.append(ys.Battle.BattleResourceManager.GetHrzIcon(var_14_1.painting))

		if type(var_14_1.castCV) == table:
			ys.Battle.BattleResourceManager.GetInstance().AddPreloadCV(var_14_1.castCV.skinID)

		if var_14_1.focus_duration:
			if var_14_1.cutin_cover:
				var_14_0.append(ys.Battle.BattleResourceManager.GetInstance().GetPaintingPath(var_14_1.cutin_cover))
			elif arg_14_3:
				var_14_3 = BattleDataFunction.GetPlayerShipSkinDataFromID(arg_14_3).painting

				var_14_0.append(ys.Battle.BattleResourceManager.GetInstance().GetPaintingPath(var_14_3))

		var_14_2(var_14_1.effect_list)

		for iter_14_0, iter_14_1 in table.ipairs(var_14_1):
			var_14_2(iter_14_1.effect_list)

		return var_14_0

	def GetShipSkillTriggerCount(arg_16_0, arg_16_1):
		def var_16_0(arg_17_0):
			var_17_0 = 0

			for iter_17_0, iter_17_1 in table.pairs(arg_17_0):
				var_17_1 = BattleDataFunction.GetBuffTemplate(iter_17_1.id).effect_list

				for iter_17_2, iter_17_3 in table.ipairs(var_17_1):
					var_17_2 = iter_17_3.trigger

					for iter_17_4, iter_17_5 in table.ipairs(var_17_2):
						if table.contains(arg_16_1, iter_17_5):
							var_17_0 = var_17_0 + 1

			return var_17_0

		var_16_1 = 0
		var_16_2 = arg_16_0.skills or table()
		var_16_3 = var_16_1 + var_16_0(var_16_2)
		var_16_4 = BattleDataFunction.GetEquipSkill(arg_16_0.equipment)
		var_16_5 = table()

		for iter_16_0, iter_16_1 in table.ipairs(var_16_4):
			table.insert(var_16_5, table(
				id = iter_16_1
			))

		return var_16_3 + var_16_0(var_16_5)

	def GetSongList(arg_18_0):
		var_18_0 = table(
			initList = table(),
			otherList = table()
		)

		for iter_18_0, iter_18_1 in table.pairs(arg_18_0):
			var_18_1 = BattleDataFunction.GetBuffTemplate(iter_18_0, 1)

			for iter_18_2, iter_18_3 in table.ipairs(var_18_1.effect_list):
				if iter_18_3.type == ys.Battle.BattleBuffDiva.__name:
					if table.contains(iter_18_3.trigger, "onInitGame"):
						for iter_18_4, iter_18_5 in table.ipairs(iter_18_3.arg_list.bgm_list):
							var_18_0.initList[iter_18_5] = True

					if not table.contains(iter_18_3.trigger, "onInitGame") or len(iter_18_3.trigger) > 1:
						for iter_18_6, iter_18_7 in table.ipairs(iter_18_3.arg_list.bgm_list):
							var_18_0.otherList[iter_18_7] = True

		return var_18_0

	def GetCardRes(arg_19_0):
		var_19_0 = table()
		var_19_1 = ys.Battle.BattleCardPuzzleCard.GetCardEffectConfig(arg_19_0)

		for iter_19_0, iter_19_1 in table.ipairs(var_19_1.effect_list):
			var_19_2 = BattleDataFunction.GetCardFXRes(iter_19_1)

			for iter_19_2, iter_19_3 in table.ipairs(var_19_2):
				table.insert(var_19_0, iter_19_3)

		for iter_19_4, iter_19_5 in table.pairs(var_19_1.effect_list):
			var_19_3 = BattleDataFunction.GetCardFXRes(iter_19_5)

			for iter_19_6, iter_19_7 in table.ipairs(var_19_3):
				table.insert(var_19_0, iter_19_7)

		return var_19_0

	def GetCardFXRes(arg_20_0):
		var_20_0 = table()

		for iter_20_0, iter_20_1 in table.ipairs(arg_20_0):
			if iter_20_1.type == "BattleCardPuzzleSkillCreateCard":
				var_20_1 = BattleDataFunction.GetCardRes(iter_20_1.arg_list.card_id)

				for iter_20_2, iter_20_3 in table.ipairs(var_20_1):
					table.insert(var_20_0, iter_20_3)
			elif iter_20_1.type == "BattleCardPuzzleSkillFire":
				var_20_2 = ys.Battle.BattleResourceManager.GetWeaponResource(iter_20_1.arg_list.weapon_id)

				for iter_20_4, iter_20_5 in table.ipairs(var_20_2):
					table.insert(var_20_0, iter_20_5)
			elif iter_20_1.type == "BattleCardPuzzleSkillAddBuff":
				var_20_3 = BattleDataFunction.GetResFromBuff(iter_20_1.arg_list.buff_id, 1, table())

				for iter_20_6, iter_20_7 in table.ipairs(var_20_3):
					table.insert(var_20_0, iter_20_7)

		return var_20_0

	def NeedSkillPainting(arg_21_0):
		var_21_0 = False

		if BattleDataFunction.GetSkillTemplate(arg_21_0).focus_duration:
			var_21_0 = True

		return var_21_0

	def SkinAdaptFXID(arg_22_0, arg_22_1):
		return arg_22_0 + "_" + arg_22_1

	def GetFleetReload(arg_23_0):
		return var_0_2.GetFleetReload(arg_23_0)

	def GetFleetTorpedoPower(arg_24_0):
		return var_0_2.GetFleetTorpedoPower(arg_24_0)

	def SortFleetList(arg_25_0, arg_25_1):
		var_25_0 = table()

		for iter_25_0, iter_25_1 in table.ipairs(arg_25_0):
			var_25_0.append(arg_25_1[iter_25_1])

			var_25_0[iter_25_0].SetFormationIndex(iter_25_0)

		return var_25_0

	def GetLimitAttributeRange(arg_26_0, arg_26_1):
		if pg.battle_attribute_range[arg_26_0]:
			return math.clamp(arg_26_1, pg.battle_attribute_range[arg_26_0].min / 10000, pg.battle_attribute_range[arg_26_0].max / 10000)

		return arg_26_1

	def GetPuzzleCardDataTemplate(arg_27_0):
		assert var_0_4[arg_27_0] != None, ">>puzzle_card_template<< 找不到卡牌配置：" + arg_27_0

		return var_0_4[arg_27_0]

	def GetPuzzleShipDataTemplate(arg_28_0):
		assert var_0_5[arg_28_0] != None, ">>puzzle_ship_template<< 找不到卡牌舰船配置：" + arg_28_0

		return var_0_5[arg_28_0]

	def GetPuzzleDungeonTemplate(arg_29_0):
		assert var_0_6[arg_29_0] != None, ">>puzzle_combat_template<< 找不到卡牌关卡配置：" + arg_29_0

		return var_0_6[arg_29_0]

	def GetPuzzleCardAffixDataTemplate(arg_30_0):
		assert var_0_7[arg_30_0] != None, ">>puzzle_card_affix<< 找不到卡牌关卡配置：" + arg_30_0

		return var_0_7[arg_30_0]


ys.Battle.BattleDataFunction = BattleDataFunction
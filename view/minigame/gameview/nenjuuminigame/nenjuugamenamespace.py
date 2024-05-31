local var_0_0 = {}
local var_0_1 = {
	def TargetObject:()
		local var_1_0 = class("TargetObject")

		function var_1_0.GetSize(arg_2_0)
			return arg_2_0.size

		function var_1_0.InTimeLine(arg_3_0)
			return False

		function var_1_0.Moveable(arg_4_0)
			return False

		function var_1_0.BreakMoveable(arg_5_0)
			return False

		function var_1_0.GetBaseOrder(arg_6_0)
			return 3

		function var_1_0.Ctor(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
			arg_7_0._tf = arg_7_2
			arg_7_0.controller = arg_7_1

			arg_7_0.Init(arg_7_3)

		function var_1_0.Init(arg_8_0, arg_8_1)
			arg_8_0.name = arg_8_1.name
			arg_8_0.size = arg_8_1.size or NewPos(1, 1)
			arg_8_0.canHide = arg_8_1.hide

			setCanvasOverrideSorting(arg_8_0._tf, True)
			arg_8_0.UpdatePos(arg_8_1.pos - NewPos(0, arg_8_0.GetSize().y - 1))

			arg_8_0.realPos = arg_8_1.realPos or arg_8_0.pos

			arg_8_0.UpdatePosition()
			arg_8_0.InitUI(arg_8_1)

		function var_1_0.InitUI(arg_9_0, arg_9_1)
			return

		function var_1_0.UpdatePos(arg_10_0, arg_10_1)
			arg_10_0._tf.GetComponent(typeof(Canvas)).sortingOrder = (arg_10_1.y + arg_10_0.GetSize().y) * 10 + arg_10_0.GetBaseOrder()

			arg_10_0.controller.UpdateTargetPos(arg_10_0, arg_10_0.pos, arg_10_1)

			arg_10_0.pos = arg_10_1

		function var_1_0.UpdatePosition(arg_11_0)
			setAnchoredPosition(arg_11_0._tf, {
				x = arg_11_0.realPos.x * 32,
				y = arg_11_0.realPos.y * -32
			})

		function var_1_0.PlayAnim(arg_12_0, arg_12_1)
			if arg_12_0.status != arg_12_1:
				arg_12_0.status = arg_12_1

				arg_12_0.mainTarget.GetComponent(typeof(Animator)).Play(arg_12_1, -1, 0)

		return var_1_0,
	def TargetIce:()
		local var_13_0 = class("TargetIce", var_0_0.TargetObject)

		function var_13_0.BreakMoveable(arg_14_0)
			return True

		function var_13_0.InitUI(arg_15_0, arg_15_1)
			arg_15_0.mainTarget = arg_15_0._tf.Find("scale/Image")

			arg_15_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				arg_15_0.controller.DestoryTarget(arg_15_0))

			if arg_15_1.create:
				if arg_15_0.controller.CheckMelt(arg_15_0.pos):
					arg_15_0.isLost = True

					arg_15_0.PlayAnim("Ice_Spawn_Melt")
				else
					arg_15_0.PlayAnim("Ice_Spawn")

		function var_13_0.Break(arg_17_0)
			if arg_17_0.isLost:
				return
			else
				arg_17_0.isLost = True

				arg_17_0.PlayAnim("Ice_Break")

		return var_13_0,
	def TargetItem:()
		local var_18_0 = class("TargetItem", var_0_0.TargetObject)

		function var_18_0.Moveable(arg_19_0)
			return True

		function var_18_0.GetBaseOrder(arg_20_0)
			return 2

		function var_18_0.InitUI(arg_21_0, arg_21_1)
			arg_21_0.point = arg_21_1.point

			eachChild(arg_21_0._tf.Find("scale/type"), function(arg_22_0)
				setActive(arg_22_0, arg_22_0.name == arg_21_0.name))

		return var_18_0,
	def TargetArbor:()
		local var_23_0 = class("TargetArbor", var_0_0.TargetObject)

		function var_23_0.InitUI(arg_24_0, arg_24_1)
			local var_24_0 = string.split(arg_24_0.name, "_")

			eachChild(arg_24_0._tf.Find("scale/Image"), function(arg_25_0)
				setActive(arg_25_0, arg_25_0.name == var_24_0[#var_24_0]))

		return var_23_0,
	def TargetMove:()
		local var_26_0 = class("TargetMove", var_0_0.TargetObject)

		function var_26_0.InTimeLine(arg_27_0)
			return True

		function var_26_0.GetBaseOrder(arg_28_0)
			return 4

		function var_26_0.InitUI(arg_29_0, arg_29_1)
			arg_29_0.rtScale = arg_29_0._tf.Find("scale")
			arg_29_0.mainTarget = arg_29_0.rtScale.Find("main")

			local var_29_0 = arg_29_0.mainTarget.GetComponent(typeof(DftAniEvent))

			var_29_0.SetStartEvent(function()
				arg_29_0.EventAnim("start"))
			var_29_0.SetTriggerEvent(function()
				arg_29_0.EventAnim("trigger"))
			var_29_0.SetEndEvent(function()
				arg_29_0.inLock = False

				arg_29_0.EventAnim("end"))
			arg_29_0.PlayIdle()

		function var_26_0.EventAnim(arg_33_0, arg_33_1)
			return

		function var_26_0.RushCheck(arg_34_0)
			return

		function var_26_0.PlayIdle(arg_35_0, arg_35_1)
			arg_35_0.PlayAnim(string.format("Idle_%s%s", arg_35_1 or arg_35_0.GetDirMark(), arg_35_0.inLantern and "_Lantern" or ""))

		function var_26_0.PlayMove(arg_36_0, arg_36_1)
			arg_36_0.PlayAnim(string.format("Move_%s%s", arg_36_1 or arg_36_0.GetDirMark(), arg_36_0.inLantern and "_Lantern" or ""))

		local var_26_1 = {
			E = {
				1,
				0
			},
			S = {
				0,
				1
			},
			W = {
				-1,
				0
			},
			N = {
				0,
				-1
			}
		}

		function var_26_0.GetDirMark(arg_37_0, arg_37_1)
			if arg_37_1:
				for iter_37_0, iter_37_1 in pairs(var_26_1):
					if iter_37_1[1] == arg_37_1.x and iter_37_1[2] == arg_37_1.y:
						return iter_37_0
			else
				local var_37_0 = string.split(arg_37_0.status, "_")[2]

				return var_26_1[var_37_0] and var_37_0 or "S"

		function var_26_0.GetDirPos(arg_38_0, arg_38_1)
			return NewPos(unpack(var_26_1[arg_38_1 or arg_38_0.GetDirMark()]))

		function var_26_0.GetStatusMark(arg_39_0, arg_39_1)
			return string.split(arg_39_1 or arg_39_0.status, "_")[1]

		function var_26_0.OnTimerUpdate(arg_40_0, arg_40_1)
			return

		var_26_0.loopAnimDic = {
			Fear = True,
			Idle = True,
			Move = True
		}

		function var_26_0.PlayAnim(arg_41_0, arg_41_1)
			local var_41_0 = tobool(arg_41_0.loopAnimDic[arg_41_0.GetStatusMark(arg_41_1)])

			if var_41_0 and arg_41_0.status == arg_41_1:
				-- block empty
			else
				arg_41_0.inLock = not var_41_0
				arg_41_0.status = arg_41_1

				arg_41_0.mainTarget.GetComponent(typeof(Animator)).Play(arg_41_1, -1, 0)
				arg_41_0.RushCheck()

		return var_26_0,
	def TargetFuShun:()
		local var_42_0 = class("TargetFuShun", var_0_0.TargetMove)

		function var_42_0.GetSpeed(arg_43_0)
			return arg_43_0.speed * (arg_43_0.controller.GetEnemyEffect("gravity") and 0.85 or 1) * (arg_43_0.inRush and NenjuuGameConfig.GetSkillParam("rush", arg_43_0.level.rush)[2] or 1) * (arg_43_0.controller.InBlackHoleRange(arg_43_0.pos) and 0.75 or 1) * (NenjuuGameConfig.GetSkillParam("blessing", arg_43_0.level.blessing) or 1)

		local var_42_1 = 0.1
		local var_42_2 = 0.1
		local var_42_3 = 5
		local var_42_4 = {
			ice = 1,
			flash = 30,
			item = 0,
			rush = 20
		}

		function var_42_0.CheckSkill(arg_44_0, arg_44_1)
			if arg_44_1 == "item":
				return arg_44_0.itemType and arg_44_0.itemCount > 0
			else
				return arg_44_0.level[arg_44_1] > 0 and arg_44_0.skillCDs[arg_44_1] <= 0

		function var_42_0.ReloadSkill(arg_45_0, arg_45_1)
			arg_45_0.skillCDs[arg_45_1] = (arg_45_1 == "flash" and NenjuuGameConfig.GetSkillParam("flash", arg_45_0.level.flash) or var_42_4[arg_45_1]) * (arg_45_0.controller.GetEnemyEffect("delay") and 1.2 or 1)

		function var_42_0.InitUI(arg_46_0, arg_46_1)
			var_42_0.super.InitUI(arg_46_0, arg_46_1)

			arg_46_0.level = arg_46_1.level
			arg_46_0.skillCDs = {
				ice = 0,
				flash = 0,
				item = 0,
				rush = 0
			}
			arg_46_0.itemType = arg_46_1.itemType
			arg_46_0.speed = 4.5
			arg_46_0.icePower = NenjuuGameConfig.GetSkillParam("ice", arg_46_0.level.ice)
			arg_46_0.flashPower = 4
			arg_46_0.decoyCount = arg_46_0.level.decoy
			arg_46_0.rushTime = checkExist(NenjuuGameConfig.GetSkillParam("rush", arg_46_0.level.rush), {
				1
			})
			arg_46_0.itemCount = 1

		function var_42_0.CalcSkillCDs(arg_47_0)
			local var_47_0 = {}

			for iter_47_0, iter_47_1 in ipairs({
				"ice",
				"flash",
				"rush",
				"item"
			}):
				local var_47_1 = arg_47_0.skillCDs[iter_47_1]
				local var_47_2 = (iter_47_1 == "flash" and NenjuuGameConfig.GetSkillParam("flash", arg_47_0.level.flash) or var_42_4[iter_47_1]) * (arg_47_0.controller.GetEnemyEffect("delay") and 1.2 or 1)

				if iter_47_1 == "item":
					if not arg_47_0.itemType:
						table.insert(var_47_0, {})
					elif arg_47_0.itemCount > 0:
						table.insert(var_47_0, {
							cd = var_47_1,
							icon = arg_47_0.itemType
						})
					else
						table.insert(var_47_0, {
							cd = True,
							icon = arg_47_0.itemType
						})
				elif arg_47_0.level[iter_47_1] > 0:
					table.insert(var_47_0, {
						cd = var_47_1,
						rate = var_47_2 == 0 and 0 or var_47_1 / var_47_2,
						icon = iter_47_1 == "ice" and arg_47_0.controller.CheckIce(arg_47_0.pos + arg_47_0.GetDirPos()) and "attack" or iter_47_1
					})
				else
					table.insert(var_47_0, {})

			return var_47_0

		function var_42_0.EventAnim(arg_48_0, arg_48_1)
			local var_48_0 = arg_48_0.GetDirMark()

			if arg_48_1 == "start":
				-- block empty
			elif arg_48_1 == "trigger":
				switch(arg_48_0.status, {
					["Freeze_" .. var_48_0 .. "_3_Shot"] = function()
						arg_48_0.controller.CreateTarget({
							name = "EF_bk_Freeze",
							parent = arg_48_0.rtScale.Find("bk")
						})
						arg_48_0.controller.BuildIce({
							pos = arg_48_0.pos,
							dirPos = arg_48_0.GetDirPos(),
							power = arg_48_0.icePower
						}),
					["Attack_" .. var_48_0] = function()
						switch(var_48_0, {
							def N:()
								arg_48_0.controller.CreateTarget({
									name = "EF_Attack_Hit_" .. var_48_0,
									parent = arg_48_0.rtScale.Find("bk")
								}),
							def S:()
								arg_48_0.controller.CreateTarget({
									name = "EF_Attack_Hit_" .. var_48_0,
									parent = arg_48_0.rtScale.Find("fr")
								})
						}, function()
							arg_48_0.controller.CreateTarget({
								name = "EF_Attack_Hit_" .. var_48_0 .. "_fr",
								parent = arg_48_0.rtScale.Find("fr")
							})
							arg_48_0.controller.CreateTarget({
								name = "EF_Attack_Hit_" .. var_48_0 .. "_bk",
								parent = arg_48_0.rtScale.Find("bk")
							}))
						arg_48_0.controller.BreakIce({
							pos = arg_48_0.pos,
							dir = arg_48_0.GetDirMark(),
							dirPos = arg_48_0.GetDirPos()
						}),
					def Lantern_Activate:()
						arg_48_0.ReloadSkill("item")

						arg_48_0.itemCount = arg_48_0.itemCount - 1
						arg_48_0.inLantern = var_42_3
						arg_48_0.effectLantern = arg_48_0.controller.CreateTarget({
							name = "EF_bk_overlay_Lantern",
							parent = arg_48_0.rtScale.Find("bk"),
							time = var_42_3
						})
				})
			elif arg_48_1 == "end":
				switch(arg_48_0.status, {
					["Bomb_" .. var_48_0 .. "_1_Start"] = function()
						arg_48_0.ReloadSkill("item")

						arg_48_0.itemCount = arg_48_0.itemCount - 1

						arg_48_0.PlayAnim("Bomb_" .. var_48_0 .. "_3_End")
						arg_48_0.controller.BuildBomb({
							pos = arg_48_0.pos,
							dir = var_48_0
						}),
					def Dead:()
						if arg_48_0.isDead:
							arg_48_0.controller.EndGame()
				})
			else
				assert(False)

		local var_42_5 = {
			E = {
				"EF_Ghost_E_bk"
			},
			N = {
				"EF_Ghost_N_bk",
				"EF_Ghost_N_fr"
			},
			S = {
				"EF_Ghost_S_bk"
			},
			W = {
				"EF_Ghost_W_bk"
			}
		}

		function var_42_0.RushCheck(arg_57_0)
			if arg_57_0.rushEffects:
				for iter_57_0, iter_57_1 in ipairs(arg_57_0.rushEffects):
					iter_57_1.Remove()

				arg_57_0.rushEffects = None

			if arg_57_0.inRush and arg_57_0.loopAnimDic[arg_57_0.GetStatusMark(arg_57_0.status)]:
				arg_57_0.rushEffects = {}

				for iter_57_2, iter_57_3 in ipairs(var_42_5[arg_57_0.GetDirMark()]):
					local var_57_0 = string.split(iter_57_3, "_")

					table.insert(arg_57_0.rushEffects, arg_57_0.controller.CreateTarget({
						name = iter_57_3,
						parent = arg_57_0.rtScale.Find(var_57_0[#var_57_0])
					}))

		function var_42_0.OnTimerUpdate(arg_58_0, arg_58_1)
			for iter_58_0, iter_58_1 in pairs(arg_58_0.skillCDs):
				arg_58_0.skillCDs[iter_58_0] = iter_58_1 - arg_58_1

			if arg_58_0.inRush:
				arg_58_0.inRush = arg_58_0.inRush - arg_58_1

				if arg_58_0.inRush <= 0:
					arg_58_0.inRush = None

			if arg_58_0.inLantern:
				arg_58_0.inLantern = arg_58_0.inLantern - arg_58_1

			if arg_58_0.inShock:
				arg_58_0.inShock = arg_58_0.inShock - arg_58_1

				if arg_58_0.inShock <= 0:
					arg_58_0.inShock = None

				return

			if arg_58_0.inCharge:
				arg_58_0.inCharge = arg_58_0.inCharge + arg_58_1

				if arg_58_0.inCharge > var_42_2:
					arg_58_0.inCharge = None

					arg_58_0.PlayAnim(string.format("Freeze_%s_3_Shot", arg_58_0.GetDirMark()))
			elif arg_58_0.inMove:
				arg_58_0.inMove = arg_58_0.inMove - arg_58_1 * arg_58_0.GetSpeed()

				if arg_58_0.inMove > 0:
					arg_58_0.realPos = arg_58_0.pos - arg_58_0.GetDirPos() * arg_58_0.inMove
				else
					arg_58_0.inMove = None
					arg_58_0.realPos = arg_58_0.pos

				arg_58_0.UpdatePosition()
			elif arg_58_0.inLock:
				return
			elif arg_58_0.controller.InBlackHoleRange(arg_58_0.pos, True):
				arg_58_0.inShock = 1

				arg_58_0.PlayAnim("Dead")
			elif arg_58_0.inLantern and arg_58_0.inLantern <= 0:
				arg_58_0.inLantern = None

				arg_58_0.effectLantern.PlayAnim("EF_bk_overlay_Lantern_Finish")

				arg_58_0.effectLantern = None
			elif arg_58_0.CheckSkill("ice") and arg_58_0.controller.GetPressInput("Skill_0"):
				arg_58_0.ReloadSkill("ice")

				if arg_58_0.controller.CheckIce(arg_58_0.pos + arg_58_0.GetDirPos()):
					arg_58_0.PlayAnim(string.format("Attack_%s", arg_58_0.GetDirMark()))
				else
					arg_58_0.inCharge = 0

					arg_58_0.PlayAnim(string.format("Freeze_%s_1_Start", arg_58_0.GetDirMark()))
			elif arg_58_0.CheckSkill("flash") and arg_58_0.controller.GetPressInput("Skill_1"):
				arg_58_0.ReloadSkill("flash")

				local var_58_0 = arg_58_0.GetDirPos()

				for iter_58_2 = arg_58_0.flashPower, 0, -1:
					if arg_58_0.controller.Moveable(arg_58_0.pos + var_58_0 * iter_58_2):
						arg_58_0.controller.CreateTarget({
							name = "EF_bk_Flash_Jump",
							pos = arg_58_0.pos
						})
						arg_58_0.UpdatePos(arg_58_0.pos + var_58_0 * iter_58_2)

						arg_58_0.realPos = arg_58_0.pos

						arg_58_0.UpdatePosition()
						arg_58_0.controller.CreateTarget({
							name = "EF_bk_Flash_Land",
							parent = arg_58_0.rtScale.Find("bk")
						})
						arg_58_0.PlayAnim(string.format("Flash_%s", arg_58_0.GetDirMark()))

						break
			elif arg_58_0.CheckSkill("rush") and arg_58_0.controller.GetPressInput("Skill_2"):
				arg_58_0.ReloadSkill("rush")

				arg_58_0.inRush = arg_58_0.rushTime

				arg_58_0.RushCheck()
			elif arg_58_0.itemType and arg_58_0.CheckSkill("item") and arg_58_0.controller.GetPressInput("Skill_3") and (arg_58_0.itemType != "lantern" or not arg_58_0.inLantern):
				if arg_58_0.itemType == "lantern":
					arg_58_0.PlayAnim("Lantern_Activate")
				elif arg_58_0.itemType == "bomb":
					arg_58_0.PlayAnim(string.format("Bomb_%s_1_Start", arg_58_0.GetDirMark()))
				else
					assert(False)
			else
				local var_58_1 = arg_58_0.controller.GetCacheInput()

				if not var_58_1:
					arg_58_0.idleTime = defaultValue(arg_58_0.idleTime, 0) - arg_58_1

					arg_58_0.PlayIdle()
				elif arg_58_0.GetStatusMark() == "Move":
					if arg_58_0.controller.Moveable(arg_58_0.pos + arg_58_0.GetDirPos(var_58_1)):
						arg_58_0.inMove = 1

						arg_58_0.UpdatePos(arg_58_0.pos + arg_58_0.GetDirPos(var_58_1))
						arg_58_0.PlayMove(var_58_1)
					else
						arg_58_0.PlayIdle(var_58_1)
				elif var_58_1 == arg_58_0.GetDirMark():
					if defaultValue(arg_58_0.idleTime, 0) <= 0 and arg_58_0.controller.Moveable(arg_58_0.pos + arg_58_0.GetDirPos()):
						arg_58_0.inMove = 1

						arg_58_0.UpdatePos(arg_58_0.pos + arg_58_0.GetDirPos())
						arg_58_0.PlayMove()
					else
						arg_58_0.idleTime = defaultValue(arg_58_0.idleTime, 0) - arg_58_1

						arg_58_0.PlayIdle()
				else
					arg_58_0.idleTime = var_42_1

					arg_58_0.PlayIdle(var_58_1)

		function var_42_0.PopPoint(arg_59_0, arg_59_1)
			local var_59_0 = arg_59_0._tf.Find("top/pop")

			setText(var_59_0.Find("Text"), "+" .. arg_59_1)
			setActive(var_59_0, False)
			setActive(var_59_0, True)

		function var_42_0.EnemyHit(arg_60_0, arg_60_1)
			if arg_60_0.isDead:
				return

			if arg_60_0.decoyCount > 0:
				arg_60_0.decoyCount = arg_60_0.decoyCount - 1
				arg_60_0.inCharge = None
				arg_60_0.inMove = None

				arg_60_0.controller.BuildDecoy(arg_60_0.pos)

				local var_60_0 = arg_60_0.controller.GetDecoyPos(arg_60_0.pos, arg_60_1)

				arg_60_0.UpdatePos(var_60_0)

				arg_60_0.realPos = arg_60_0.pos

				arg_60_0.UpdatePosition()
				arg_60_0.PlayAnim("Decoy_2")
			else
				arg_60_0.isDead = True
				arg_60_0.inCharge = None
				arg_60_0.inMove = None

				arg_60_0.PlayAnim("Dead")

		function var_42_0.UpdatePosition(arg_61_0)
			var_42_0.super.UpdatePosition(arg_61_0)
			arg_61_0.controller.WindowFocrus(arg_61_0._tf.localPosition)

			if arg_61_0.realPos == arg_61_0.pos:
				arg_61_0.controller.EatItem(arg_61_0.pos)

		return var_42_0,
	def TargetNenjuu:()
		local var_62_0 = class("TargetNenjuu", var_0_0.TargetMove)

		function var_62_0.GetSpeed(arg_63_0)
			return arg_63_0.speed * (arg_63_0.CheckAbility("rush") and 1.2 or 1) * (arg_63_0.inStealth and 1.3 or 1) * (arg_63_0.isDoppel and 0.8 or 1)

		local var_62_1 = 1.5
		local var_62_2 = 5
		local var_62_3 = 5
		local var_62_4 = 12
		local var_62_5 = {
			gravity = 0,
			teleport = 7,
			doppelgangers = 0,
			delay = 0,
			blackhole = 20,
			stealth = 10,
			rush = 0,
			attack = 2,
			breakpassable = 0
		}

		function var_62_0.CheckAbility(arg_64_0, arg_64_1)
			return arg_64_0.featuresAbility[arg_64_1] and arg_64_0.abilityCDs[arg_64_1] <= 0

		function var_62_0.ReloadAbility(arg_65_0, arg_65_1)
			arg_65_0.abilityCDs[arg_65_1] = var_62_5[arg_65_1]

		function var_62_0.InitUI(arg_66_0, arg_66_1)
			var_62_0.super.InitUI(arg_66_0, arg_66_1)

			arg_66_0.isDoppel = arg_66_1.isDoppel
			arg_66_0.speed = 1.5
			arg_66_0.featuresAbility = {
				attack = True
			}

			for iter_66_0, iter_66_1 in ipairs(NenjuuGameConfig.ABILITY_LIST):
				arg_66_0.featuresAbility[iter_66_1] = tobool(arg_66_1.abilitys[iter_66_1])

			arg_66_0.abilityCDs = {
				gravity = 0,
				teleport = 10,
				doppelgangers = 0,
				delay = 0,
				blackhole = 0,
				stealth = 0,
				rush = 0,
				attack = 0,
				breakpassable = 0
			}

		function var_62_0.EventAnim(arg_67_0, arg_67_1)
			local var_67_0 = arg_67_0.GetDirMark()

			if arg_67_1 == "start":
				-- block empty
			elif arg_67_1 == "trigger":
				switch(arg_67_0.status, {
					["Attack_" .. var_67_0] = function()
						arg_67_0.controller.CreateTarget({
							name = "EF_Attack_" .. var_67_0,
							parent = arg_67_0.rtScale.Find(var_67_0 == "N" and "bk" or "fr")
						})

						if not arg_67_0.isDoppel:
							arg_67_0.controller.BreakIce({
								pos = arg_67_0.pos,
								dir = arg_67_0.GetDirMark(),
								dirPos = arg_67_0.GetDirPos(),
								power = arg_67_0.CheckAbility("breakpassable") and 3 or 1
							})

						arg_67_0.controller.EnemyAttack({
							pos = arg_67_0.pos,
							dirPos = arg_67_0.GetDirPos()
						})
				})
			elif arg_67_1 == "end":
				switch(arg_67_0.status, {
					def Warp_1_Jump:()
						arg_67_0.UpdatePos(arg_67_0.telePos)

						arg_67_0.realPos = arg_67_0.pos

						arg_67_0.UpdatePosition()

						arg_67_0.telePos = None

						arg_67_0.PlayAnim("Warp_2_Land")
						arg_67_0.controller.OnlyBreakIce(arg_67_0.pos)
				})
			else
				assert(False)

		local var_62_6 = {
			E = {
				"EF_Nenjuu_Ghost_E_bk"
			},
			N = {
				"EF_Nenjuu_Ghost_N_bk",
				"EF_Nenjuu_Ghost_N_fr"
			},
			S = {
				"EF_Nenjuu_Ghost_S_bk"
			},
			W = {
				"EF_Nenjuu_Ghost_W_bk"
			}
		}

		function var_62_0.RushCheck(arg_70_0)
			if arg_70_0.rushEffects:
				for iter_70_0, iter_70_1 in ipairs(arg_70_0.rushEffects):
					iter_70_1.Remove()

				arg_70_0.rushEffects = None

			if arg_70_0.inStealth and arg_70_0.loopAnimDic[arg_70_0.GetStatusMark(arg_70_0.status)]:
				arg_70_0.rushEffects = {}

				for iter_70_2, iter_70_3 in ipairs(var_62_6[arg_70_0.GetDirMark()]):
					local var_70_0 = string.split(iter_70_3, "_")

					table.insert(arg_70_0.rushEffects, arg_70_0.controller.CreateTarget({
						name = iter_70_3,
						parent = arg_70_0.rtScale.Find(var_70_0[#var_70_0])
					}))

		function var_62_0.OnTimerUpdate(arg_71_0, arg_71_1)
			for iter_71_0, iter_71_1 in pairs(arg_71_0.featuresAbility):
				if iter_71_1 and var_62_5[iter_71_0] > 0:
					arg_71_0.abilityCDs[iter_71_0] = arg_71_0.abilityCDs[iter_71_0] - arg_71_1

			if arg_71_0.inStealth:
				arg_71_0.inStealth = arg_71_0.inStealth - arg_71_1

				if arg_71_0.inStealth <= 0:
					arg_71_0.inStealth = None

			if arg_71_0.inScare:
				arg_71_0.inScare = arg_71_0.inScare - arg_71_1

				if arg_71_0.inScare <= 0:
					arg_71_0.inScare = None

			if arg_71_0.CheckAbility("doppelgangers") and not arg_71_0.isSummon:
				arg_71_0.isSummon = True

				arg_71_0.controller.BuildDoppelgangers(arg_71_0.pos)

			if arg_71_0.inCharge:
				arg_71_0.inCharge = arg_71_0.inCharge + arg_71_1

				if arg_71_0.inCharge > var_62_1:
					arg_71_0.inCharge = None

					arg_71_0.PlayAnim("Warp_1_Jump")
			elif arg_71_0.inMove:
				arg_71_0.inMove = arg_71_0.inMove - arg_71_1 * arg_71_0.GetSpeed()

				if arg_71_0.inMove > 0:
					arg_71_0.realPos = arg_71_0.pos - arg_71_0.GetDirPos() * arg_71_0.inMove
				else
					arg_71_0.inMove = None
					arg_71_0.realPos = arg_71_0.pos

				arg_71_0.UpdatePosition()
			elif arg_71_0.inLock:
				return
			else
				if arg_71_0.CheckAbility("blackhole"):
					arg_71_0.ReloadAbility("blackhole")
					arg_71_0.controller.BuildBlackHole()

				if arg_71_0.CheckAbility("stealth") and arg_71_0.controller.StealthCheck(arg_71_0.pos) and not arg_71_0.inScare:
					arg_71_0.ReloadAbility("stealth")

					arg_71_0.inStealth = var_62_2

					arg_71_0.RushCheck()

				if arg_71_0.CheckAbility("attack") and not arg_71_0.inScare:
					for iter_71_2, iter_71_3 in ipairs({
						"E",
						"S",
						"W",
						"N"
					}):
						if arg_71_0.controller.AttackCheck({
							pos = arg_71_0.pos,
							dirPos = arg_71_0.GetDirPos(iter_71_3)
						}):
							arg_71_0.DoAttack(iter_71_3)

							return

				local var_71_0 = arg_71_0.controller.GetWayfindingMap(arg_71_0.pos, tobool(arg_71_0.isDoppel))
				local var_71_1 = arg_71_0.pos

				for iter_71_4, iter_71_5 in ipairs({
					"E",
					"S",
					"W",
					"N"
				}):
					local var_71_2 = var_71_0[tostring(arg_71_0.pos + arg_71_0.GetDirPos(iter_71_5))]

					if var_71_2:
						local var_71_3 = var_71_0[tostring(var_71_1)]

						if arg_71_0.inScare:
							if not var_71_3 or var_71_3.value < var_71_2.value:
								var_71_1 = arg_71_0.pos + arg_71_0.GetDirPos(iter_71_5)
						elif not var_71_3 or (var_71_3.lightValue or var_71_3.value) > (var_71_2.lightValue or var_71_2.value):
							var_71_1 = arg_71_0.pos + arg_71_0.GetDirPos(iter_71_5)

				if arg_71_0.CheckAbility("teleport") and not arg_71_0.inScare:
					if var_71_1 == arg_71_0.pos:
						if not arg_71_0.lostTime:
							arg_71_0.lostTime = 3 - arg_71_1
						elif arg_71_1 >= arg_71_0.lostTime and arg_71_0.controller.timeCount > 5:
							arg_71_0.lostTime = None

							arg_71_0.DoTeleport(var_71_0)
						else
							arg_71_0.lostTime = arg_71_0.lostTime - arg_71_1

						arg_71_0.PlayIdle()

						return
					else
						arg_71_0.lostTime = None

						if var_71_0[tostring(var_71_1)] and var_71_0[tostring(var_71_1)].value > var_62_4:
							arg_71_0.DoTeleport(var_71_0)
							arg_71_0.PlayIdle()

							return

				if not arg_71_0.isDoppel and arg_71_0.CheckAbility("attack") and arg_71_0.controller.CheckIce(var_71_1):
					arg_71_0.DoAttack(arg_71_0.GetDirMark(var_71_1 - arg_71_0.pos))
				elif arg_71_0.controller.Moveable(var_71_1):
					local var_71_4 = arg_71_0.GetDirMark(var_71_1 - arg_71_0.pos)

					arg_71_0.inMove = 1

					arg_71_0.UpdatePos(var_71_1)

					if arg_71_0.inScare:
						arg_71_0.PlayAnim("Fear_" .. var_71_4)
					else
						arg_71_0.PlayMove(var_71_4)
				elif arg_71_0.inScare:
					arg_71_0.PlayAnim("Fear_" .. arg_71_0.GetDirMark())
				else
					arg_71_0.PlayIdle()

		function var_62_0.DoAttack(arg_72_0, arg_72_1)
			if arg_72_0.inStealth:
				arg_72_0.inStealth = None

			arg_72_0.ReloadAbility("attack")
			arg_72_0.PlayAnim(string.format("Attack_%s", arg_72_1))

		function var_62_0.DoTeleport(arg_73_0, arg_73_1)
			if arg_73_0.inStealth:
				arg_73_0.inStealth = None

			arg_73_0.ReloadAbility("teleport")

			arg_73_0.inCharge = 0
			arg_73_0.telePos = arg_73_0.controller.GetTeleportTargetPos(arg_73_1, arg_73_0.pos)

			arg_73_0.controller.BuildTeleportSign({
				pos = arg_73_0.telePos,
				time = var_62_1
			})

		function var_62_0.BeScare(arg_74_0)
			arg_74_0.inCharge = None
			arg_74_0.inStealth = None
			arg_74_0.inScare = var_62_3

			if not arg_74_0.inMove:
				arg_74_0.PlayIdle()

		return var_62_0,
	def TargetEffect:()
		local var_75_0 = class("TargetEffect", var_0_0.TargetObject)

		function var_75_0.Moveable(arg_76_0)
			return True

		function var_75_0.GetBaseOrder(arg_77_0)
			return 5

		function var_75_0.InitUI(arg_78_0, arg_78_1)
			arg_78_0.mainTarget = arg_78_0._tf.Find("scale/Image")

			arg_78_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				arg_78_0.controller.DestoryTarget(arg_78_0))

		return var_75_0,
	def TargetBomb:()
		local var_80_0 = class("TargetBomb", var_0_0.TargetEffect)

		function var_80_0.InTimeLine(arg_81_0)
			return True

		function var_80_0.GetBaseOrder(arg_82_0)
			return 1

		function var_80_0.OnTimerUpdate(arg_83_0, arg_83_1)
			arg_83_0.controller.ScareEnemy({
				range = 1,
				pos = arg_83_0.pos
			})

		return var_80_0,
	def TargetTimeEffect:()
		local var_84_0 = class("TargetTimeEffect", var_0_0.TargetEffect)

		function var_84_0.GetBaseOrder(arg_85_0)
			return 1

		function var_84_0.InTimeLine(arg_86_0)
			return True

		function var_84_0.InitUI(arg_87_0, arg_87_1)
			arg_87_0.time = arg_87_1.time

		function var_84_0.OnTimerUpdate(arg_88_0, arg_88_1)
			if arg_88_1 < arg_88_0.time:
				arg_88_0.time = arg_88_0.time - arg_88_1
			else
				arg_88_0.controller.DestoryTarget(arg_88_0)

		return var_84_0,
	def TargetBlackHole:()
		local var_89_0 = class("TargetBlackHole", var_0_0.TargetEffect)

		function var_89_0.InTimeLine(arg_90_0)
			return True

		function var_89_0.GetBaseOrder(arg_91_0)
			return 3

		function var_89_0.InitUI(arg_92_0, arg_92_1)
			var_89_0.super.InitUI(arg_92_0, arg_92_1)

			arg_92_0.time = arg_92_1.time

		function var_89_0.OnTimerUpdate(arg_93_0, arg_93_1)
			if arg_93_0.isLost:
				return

			arg_93_0.controller.OnlyBreakIce(arg_93_0.pos)

			if arg_93_1 < arg_93_0.time:
				arg_93_0.time = arg_93_0.time - arg_93_1
			else
				arg_93_0.isLost = True

				arg_93_0.PlayAnim("BlackHole_3_Despawn")

		function var_89_0.BeTrigger(arg_94_0)
			if arg_94_0.isLost:
				return
			else
				arg_94_0.isLost = True

				arg_94_0.PlayAnim("BlackHole_3_Despawn")

		return var_89_0,
	def TargetSubEffect:()
		local var_95_0 = class("TargetSubEffect", var_0_0.TargetObject)

		function var_95_0.Init(arg_96_0, arg_96_1)
			arg_96_0.name = arg_96_1.name

			arg_96_0.InitUI(arg_96_1)

		function var_95_0.InitUI(arg_97_0, arg_97_1)
			arg_97_0.mainTarget = arg_97_0._tf.Find("scale/Image")

			arg_97_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				Destroy(arg_97_0._tf))

		return var_95_0,
	def TargetRushEffect:()
		local var_99_0 = class("TargetRushEffect", var_0_0.TargetSubEffect)

		function var_99_0.InTimeLine(arg_100_0)
			return True

		function var_99_0.InitUI(arg_101_0, arg_101_1)
			arg_101_0.rtScale = arg_101_0._tf.Find("scale")

			GetOrAddComponent(arg_101_0.rtScale, typeof(CanvasGroup))

			arg_101_0.alpha = 0

			setCanvasGroupAlpha(arg_101_0.rtScale, arg_101_0.alpha)

		local var_99_1 = 0.01

		function var_99_0.OnTimerUpdate(arg_102_0, arg_102_1)
			if arg_102_0.inRemove:
				arg_102_0.alpha = arg_102_0.alpha - arg_102_1 / var_99_1

				if arg_102_0.alpha <= 0:
					table.removebyvalue(arg_102_0.controller.timeFlow, arg_102_0)
					Destroy(arg_102_0._tf)
			elif arg_102_0.alpha < 1:
				arg_102_0.alpha = math.max(1, arg_102_0.alpha + arg_102_1 / var_99_1)

				setCanvasGroupAlpha(arg_102_0.rtScale, arg_102_0.alpha)

		function var_99_0.Remove(arg_103_0)
			arg_103_0.inRemove = True

		return var_99_0
}

for iter_0_0, iter_0_1 in ipairs({
	"TargetObject",
	"TargetIce",
	"TargetMove",
	"TargetFuShun",
	"TargetNenjuu",
	"TargetEffect",
	"TargetBomb",
	"TargetTimeEffect",
	"TargetBlackHole",
	"TargetSubEffect",
	"TargetItem",
	"TargetRushEffect",
	"TargetArbor"
}):
	var_0_0[iter_0_1] = var_0_1[iter_0_1]()

return var_0_0

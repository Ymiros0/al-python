local var_0_0 = class("LaunchBallPlayerControl")
local var_0_1 = {
	{
		id = 1,
		name = "Hatsuduki",
		tpl = "Hatsuduki",
		skill = {
			1,
			2,
			3,
			4
		}
	},
	{
		id = 2,
		name = "Shinano",
		tpl = "Shinano",
		skill = {
			1,
			5,
			6
		}
	},
	{
		id = 3,
		name = "Yura",
		tpl = "Yura",
		skill = {
			1,
			7,
			8
		}
	},
	{
		id = 4,
		name = "Shimakaze",
		tpl = "Shimakaze",
		skill = {
			1,
			9,
			10
		}
	}
}
local var_0_2 = 1
local var_0_3 = "skill trigger"
local var_0_4 = "skill passive"
local var_0_5 = "skill type fire"
local var_0_6 = "skill type press"
local var_0_7 = "skill type passive"

var_0_0.buff_amulet_back_time = 0.4
var_0_0.buff_panic_fire_speed = 1
var_0_0.buff_panic_enemy_rate = 5
var_0_0.buff_sleep_butterfly_time = 2
var_0_0.slash_split_time = 0.5
var_0_0.stop_enemy_time = 10
var_0_0.buff_amulet_back = 1
var_0_0.buff_panic = 2
var_0_0.buff_neglect = 3
var_0_0.buff_sleep = 4
var_0_0.buff_time_max = 5
var_0_0.buff_time_slash = 6
var_0_0.script_remove_all_enemys = "remove all enemys"
var_0_0.script_stop_enemy = "script_stop_enemy"
var_0_0.script_slash = "script_slash"
var_0_0.player_skill = {
	{
		cd_time = 0.5,
		play_time = 0.25,
		weight = 1,
		name = "atk",
		type = var_0_5,
		color = {
			1,
			2,
			3,
			4,
			5,
			6,
			7
		}
	},
	{
		cd_time = 20,
		play_time = 0.7,
		name = "player1skillA",
		skill_direct = False,
		weight = 2,
		type = var_0_6,
		buff = {
			{
				time = 10,
				type = var_0_0.buff_amulet_back
			}
		}
	},
	{
		cd_time = 0,
		play_time = 0,
		weight = 0,
		name = "panic",
		type = var_0_7,
		buff = {
			{
				time = 999999,
				type = var_0_0.buff_panic
			}
		}
	},
	{
		cd_time = 0,
		play_time = 1,
		weight = 0,
		name = "neglect",
		type = var_0_7,
		buff = {
			{
				time = 999999,
				type = var_0_0.buff_neglect,
				active_rule = {
					time = 10,
					play_time = 3.5,
					weight = 10
				}
			}
		}
	},
	{
		cd_time = 0,
		play_time = 1,
		weight = 0,
		name = "sleep",
		type = var_0_7,
		buff = {
			{
				time = 999999,
				type = var_0_0.buff_sleep,
				active_rule = {
					time = 10,
					play_time = 3,
					weight = 10
				}
			}
		}
	},
	{
		cd_time = 60,
		play_time = 1.3,
		name = "player2SkillA",
		skill_direct = False,
		weight = 2,
		type = var_0_6,
		script = var_0_0.script_remove_all_enemys,
		buff = {}
	},
	{
		cd_time = 22,
		play_time = 1.3,
		name = "player3SkillA",
		skill_direct = False,
		weight = 2,
		type = var_0_6,
		script = var_0_0.script_stop_enemy,
		buff = {}
	},
	{
		cd_time = 0,
		play_time = 0,
		weight = 0,
		name = "player3Time",
		type = var_0_7,
		buff = {
			{
				time = 999999,
				type = var_0_0.buff_time_max
			}
		}
	},
	{
		cd_time = 20,
		name = "player4SkillA",
		play_time = 1,
		skill_direct = True,
		script_time = 0.5,
		weight = 2,
		type = var_0_6,
		script = var_0_0.script_slash,
		effect = {
			distance = 200,
			name = "Slash",
			time = 0.7,
			direct = True,
			remove_time = 0.5,
			anim = "Slash"
		}
	},
	{
		cd_time = 0,
		play_time = 0,
		weight = 0,
		name = "player4SlashTime",
		type = var_0_7,
		buff = {
			{
				time = 999999,
				type = var_0_0.buff_time_slash
			}
		}
	}
}

local var_0_8 = 270
local var_0_9 = {
	{
		anim_name = "E",
		range = {
			0,
			45
		},
		direct = {
			1,
			0
		}
	},
	{
		anim_name = "N",
		range = {
			45,
			135
		},
		direct = {
			0,
			1
		}
	},
	{
		anim_name = "W",
		range = {
			135,
			225
		},
		direct = {
			-1,
			0
		}
	},
	{
		anim_name = "S",
		range = {
			225,
			315
		},
		direct = {
			0,
			-1
		}
	},
	{
		anim_name = "E",
		range = {
			315,
			360
		},
		direct = {
			1,
			0
		}
	}
}
local var_0_10 = "Idle"
local var_0_11 = "Buff"
local var_0_12 = "Panic"
local var_0_13 = "Attack"
local var_0_14 = "Skill_A"
local var_0_15 = "Skill_B"
local var_0_16 = {
	{
		anim_name = "01_Yellow"
	},
	{
		anim_name = "02_Green"
	},
	{
		anim_name = "03_White"
	},
	{
		anim_name = "04_Red"
	},
	{
		anim_name = "05_Blue"
	},
	{
		anim_name = "06_Black"
	},
	{
		anim_name = "07_Purple"
	}
}

local function var_0_17(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0.playerTf = arg_1_0
			arg_2_0.animator = GetComponent(findTF(arg_2_0.playerTf, "ad/anim"), typeof(Animator))
			arg_2_0.data = arg_1_1
			arg_2_0.eventCall = arg_1_2
			arg_2_0.panicFlag = False
			arg_2_0.directRange = Clone(var_0_9)
			arg_2_0.colors = Clone(var_0_16)
			arg_2_0.skills = {}

			for iter_2_0 = 1, #arg_1_1.skill:
				local var_2_0 = var_0_0.player_skill[arg_1_1.skill[iter_2_0]]

				table.insert(arg_2_0.skills, {
					data = var_2_0,
					time = var_2_0.cd_time
				})

			local var_2_1 = findTF(arg_2_0.playerTf, "ad/change")

			arg_2_0.changeListener = GetOrAddComponent(var_2_1, typeof(EventTriggerListener))

			arg_2_0.changeListener.AddPointDownFunc(function(arg_3_0, arg_3_1)
				arg_2_0.eventCall(LaunchBallGameScene.CHANGE_AMULET)
				arg_2_0.changePlayerStopTime(0)),
		def getId:(arg_4_0)
			return arg_4_0.data.id,
		def start:(arg_5_0)
			arg_5_0.useSkillTime = None
			arg_5_0.buffs = {}
			arg_5_0.angle = var_0_8

			arg_5_0.changePlaying(False)

			arg_5_0.panicFlag = False
			arg_5_0.idleAnimName = arg_5_0.getIdleName()

			arg_5_0.playAnim(arg_5_0.idleAnimName)

			LaunchBallGameVo.pressSkill = arg_5_0.getSkillByType(var_0_6)
			LaunchBallGameVo.buffs = arg_5_0.buffs

			for iter_5_0 = 1, #arg_5_0.skills:
				arg_5_0.skills[iter_5_0].time = arg_5_0.skills[iter_5_0].data.cd_time

				if arg_5_0.skills[iter_5_0].data.type == var_0_7:
					local var_5_0 = arg_5_0.skills[iter_5_0].data.buff

					for iter_5_1 = 1, #var_5_0:
						table.insert(arg_5_0.buffs, {
							data = var_5_0[iter_5_1],
							time = var_5_0[iter_5_1].time
						})

			arg_5_0.changePlayerStopTime(0),
		def step:(arg_6_0)
			if arg_6_0.playTime and arg_6_0.playTime > 0:
				arg_6_0.playTime = arg_6_0.playTime - LaunchBallGameVo.deltaTime

				if arg_6_0.playTime <= 0:
					arg_6_0.changePlaying(False)

			if arg_6_0.randomFireTime and arg_6_0.randomFireTime > 0:
				arg_6_0.randomFireTime = arg_6_0.randomFireTime - LaunchBallGameVo.deltaTime

				if arg_6_0.randomFireTime <= 0:
					arg_6_0.randomFireTime = None

					arg_6_0.eventCall(LaunchBallGameScene.RANDOM_FIRE, {
						num = 3,
						data = {
							[LaunchBallGameConst.amulet_buff_back] = True
						}
					})

			if arg_6_0.sleepTimeTrigger and arg_6_0.sleepTimeTrigger > 0:
				arg_6_0.sleepTimeTrigger = arg_6_0.sleepTimeTrigger - LaunchBallGameVo.deltaTime

				if arg_6_0.sleepTimeTrigger <= 0:
					arg_6_0.sleepTimeTrigger = None

					arg_6_0.eventCall(LaunchBallGameScene.SLEEP_TIME_TRIGGER)

			if not arg_6_0.isPlaying:
				local var_6_0 = arg_6_0.getIdleName()

				if arg_6_0.idleAnimName != var_6_0:
					arg_6_0.playAnim(var_6_0)

					arg_6_0.idleAnimName = var_6_0

			for iter_6_0 = 1, #arg_6_0.skills:
				if arg_6_0.skills[iter_6_0].time > 0:
					arg_6_0.skills[iter_6_0].time = arg_6_0.skills[iter_6_0].time - LaunchBallGameVo.deltaTime

					if arg_6_0.skills[iter_6_0].time <= 0:
						arg_6_0.skills[iter_6_0].time = 0

			for iter_6_1 = #arg_6_0.buffs, 1, -1:
				local var_6_1 = arg_6_0.buffs[iter_6_1]

				if var_6_1.time > 0:
					var_6_1.time = var_6_1.time - LaunchBallGameVo.deltaTime

					if var_6_1.time <= 0:
						table.remove(arg_6_0.buffs, iter_6_1)

			for iter_6_2 = #arg_6_0.buffs, 1, -1:
				local var_6_2 = arg_6_0.buffs[iter_6_2]

				if var_6_2.data.type == var_0_0.buff_panic:
					local var_6_3 = False

					if LaunchBallGameVo.enemyToEndRate:
						for iter_6_3 = 1, #LaunchBallGameVo.enemyToEndRate:
							if not var_6_3 and LaunchBallGameVo.enemyToEndRate[iter_6_3] > var_0_0.buff_panic_enemy_rate:
								var_6_3 = True

					var_6_2.active = var_6_3

					if var_6_2.active:
						local var_6_4 = arg_6_0.getSkillByType(var_0_5)

						if var_6_4.time > 0:
							var_6_4.time = var_6_4.time - LaunchBallGameVo.deltaTime * var_0_0.buff_panic_fire_speed
				elif var_6_2.data.type == var_0_0.buff_neglect:
					arg_6_0.updateBuffStopTime(var_6_2)
				elif var_6_2.data.type == var_0_0.buff_sleep:
					arg_6_0.updateBuffStopTime(var_6_2)
				else
					var_6_2.active = True

			arg_6_0.changePlayerStopTime(arg_6_0.playerStopTime + LaunchBallGameVo.deltaTime),
		def setPlayTime:(arg_7_0, arg_7_1)
			if arg_7_1 and arg_7_1 > 0:
				print("set play time " .. arg_7_1)

				arg_7_0.isPlaying = True
			else
				print("clear play time" .. arg_7_1)

				arg_7_0.isPlaying = False

			arg_7_0.playTime = arg_7_1,
		def updateBuffStopTime:(arg_8_0, arg_8_1)
			if not arg_8_1.active and arg_8_0.playerStopTime > arg_8_1.data.active_rule.time:
				arg_8_1.active = True

				LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_use_pass_skill, 1)
				arg_8_0.setPlayTime(arg_8_1.data.active_rule.play_time)

				arg_8_0.weight = arg_8_1.data.active_rule.weight

				if arg_8_1.data.type == var_0_0.buff_neglect:
					arg_8_0.randomFireTime = 1.5

					if arg_8_0.getBuff(var_0_0.buff_panic).active:
						arg_8_0.playAnim("Skill_B_Panic_Start")
					else
						arg_8_0.playAnim("Skill_B_Start")
				elif arg_8_1.data.type == var_0_0.buff_sleep:
					local var_8_0 = "Trans_Sleep_" .. arg_8_0.getDirectName(arg_8_0.angle)

					arg_8_0.playAnim(var_8_0)

			if arg_8_1.active and arg_8_1.data.type == var_0_0.buff_sleep and not arg_8_0.sleepTimeTrigger:
				arg_8_0.sleepTimeTrigger = var_0_0.buff_sleep_butterfly_time

			if arg_8_1.active and arg_8_0.playerStopTime < arg_8_1.data.active_rule.time:
				arg_8_1.active = False,
		def split:(arg_9_0, arg_9_1)
			if arg_9_1.split and arg_9_0.getBuff(var_0_0.buff_time_slash):
				local var_9_0 = arg_9_0.getSkillByType(var_0_6)

				if var_9_0 and var_9_0.time > 0:
					var_9_0.time = var_9_0.time - var_0_0.slash_split_time,
		def changePlaying:(arg_10_0, arg_10_1, arg_10_2)
			if arg_10_1:
				arg_10_0.setPlayTime(arg_10_2.data.play_time)

				arg_10_0.weight = arg_10_2.data.weight
			else
				arg_10_0.setPlayTime(0)

				arg_10_0.weight = 0

			if arg_10_0.eventCall:
				arg_10_0.eventCall(LaunchBallGameScene.PLAYING_CHANGE, arg_10_1),
		def fire:(arg_11_0)
			local var_11_0 = arg_11_0.getSkillByType(var_0_5)

			if arg_11_0.checkSkillAble(var_11_0):
				arg_11_0.changePlayerStopTime(0)

				if not LaunchBallGameVo.amulet:
					print("当前没有可以发射的符咒")

					return

				arg_11_0.appearSkill(var_11_0),
		def getSkillByType:(arg_12_0, arg_12_1)
			for iter_12_0 = 1, #arg_12_0.skills:
				local var_12_0 = arg_12_0.skills[iter_12_0]

				if var_12_0.data.type == arg_12_1:
					return var_12_0

			return None,
		def checkSkillAble:(arg_13_0, arg_13_1)
			if arg_13_1.time > 0:
				print("还在cd中 cd = " .. arg_13_1.time)

				return False

			if arg_13_0.isPlaying and arg_13_1.data.weight <= arg_13_0.weight:
				print("权重不够无法覆盖当前的技能")

				return False

			return True,
		def appearSkill:(arg_14_0, arg_14_1)
			arg_14_0.changePlayerStopTime(0)
			arg_14_0.changePlaying(True, arg_14_1)

			arg_14_1.time = arg_14_1.data.cd_time

			if arg_14_1.data.type == var_0_5:
				local var_14_0 = LaunchBallGameVo.amulet.color
				local var_14_1 = arg_14_0.getSkillAnimName(arg_14_1, var_14_0)

				arg_14_0.playAnim(var_14_1)
				arg_14_0.eventCall(LaunchBallGameScene.FIRE_AMULET)
			elif arg_14_1.data.type == var_0_6:
				print("使用了主动技能")

				local var_14_2 = arg_14_0.getSkillAnimName(arg_14_1)

				arg_14_0.playAnim(var_14_2)

				arg_14_0.idleAnimName = None

				if arg_14_0.useSkillTime:
					local var_14_3 = LaunchBallGameVo.gameStepTime - arg_14_0.useSkillTime

					LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.reuslt_double_skill_time, var_14_3)
				else
					arg_14_0.useSkillTime = LaunchBallGameVo.gameStepTime

				pg.CriMgr.GetInstance().PlaySoundEffect_V3(LaunchBallGameVo.SFX_PRESS_SKILL)
				LaunchBallGameVo.AddGameResultData(LaunchBallGameVo.result_use_skill, 1)

			local var_14_4 = arg_14_1.data.buff

			if var_14_4:
				for iter_14_0 = 1, #var_14_4:
					local var_14_5 = var_14_4[iter_14_0]
					local var_14_6 = var_14_5.time

					table.insert(arg_14_0.buffs, {
						data = var_14_5,
						time = var_14_6
					})

			if arg_14_1.data.script:
				if arg_14_1.data.script == var_0_0.script_remove_all_enemys:
					arg_14_0.eventCall(LaunchBallGameScene.SPLIT_ALL_ENEMYS, {
						time = 1.3,
						effect = True
					})
				elif arg_14_1.data.script == var_0_0.script_stop_enemy:
					arg_14_0.eventCall(LaunchBallGameScene.STOP_ENEMY_TIME, {
						time = var_0_0.stop_enemy_time
					})
				elif arg_14_1.data.script == var_0_0.script_slash:
					arg_14_0.eventCall(LaunchBallGameScene.SLASH_ENEMY, {
						time = arg_14_1.data.script_time,
						direct = arg_14_0.getDirectName(arg_14_0.angle)
					})
					arg_14_0.eventCall(LaunchBallGameScene.PLAYER_EFFECT, arg_14_1.data.effect),
		def getSkillAnimName:(arg_15_0, arg_15_1, arg_15_2)
			local var_15_0 = ""
			local var_15_1
			local var_15_2
			local var_15_3
			local var_15_4
			local var_15_5 = arg_15_1.data

			if var_15_5.type == var_0_5:
				local var_15_6 = var_0_13
				local var_15_7 = arg_15_0.getBuff(var_0_0.buff_panic)

				if var_15_7 and var_15_7.active:
					var_15_2 = var_0_12

				local var_15_8 = arg_15_0.getDirectName(arg_15_0.angle)

				if arg_15_2:
					var_15_4 = arg_15_0.getColorName(arg_15_2)

				if var_15_2:
					var_15_0 = var_15_6 .. "_" .. var_15_2 .. "_" .. var_15_8 .. "_" .. var_15_4
				else
					var_15_0 = var_15_6 .. "_" .. var_15_8 .. "_" .. var_15_4
			elif var_15_5.type == var_0_6:
				var_15_0 = var_0_14

				if var_15_5.skill_direct:
					local var_15_9 = arg_15_0.getDirectName(arg_15_0.angle)

					var_15_0 = var_15_0 .. "_" .. var_15_9

			return var_15_0,
		def getBuff:(arg_16_0, arg_16_1)
			for iter_16_0 = 1, #arg_16_0.buffs:
				if arg_16_0.buffs[iter_16_0].data.type == arg_16_1:
					return arg_16_0.buffs[iter_16_0]

			return None,
		def getColorName:(arg_17_0, arg_17_1)
			return arg_17_0.colors[arg_17_1].anim_name,
		def useSkill:(arg_18_0)
			local var_18_0 = arg_18_0.getSkillByType(var_0_6)

			if not var_18_0:
				return

			if arg_18_0.checkSkillAble(var_18_0):
				arg_18_0.appearSkill(var_18_0),
		def clear:(arg_19_0)
			return,
		def setAngle:(arg_20_0, arg_20_1)
			arg_20_0.changePlayerStopTime(0)

			arg_20_0.angle = (LaunchBallGameVo.joyStickData.angle + 360) % 360,
		def changePlayerStopTime:(arg_21_0, arg_21_1)
			if arg_21_0.getBuff(var_0_0.buff_neglect):
				if arg_21_0.getBuff(var_0_0.buff_neglect).active and arg_21_0.playTime > 0:
					return
			elif arg_21_0.getBuff(var_0_0.buff_sleep) and arg_21_0.getBuff(var_0_0.buff_sleep).active and arg_21_0.playTime > 0:
				return

			arg_21_0.playerStopTime = arg_21_1,
		def playAnim:(arg_22_0, arg_22_1)
			print("play anim is " .. arg_22_1)
			arg_22_0.animator.Play(arg_22_1),
		def getIdleName:(arg_23_0)
			local var_23_0 = var_0_10
			local var_23_1
			local var_23_2
			local var_23_3
			local var_23_4 = arg_23_0.getDirectName(arg_23_0.angle)
			local var_23_5 = arg_23_0.getBuff(var_0_0.buff_amulet_back)
			local var_23_6 = arg_23_0.getBuff(var_0_0.buff_panic)

			if var_23_5 and var_23_5.active:
				var_23_3 = var_0_11

			if var_23_6 and var_23_6.active:
				var_23_2 = var_0_12

			if var_23_3:
				var_23_0 = var_23_0 .. "_" .. var_23_3
			elif var_23_2:
				var_23_0 = var_23_0 .. "_" .. var_23_2

			if var_23_4:
				var_23_0 = var_23_0 .. "_" .. var_23_4

			return var_23_0,
		def getDirectName:(arg_24_0, arg_24_1)
			local var_24_0
			local var_24_1

			for iter_24_0 = 1, #arg_24_0.directRange:
				local var_24_2 = arg_24_0.directRange[iter_24_0].range

				if arg_24_1 >= var_24_2[1] and arg_24_1 < var_24_2[2]:
					var_24_0 = arg_24_0.directRange[iter_24_0].anim_name
					var_24_1 = arg_24_0.directRange[iter_24_0].direct

			return var_24_0, var_24_1,
		def setContent:(arg_25_0, arg_25_1, arg_25_2)
			setParent(arg_25_0.playerTf, arg_25_1)
			setActive(arg_25_0.playerTf, True)

			if arg_25_2:
				arg_25_0.playerTf.anchoredPosition = arg_25_2
			else
				arg_25_0.playerTf.anchoredPosition = Vector2(0, 0),
		def dispose:(arg_26_0)
			if arg_26_0.changeListener:
				ClearEventTrigger(arg_26_0.changeListener)

			if arg_26_0.playerTf:
				Destroy(arg_26_0.playerTf)

				arg_26_0.playerTf = None
	}

	var_1_0.ctor()

	return var_1_0

def var_0_0.Ctor(arg_27_0, arg_27_1, arg_27_2, arg_27_3, arg_27_4):
	arg_27_0._topContent = arg_27_1
	arg_27_0._content = arg_27_2
	arg_27_0._tpl = arg_27_3
	arg_27_0._eventCall = arg_27_4

def var_0_0.setPlayerData(arg_28_0, arg_28_1):
	if arg_28_0.player and arg_28_0.player.getId() != arg_28_1.id:
		arg_28_0.player.dispose()

		arg_28_0.player = None
		arg_28_0.player = arg_28_0.createPlayer(arg_28_1)
	elif not arg_28_0.player:
		arg_28_0.player = arg_28_0.createPlayer(arg_28_1)

def var_0_0.createPlayer(arg_29_0, arg_29_1):
	local var_29_0 = tf(instantiate(findTF(arg_29_0._tpl, arg_29_1.tpl)))
	local var_29_1 = var_0_17(var_29_0, arg_29_1, arg_29_0._eventCall)

	var_29_1.setContent(arg_29_0._content)

	return var_29_1

def var_0_0.start(arg_30_0):
	arg_30_0.playerId = LaunchBallGameVo.selectPlayer

	arg_30_0.setPlayerData(var_0_1[arg_30_0.playerId])
	arg_30_0.player.start()

	arg_30_0.effects = {}

def var_0_0.step(arg_31_0):
	if LaunchBallGameVo.joyStickData and LaunchBallGameVo.joyStickData.active and LaunchBallGameVo.joyStickData.angle:
		arg_31_0.player.setAngle(LaunchBallGameVo.joyStickData.angle)

	if arg_31_0.effects and #arg_31_0.effects > 0:
		for iter_31_0 = #arg_31_0.effects, 1, -1:
			local var_31_0 = arg_31_0.effects[iter_31_0].tf
			local var_31_1 = arg_31_0.effects[iter_31_0].anim
			local var_31_2 = arg_31_0.effects[iter_31_0].animName
			local var_31_3 = arg_31_0.effects[iter_31_0].removeTime

			if arg_31_0.effects[iter_31_0].time and arg_31_0.effects[iter_31_0].time > 0:
				arg_31_0.effects[iter_31_0].time = arg_31_0.effects[iter_31_0].time - LaunchBallGameVo.deltaTime

				if arg_31_0.effects[iter_31_0].time < 0:
					arg_31_0.effects[iter_31_0].time = None

					setActive(var_31_0, False)
					setActive(var_31_0, True)
					var_31_1.Play(var_31_2)
			elif arg_31_0.effects[iter_31_0].removeTime and arg_31_0.effects[iter_31_0].removeTime > 0:
				arg_31_0.effects[iter_31_0].removeTime = arg_31_0.effects[iter_31_0].removeTime - LaunchBallGameVo.deltaTime

				if arg_31_0.effects[iter_31_0].removeTime < 0:
					arg_31_0.effects[iter_31_0].removeTime = None

					setActive(var_31_0, False)
					table.remove(arg_31_0.effects, iter_31_0)

	arg_31_0.player.step()

def var_0_0.eventCall(arg_32_0, arg_32_1, arg_32_2):
	if arg_32_1 == LaunchBallGameScene.CHANGE_AMULET:
		-- block empty
	elif arg_32_1 == LaunchBallGameScene.PLAYER_EFFECT:
		local var_32_0 = arg_32_2

		if var_32_0:
			local var_32_1
			local var_32_2 = var_32_0.name
			local var_32_3 = findTF(arg_32_0._topContent, "effect/" .. var_32_2)
			local var_32_4 = GetComponent(findTF(var_32_3, "ad/anim"), typeof(Animator))
			local var_32_5 = var_32_0.anim
			local var_32_6 = var_32_0.distance
			local var_32_7 = Vector2(0, 0)

			if var_32_0.direct:
				local var_32_8, var_32_9 = arg_32_0.player.getDirectName(arg_32_0.player.angle)

				var_32_5 = var_32_5 .. "_" .. var_32_8
				var_32_3.anchoredPosition = Vector2(var_32_9[1] * var_32_6, var_32_9[2] * var_32_6)

			table.insert(arg_32_0.effects, {
				tf = var_32_3,
				anim = var_32_4,
				time = var_32_0.time,
				removeTime = var_32_0.remove_time,
				animName = var_32_5
			})
	elif arg_32_1 == LaunchBallGameScene.SPILT_ENEMY_SCORE:
		arg_32_0.player.split(arg_32_2)

def var_0_0.press(arg_33_0, arg_33_1):
	if arg_33_1 == KeyCode.J and arg_33_0.player:
		arg_33_0.player.fire()

def var_0_0.joystickActive(arg_34_0, arg_34_1):
	if not arg_34_1 and arg_34_0.player:
		arg_34_0.player.fire()

def var_0_0.useSkill(arg_35_0):
	if arg_35_0.player:
		arg_35_0.player.useSkill()

def var_0_0.clear(arg_36_0):
	arg_36_0.player.clear()

return var_0_0

local var_0_0 = class("ShipStatus")

var_0_0.flagList = {
	"inChapter",
	"inFleet",
	"inElite",
	"inActivity",
	"inPvP",
	"inExercise",
	"inEvent",
	"inClass",
	"inTactics",
	"inBackyard",
	"inAdmiral",
	"inWorld",
	"isActivityNpc",
	"inGuildEvent",
	"inGuildBossEvent",
	"inChallenge",
	"inSupport"
}

def var_0_0.checkShipFlag(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = defaultValue(arg_1_1[arg_1_2], var_0_0.TAG_HIDE_BASE[arg_1_2])

	if type(var_1_0) == "boolean":
		return not var_1_0 and arg_1_0.getFlag(arg_1_2)
	elif type(var_1_0) == "number":
		return arg_1_0.getFlag(arg_1_2, var_1_0)
	else
		assert(False, "type error")

def var_0_0.ShipStatusToTag(arg_2_0, arg_2_1):
	if var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inChapter"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_inFight")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inFleet"):
		local var_2_0 = getProxy(FleetProxy).GetRegularFleetByShip(arg_2_0)

		assert(var_2_0)

		local var_2_1 = var_2_0.id

		if var_2_0.isRegularFleet():
			var_2_1 = math.fmod(var_2_1, 10)

			return {
				"ui/dockyardui_atlas",
				"biandui0" .. var_2_1,
				""
			}
		else
			return {
				"shipstatus",
				"red",
				Fleet.DEFAULT_NAME_FOR_DOCKYARD[var_2_1]
			}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inElite"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_inHardFormation")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inSupport"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_inSupportFleet")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inActivity"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_activity")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inChallenge"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_challenge")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inPvP"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_inPVP")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inEvent"):
		return {
			"shipstatus",
			"green",
			i18n("word_status_inEvent")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inBackyard"):
		if arg_2_0.state == Ship.STATE_REST:
			return {
				"shipstatus",
				"purple",
				i18n("word_status_rest")
			}
		elif arg_2_0.state == Ship.STATE_TRAIN:
			return {
				"shipstatus",
				"purple",
				i18n("word_status_train")
			}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inClass"):
		return {
			"shipstatus",
			"blue",
			i18n("word_status_inClass")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inTactics"):
		return {
			"shipstatus",
			"blue",
			i18n("word_status_inTactics")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inAdmiral"):
		return {
			"shipstatus",
			"light_green",
			i18n("common_flag_ship")
		}
	elif var_0_0.checkShipFlag(arg_2_0, arg_2_1, "inWorld"):
		return {
			"shipstatus",
			"red",
			i18n("word_status_world")
		}
	elif getProxy(SettingsProxy).IsRandomFlagShip(arg_2_0.id):
		return {
			"shipstatus",
			"light_yellow",
			i18n("random_flag_ship")
		}

var_0_0.FILTER_SHIPS_FLAGS_1 = {
	inExercise = False,
	inChapter = True,
	inFleet = False,
	inSupport = True,
	inPvP = False,
	inActivity = True,
	inTactics = False,
	inElite = False,
	inGuildEvent = True,
	inEvent = True,
	inBackyard = False,
	inClass = True,
	isActivityNpc = True,
	inChallenge = True,
	inWorld = True,
	inAdmiral = True
}
var_0_0.FILTER_SHIPS_FLAGS_2 = {
	inGuildBossEvent = True,
	inChallenge = True,
	inBackyard = True,
	inSupport = True,
	inClass = True,
	inActivity = True,
	inGuildEvent = True,
	isActivityNpc = True,
	inWorld = True,
	inAdmiral = True,
	inExercise = True,
	inChapter = True,
	inFleet = True,
	inPvP = True,
	inTactics = True,
	inElite = True,
	inEvent = True
}
var_0_0.FILTER_SHIPS_FLAGS_3 = {
	inExercise = False,
	inChapter = True,
	inFleet = False,
	inSupport = True,
	inPvP = False,
	inActivity = True,
	inTactics = False,
	inElite = False,
	inGuildEvent = True,
	inEvent = True,
	inBackyard = False,
	inClass = True,
	isActivityNpc = True,
	inChallenge = True,
	inWorld = True,
	inAdmiral = False
}
var_0_0.FILTER_SHIPS_FLAGS_4 = {
	inPvP = True,
	inChallenge = True,
	inBackyard = True,
	inSupport = True,
	inClass = True,
	inActivity = True,
	inGuildEvent = True,
	isActivityNpc = True,
	inWorld = True,
	inAdmiral = True,
	inExercise = True,
	inChapter = True,
	inFleet = True,
	inGuildBossEvent = True,
	inTactics = True,
	inElite = True,
	inEvent = True
}
var_0_0.TAG_HIDE_ALL = {
	inExercise = True,
	inChallenge = True,
	inChapter = True,
	inFleet = True,
	inPvP = True,
	inActivity = True,
	inTactics = True,
	inElite = True,
	inClass = True,
	inEvent = True,
	inBackyard = True,
	isActivityNpc = True,
	inWorld = True,
	inAdmiral = True
}
var_0_0.TAG_HIDE_BASE = {
	inExercise = True,
	inChallenge = False,
	inChapter = False,
	inSupport = False,
	inPvP = False,
	inActivity = False,
	inTactics = False,
	inElite = True,
	inClass = False,
	inEvent = False,
	inFleet = False,
	inBackyard = False,
	isActivityNpc = False,
	inWorld = False,
	inAdmiral = False
}
var_0_0.TAG_HIDE_ACTIVITY_BOSS = {
	inChallenge = True,
	inChapter = True,
	inPvP = True,
	inFleet = True,
	inClass = True,
	inBackyard = True,
	inTactics = True,
	inAdmiral = True
}
var_0_0.TAG_HIDE_BACKYARD = {
	inExercise = False,
	inChallenge = True,
	inChapter = True,
	inEvent = True,
	inPvP = True,
	inActivity = True,
	inTactics = True
}
var_0_0.TAG_HIDE_PVP = {
	inExercise = False,
	inChapter = True,
	inChallenge = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True,
	inPvP = True
}
var_0_0.TAG_HIDE_DEFENSE = {
	inExercise = False,
	inChapter = True,
	inChallenge = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True,
	inPvP = True,
	inEvent = True
}
var_0_0.TAG_HIDE_LEVEL = {
	inBackyard = True,
	inChallenge = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inAdmiral = True
}
var_0_0.TAG_HIDE_SUPPORT = {
	inBackyard = True,
	inChallenge = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inAdmiral = True
}
var_0_0.TAG_HIDE_NORMAL = {
	inExercise = False,
	inChallenge = True,
	inPvP = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True
}
var_0_0.TAG_HIDE_CHALLENGE = {
	inPvP = True,
	inChapter = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True,
	inEvent = False,
	inAdmiral = True
}
var_0_0.TAG_HIDE_EVENT = {
	inExercise = False,
	inChallenge = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True
}
var_0_0.TAG_HIDE_TACTICES = {
	inExercise = False,
	inChapter = True,
	inChallenge = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True,
	inPvP = True,
	inEvent = True
}
var_0_0.TAG_HIDE_ADMIRAL = {
	inExercise = False,
	inChapter = True,
	inChallenge = True,
	inFleet = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True,
	inPvP = True,
	inEvent = True
}
var_0_0.TAG_HIDE_FORMATION = {
	inExercise = False,
	inChallenge = True,
	inPvP = True,
	inClass = True,
	inActivity = True,
	inTactics = True,
	inBackyard = True
}
var_0_0.TAG_HIDE_WORLD = {
	inActivity = True,
	inChallenge = True,
	inFleet = True
}
var_0_0.TAG_HIDE_DESTROY = {
	inElite = False
}
var_0_0.TAG_BLOCK_EVENT = {
	inEvent = True
}
var_0_0.TAG_BLOCK_PVP = {
	inEvent = True
}
var_0_0.TAG_BLOCK_BACKYARD = {
	inClass = True
}
var_0_0.STATE_CHANGE_OK = -1
var_0_0.STATE_CHANGE_FAIL = 0
var_0_0.STATE_CHANGE_CHECK = 1
var_0_0.STATE_CHANGE_TIP = 2

local var_0_1 = {
	inFleet = {
		inEvent = 0,
		inSupport = 1
	},
	inSupport = {
		inEvent = 0,
		inFleet = 0
	},
	inElite = {
		inEvent = 0,
		inElite = 0
	},
	inActivity = {
		isActivityNpc = 0,
		inEvent = 0
	},
	inChallenge = {
		isActivityNpc = 0,
		inEvent = 0
	},
	inEvent = {
		inEvent = 0,
		inChapter = 0,
		inSupport = 0,
		inFleet = 1,
		isActivityNpc = 0,
		inPvP = 1
	},
	inClass = {
		isActivityNpc = 0,
		inClass = 0,
		inBackyard = 1
	},
	inTactics = {
		inTactics = 0
	},
	inBackyard = {
		inClass = 0,
		isActivityNpc = 0
	},
	inWorld = {
		isActivityNpc = 0
	},
	onPropose = {
		inChapter = 0,
		inEvent = 0
	},
	onModify = {
		inChapter = 0
	},
	onDestroy = {
		inExercise = 1,
		inChallenge = 0,
		inSupport = 0,
		inFleet = 1,
		inClass = 0,
		inActivity = 0,
		inTactics = 1,
		inBackyard = 1,
		inGuildEvent = 0,
		inEvent = 0,
		inChapter = 0,
		inPvP = 1,
		isActivityNpc = 0,
		inGuildBossEvent = 1,
		inWorld = 0,
		inAdmiral = 0
	},
	onTeamChange = {
		inExercise = 1,
		inChallenge = 0,
		inChapter = 0,
		inFleet = 1,
		inPvP = 1,
		inActivity = 0,
		inWorld = 1,
		inGuildBossEvent = 1
	}
}
local var_0_2 = {
	inChapter = {
		tips_block = "word_shipState_fight"
	},
	inFleet = {
		tips_block = "word_shipState_fight"
	},
	inElite = {
		tips_block = "word_shipState_fight"
	},
	inActivity = {
		tips_block = "shipmodechange_reject_inactivity"
	},
	inChallenge = {
		tips_block = "shipmodechange_reject_inchallenge"
	},
	inPvP = {
		tips_block = "word_shipState_fight"
	},
	inExercise = {
		tips_block = "word_shipState_fight"
	},
	inEvent = {
		tips_block = "word_shipState_event"
	},
	inClass = {
		tips_block = "word_shipState_study"
	},
	inTactics = {
		tips_block = "word_shipState_tactics"
	},
	inBackyard = {
		tips_block = "word_shipState_rest"
	},
	inAdmiral = {
		tips_block = "playerinfo_ship_is_already_flagship"
	},
	inGuildEvent = {
		tips_block = "word_shipState_guild_event"
	},
	inGuildBossEvent = {
		tips_block = "word_shipState_guild_event"
	},
	isActivityNpc = {
		tips_block = "word_shipState_npc"
	},
	inWorld = {
		tips_block = "word_shipState_world"
	},
	inSupport = {
		tips_block = "word_shipState_support"
	}
}

def var_0_0.ShipStatusCheck(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0, var_3_1 = var_0_0.ShipStatusConflict(arg_3_0, arg_3_1, arg_3_3)

	if var_3_0 == var_0_0.STATE_CHANGE_FAIL:
		return False, i18n(var_3_1)
	elif var_3_0 == var_0_0.STATE_CHANGE_CHECK:
		if arg_3_2:
			return var_0_0.ChangeStatusCheckBox(var_3_1, arg_3_1, arg_3_2)
		else
			return False
	elif var_3_0 == var_0_0.STATE_CHANGE_TIP:
		return var_0_0.ChangeStatusTipBox(var_3_1, arg_3_1)
	elif var_3_0 == var_0_0.STATE_CHANGE_OK:
		return True
	else
		assert(False, "unknow error")

def var_0_0.ShipStatusConflict(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = var_0_1[arg_4_0]

	arg_4_2 = arg_4_2 or {}

	for iter_4_0, iter_4_1 in ipairs(var_0_0.flagList):
		if var_4_0[iter_4_1] == var_0_0.STATE_CHANGE_FAIL and arg_4_1.getFlag(iter_4_1, arg_4_2[iter_4_1]):
			return var_0_0.STATE_CHANGE_FAIL, var_0_2[iter_4_1].tips_block

	for iter_4_2, iter_4_3 in ipairs(var_0_0.flagList):
		if var_4_0[iter_4_3] == var_0_0.STATE_CHANGE_CHECK and arg_4_1.getFlag(iter_4_3, arg_4_2[iter_4_3]):
			return var_0_0.STATE_CHANGE_CHECK, iter_4_3

	for iter_4_4, iter_4_5 in ipairs(var_0_0.flagList):
		if var_4_0[iter_4_5] == var_0_0.STATE_CHANGE_TIP and arg_4_1.getFlag(iter_4_5, arg_4_2[iter_4_5]):
			return var_0_0.STATE_CHANGE_TIP, iter_4_5

	return var_0_0.STATE_CHANGE_OK

def var_0_0.ChangeStatusCheckBox(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_0 == "inBackyard":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("ship_vo_moveout_backyard"),
			def onYes:()
				pg.m02.sendNotification(GAME.EXIT_SHIP, {
					callback = arg_5_2,
					shipId = arg_5_1.id
				})
		})

		return False, None
	elif arg_5_0 == "inFleet":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("shipchange_alert_infleet"),
			def onYes:()
				local var_7_0 = getProxy(FleetProxy).GetRegularFleetByShip(arg_5_1)

				if var_7_0.canRemove(arg_5_1):
					var_7_0.removeShip(arg_5_1)
					pg.m02.sendNotification(GAME.UPDATE_FLEET, {
						callback = arg_5_2,
						fleet = var_7_0
					})
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("shipmodechange_reject_1stfleet_only"))
		})

		return False, None
	elif arg_5_0 == "inPvP":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("shipchange_alert_inpvp"),
			def onYes:()
				local var_8_0 = getProxy(FleetProxy).getFleetById(FleetProxy.PVP_FLEET_ID)

				if var_8_0.canRemove(arg_5_1):
					var_8_0.removeShip(arg_5_1)
					pg.m02.sendNotification(GAME.UPDATE_FLEET, {
						callback = arg_5_2,
						fleet = var_8_0
					})
				else
					local var_8_1 = arg_5_1.getTeamType()

					if var_8_1 == TeamType.Vanguard:
						pg.TipsMgr.GetInstance().ShowTips(i18n("ship_vo_vanguardFleet_must_hasShip"))
					elif var_8_1 == TeamType.Main:
						pg.TipsMgr.GetInstance().ShowTips(i18n("ship_vo_mainFleet_must_hasShip"))
		})

		return False, None
	elif arg_5_0 == "inExercise":
		local var_5_0 = getProxy(MilitaryExerciseProxy).getExerciseFleet()

		if var_5_0.canRemove(arg_5_1):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("shipchange_alert_inexercise"),
				def onYes:()
					var_5_0.removeShip(arg_5_1)
					pg.m02.sendNotification(GAME.UPDATE_EXERCISE_FLEET, {
						fleet = var_5_0,
						callback = arg_5_2
					})
			})
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("exercise_clear_fleet_tip"),
				def onYes:()
					var_5_0.removeShip(arg_5_1)
					pg.m02.sendNotification(GAME.UPDATE_EXERCISE_FLEET, {
						fleet = var_5_0,
						callback = arg_5_2
					})
			})

		return False, None
	elif arg_5_0 == "inTactics":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("tactics_lesson_cancel"),
			def onYes:()
				local var_11_0 = getProxy(NavalAcademyProxy).getStudentIdByShipId(arg_5_1.id)

				pg.m02.sendNotification(GAME.CANCEL_LEARN_TACTICS, {
					callback = arg_5_2,
					shipId = var_11_0,
					type = Student.CANCEL_TYPE_MANUAL
				})
		})

		return False, None
	elif arg_5_0 == "inGuildBossEvent":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("word_shipState_guild_boss"),
			def onYes:()
				local var_12_0 = getProxy(GuildProxy).getRawData()

				if not var_12_0:
					return

				local var_12_1 = var_12_0.GetActiveEvent()

				if not var_12_1:
					return

				local var_12_2 = var_12_1.GetBossMission()

				if not var_12_2 or not var_12_2.IsActive():
					return

				local var_12_3 = getProxy(PlayerProxy).getRawData().id
				local var_12_4 = var_12_2.GetFleetUserId(var_12_3, arg_5_1.id)

				if not var_12_4:
					return

				local var_12_5 = Clone(var_12_4)

				var_12_5.RemoveUserShip(var_12_3, arg_5_1.id)
				pg.m02.sendNotification(GAME.GUILD_UPDATE_BOSS_FORMATION, {
					force = True,
					editFleet = {
						[var_12_5.id] = var_12_5
					},
					callback = arg_5_2
				})
		})

		return False, None
	elif arg_5_0 == "inWorld":
		local var_5_1 = nowWorld()

		if var_5_1.type == World.TypeBase:
			WorldConst.ReqWorldCheck(arg_5_2)

			return False, None
		else
			local var_5_2 = var_5_1.GetShip(arg_5_1.id).fleetId

			if #var_5_1.GetFleet(var_5_2)[arg_5_1.getTeamType()] > 1:
				return True
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("shipmodechange_reject_worldfleet_only"))

				return False, None

	return True

def var_0_0.ChangeStatusTipBox(arg_13_0, arg_13_1):
	if arg_13_0 == "inElite":
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("ship_vo_moveout_hardFormation")
		})

	return True

def var_0_0.canDestroyShip(arg_14_0, arg_14_1):
	if arg_14_0.isBluePrintShip():
		return False, i18n("blueprint_destory_tip")
	elif arg_14_0.GetLockState() == Ship.LOCK_STATE_LOCK:
		return False, i18n("ship_vo_locked")
	elif arg_14_0.isMetaShip():
		return False, i18n("meta_destroy_tip")

	return var_0_0.ShipStatusCheck("onDestroy", arg_14_0, arg_14_1)

return var_0_0

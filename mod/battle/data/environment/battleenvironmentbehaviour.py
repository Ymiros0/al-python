ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviour")

var_0_0.Battle.BattleEnvironmentBehaviour = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviour"
var_0_3.STATE_DELAY = "STATE_DELAY"
var_0_3.STATE_READY = "STATE_READY"
var_0_3.STATE_OVERHEAT = "STATE_OVERHEAT"
var_0_3.STATE_EXPIRE = "STATE_EXPIRE"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._cldUnitList = {}

def var_0_3.SetUnitRef(arg_2_0, arg_2_1):
	assert(arg_2_1, "Shounld Bind A Unit")

	arg_2_0._unit = arg_2_1

def var_0_3.SetTemplate(arg_3_0, arg_3_1):
	arg_3_0._tmpData = arg_3_1

	if arg_3_0._tmpData.delay:
		arg_3_0._delayStartTime = pg.TimeMgr.GetInstance().GetCombatTime()
		arg_3_0._state = var_0_3.STATE_DELAY
	else
		arg_3_0._state = var_0_3.STATE_READY

	if arg_3_0._tmpData.life_time:
		arg_3_0._liftStartTime = pg.TimeMgr.GetInstance().GetCombatTime()

	arg_3_0._diveFilter = arg_3_0._tmpData.diveFilter or {}

def var_0_3.UpdateCollideUnitList(arg_4_0, arg_4_1):
	if #arg_4_0._diveFilter != 0:
		local var_4_0 = #arg_4_1

		while var_4_0 > 0:
			local var_4_1 = arg_4_1[var_4_0].GetCurrentOxyState()

			for iter_4_0, iter_4_1 in ipairs(arg_4_0._diveFilter):
				if var_4_1 == iter_4_1:
					table.remove(arg_4_1, var_4_0)

					break

			var_4_0 = var_4_0 - 1

	arg_4_0._cldUnitList = arg_4_1

def var_0_3.OnUpdate(arg_5_0):
	arg_5_0.updateDelay()
	arg_5_0.updateReload()
	arg_5_0.updateLifeTime()

	if arg_5_0._state == var_0_3.STATE_READY:
		arg_5_0.doBehaviour()

def var_0_3.Dispose(arg_6_0):
	arg_6_0._cldUnitList = None
	arg_6_0._tmpData = None
	arg_6_0._CDstartTime = None

def var_0_3.OnCollide(arg_7_0, arg_7_1):
	return

def var_0_3.GetCurrentState(arg_8_0):
	return arg_8_0._state

def var_0_3.updateDelay(arg_9_0):
	if arg_9_0._delayStartTime and arg_9_0._tmpData.delay + arg_9_0._delayStartTime <= pg.TimeMgr.GetInstance().GetCombatTime():
		arg_9_0._delayStartTime = None

		arg_9_0.handleCoolDown()

def var_0_3.updateReload(arg_10_0):
	if arg_10_0._CDstartTime:
		if arg_10_0.getReloadFinishTimeStamp() <= pg.TimeMgr.GetInstance().GetCombatTime():
			arg_10_0.handleCoolDown()
		else
			return

def var_0_3.updateLifeTime(arg_11_0):
	if arg_11_0._liftStartTime and arg_11_0._liftStartTime + arg_11_0._tmpData.life_time <= pg.TimeMgr.GetInstance().GetCombatTime():
		arg_11_0._state = var_0_3.STATE_EXPIRE

		arg_11_0.doExpire()

def var_0_3.getReloadFinishTimeStamp(arg_12_0):
	return arg_12_0._tmpData.reload_time + arg_12_0._CDstartTime

def var_0_3.handleCoolDown(arg_13_0):
	arg_13_0._state = var_0_3.STATE_READY
	arg_13_0._CDstartTime = None

def var_0_3.doBehaviour(arg_14_0):
	if arg_14_0._tmpData.reload_time:
		arg_14_0._CDstartTime = pg.TimeMgr.GetInstance().GetCombatTime()
		arg_14_0._state = var_0_3.STATE_OVERHEAT

def var_0_3.doExpire(arg_15_0):
	arg_15_0._state = var_0_3.STATE_EXPIRE

var_0_3.BehaviourClassEnum = {
	[var_0_1.EnviroumentBehaviour.PLAY_FX] = "BattleEnvironmentBehaviourPlayFX",
	[var_0_1.EnviroumentBehaviour.DAMAGE] = "BattleEnvironmentBehaviourDamage",
	[var_0_1.EnviroumentBehaviour.BUFF] = "BattleEnvironmentBehaviourBuff",
	[var_0_1.EnviroumentBehaviour.MOVEMENT] = "BattleEnvironmentBehaviourMovement",
	[var_0_1.EnviroumentBehaviour.FORCE] = "BattleEnvironmentBehaviourForce",
	[var_0_1.EnviroumentBehaviour.SPAWN] = "BattleEnvironmentBehaviourSpawn",
	[var_0_1.EnviroumentBehaviour.PLAY_SFX] = "BattleEnvironmentBehaviourPlaySFX",
	[var_0_1.EnviroumentBehaviour.SHAKE_SCREEN] = "BattleEnvironmentBehaviourShakeScreen"
}

def var_0_3.CreateBehaviour(arg_16_0):
	return var_0_0.Battle[var_0_3.BehaviourClassEnum[arg_16_0.type]].New()

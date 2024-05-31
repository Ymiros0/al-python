pg = pg or {}

local var_0_0 = pg
local var_0_1 = singletonClass("EffectMgr")

var_0_0.EffectMgr = var_0_1

def var_0_1.Ctor(arg_1_0):
	local var_1_0 = ys.Battle.BattleResourceManager.GetInstance()

	arg_1_0.effectCbMap = setmetatable({}, {
		__mode = "k"
	})

	function arg_1_0.commonEffectEvent(arg_2_0)
		local var_2_0 = arg_1_0.effectCbMap[arg_2_0]

		if var_2_0 == None:
			var_1_0.DestroyOb(arg_2_0)

			return

		local var_2_1 = var_2_0[2]

		if var_2_1 != None:
			var_2_1(arg_2_0)

		arg_1_0.effectCbMap[arg_2_0] = None

		if var_2_0[1]:
			var_1_0.DestroyOb(arg_2_0)
		else
			arg_2_0.SetActive(False)

def var_0_1.ClearBattleEffectMap(arg_3_0):
	arg_3_0.effectCbMap = setmetatable({}, {
		__mode = "k"
	})

def var_0_1.CommonEffectEvent(arg_4_0, arg_4_1):
	LuaHelper.SetParticleEndEvent(arg_4_1, arg_4_0.commonEffectEvent)

def var_0_1.PlayBattleEffect(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5):
	arg_5_1.transform.localPosition = arg_5_2

	arg_5_1.SetActive(True)

	if arg_5_5:
		LuaHelper.SetParticleSpeed(arg_5_1, 1 / Time.timeScale)

	arg_5_0.effectCbMap[arg_5_1] = {
		arg_5_3,
		arg_5_4
	}

def var_0_1.BattleUIEffect(arg_6_0, arg_6_1, arg_6_2):
	assert(string.sub(arg_6_1, -2, -1) == "UI", "UI效果不是以UI结尾，请检查")
	LoadAndInstantiateAsync("UI", arg_6_1, function(arg_7_0)
		local var_7_0 = ys.Battle.BattleState.GetInstance()

		if var_7_0.GetState() != var_7_0.BATTLE_STATE_FIGHT:
			Destroy(arg_7_0)

			return

		local var_7_1 = var_0_0.UIMgr.GetInstance().UIMain

		LuaHelper.SetGOParentGO(arg_7_0, var_7_1, False)
		SetActive(arg_7_0, True)
		arg_6_2(arg_7_0))

def var_0_1.EndEffect(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0._effectMap[arg_8_1]

	if var_8_0 != None:
		var_8_0.GetComponent(typeof(ParticleSystem)).Stop()

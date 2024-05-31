ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleArcEffect")

var_0_0.Battle.BattleArcEffect = var_0_3
var_0_3.__name = "BattleArcEffect"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0._go = arg_1_1
	arg_1_0._characterA = arg_1_2
	arg_1_0._unitA = arg_1_2.GetUnitData()
	arg_1_0._unitB = arg_1_3
	arg_1_0._boundBone = arg_1_4
	arg_1_0._material = arg_1_0._go.transform.GetComponent(typeof(Renderer)).material

	local var_1_0 = arg_1_0._characterA.GetBonePos(arg_1_0._boundBone)
	local var_1_1 = arg_1_0._unitB.GetPosition()

	arg_1_0._vectorA = Vector4.New(var_1_0.x, 5, var_1_0.z, 1)
	arg_1_0._vectorB = Vector4.New(var_1_1.x, 5, var_1_1.z, 1)

	arg_1_0._material.SetVector("_PosBegin", arg_1_0._vectorA)
	arg_1_0._material.SetVector("_PosEnd", arg_1_0._vectorB)

def var_0_3.Update(arg_2_0):
	if arg_2_0._unitA.IsAlive() and arg_2_0._unitB.IsAlive():
		local var_2_0 = arg_2_0._characterA.GetBonePos(arg_2_0._boundBone)
		local var_2_1 = arg_2_0._unitB.GetPosition()

		arg_2_0._vectorA.x = var_2_0.x
		arg_2_0._vectorA.z = var_2_0.z
		arg_2_0._vectorB.x = var_2_1.x
		arg_2_0._vectorB.z = var_2_1.z

		arg_2_0._material.SetVector("_PosBegin", arg_2_0._vectorA)
		arg_2_0._material.SetVector("_PosEnd", arg_2_0._vectorB)

		arg_2_0._go.transform.position = arg_2_0._vectorA
	else
		arg_2_0._callback()

def var_0_3.ConfigCallback(arg_3_0, arg_3_1):
	arg_3_0._callback = arg_3_1

	pg.EffectMgr.GetInstance().PlayBattleEffect(arg_3_0._go, Vector3.zero, True, arg_3_0._callback)

def var_0_3.Dispose(arg_4_0):
	arg_4_0._callback = None
	arg_4_0._material = None
	arg_4_0._go = None
	arg_4_0._unitA = None
	arg_4_0._unitB = None
	arg_4_0._vectorA = None
	arg_4_0._vectorB = None

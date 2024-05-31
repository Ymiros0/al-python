ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleAOEMobilizedComponent")

var_0_0.Battle.BattleAOEMobilizedComponent = var_0_2
var_0_2.__name = "BattleAOEMobilizedComponent"
var_0_2.STAY = 0
var_0_2.FOLLOW = 1
var_0_2.REFERENCE = 2

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._area = arg_1_1

	arg_1_0._area.AppendComponent(arg_1_0)

	local var_1_0 = arg_1_0._area.Settle

	function arg_1_0._area.Settle()
		arg_1_0.updatePosition()
		var_1_0(arg_1_0._area)

def var_0_2.Dispose(arg_3_0):
	arg_3_0._area = None
	arg_3_0._referenceUnit = None

def var_0_2.SetReferenceUnit(arg_4_0, arg_4_1):
	arg_4_0._referenceUnit = arg_4_1
	arg_4_0._referencePoint = Clone(arg_4_1.GetPosition())

def var_0_2.ConfigData(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1 == var_0_2.STAY:
		arg_5_0.updatePosition = var_0_2.doStay
	elif arg_5_1 == var_0_2.FOLLOW:
		arg_5_0.updatePosition = var_0_2.doFollow
	elif arg_5_1 == var_0_2.REFERENCE:
		arg_5_0.updatePosition = var_0_2.doReference
		arg_5_0._speedVector = Vector3.New(arg_5_2.speedX, 0, 0)

def var_0_2.doStay():
	return

def var_0_2.doFollow(arg_7_0):
	local var_7_0 = setmetatable({}, {
		__index = arg_7_0._referenceUnit.GetPosition()
	})

	arg_7_0._area.SetPosition(var_7_0)

def var_0_2.doReference(arg_8_0):
	arg_8_0._referencePoint.Add(arg_8_0._speedVector)
	arg_8_0._area.SetPosition(arg_8_0._referencePoint)

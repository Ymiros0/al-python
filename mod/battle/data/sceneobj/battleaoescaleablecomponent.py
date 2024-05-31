ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleAOEScaleableComponent")

var_0_0.Battle.BattleAOEScaleableComponent = var_0_3
var_0_3.__name = "BattleAOEScaleableComponent"
var_0_3.FILL = 1
var_0_3.EXPEND = 2

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._area = arg_1_1

	arg_1_0._area.AppendComponent(arg_1_0)

	local var_1_0 = arg_1_0._area.Settle

	function arg_1_0._area.Settle()
		arg_1_0.updateScale()
		var_1_0(arg_1_0._area)

def var_0_3.Dispose(arg_3_0):
	arg_3_0._area = None
	arg_3_0._referenceUnit = None

def var_0_3.SetReferenceUnit(arg_4_0, arg_4_1):
	arg_4_0._referenceUnit = arg_4_1
	arg_4_0._referencePoint = Clone(arg_4_1.GetPosition())

def var_0_3.ConfigData(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1 == var_0_3.FILL:
		arg_5_0.updateScale = var_0_3.doFill
		arg_5_0._upperBound = arg_5_2.upperBound
		arg_5_0._lowerBound = arg_5_2.lowerBound
		arg_5_0._rearBound = arg_5_2.rearBound
		arg_5_0._frontOffset = arg_5_2.frontOffset
	elif arg_5_1 == var_0_3.EXPEND:
		arg_5_0._area.SetFXStatic(False)

		arg_5_0.updateScale = var_0_3.doExpend
		arg_5_0._expendDuration = arg_5_2.expendDuration
		arg_5_0._widthExpendSpeed = arg_5_2.widthSpeed
		arg_5_0._heightExpendSpeed = arg_5_2.heightSpeed
		arg_5_0._expendStartTime = pg.TimeMgr.GetInstance().GetCombatTime()
		arg_5_0._lastExpendTime = pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_3.doFill(arg_6_0):
	local var_6_0 = setmetatable({}, {
		__index = arg_6_0._referenceUnit.GetPosition()
	})
	local var_6_1 = arg_6_0._area.GetIFF()
	local var_6_2 = math.abs(arg_6_0._upperBound - arg_6_0._lowerBound)
	local var_6_3 = arg_6_0._frontOffset * 2

	arg_6_0._area.SetWidth(var_6_3)
	arg_6_0._area.SetHeight(var_6_2)
	arg_6_0._area.GetCldComponent().ResetSize(var_6_3, 5, var_6_2)

	local var_6_4 = var_6_2 * 0.5 + arg_6_0._lowerBound
	local var_6_5 = var_6_0.x

	arg_6_0._referencePoint.x = var_6_5
	arg_6_0._referencePoint.z = var_6_4

	arg_6_0._area.SetPosition(arg_6_0._referencePoint)

def var_0_3.doExpend(arg_7_0):
	local var_7_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	if var_7_0 - arg_7_0._expendStartTime < arg_7_0._expendDuration:
		local var_7_1 = arg_7_0._area.GetWidth()
		local var_7_2 = arg_7_0._area.GetHeight()
		local var_7_3 = var_7_0 - arg_7_0._lastExpendTime
		local var_7_4 = var_7_1 + arg_7_0._widthExpendSpeed * var_7_3
		local var_7_5 = var_7_2 + arg_7_0._heightExpendSpeed * var_7_3

		arg_7_0._area.SetWidth(var_7_4)
		arg_7_0._area.SetHeight(var_7_5)
		arg_7_0._area.GetCldComponent().ResetSize(var_7_1, 5, var_7_2)

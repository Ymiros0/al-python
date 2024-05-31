ys = ys or {}

local var_0_0 = ys
local var_0_1 = require("Mgr/Pool/PoolUtil")
local var_0_2 = singletonClass("BattleArrowManager")

var_0_0.Battle.BattleArrowManager = var_0_2
var_0_2.__name = "BattleArrowManager"
var_0_2.ROOT_NAME = "EnemyArrowContainer"
var_0_2.ARROW_NAME = "EnemyArrow"

function var_0_2.Ctor(arg_1_0)
	return
end

local var_0_3 = Vector3(0, 10000, 0)

function var_0_2.HideBullet(arg_2_0)
	arg_2_0.transform.position = var_0_3
end

function var_0_2.Init(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:Find(var_0_2.ARROW_NAME).gameObject

	var_3_0.transform.position = var_0_3

	var_3_0:SetActive(true)

	local var_3_1 = pg.Pool.New(arg_3_1, var_3_0, 5, 10, true, true)

	var_3_1:SetRecycleFuncs(var_0_2.HideBullet)
	var_3_1:InitSize()

	arg_3_0._arrowPool = var_3_1
end

function var_0_2.Clear(arg_4_0)
	arg_4_0._arrowPool:Dispose()
end

function var_0_2.GetArrow(arg_5_0)
	return (arg_5_0._arrowPool:GetObject())
end

function var_0_2.DestroyObj(arg_6_0, arg_6_1)
	if arg_6_1 == nil then
		return
	end

	arg_6_0._arrowPool:Recycle(arg_6_1)
end

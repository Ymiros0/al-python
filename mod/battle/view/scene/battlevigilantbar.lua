ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleVigilantBar = class("BattleVigilantBar")
var_0_0.Battle.BattleVigilantBar.__name = "BattleVigilantBar"

local var_0_1 = var_0_0.Battle.BattleVigilantBar

var_0_1.MIN = 0.267
var_0_1.MAX = 0.7335
var_0_1.METER_LENGTH = var_0_1.MAX - var_0_1.MIN
var_0_1.STATE_CALM = 0
var_0_1.STATE_SUSPICIOUS = 1
var_0_1.STATE_VIGILANT = 2
var_0_1.STATE_ENGAGE = 3

function var_0_1.Ctor(arg_1_0, arg_1_1)
	arg_1_0._vigilantBar = arg_1_1
	arg_1_0._vigilantBarGO = arg_1_0._vigilantBar.gameObject
	arg_1_0._progress = arg_1_0._vigilantBar:Find("progress"):GetComponent(typeof(Image))
	arg_1_0._markList = {}
	arg_1_0._markList[var_0_1.STATE_CALM] = arg_1_0._vigilantBar:Find("mark/" .. var_0_1.STATE_CALM)
	arg_1_0._markList[var_0_1.STATE_SUSPICIOUS] = arg_1_0._vigilantBar:Find("mark/" .. var_0_1.STATE_SUSPICIOUS)
	arg_1_0._markList[var_0_1.STATE_VIGILANT] = arg_1_0._vigilantBar:Find("mark/" .. var_0_1.STATE_VIGILANT)
	arg_1_0._markList[var_0_1.STATE_ENGAGE] = arg_1_0._vigilantBar:Find("mark/" .. var_0_1.STATE_ENGAGE)
end

function var_0_1.ConfigVigilant(arg_2_0, arg_2_1)
	arg_2_0._vigilantState = arg_2_1
end

function var_0_1.UpdateVigilantProgress(arg_3_0)
	local var_3_0 = arg_3_0._vigilantState:GetVigilantRate()

	arg_3_0._progress.fillAmount = arg_3_0.meterConvert(var_3_0)
end

function var_0_1.UpdateVigilantMark(arg_4_0)
	local var_4_0 = arg_4_0._vigilantState:GetVigilantMark()

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._markList) do
		SetActive(iter_4_1, var_4_0 == iter_4_0)
	end
end

function var_0_1.UpdateVigilantBarPosition(arg_5_0, arg_5_1)
	arg_5_0._vigilantBar.position = arg_5_1
end

function var_0_1.meterConvert(arg_6_0)
	return var_0_1.METER_LENGTH * arg_6_0 + var_0_1.MIN
end

function var_0_1.Dispose(arg_7_0)
	arg_7_0._vigilantState = nil

	Object.Destroy(arg_7_0._vigilantBarGO)

	arg_7_0._vigilantBar = nil
	arg_7_0._vigilantBarGO = nil
	arg_7_0._markList = nil
	arg_7_0._progress = nil
end

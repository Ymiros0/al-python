ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleMainDamagedView = class("BattleMainDamagedView")

local var_0_2 = class("BattleMainDamagedView")

var_0_0.Battle.BattleMainDamagedView = var_0_2
var_0_2.__name = "BattleMainDamagedView"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1

	arg_1_0:Init()
end

function var_0_2.Init(arg_2_0)
	arg_2_0._tf = arg_2_0._go.transform
	arg_2_0._bleedView = findTF(arg_2_0._tf, "mainUnitDamaged")
	arg_2_0._bleedAnimation = arg_2_0._bleedView:GetComponent(typeof(Animator))

	arg_2_0._bleedView:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_3_0)
		setActive(arg_2_0._bleedView, false)

		arg_2_0._isPlaying = false
	end)
	setActive(arg_2_0._bleedView, false)

	arg_2_0._isPlaying = false
end

function var_0_2.Play(arg_4_0)
	if not arg_4_0._isPlaying then
		setActive(arg_4_0._bleedView, true)
	end

	arg_4_0._isPlaying = true
end

function var_0_2.Dispose(arg_5_0)
	arg_5_0._bleedView = nil
	arg_5_0._bleedAnimation = nil
	arg_5_0._tf = nil
	arg_5_0._go = nil
end

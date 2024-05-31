ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleTorpedoBullet
local var_0_2 = var_0_0.Battle.BattleResourceManager

var_0_0.Battle.BattleTorpedoBullet = class("BattleTorpedoBullet", var_0_0.Battle.BattleBullet)
var_0_0.Battle.BattleTorpedoBullet.__name = "BattleTorpedoBullet"

local var_0_3 = var_0_0.Battle.BattleTorpedoBullet

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.Dispose(arg_2_0):
	if arg_2_0._alert:
		arg_2_0._alert.Dispose()

	var_0_3.super.Dispose(arg_2_0)

def var_0_3.Advance(arg_3_0):
	arg_3_0._speed = arg_3_0._speed * 2

def var_0_3.GetZExtraOffset(arg_4_0):
	return 0

def var_0_3.MakeAlert(arg_5_0, arg_5_1):
	arg_5_0._alert = var_0_0.Battle.TorAlert.New(arg_5_1)

	arg_5_0._alert.SetPosition(arg_5_0._bulletData.GetPosition(), arg_5_0._bulletData.GetYAngle())

def var_0_3.Neutrailze(arg_6_0):
	SetActive(arg_6_0._go, False)

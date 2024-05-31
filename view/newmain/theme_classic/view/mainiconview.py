local var_0_0 = class("MainIconView", import("...base.MainBaseView"))
local var_0_1 = 1
local var_0_2 = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, None)

	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject
	arg_1_0.iconList = {
		[var_0_1] = MainSpineIcon.New(arg_1_1),
		[var_0_2] = MainEducateCharIcon.New(arg_1_1)
	}

def var_0_0.GetIconType(arg_2_0, arg_2_1):
	if isa(arg_2_1, VirtualEducateCharShip):
		return var_0_2
	else
		return var_0_1

def var_0_0.Init(arg_3_0, arg_3_1):
	arg_3_0.ship = arg_3_1

	local var_3_0 = arg_3_0.GetIconType(arg_3_1)

	if arg_3_0.iconInstance:
		arg_3_0.iconInstance.Unload()

		arg_3_0.iconInstance = None

	arg_3_0.iconInstance = arg_3_0.iconList[var_3_0]

	arg_3_0.iconInstance.Load(arg_3_1.getPrefab())

def var_0_0.Refresh(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getPrefab()
	local var_4_1 = arg_4_0.GetIconType(arg_4_1)

	if arg_4_0.iconList[var_4_1] != arg_4_0.iconInstance or arg_4_0.name != var_4_0:
		arg_4_0.Init(arg_4_1)
	elif arg_4_0.iconInstance:
		arg_4_0.iconInstance.Resume()

	arg_4_0.ship = arg_4_1

def var_0_0.Disable(arg_5_0):
	if arg_5_0.iconInstance:
		arg_5_0.iconInstance.Pause()

def var_0_0.IsLoading(arg_6_0):
	if arg_6_0.iconInstance:
		return arg_6_0.iconInstance.IsLoading()

	return False

def var_0_0.GetDirection(arg_7_0):
	return Vector2(0, 1)

def var_0_0.Dispose(arg_8_0):
	var_0_0.super.Dispose(arg_8_0)

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.iconList):
		iter_8_1.Dispose()

	arg_8_0.iconList = None
	arg_8_0.iconInstance = None

return var_0_0

local var_0_0 = class("NewSystemSubmarineRunResultGradePage", import("..dodgem.NewDodgemResultGradePage"))

def var_0_0.GetFlagShip(arg_1_0):
	return Ship.New({
		id = 9999,
		configId = 900180,
		skin_id = 900180
	})

def var_0_0.RegisterEvent(arg_2_0, arg_2_1):
	seriesAsync({
		function(arg_3_0)
			arg_2_0.LoadPainitingContainer(arg_3_0),
		function(arg_4_0)
			arg_2_0.MovePainting(arg_4_0)
	}, function()
		onButton(arg_2_0, arg_2_0._tf, function()
			arg_2_1(), SFX_PANEL))

def var_0_0.GetGetObjectives(arg_7_0):
	return {}

return var_0_0

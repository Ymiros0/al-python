pg = pg or {}
pg.Live2DMgr = singletonClass("Live2DMgr")

local var_0_0 = pg.Live2DMgr

def var_0_0.Ctor(arg_1_0):
	arg_1_0.loader = AutoLoader.New()

def var_0_0.GetLive2DModelAsync(arg_2_0, arg_2_1, arg_2_2):
	return (arg_2_0.loader.LoadLive2D(arg_2_1, arg_2_2))

def var_0_0.StopLoadingLive2d(arg_3_0, arg_3_1):
	arg_3_0.loader.ClearRequest(arg_3_1)

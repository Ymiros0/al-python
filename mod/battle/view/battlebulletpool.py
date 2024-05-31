ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleBulletPool")

var_0_0.Battle.BattleBulletPool = var_0_1
var_0_1.__name = "BattleBulletPool"

def var_0_1.Ctor(arg_1_0):
	return

def var_0_1.Init(arg_2_0):
	arg_2_0._bulletResCache = {}

def var_0_1.InstantiateBullet(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0._bulletResCache[arg_3_1] != None:
		arg_3_2(arg_3_0._bulletResCache[arg_3_1])
	else
		ResourceMgr.Inst.getAssetAsync("Item/" .. arg_3_1, arg_3_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_4_0)
			assert(arg_4_0, "子弹资源加载失败：" .. arg_3_1)
			arg_3_2(arg_4_0)

			arg_3_0._bulletResCache[arg_3_1] = arg_4_0), True, True)

def var_0_1.Clear(arg_5_0):
	arg_5_0._bulletResCache = None

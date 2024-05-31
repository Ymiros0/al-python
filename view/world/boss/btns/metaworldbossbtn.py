local var_0_0 = class("MetaWorldbossBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.event = arg_1_2
	arg_1_0.metaBtn = arg_1_1
	arg_1_0.metaProgress = arg_1_1.Find("Text").GetComponent(typeof(Text))
	arg_1_0.metaTip = arg_1_1.Find("tip")

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	onButton(arg_2_0, arg_2_0.metaBtn, function()
		local var_3_0 = WorldBossConst.GetCurrBossGroup()

		arg_2_0.event.emit(WorldBossMediator.GO_META, var_3_0), SFX_PANEL)
	arg_2_0.Update()

def var_0_0.Update(arg_4_0):
	local var_4_0 = WorldBossConst.GetCurrBossGroup()

	setActive(arg_4_0.metaTip, MetaCharacterConst.isMetaSynRedTag(var_4_0))

def var_0_0.Dispose(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)

return var_0_0

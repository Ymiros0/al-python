pg = pg or {}
pg.GuildPaintingMgr = singletonClass("GuildPaintingMgr")

local var_0_0 = pg.GuildPaintingMgr

def var_0_0.Enter(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.isShipPainting = arg_2_3

	arg_2_0.Show()

	if arg_2_0.name == arg_2_1:
		return

	arg_2_0.Clear()

	if arg_2_0.isShipPainting:
		setPaintingPrefabAsync(arg_2_0._tf, arg_2_1, "chuanwu")
	else
		setGuildPaintingPrefabAsync(arg_2_0._tf, arg_2_1, "chuanwu")

	arg_2_0.name = arg_2_1

	if arg_2_2:
		arg_2_0._tf.localPosition = arg_2_2

def var_0_0.Show(arg_3_0):
	if not IsNil(arg_3_0._tf):
		setActive(arg_3_0._tf, True)

def var_0_0.Hide(arg_4_0):
	if not IsNil(arg_4_0._tf):
		setActive(arg_4_0._tf, False)

def var_0_0.Clear(arg_5_0):
	if arg_5_0.name:
		if arg_5_0.isShipPainting:
			retPaintingPrefab(arg_5_0._tf, arg_5_0.name)
		else
			retGuildPaintingPrefab(arg_5_0._tf, arg_5_0.name)

		arg_5_0.name = None

def var_0_0.Exit(arg_6_0):
	arg_6_0.Clear()

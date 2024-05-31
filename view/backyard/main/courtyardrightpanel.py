local var_0_0 = class("CourtYardRightPanel", import(".CourtYardBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "main/rightPanel"

def var_0_0.init(arg_2_0):
	arg_2_0.buffBtn = arg_2_0._tf.Find("buff")
	arg_2_0.oneKeyBtn = arg_2_0._tf.Find("onekey")
	arg_2_0.buffPage = CourtYardBuffPage.New(arg_2_0._tf.parent.parent, arg_2_0.parent)

def var_0_0.GenBuffData(arg_3_0):
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(BuffHelper.GetBackYardPlayerBuffs()):
		if iter_3_1.isActivate():
			table.insert(var_3_0, iter_3_1)

	return var_3_0

def var_0_0.OnRegister(arg_4_0):
	onButton(arg_4_0, arg_4_0.buffBtn, function()
		local var_5_0 = arg_4_0.buffList or arg_4_0.GenBuffData()

		if #var_5_0 > 0:
			arg_4_0.buffPage.ExecuteAction("Show", var_5_0), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.oneKeyBtn, function()
		arg_4_0.emit(CourtYardMediator.ONE_KEY), SFX_PANEL)

def var_0_0.OnVisitRegister(arg_7_0):
	setActive(arg_7_0._tf, False)

def var_0_0.OnFlush(arg_8_0, arg_8_1):
	arg_8_1 = arg_8_1 or bit.bor(BackYardConst.DORM_UPDATE_TYPE_LEVEL, BackYardConst.DORM_UPDATE_TYPE_USEFOOD, BackYardConst.DORM_UPDATE_TYPE_SHIP)

	local var_8_0 = arg_8_0.dorm

	if bit.band(arg_8_1, BackYardConst.DORM_UPDATE_TYPE_USEFOOD) > 0 and arg_8_0.IsInner():
		arg_8_0.buffList = arg_8_0.GenBuffData()

		setActive(arg_8_0.buffBtn, #arg_8_0.buffList > 0)

	if bit.band(arg_8_1, BackYardConst.DORM_UPDATE_TYPE_SHIP) > 0:
		setActive(arg_8_0.oneKeyBtn, var_8_0.AnyShipExistIntimacyOrMoney())

def var_0_0.GetMoveX(arg_9_0):
	return {
		{
			arg_9_0._tf,
			1
		}
	}

def var_0_0.OnDispose(arg_10_0):
	if arg_10_0.buffPage:
		arg_10_0.buffPage.Destroy()

		arg_10_0.buffPage = None

return var_0_0

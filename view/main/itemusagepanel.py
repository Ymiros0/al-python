local var_0_0 = class("ItemUsagePanel")

var_0_0.SINGLE = 1
var_0_0.BATCH = 2
var_0_0.INFO = 3
var_0_0.SEE = 4

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_1

	setActive(arg_1_0._go, False)

	arg_1_0._parent = arg_1_2
	arg_1_0.backBtn = findTF(arg_1_0._go, "window/top/btnBack")
	arg_1_0.itemTF = findTF(arg_1_0._go, "window/item")
	arg_1_0.itemIntro = findTF(arg_1_0.itemTF, "display_panel/desc/Text")
	arg_1_0.itemName = findTF(arg_1_0.itemTF, "display_panel/name_container/name/Text")
	arg_1_0.resetBtn = findTF(arg_1_0.itemTF, "reset_btn")
	arg_1_0.useBtn = findTF(arg_1_0._go, "window/actions/use_one_button")

	setActive(arg_1_0.useBtn, False)

	arg_1_0.batchUseBtn = findTF(arg_1_0._go, "window/actions/batch_use_button")

	setActive(arg_1_0.batchUseBtn, False)

	arg_1_0.useOneBtn = findTF(arg_1_0._go, "window/actions/use_button")

	setActive(arg_1_0.useOneBtn, False)

	arg_1_0.confirmBtn = findTF(arg_1_0._go, "window/actions/confirm_button")

	setActive(arg_1_0.confirmBtn, False)

	arg_1_0.seeBtn = findTF(arg_1_0._go, "window/actions/see_button")

	setActive(arg_1_0.seeBtn, False)

	arg_1_0.batchText = arg_1_0.batchUseBtn.Find("text")

	onButton(arg_1_0, arg_1_0.backBtn, function()
		arg_1_0.Close(), SFX_PANEL)
	onButton(arg_1_0, findTF(arg_1_0._go, "bg"), function()
		arg_1_0.Close(), SFX_PANEL)

def var_0_0.Open(arg_4_0, arg_4_1):
	arg_4_0.settings = arg_4_1 or {}

	local var_4_0 = arg_4_0.settings.item

	arg_4_0.Update(var_4_0)
	arg_4_0.UpdateAction(var_4_0)
	setActive(arg_4_0.resetBtn, True)
	setActive(arg_4_0._go, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0._go)

def var_0_0.Close(arg_5_0):
	arg_5_0.settings = None

	setActive(arg_5_0._go, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_5_0._go, arg_5_0._parent)

def var_0_0.Update(arg_6_0, arg_6_1):
	local var_6_0 = Drop.New({
		type = DROP_TYPE_WORLD_ITEM,
		id = arg_6_1.id,
		count = arg_6_1.count
	})

	updateDrop(arg_6_0.itemTF.Find("left/IconTpl"), var_6_0)
	UpdateOwnDisplay(arg_6_0.itemTF.Find("left/own"), var_6_0)
	RegisterDetailButton(arg_6_0, arg_6_0.itemTF.Find("left/detail"), var_6_0)
	setText(arg_6_0.itemIntro, arg_6_1.getConfig("display"))
	setText(arg_6_0.itemName, arg_6_1.getConfig("name"))
	onButton(arg_6_0, arg_6_0.resetBtn, function()
		assert(arg_6_0.settings.onResetInfo, "without reset info callback")
		arg_6_0.settings.onResetInfo(Drop.New({
			count = 1,
			type = DROP_TYPE_WORLD_ITEM,
			id = arg_6_1.id
		})), SFX_PANEL)

def var_0_0.UpdateAction(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.settings
	local var_8_1 = arg_8_0.settings.mode or var_0_0.SINGLE

	setActive(arg_8_0.useBtn, var_8_1 == var_0_0.SINGLE)
	setActive(arg_8_0.batchUseBtn, var_8_1 == var_0_0.BATCH)
	setActive(arg_8_0.useOneBtn, var_8_1 == var_0_0.BATCH)
	setActive(arg_8_0.confirmBtn, var_8_1 == var_0_0.INFO)
	setActive(arg_8_0.seeBtn, var_8_1 == var_0_0.SEE)

	if var_8_1 == var_0_0.SINGLE:
		onButton(arg_8_0, arg_8_0.useBtn, function()
			if arg_8_1.count == 0:
				return

			if var_8_0.onUse:
				var_8_0.onUse()

			arg_8_0.Close(), SFX_PANEL)
	elif var_8_1 == var_0_0.BATCH:
		local var_8_2 = math.min(arg_8_1.count, 10)

		setText(arg_8_0.batchText, var_8_2)
		onButton(arg_8_0, arg_8_0.batchUseBtn, function()
			if arg_8_1.count == 0:
				return

			if var_8_0.onUseBatch:
				var_8_0.onUseBatch(var_8_2)

			arg_8_0.Close(), SFX_PANEL)
		onButton(arg_8_0, arg_8_0.useOneBtn, function()
			if arg_8_1.count == 0:
				return

			if var_8_0.onUseOne:
				var_8_0.onUseOne()

			arg_8_0.Close(), SFX_PANEL)
		setActive(arg_8_0.batchUseBtn, var_8_2 > 1)
	elif var_8_1 == var_0_0.INFO:
		onButton(arg_8_0, arg_8_0.confirmBtn, function()
			arg_8_0.Close(), SFX_PANEL)
	elif var_8_1 == var_0_0.SEE:
		onButton(arg_8_0, arg_8_0.seeBtn, function()
			if arg_8_1.count == 0:
				return

			if var_8_0.onUse:
				var_8_0.onUse()

			arg_8_0.Close(), SFX_PANEL)

def var_0_0.Dispose(arg_14_0):
	pg.DelegateInfo.Dispose(arg_14_0)
	arg_14_0.Close()

return var_0_0

local var_0_0 = class("AttireFramePanel", import("...base.BaseSubView"))

def var_0_0.Card(arg_1_0):
	local var_1_0 = {}

	local function var_1_1(arg_2_0)
		arg_2_0._go = arg_1_0
		arg_2_0._tf = tf(arg_1_0)
		arg_2_0.mark = arg_2_0._tf.Find("info/mark")
		arg_2_0.print5 = arg_2_0._tf.Find("prints/line5")
		arg_2_0.print6 = arg_2_0._tf.Find("prints/line6")
		arg_2_0.emptyTF = arg_2_0._tf.Find("empty")
		arg_2_0.infoTF = arg_2_0._tf.Find("info")
		arg_2_0.tags = {
			arg_2_0._tf.Find("info/tags/e"),
			arg_2_0._tf.Find("info/tags/new")
		}
		arg_2_0.icon = arg_2_0._tf.Find("info/icon")
		arg_2_0.mask = arg_2_0._tf.Find("info/mask")

	function var_1_0.isEmpty(arg_3_0)
		return not arg_3_0.attireFrame or arg_3_0.attireFrame.id == -1

	local function var_1_2(arg_4_0, arg_4_1, arg_4_2)
		arg_4_0.state = arg_4_1.getState()

		_.each(arg_4_0.tags, function(arg_5_0)
			setActive(arg_5_0, False))
		setActive(arg_4_0.mask, arg_4_0.state == AttireFrame.STATE_LOCK)

		local var_4_0 = arg_4_2.getAttireByType(arg_4_1.getType())

		setActive(arg_4_0.tags[1], arg_4_0.state == AttireFrame.STATE_UNLOCK and var_4_0 == arg_4_1.id)
		setActive(arg_4_0.tags[2], arg_4_0.state == AttireFrame.STATE_UNLOCK and arg_4_1.isNew())

	function var_1_0.Update(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
		arg_6_0.UpdateSelected(False)

		arg_6_0.attireFrame = arg_6_1

		local var_6_0 = arg_6_0.isEmpty()

		if not var_6_0:
			var_1_2(arg_6_0, arg_6_1, arg_6_2)

		setActive(arg_6_0.infoTF, not var_6_0)
		setActive(arg_6_0.emptyTF, var_6_0)
		setActive(arg_6_0.print5, not arg_6_3)
		setActive(arg_6_0.print6, not arg_6_3)

	function var_1_0.LoadPrefab(arg_7_0, arg_7_1, arg_7_2)
		local var_7_0 = arg_7_1.getType()
		local var_7_1 = arg_7_1.getIcon()
		local var_7_2 = arg_7_1.getPrefabName()

		PoolMgr.GetInstance().GetPrefab(var_7_1, var_7_2, True, function(arg_8_0)
			if not arg_7_0.icon:
				local var_8_0

				if var_7_0 == AttireConst.TYPE_ICON_FRAME:
					var_8_0 = IconFrame.GetIcon(var_7_2)
				elif var_7_0 == AttireConst.TYPE_CHAT_FRAME:
					var_8_0 = ChatFrame.GetIcon(var_7_2)

				PoolMgr.GetInstance().ReturnPrefab(var_8_0, var_7_2, arg_8_0)
			else
				arg_8_0.name = var_7_2

				setParent(arg_8_0, arg_7_0.icon, False)

				local var_8_1

				var_8_1 = arg_7_1.getState() == AttireFrame.STATE_LOCK

				arg_7_2(arg_8_0))

	function var_1_0.ReturnIconFrame(arg_9_0, arg_9_1)
		eachChild(arg_9_0.icon, function(arg_10_0)
			local var_10_0 = arg_10_0.gameObject.name
			local var_10_1

			if arg_9_1 == AttireConst.TYPE_ICON_FRAME:
				var_10_1 = IconFrame.GetIcon(var_10_0)
			elif arg_9_1 == AttireConst.TYPE_CHAT_FRAME:
				var_10_1 = ChatFrame.GetIcon(var_10_0)

			assert(var_10_1)
			PoolMgr.GetInstance().ReturnPrefab(var_10_1, var_10_0, arg_10_0.gameObject))

	function var_1_0.UpdateSelected(arg_11_0, arg_11_1)
		setActive(arg_11_0.mark, arg_11_1)

	function var_1_0.Dispose(arg_12_0)
		return

	var_1_1(var_1_0)

	return var_1_0

def var_0_0.getUIName(arg_13_0):
	assert(False)

def var_0_0.GetData(arg_14_0):
	assert(False)

def var_0_0.OnInit(arg_15_0):
	arg_15_0.listPanel = arg_15_0.findTF("list_panel")
	arg_15_0.scolrect = arg_15_0.findTF("scrollrect", arg_15_0.listPanel).GetComponent("LScrollRect")

	function arg_15_0.scolrect.onInitItem(arg_16_0)
		arg_15_0.OnInitItem(arg_16_0)

	function arg_15_0.scolrect.onUpdateItem(arg_17_0, arg_17_1)
		arg_15_0.OnUpdateItem(arg_17_0, arg_17_1)

	arg_15_0.cards = {}

	local var_15_0 = arg_15_0.findTF("desc_panel")

	arg_15_0.descPanel = AttireDescPanel.New(var_15_0)
	arg_15_0.totalCount = arg_15_0.findTF("total_count/Text").GetComponent(typeof(Text))

def var_0_0.OnInitItem(arg_18_0, arg_18_1):
	assert(False)

def var_0_0.OnUpdateItem(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = arg_19_0.cards[arg_19_2]

	if not var_19_0:
		arg_19_0.OnInitItem(arg_19_2)

		var_19_0 = arg_19_0.cards[arg_19_2]

	local var_19_1 = arg_19_0.displayVOs[arg_19_1 + 1]
	local var_19_2 = arg_19_1 < arg_19_0.scolrect.content.GetComponent(typeof(GridLayoutGroup)).constraintCount

	var_19_0.Update(var_19_1, arg_19_0.playerVO, var_19_2)

def var_0_0.Update(arg_20_0, arg_20_1, arg_20_2):
	arg_20_0.playerVO = arg_20_2
	arg_20_0.rawAttireVOs = arg_20_1

	local var_20_0, var_20_1 = arg_20_0.GetDisplayVOs()

	arg_20_0.displayVOs = var_20_0

	arg_20_0.Filter()

	arg_20_0.totalCount.text = var_20_1

def var_0_0.GetDisplayVOs(arg_21_0):
	local var_21_0 = {}
	local var_21_1 = 0

	for iter_21_0, iter_21_1 in pairs(arg_21_0.GetData()):
		table.insert(var_21_0, iter_21_1)

		if iter_21_1.getState() == AttireFrame.STATE_UNLOCK and iter_21_1.id > 0:
			var_21_1 = var_21_1 + 1

	return var_21_0, var_21_1

def var_0_0.Filter(arg_22_0):
	if #arg_22_0.displayVOs == 0:
		return

	local var_22_0 = arg_22_0.playerVO.getAttireByType(arg_22_0.displayVOs[1].getType())

	table.sort(arg_22_0.displayVOs, function(arg_23_0, arg_23_1)
		local var_23_0 = var_22_0 == arg_23_0.id and 1 or 0
		local var_23_1 = var_22_0 == arg_23_1.id and 1 or 0

		if var_23_0 == 1:
			return True
		elif var_23_1 == 1:
			return False

		local var_23_2 = arg_23_0.getState()
		local var_23_3 = arg_23_1.getState()

		if var_23_2 == var_23_3:
			return arg_23_0.id < arg_23_1.id
		else
			return var_23_3 < var_23_2)

	local var_22_1 = arg_22_0.scolrect.content.GetComponent(typeof(GridLayoutGroup)).constraintCount
	local var_22_2 = var_22_1 - #arg_22_0.displayVOs % var_22_1

	if var_22_2 == var_22_1:
		var_22_2 = 0

	local var_22_3 = var_22_1 * arg_22_0.GetColumn()

	if var_22_3 > #arg_22_0.displayVOs:
		var_22_2 = var_22_3 - #arg_22_0.displayVOs

	for iter_22_0 = 1, var_22_2:
		table.insert(arg_22_0.displayVOs, {
			id = -1
		})

	arg_22_0.scolrect.SetTotalCount(#arg_22_0.displayVOs, 0)

def var_0_0.UpdateDesc(arg_24_0, arg_24_1):
	if arg_24_1.isEmpty():
		return

	if not arg_24_0.descPanel:
		arg_24_0.descPanel = AttireDescPanel.New(arg_24_0.descPanelTF)

	arg_24_0.descPanel.Update(arg_24_1.attireFrame, arg_24_0.playerVO)
	onButton(arg_24_0, arg_24_0.descPanel.applyBtn, function()
		local var_25_0 = arg_24_1.attireFrame.getType()

		arg_24_0.emit(AttireMediator.ON_APPLY, var_25_0, arg_24_1.attireFrame.id), SFX_PANEL)

def var_0_0.OnDestroy(arg_26_0):
	arg_26_0.descPanel.Dispose()

return var_0_0

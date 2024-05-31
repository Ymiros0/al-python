local var_0_0 = class("EquipmentTransformTreeScene", import("view.base.BaseUI"))
local var_0_1 = require("Mgr/Pool/PoolPlural")
local var_0_2 = "ui/EquipmentTransformTreeUI_atlas"

def var_0_0.getUIName(arg_1_0):
	return "EquipmentTransformTreeUI"

var_0_0.optionsPath = {
	"blur_panel/adapt/top/option"
}
var_0_0.MODE_NORMAL = 1
var_0_0.MODE_HIDESIDE = 2

def var_0_0.init(arg_2_0):
	arg_2_0.leftPanel = arg_2_0._tf.Find("Adapt/Left")
	arg_2_0.rightPanel = arg_2_0._tf.Find("Adapt/Right")
	arg_2_0.nationToggleGroup = arg_2_0.leftPanel.Find("Nations").Find("ViewPort/Content")

	setActive(arg_2_0.nationToggleGroup.GetChild(0), False)
	arg_2_0.nationToggleGroup.GetChild(0).Find("selectedCursor").gameObject.SetActive(False)

	arg_2_0.equipmentTypeToggleGroup = arg_2_0.leftPanel.Find("EquipmentTypes").Find("ViewPort/Content")

	setActive(arg_2_0.equipmentTypeToggleGroup.GetChild(0), False)
	arg_2_0.equipmentTypeToggleGroup.GetChild(0).Find("selectedframe").gameObject.SetActive(False)

	arg_2_0.TreeCanvas = arg_2_0.rightPanel.Find("ViewPort/Content")

	setActive(arg_2_0.rightPanel.Find("EquipNode"), False)
	setActive(arg_2_0.rightPanel.Find("Link"), False)

	arg_2_0.nodes = {}
	arg_2_0.links = {}
	arg_2_0.plurals = {
		EquipNode = var_0_1.New(arg_2_0.rightPanel.Find("EquipNode").gameObject, 5),
		Link = var_0_1.New(arg_2_0.rightPanel.Find("Link").gameObject, 8)
	}
	arg_2_0.pluralRoot = pg.PoolMgr.GetInstance().root
	arg_2_0.top = arg_2_0._tf.Find("blur_panel")
	arg_2_0.loader = AutoLoader.New()

def var_0_0.GetEnv(arg_3_0):
	arg_3_0.env = arg_3_0.env or {}

	return arg_3_0.env

def var_0_0.SetEnv(arg_4_0, arg_4_1):
	arg_4_0.env = arg_4_1

def var_0_0.didEnter(arg_5_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0.top)
	onButton(arg_5_0, arg_5_0.top.Find("adapt/top/back"), function()
		arg_5_0.closeView(), SFX_CANCEL)

	if arg_5_0.contextData.targetEquipId:
		local var_5_0
		local var_5_1
		local var_5_2 = False

		for iter_5_0, iter_5_1 in pairs(arg_5_0.env.nationsTree):
			for iter_5_2, iter_5_3 in pairs(iter_5_1):
				for iter_5_4, iter_5_5 in ipairs(iter_5_3.equipments):
					if iter_5_5[3] == arg_5_0.contextData.targetEquipId:
						var_5_0, var_5_1 = iter_5_0, iter_5_2
						var_5_2 = True

						break

			if var_5_2:
				break

		if var_5_2:
			arg_5_0.contextData.nation = var_5_0
			arg_5_0.contextData.equipmentTypeIndex = var_5_1

		arg_5_0.contextData.targetEquipId = None

	arg_5_0.InitPage()

	if arg_5_0.contextData.mode == var_0_0.MODE_HIDESIDE:
		setActive(arg_5_0.leftPanel, False)

		local var_5_3 = arg_5_0.rightPanel.sizeDelta

		var_5_3.x = 0
		arg_5_0.rightPanel.sizeDelta = var_5_3

		setAnchoredPosition(arg_5_0.rightPanel, {
			x = 0
		})

def var_0_0.GetSortKeys(arg_7_0):
	local var_7_0 = _.keys(arg_7_0)

	table.sort(var_7_0, function(arg_8_0, arg_8_1)
		return arg_8_0 < arg_8_1)

	return var_7_0

def var_0_0.GetSortTypes(arg_9_0):
	local var_9_0 = _.values(arg_9_0)

	table.sort(var_9_0, function(arg_10_0, arg_10_1)
		return arg_10_0.id < arg_10_1.id)

	return _.map(var_9_0, function(arg_11_0)
		return arg_11_0.category2)

def var_0_0.InitPage(arg_12_0):
	arg_12_0.firstInit = True

	local var_12_0 = arg_12_0.contextData
	local var_12_1 = arg_12_0.env

	var_12_0.mode = var_12_0.mode or var_0_0.MODE_NORMAL

	local var_12_2 = var_12_0.nation
	local var_12_3 = var_0_0.GetSortKeys(var_12_1.nationsTree)

	if not var_12_2 or not table.contains(var_12_3, var_12_2):
		var_12_2 = var_12_3[1]

	if next(var_12_1.nationsTree[var_12_2]) == None:
		for iter_12_0 = 2, #var_12_3:
			if next(var_12_1.nationsTree[var_12_3[iter_12_0]]) != None:
				var_12_2 = var_12_3[iter_12_0]

				break

	var_12_0.nation = None

	arg_12_0.UpdateNations()

	local var_12_4 = table.indexof(var_12_3, var_12_2) or 1

	triggerButton(arg_12_0.nationToggles[var_12_4])

	arg_12_0.firstInit = None

def var_0_0.UpdateNations(arg_13_0):
	local var_13_0 = var_0_0.GetSortKeys(arg_13_0.env.nationsTree)

	arg_13_0.nationToggles = CustomIndexLayer.Clone2Full(arg_13_0.nationToggleGroup, #var_13_0)

	for iter_13_0 = 1, #arg_13_0.nationToggles:
		local var_13_1 = arg_13_0.nationToggles[iter_13_0]
		local var_13_2 = var_13_0[iter_13_0]

		arg_13_0.loader.GetSprite(var_0_2, "nation" .. var_13_2 .. "_disable", var_13_1.Find("selectedIcon"))
		setActive(var_13_1.Find("selectedCursor"), False)
		onButton(arg_13_0, var_13_1, function()
			if arg_13_0.contextData.nation != var_13_2:
				if next(arg_13_0.env.nationsTree[var_13_2]) == None:
					pg.TipsMgr.GetInstance().ShowTips(i18n("word_comingSoon"))

					return

				arg_13_0.loader.GetSprite(var_0_2, "nation" .. var_13_2, var_13_1.Find("selectedIcon"))

				if arg_13_0.contextData.nation:
					local var_14_0 = table.indexof(var_13_0, arg_13_0.contextData.nation)

					setActive(arg_13_0.nationToggles[var_14_0].Find("selectedCursor"), False)
					arg_13_0.loader.GetSprite(var_0_2, "nation" .. arg_13_0.contextData.nation .. "_disable", arg_13_0.nationToggles[var_14_0].Find("selectedIcon"))

				arg_13_0.contextData.nation = var_13_2

				arg_13_0.UpdateEquipmentTypes()

				local var_14_1 = var_0_0.GetSortTypes(arg_13_0.env.nationsTree[var_13_2])
				local var_14_2 = var_14_1[1]

				if arg_13_0.firstInit:
					local var_14_3 = arg_13_0.contextData.equipmentTypeIndex

					if var_14_3 and table.contains(var_14_1, var_14_3):
						var_14_2 = var_14_3

				arg_13_0.contextData.equipmentTypeIndex = None

				local var_14_4 = table.indexof(var_14_1, var_14_2) or 1

				triggerToggle(arg_13_0.equipmentTypeToggles[var_14_4], True), SFX_UI_TAG)

def var_0_0.UpdateEquipmentTypes(arg_15_0):
	local var_15_0 = var_0_0.GetSortTypes(arg_15_0.env.nationsTree[arg_15_0.contextData.nation])

	arg_15_0.equipmentTypeToggles = CustomIndexLayer.Clone2Full(arg_15_0.equipmentTypeToggleGroup, #var_15_0)

	for iter_15_0 = 1, #arg_15_0.equipmentTypeToggles:
		local var_15_1 = arg_15_0.equipmentTypeToggles[iter_15_0]

		var_15_1.GetComponent(typeof(Toggle)).isOn = False

		local var_15_2 = var_15_0[iter_15_0]

		arg_15_0.loader.GetSprite(var_0_2, "equipmentType" .. var_15_2, var_15_1.Find("itemName"), True)
		setActive(var_15_1.Find("selectedframe"), False)
		onToggle(arg_15_0, var_15_1, function(arg_16_0)
			if arg_16_0 and arg_15_0.contextData.equipmentTypeIndex != var_15_2:
				arg_15_0.contextData.equipmentTypeIndex = var_15_2

				arg_15_0.ResetCanvas()

			setActive(var_15_1.Find("selectedframe"), arg_16_0), SFX_UI_TAG)

	arg_15_0.equipmentTypeToggleGroup.anchoredPosition = Vector2.zero
	arg_15_0.leftPanel.Find("EquipmentTypes").GetComponent(typeof(ScrollRect)).velocity = Vector2.zero

local var_0_3 = {
	15,
	-4,
	15,
	6
}

def var_0_0.ResetCanvas(arg_17_0):
	local var_17_0 = EquipmentProxy.EquipmentTransformTreeTemplate[arg_17_0.contextData.nation][arg_17_0.contextData.equipmentTypeIndex]

	assert(var_17_0, "can't find Equip_upgrade_template Nation. " .. arg_17_0.contextData.nation .. " Type. " .. arg_17_0.contextData.equipmentTypeIndex)

	arg_17_0.TreeCanvas.sizeDelta = Vector2(unpack(var_17_0.canvasSize))
	arg_17_0.TreeCanvas.anchoredPosition = Vector2.zero
	arg_17_0.rightPanel.GetComponent(typeof(ScrollRect)).velocity = Vector2.zero

	arg_17_0.ReturnCanvasItems()

	for iter_17_0, iter_17_1 in ipairs(var_17_0.equipments):
		local var_17_1 = arg_17_0.plurals.EquipNode.Dequeue()

		setActive(var_17_1, True)
		setParent(var_17_1, arg_17_0.TreeCanvas)
		table.insert(arg_17_0.nodes, {
			id = iter_17_1[3],
			cfg = iter_17_1,
			go = var_17_1
		})

		var_17_1.name = iter_17_1[3]

		arg_17_0.UpdateItemNode(tf(var_17_1), iter_17_1)

	for iter_17_2, iter_17_3 in ipairs(var_17_0.links):
		for iter_17_4 = 1, #iter_17_3 - 1:
			local var_17_2 = iter_17_3[iter_17_4]
			local var_17_3 = iter_17_3[iter_17_4 + 1]
			local var_17_4 = {
				var_17_3[1] - var_17_2[1],
				var_17_2[2] - var_17_3[2]
			}
			local var_17_5 = math.abs(var_17_4[1]) > math.abs(var_17_4[2])
			local var_17_6 = var_17_5 and math.abs(var_17_4[1]) or math.abs(var_17_4[2])

			if var_17_5:
				var_17_4[2] = 0
			else
				var_17_4[1] = 0

			local var_17_7 = 1 - math.sign(var_17_4[1])

			var_17_7 = var_17_7 != 1 and var_17_7 or 2 - math.sign(var_17_4[2])

			local var_17_8 = math.deg2Rad * 90 * var_17_7

			if #iter_17_3 == 2:
				local var_17_9 = arg_17_0.plurals.Link.Dequeue()

				table.insert(arg_17_0.links, go(var_17_9))
				setActive(var_17_9, True)
				setParent(var_17_9, arg_17_0.TreeCanvas)
				arg_17_0.loader.GetSprite(var_0_2, var_17_4[2] == 0 and "wirehead" or "wireline", var_17_9)

				tf(var_17_9).sizeDelta = Vector2(28, 26)
				tf(var_17_9).pivot = Vector2(0.5, 0.5)
				tf(var_17_9).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)

				local var_17_10 = Vector2(math.cos(var_17_8), math.sin(var_17_8)) * var_0_3[(var_17_7 - 1) % 4 + 1]

				tf(var_17_9).anchoredPosition = Vector2(var_17_2[1] + var_17_10.x, -var_17_2[2] + var_17_10.y)

				local var_17_11 = arg_17_0.plurals.Link.Dequeue()

				table.insert(arg_17_0.links, go(var_17_11))
				setActive(var_17_11, True)
				setParent(var_17_11, arg_17_0.TreeCanvas)
				arg_17_0.loader.GetSprite(var_0_2, "wiretail", var_17_11)

				tf(var_17_11).sizeDelta = Vector2(28, 26)
				tf(var_17_11).pivot = Vector2(0.5, 0.5)
				tf(var_17_11).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)

				local var_17_12 = Vector2(math.cos(var_17_8), math.sin(var_17_8)) * -var_0_3[(var_17_7 + 1) % 4 + 1]

				tf(var_17_11).anchoredPosition = Vector2(var_17_3[1] + var_17_12.x, -var_17_3[2] + var_17_12.y)

				local var_17_13 = arg_17_0.plurals.Link.Dequeue()

				table.insert(arg_17_0.links, go(var_17_13))
				setActive(var_17_13, True)
				setParent(var_17_13, arg_17_0.TreeCanvas)
				arg_17_0.loader.GetSprite(var_0_2, "wireline", var_17_13)

				tf(var_17_13).sizeDelta = Vector2(math.max(0, var_17_6 - var_0_3[(var_17_7 - 1) % 4 + 1] - var_0_3[(var_17_7 + 1) % 4 + 1] - 28), 16)
				tf(var_17_13).pivot = Vector2(0, 0.5)
				tf(var_17_13).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)

				local var_17_14 = Vector2(math.cos(var_17_8), math.sin(var_17_8)) * 14

				tf(var_17_13).anchoredPosition = Vector2(var_17_2[1] + var_17_10.x, -var_17_2[2] + var_17_10.y) + var_17_14

				break

			local var_17_15 = arg_17_0.plurals.Link.Dequeue()

			table.insert(arg_17_0.links, go(var_17_15))
			setActive(var_17_15, True)
			setParent(var_17_15, arg_17_0.TreeCanvas)

			local var_17_16 = 1

			if iter_17_4 == 1:
				arg_17_0.loader.GetSprite(var_0_2, var_17_4[2] == 0 and "wirehead" or "wireline", var_17_15)

				local var_17_17 = var_17_6 + 14 + var_17_16 - var_0_3[(var_17_7 - 1) % 4 + 1]

				tf(var_17_15).sizeDelta = Vector2(var_17_17, 26)
				tf(var_17_15).pivot = Vector2((var_17_17 - var_17_16) / var_17_17, 0.5)
				tf(var_17_15).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)
				tf(var_17_15).anchoredPosition = Vector2(var_17_3[1], -var_17_3[2])
			elif iter_17_4 + 1 == #iter_17_3:
				arg_17_0.loader.GetSprite(var_0_2, "wiretail", var_17_15)

				tf(var_17_15).sizeDelta = Vector2(var_17_6 + 14 + var_17_16 - var_0_3[(var_17_7 + 1) % 4 + 1], 26)
				tf(var_17_15).pivot = Vector2(var_17_16 / (var_17_6 + 14 + var_17_16 - var_0_3[(var_17_7 + 1) % 4 + 1]), 0.5)
				tf(var_17_15).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)
				tf(var_17_15).anchoredPosition = Vector2(var_17_2[1], -var_17_2[2])
			else
				arg_17_0.loader.GetSprite(var_0_2, "wireline", var_17_15)

				tf(var_17_15).sizeDelta = Vector2(var_17_6 + var_17_16 * 2, 16)
				tf(var_17_15).pivot = Vector2(var_17_16 / (var_17_6 + var_17_16 * 2), 0.5)
				tf(var_17_15).localRotation = Quaternion.Euler(0, 0, var_17_7 * 90)
				tf(var_17_15).anchoredPosition = Vector2(var_17_2[1], -var_17_2[2])

def var_0_0.UpdateItemNode(arg_18_0, arg_18_1, arg_18_2):
	arg_18_1 = tf(arg_18_1)
	arg_18_1.anchoredPosition = Vector2(arg_18_2[1], -arg_18_2[2])

	updateDrop(arg_18_1.Find("Item"), {
		id = arg_18_2[3],
		type = DROP_TYPE_EQUIP
	})
	onButton(arg_18_0, arg_18_1.Find("Item"), function()
		local var_19_0 = EquipmentProxy.GetTransformSources(arg_18_2[3])[1]

		if not var_19_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_initial_node"))

			return

		arg_18_0.emit(EquipmentTransformTreeMediator.OPEN_LAYER, Context.New({
			mediator = EquipmentTransformMediator,
			viewComponent = EquipmentTransformLayer,
			data = {
				formulaId = var_19_0
			}
		})), SFX_PANEL)
	arg_18_1.Find("Mask/NameText").GetComponent("ScrollText").SetText(Equipment.getConfigData(arg_18_2[3]).name)

	local var_18_0 = arg_18_0.env.tracebackHelper.GetSortedEquipTraceBack(arg_18_2[3])
	local var_18_1 = _.any(var_18_0, function(arg_20_0)
		local var_20_0 = arg_20_0.candicates

		return var_20_0 and #var_20_0 > 0 and EquipmentTransformUtil.CheckTransformFormulasSucceed(arg_20_0.formulas, var_20_0[#var_20_0]))

	setActive(arg_18_1.Find("cratfable"), var_18_1)
	onButton(arg_18_0, arg_18_1.Find("cratfable"), function()
		arg_18_0.emit(EquipmentTransformTreeMediator.OPEN_LAYER, Context.New({
			mediator = EquipmentTraceBackMediator,
			viewComponent = EquipmentTraceBackLayer,
			data = {
				TargetEquipmentId = arg_18_2[3]
			}
		})))

	local var_18_2 = arg_18_2[4] and PlayerPrefs.GetInt("ShowTransformTip_" .. arg_18_2[3], 0) == 0

	setActive(arg_18_1.Find("Item/new"), var_18_2)

def var_0_0.UpdateItemNodes(arg_22_0):
	for iter_22_0, iter_22_1 in ipairs(arg_22_0.nodes):
		arg_22_0.UpdateItemNode(iter_22_1.go, iter_22_1.cfg)

def var_0_0.UpdateItemNodeByID(arg_23_0, arg_23_1):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.nodes):
		if arg_23_1 == iter_23_1.id:
			arg_23_0.UpdateItemNode(iter_23_1.go, iter_23_1.cfg)

			break

def var_0_0.ReturnCanvasItems(arg_24_0, arg_24_1):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.nodes):
		if not arg_24_0.plurals.EquipNode.Enqueue(iter_24_1.go, arg_24_1):
			setParent(iter_24_1.go, arg_24_0.pluralRoot)

	table.clean(arg_24_0.nodes)

	for iter_24_2, iter_24_3 in ipairs(arg_24_0.links):
		if not arg_24_0.plurals.Link.Enqueue(iter_24_3, arg_24_1):
			setParent(iter_24_3, arg_24_0.pluralRoot)

	table.clean(arg_24_0.links)

def var_0_0.willExit(arg_25_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_25_0.top, arg_25_0._tf)
	arg_25_0.ReturnCanvasItems(True)

	for iter_25_0, iter_25_1 in pairs(arg_25_0.plurals):
		iter_25_1.Clear()

	arg_25_0.loader.Clear()

return var_0_0

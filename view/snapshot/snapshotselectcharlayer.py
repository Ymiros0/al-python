local var_0_0 = class("SnapshotSelectCharLayer", import("..base.BaseUI"))

var_0_0.ON_INDEX = "SnapshotSelectCharLayer.ON_INDEX"
var_0_0.SELECT_CHAR = "SnapshotSelectCharLayer.SELECT_CHAR"
var_0_0.TOGGLE_UNDEFINED = -1
var_0_0.TOGGLE_CHAR = 0
var_0_0.TOGGLE_LINK = 1
var_0_0.TOGGLE_BLUEPRINT = 2
var_0_0.ShipIndex = {
	typeIndex = ShipIndexConst.TypeAll,
	campIndex = ShipIndexConst.CampAll,
	rarityIndex = ShipIndexConst.RarityAll
}
var_0_0.ShipIndexData = {
	customPanels = {
		typeIndex = {
			blueSeleted = True,
			mode = CustomIndexLayer.Mode.AND,
			options = ShipIndexConst.TypeIndexs,
			names = ShipIndexConst.TypeNames
		},
		campIndex = {
			blueSeleted = True,
			mode = CustomIndexLayer.Mode.AND,
			options = ShipIndexConst.CampIndexs,
			names = ShipIndexConst.CampNames
		},
		rarityIndex = {
			blueSeleted = True,
			mode = CustomIndexLayer.Mode.AND,
			options = ShipIndexConst.RarityIndexs,
			names = ShipIndexConst.RarityNames
		}
	},
	groupList = {
		{
			dropdown = False,
			titleTxt = "indexsort_index",
			titleENTxt = "indexsort_indexeng",
			tags = {
				"typeIndex"
			}
		},
		{
			dropdown = False,
			titleTxt = "indexsort_camp",
			titleENTxt = "indexsort_campeng",
			tags = {
				"campIndex"
			}
		},
		{
			dropdown = False,
			titleTxt = "indexsort_rarity",
			titleENTxt = "indexsort_rarityeng",
			tags = {
				"rarityIndex"
			}
		}
	}
}

def var_0_0.setShipGroups(arg_1_0, arg_1_1):
	arg_1_0.shipGroups = arg_1_1

def var_0_0.setProposeList(arg_2_0, arg_2_1):
	arg_2_0.proposeList = arg_2_1

def var_0_0.getUIName(arg_3_0):
	return "snapshotselectchar"

def var_0_0.back(arg_4_0):
	if arg_4_0.exited:
		return

	arg_4_0.emit(var_0_0.ON_CLOSE)

	arg_4_0.scrollValue = 0

def var_0_0.init(arg_5_0):
	arg_5_0.toggleType = var_0_0.TOGGLE_UNDEFINED
	arg_5_0.topTF = arg_5_0.findTF("blur_panel/adapt/top")
	arg_5_0.backBtn = arg_5_0.findTF("back_btn", arg_5_0.topTF)
	arg_5_0.indexBtn = arg_5_0.findTF("index_button", arg_5_0.topTF)
	arg_5_0.toggleChar = arg_5_0.findTF("list_card/types/char")
	arg_5_0.toggleLink = arg_5_0.findTF("list_card/types/link")
	arg_5_0.toggleBlueprint = arg_5_0.findTF("list_card/types/blueprint")
	arg_5_0.cardItems = {}
	arg_5_0.cardList = arg_5_0.findTF("list_card/scroll").GetComponent("LScrollRect")

	function arg_5_0.cardList.onInitItem(arg_6_0)
		arg_5_0.onInitCard(arg_6_0)

	function arg_5_0.cardList.onUpdateItem(arg_7_0, arg_7_1)
		arg_5_0.onUpdateCard(arg_7_0, arg_7_1)

	function arg_5_0.cardList.onReturnItem(arg_8_0, arg_8_1)
		arg_5_0.onReturnCard(arg_8_0, arg_8_1)

	arg_5_0.initSelectSkinPanel()
	cameraPaintViewAdjust(False)
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf)

def var_0_0.didEnter(arg_9_0):
	onButton(arg_9_0, arg_9_0.backBtn, function()
		arg_9_0.back())
	onToggle(arg_9_0, arg_9_0.toggleChar, function()
		if arg_9_0.toggleType == var_0_0.TOGGLE_CHAR:
			return

		arg_9_0.toggleType = var_0_0.TOGGLE_CHAR

		arg_9_0.updateCardList())
	onToggle(arg_9_0, arg_9_0.toggleLink, function()
		if arg_9_0.toggleType == var_0_0.TOGGLE_LINK:
			return

		arg_9_0.toggleType = var_0_0.TOGGLE_LINK

		arg_9_0.updateCardList())
	onToggle(arg_9_0, arg_9_0.toggleBlueprint, function()
		if arg_9_0.toggleType == var_0_0.TOGGLE_BLUEPRINT:
			return

		arg_9_0.toggleType = var_0_0.TOGGLE_BLUEPRINT

		arg_9_0.updateCardList())
	onButton(arg_9_0, arg_9_0.indexBtn, function()
		local var_14_0 = Clone(var_0_0.ShipIndexData)

		if arg_9_0.toggleType == var_0_0.TOGGLE_LINK:
			var_14_0.customPanels.campIndex = None
			var_14_0.groupList[2] = None

		var_14_0.indexDatas = Clone(var_0_0.ShipIndex)

		function var_14_0.callback(arg_15_0)
			var_0_0.ShipIndex.typeIndex = arg_15_0.typeIndex

			if arg_15_0.campIndex:
				var_0_0.ShipIndex.campIndex = arg_15_0.campIndex

			var_0_0.ShipIndex.rarityIndex = arg_15_0.rarityIndex

			arg_9_0.updateCardList()

		arg_9_0.emit(var_0_0.ON_INDEX, var_14_0))
	triggerToggle(arg_9_0.toggleChar, True)

def var_0_0.willExit(arg_16_0):
	cameraPaintViewAdjust(True)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_16_0._tf)

local function var_0_1(arg_17_0, arg_17_1, arg_17_2)
	if arg_17_0 == var_0_0.TOGGLE_CHAR and not arg_17_1:
		return arg_17_2
	elif arg_17_0 == var_0_0.TOGGLE_LINK and arg_17_1:
		return arg_17_2 - 10000
	elif arg_17_0 == var_0_0.TOGGLE_BLUEPRINT:
		return arg_17_2 - 20000

	return -1

def var_0_0.updateCardList(arg_18_0):
	local var_18_0 = {}
	local var_18_1 = _.filter(pg.ship_data_group.all, function(arg_19_0)
		return pg.ship_data_group[arg_19_0].handbook_type == arg_18_0.toggleType)

	if var_0_0.ShipIndex.typeIndex == ShipIndexConst.TypeAll and var_0_0.ShipIndex.rarityIndex == ShipIndexConst.RarityAll and var_0_0.ShipIndex.campIndex == ShipIndexConst.CampAll and arg_18_0.toggleType == var_0_0.TOGGLE_CHAR:
		for iter_18_0, iter_18_1 in ipairs(var_18_1):
			local var_18_2 = pg.ship_data_group[iter_18_1]
			local var_18_3
			local var_18_4 = False

			if var_18_2:
				var_18_3 = arg_18_0.shipGroups[var_18_2.group_type]
				var_18_4 = Nation.IsLinkType(ShipGroup.getDefaultShipConfig(var_18_2.group_type).nationality)

			local var_18_5 = var_0_1(arg_18_0.toggleType, var_18_4, iter_18_1)

			if var_18_5 != -1:
				var_18_0[iter_18_0] = {
					showTrans = False,
					code = var_18_5,
					group = var_18_3
				}
	else
		for iter_18_2, iter_18_3 in ipairs(var_18_1):
			local var_18_6 = pg.ship_data_group[iter_18_3]

			if var_18_6:
				local var_18_7 = ShipGroup.New({
					id = var_18_6.group_type
				})
				local var_18_8 = arg_18_0.shipGroups[var_18_6.group_type]

				if var_18_7 and ShipIndexConst.filterByType(var_18_7, var_0_0.ShipIndex.typeIndex) and ShipIndexConst.filterByRarity(var_18_7, var_0_0.ShipIndex.rarityIndex):
					local var_18_9 = Nation.IsLinkType(var_18_7.getNation())

					if arg_18_0.toggleType == var_0_0.TOGGLE_CHAR and not var_18_9 and ShipIndexConst.filterByCamp(var_18_7, var_0_0.ShipIndex.campIndex):
						var_18_0[#var_18_0 + 1] = {
							showTrans = False,
							code = var_0_1(arg_18_0.toggleType, var_18_9, iter_18_3),
							group = var_18_8
						}
					elif arg_18_0.toggleType == var_0_0.TOGGLE_LINK and var_18_9:
						var_18_0[#var_18_0 + 1] = {
							showTrans = False,
							code = var_0_1(arg_18_0.toggleType, var_18_9, iter_18_3),
							group = var_18_8
						}
					elif arg_18_0.toggleType == var_0_0.TOGGLE_BLUEPRINT and ShipIndexConst.filterByCamp(var_18_7, var_0_0.ShipIndex.campIndex):
						var_18_0[#var_18_0 + 1] = {
							showTrans = False,
							code = var_0_1(arg_18_0.toggleType, var_18_9, iter_18_3),
							group = var_18_8
						}

	arg_18_0.cardInfos = var_18_0

	arg_18_0.cardList.SetTotalCount(#arg_18_0.cardInfos, -1)
	arg_18_0.cardList.ScrollTo(arg_18_0.scrollValue or 0)

local function var_0_2(arg_20_0)
	return getProxy(ShipSkinProxy).GetAllSkinForARCamera(arg_20_0)

local function var_0_3(arg_21_0)
	local var_21_0 = {}
	local var_21_1 = getProxy(ShipSkinProxy).getSkinList()
	local var_21_2 = getProxy(CollectionProxy).getShipGroup(arg_21_0)

	if var_21_2:
		local var_21_3 = ShipGroup.getSkinList(arg_21_0)

		for iter_21_0, iter_21_1 in ipairs(var_21_3):
			if iter_21_1.skin_type == ShipSkin.SKIN_TYPE_DEFAULT or table.contains(var_21_1, iter_21_1.id) or iter_21_1.skin_type == ShipSkin.SKIN_TYPE_REMAKE and var_21_2.trans or iter_21_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE and var_21_2.married == 1:
				var_21_0[iter_21_1.id] = True

	return var_21_0

def var_0_0.onInitCard(arg_22_0, arg_22_1):
	local var_22_0 = SnapshotShipCard.New(arg_22_1)

	onButton(arg_22_0, var_22_0.go, function()
		if var_22_0.shipGroup:
			if HXSet.isHxSkin():
				local var_23_0 = ShipGroup.getDefaultSkin(var_22_0.shipGroup.id)

				arg_22_0.emit(var_0_0.SELECT_CHAR, var_23_0.id)
				arg_22_0.back()

				return

			local var_23_1 = var_0_2(var_22_0.shipGroup.id)

			if #var_23_1 > 1:
				local var_23_2 = var_0_3(var_22_0.shipGroup.id)

				arg_22_0.openSelectSkinPanel(var_23_1, var_23_2)
			elif #var_23_1 == 1:
				arg_22_0.emit(var_0_0.SELECT_CHAR, var_23_1[1].id)
				arg_22_0.back())

	arg_22_0.cardItems[arg_22_1] = var_22_0

def var_0_0.onUpdateCard(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = arg_24_0.cardItems[arg_24_2]

	if not var_24_0:
		arg_24_0.onInitCard(arg_24_2)

		var_24_0 = arg_24_0.cardItems[arg_24_2]

	local var_24_1 = arg_24_1 + 1
	local var_24_2 = arg_24_0.cardInfos[var_24_1]

	if not var_24_2:
		return

	local var_24_3

	if var_24_2.group:
		var_24_3 = arg_24_0.proposeList[var_24_2.group.id]

	var_24_0.update(var_24_2.code, var_24_2.group, var_24_2.showTrans, var_24_3)

def var_0_0.onReturnCard(arg_25_0, arg_25_1, arg_25_2):
	if arg_25_0.exited:
		return

	local var_25_0 = arg_25_0.cardItems[arg_25_2]

	if var_25_0:
		var_25_0.clear()

	arg_25_0.cardItems[arg_25_2] = None

def var_0_0.initSelectSkinPanel(arg_26_0):
	arg_26_0.skinPanel = arg_26_0.findTF("selectSkinPnl")

	local var_26_0 = arg_26_0.findTF("select_skin/btnBack", arg_26_0.skinPanel)

	onButton(arg_26_0, var_26_0, function()
		arg_26_0.closeSelectSkinPanel())

	arg_26_0.skinScroll = arg_26_0.findTF("select_skin/style_scroll", arg_26_0.skinPanel)
	arg_26_0.skinContainer = arg_26_0.findTF("view_port", arg_26_0.skinScroll)
	arg_26_0.skinCard = arg_26_0._tf.GetComponent(typeof(ItemList)).prefabItem[0]

	setActive(arg_26_0.skinCard, False)
	setActive(arg_26_0.skinPanel, False)

	arg_26_0.skinCardMap = {}

def var_0_0.openSelectSkinPanel(arg_28_0, arg_28_1, arg_28_2):
	setActive(arg_28_0.skinPanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_28_0.skinPanel, False)

	for iter_28_0 = arg_28_0.skinContainer.childCount, #arg_28_1 - 1:
		cloneTplTo(arg_28_0.skinCard, arg_28_0.skinContainer)

	for iter_28_1 = #arg_28_1, arg_28_0.skinContainer.childCount - 1:
		setActive(arg_28_0.skinContainer.GetChild(iter_28_1), False)

	local var_28_0 = arg_28_0.skinContainer.childCount

	for iter_28_2, iter_28_3 in ipairs(arg_28_1):
		local var_28_1 = arg_28_0.skinContainer.GetChild(iter_28_2 - 1)
		local var_28_2 = arg_28_0.skinCardMap[var_28_1]

		if not var_28_2:
			var_28_2 = ShipSkinCard.New(var_28_1.gameObject)
			arg_28_0.skinCardMap[var_28_1] = var_28_2

		local var_28_3 = arg_28_2[iter_28_3.id]

		var_28_2.updateSkin(iter_28_3, var_28_3)
		var_28_2.updateUsing(False)
		removeOnButton(var_28_1)
		onButton(arg_28_0, var_28_1, function()
			if var_28_3:
				arg_28_0.emit(var_0_0.SELECT_CHAR, iter_28_3.id)
				arg_28_0.closeSelectSkinPanel()
				arg_28_0.back())
		setActive(var_28_1, True)

def var_0_0.closeSelectSkinPanel(arg_30_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_30_0.skinPanel, arg_30_0._tf)
	setActive(arg_30_0.skinPanel, False)

return var_0_0

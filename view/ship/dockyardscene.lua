local var_0_0 = class("DockyardScene", import("..base.BaseUI"))
local var_0_1 = 2
local var_0_2 = 0.2
local var_0_3 = 1

var_0_0.MODE_OVERVIEW = "overview"
var_0_0.MODE_DESTROY = "destroy"
var_0_0.MODE_SELECT = "select"
var_0_0.MODE_MOD = "modify"
var_0_0.MODE_WORLD = "world"
var_0_0.MODE_REMOULD = "remould"
var_0_0.MODE_UPGRADE = "upgrade"
var_0_0.MODE_GUILD_BOSS = "guildboss"
var_0_0.TITLE_CN_OVERVIEW = i18n("word_dockyard")
var_0_0.TITLE_CN_UPGRADE = i18n("word_dockyardUpgrade")
var_0_0.TITLE_CN_DESTROY = i18n("word_dockyardDestroy")
var_0_0.TITLE_EN_OVERVIEW = "dockyard"
var_0_0.TITLE_EN_UPGRADE = "modernization"
var_0_0.TITLE_EN_DESTROY = "retirement"
var_0_0.PRIOR_MODE_EQUIP_UP = 1
var_0_0.PRIOR_MODE_SHIP_UP = 2

function var_0_0.getUIName(arg_1_0)
	return "DockyardUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0._tf:SetAsLastSibling()

	local var_2_0 = arg_2_0.contextData

	var_2_0.mode = defaultValue(var_2_0.mode, var_0_0.MODE_SELECT)
	var_2_0.otherSelectedIds = defaultValue(var_2_0.otherSelectedIds, {})
	arg_2_0.teamTypeFilter = var_2_0.teamFilter
	arg_2_0.selectedMin = var_2_0.selectedMin or 1
	arg_2_0.leastLimitMsg = var_2_0.leastLimitMsg
	arg_2_0.selectedMax = var_2_0.selectedMax or 0
	var_2_0.selectedIds = var_2_0.selectedIds or {}

	if var_2_0.infoShipId then
		table.insert(var_2_0.selectedIds, var_2_0.infoShipId)

		var_2_0.infoShipId = nil
	end

	arg_2_0.selectedIds = underscore(var_2_0.selectedIds):chain():select(function(arg_3_0)
		return getProxy(BayProxy):RawGetShipById(arg_3_0) ~= nil
	end):first(arg_2_0.selectedMax):value()
	var_2_0.selectedIds = nil
	arg_2_0.checkShip = var_2_0.onShip or function(arg_4_0, arg_4_1, arg_4_2)
		return true
	end
	arg_2_0.onCancelShip = var_2_0.onCancelShip or function(arg_5_0, arg_5_1, arg_5_2)
		return true
	end
	arg_2_0.onClick = var_2_0.onClick or function(arg_6_0, arg_6_1, arg_6_2)
		arg_2_0:emit(DockyardMediator.ON_SHIP_DETAIL, arg_6_0, arg_6_1, arg_6_2)
	end
	arg_2_0.confirmSelect = var_2_0.confirmSelect
	arg_2_0.callbackQuit = var_2_0.callbackQuit
	arg_2_0.onSelected = var_2_0.onSelected or function(arg_7_0, arg_7_1)
		warning("not implemented.")
	end
	arg_2_0.blurPanel = arg_2_0:findTF("blur_panel")
	arg_2_0.settingBtn = arg_2_0.blurPanel:Find("adapt/left_length/frame/setting")
	arg_2_0.settingPanel = DockyardQuickSelectSettingPage.New(arg_2_0._tf, arg_2_0.event)

	arg_2_0.settingPanel:OnSettingChanged(function()
		arg_2_0:unselecteAllShips()
	end)

	arg_2_0.topPanel = arg_2_0.blurPanel:Find("adapt/top")
	arg_2_0.sortBtn = arg_2_0.topPanel:Find("sort_button")
	arg_2_0.sortImgAsc = arg_2_0.sortBtn:Find("asc")
	arg_2_0.sortImgDesc = arg_2_0.sortBtn:Find("desc")
	arg_2_0.leftTipsText = arg_2_0.topPanel:Find("capacity")

	onButton(arg_2_0, arg_2_0.leftTipsText:Find("switch"), function()
		arg_2_0.isCapacityMeta = not arg_2_0.isCapacityMeta

		arg_2_0:updateCapacityDisplay()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.leftTipsText:Find("plus"), function()
		gotoChargeScene()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.leftTipsText:Find("tip"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			hideNo = true,
			content = i18n("specialshipyard_tip")
		})
	end, SFX_PANEL)
	setActive(arg_2_0.leftTipsText, false)

	arg_2_0.indexBtn = arg_2_0.topPanel:Find("index_button")
	arg_2_0.switchPanel = arg_2_0.topPanel:Find("switch")

	triggerToggle(arg_2_0.switchPanel:Find("Image"), true)

	arg_2_0.preferenceBtn = arg_2_0.switchPanel:Find("toggles/preference_toggle")
	arg_2_0.attrBtn = arg_2_0.switchPanel:Find("toggles/attr_toggle")
	arg_2_0.nameSearchInput = arg_2_0.switchPanel:Find("search")

	setText(arg_2_0.nameSearchInput:Find("holder"), i18n("dockyard_search_holder"))
	setInputText(arg_2_0.nameSearchInput, "")
	onInputChanged(arg_2_0, arg_2_0.nameSearchInput, function()
		arg_2_0:filter()
	end)

	arg_2_0.modLockFilter = arg_2_0:findTF("mod_flter_lock", arg_2_0.topPanel)
	arg_2_0.modLeveFilter = arg_2_0:findTF("mod_flter_level", arg_2_0.topPanel)
	arg_2_0.energyDescTF = arg_2_0:findTF("energy_desc")
	arg_2_0.energyDescTextTF = arg_2_0.energyDescTF:Find("Text")
	arg_2_0.selectPanel = arg_2_0.blurPanel:Find("select_panel")
	arg_2_0.bottomTipsText = arg_2_0.selectPanel:Find("tip")
	arg_2_0.bottomTipsWithFrame = arg_2_0.selectPanel:Find("tipwithframe")

	setText(arg_2_0.selectPanel:Find("bottom_info/bg_input/selected"), i18n("disassemble_selected") .. ":")

	arg_2_0.awardTF = arg_2_0.selectPanel:Find("bottom_info/bg_award")

	setText(arg_2_0.awardTF:Find("label"), i18n("disassemble_available") .. ":")

	arg_2_0.modAttrsTF = arg_2_0.selectPanel:Find("bottom_info/bg_mod")
	arg_2_0.viewEquipmentBtn = arg_2_0.selectPanel:Find("view_equipments")
	arg_2_0.tipPanel = arg_2_0.blurPanel:Find("TipPanel")

	setActive(arg_2_0.tipPanel, false)

	arg_2_0.worldPanel = arg_2_0.blurPanel:Find("world_port_panel")

	setActive(arg_2_0.worldPanel, arg_2_0.contextData.mode == var_0_0.MODE_WORLD)

	arg_2_0.assultBtn = arg_2_0.blurPanel:Find("adapt/top/assult_btn")
	arg_2_0.stampBtn = arg_2_0.topPanel:Find("stamp")
	arg_2_0.isRemouldOrUpgradeMode = arg_2_0.contextData.mode == var_0_0.MODE_REMOULD or arg_2_0.contextData.mode == var_0_0.MODE_UPGRADE

	setActive(arg_2_0.switchPanel, not arg_2_0.isRemouldOrUpgradeMode)
	setActive(arg_2_0.indexBtn, not arg_2_0.isRemouldOrUpgradeMode)
	setActive(arg_2_0.sortBtn, not arg_2_0.isRemouldOrUpgradeMode)
	setActive(arg_2_0.modLeveFilter, arg_2_0.isRemouldOrUpgradeMode)
	setActive(arg_2_0.modLockFilter, arg_2_0.isRemouldOrUpgradeMode)
	setActive(arg_2_0.assultBtn, arg_2_0.contextData.mode == var_0_0.MODE_GUILD_BOSS)
	switch(arg_2_0.contextData.mode, {
		[var_0_0.MODE_OVERVIEW] = function()
			arg_2_0.selecteEnabled = false
		end,
		[var_0_0.MODE_DESTROY] = function()
			arg_2_0.selecteEnabled = true
			arg_2_0.blacklist = {}
			arg_2_0.destroyResList = UIItemList.New(arg_2_0.awardTF:Find("res_list"), arg_2_0.awardTF:Find("res_list/res"))
		end,
		[var_0_0.MODE_MOD] = function()
			arg_2_0.selecteEnabled = true

			setText(arg_2_0.modAttrsTF:Find("title/Text"), i18n("word_mod_value"))

			arg_2_0.modAttrContainer = arg_2_0.modAttrsTF:Find("attrs")
		end
	}, function()
		arg_2_0.selecteEnabled = true
	end)
	setActive(arg_2_0.selectPanel, arg_2_0.selecteEnabled and arg_2_0.contextData.mode ~= var_0_0.MODE_WORLD)
	setActive(arg_2_0.worldPanel, arg_2_0.contextData.mode == var_0_0.MODE_WORLD)

	local var_2_1 = arg_2_0.contextData.mode == var_0_0.MODE_DESTROY

	setActive(arg_2_0.settingBtn, var_2_1)
	setActive(arg_2_0.selectPanel:Find("quick_select"), var_2_1)

	if arg_2_0.contextData.priorEquipUpShipIDList and arg_2_0.contextData.priorMode then
		setActive(arg_2_0.tipPanel, true)

		local var_2_2 = arg_2_0:findTF("EquipUP", arg_2_0.tipPanel)
		local var_2_3 = arg_2_0:findTF("ShipUP", arg_2_0.tipPanel)

		setText(var_2_2, i18n("fightfail_choiceequip"))
		setText(var_2_3, i18n("fightfail_choicestrengthen"))
		setActive(var_2_2, arg_2_0.contextData.priorMode == var_0_0.PRIOR_MODE_EQUIP_UP)
		setActive(var_2_3, arg_2_0.contextData.priorMode == var_0_0.PRIOR_MODE_SHIP_UP)
	end

	if arg_2_0.contextData.selectFriend then
		arg_2_0.shipContainer = arg_2_0:findTF("main/friend_container/ships"):GetComponent("LScrollRect")
	else
		arg_2_0.shipContainer = arg_2_0:findTF("main/ship_container/ships"):GetComponent("LScrollRect")
	end

	arg_2_0.shipContainer.enabled = true
	arg_2_0.shipContainer.decelerationRate = 0.07

	setActive(arg_2_0:findTF("main/ship_container"), not arg_2_0.contextData.selectFriend)

	function arg_2_0.shipContainer.onInitItem(arg_17_0)
		arg_2_0:onInitItem(arg_17_0)
	end

	function arg_2_0.shipContainer.onUpdateItem(arg_18_0, arg_18_1)
		arg_2_0:onUpdateItem(arg_18_0, arg_18_1)
	end

	function arg_2_0.shipContainer.onReturnItem(arg_19_0, arg_19_1)
		arg_2_0:onReturnItem(arg_19_0, arg_19_1)
	end

	function arg_2_0.shipContainer.onStart()
		arg_2_0:updateSelected()
	end

	arg_2_0.shipLayout = arg_2_0:findTF("main/ship_container/ships")
	arg_2_0.scrollItems = {}

	local var_2_4 = _G[arg_2_0.contextData.preView]

	if var_2_4 then
		arg_2_0.sortIndex = var_2_4.sortIndex or ShipIndexConst.SortLevel
		arg_2_0.selectAsc = var_2_4.selectAsc or false
		arg_2_0.typeIndex = var_2_4.typeIndex or ShipIndexConst.TypeAll
		arg_2_0.campIndex = var_2_4.campIndex or ShipIndexConst.CampAll
		arg_2_0.rarityIndex = var_2_4.rarityIndex or ShipIndexConst.RarityAll
		arg_2_0.extraIndex = var_2_4.extraIndex or ShipIndexConst.ExtraAll
		arg_2_0.commonTag = var_2_4.commonTag or Ship.PREFERENCE_TAG_NONE
	elseif arg_2_0.contextData.sortData then
		local var_2_5 = arg_2_0.contextData.sortData

		arg_2_0.sortIndex = var_2_5.sort or ShipIndexConst.SortLevel
		arg_2_0.selectAsc = var_2_5.Asc or false
		arg_2_0.typeIndex = var_2_5.typeIndex or ShipIndexConst.TypeAll
		arg_2_0.campIndex = var_2_5.campIndex or ShipIndexConst.CampAll
		arg_2_0.rarityIndex = var_2_5.rarityIndex or ShipIndexConst.RarityAll
		arg_2_0.extraIndex = var_2_5.extraIndex or ShipIndexConst.ExtraAll
		arg_2_0.commonTag = var_2_5.commonTag or Ship.PREFERENCE_TAG_NONE
	else
		arg_2_0.selectAsc = DockyardScene.selectAsc or false
		arg_2_0.sortIndex = DockyardScene.sortIndex or ShipIndexConst.SortLevel
		arg_2_0.typeIndex = DockyardScene.typeIndex or ShipIndexConst.TypeAll
		arg_2_0.campIndex = DockyardScene.campIndex or ShipIndexConst.CampAll
		arg_2_0.rarityIndex = DockyardScene.rarityIndex or ShipIndexConst.RarityAll
		arg_2_0.extraIndex = DockyardScene.extraIndex or ShipIndexConst.ExtraAll
		arg_2_0.commonTag = DockyardScene.commonTag or Ship.PREFERENCE_TAG_NONE
	end

	arg_2_0:updateIndexDatas()
	triggerToggle(arg_2_0.preferenceBtn, arg_2_0.commonTag == Ship.PREFERENCE_TAG_COMMON)
	arg_2_0:initIndexPanel()

	arg_2_0.itemDetailType = -1
	arg_2_0.listEmptyTF = arg_2_0:findTF("empty")

	setActive(arg_2_0.listEmptyTF, false)

	arg_2_0.listEmptyTxt = arg_2_0:findTF("Text", arg_2_0.listEmptyTF)

	setText(arg_2_0.listEmptyTxt, i18n("list_empty_tip_dockyardui"))

	if arg_2_0.contextData.mode == var_0_0.MODE_DESTROY then
		arg_2_0.blacklist = {}
		arg_2_0.selectPanel:GetComponent("HorizontalLayoutGroup").padding.right = 50

		setActive(arg_2_0.selectPanel:Find("quick_select"), true)
		setActive(arg_2_0.settingBtn, true)
	else
		arg_2_0.selectPanel:GetComponent("HorizontalLayoutGroup").padding.right = 90

		setActive(arg_2_0.selectPanel:Find("quick_select"), false)
		setActive(arg_2_0.settingBtn, false)
	end

	arg_2_0.destroyPage = ShipDestroyPage.New(arg_2_0._tf, arg_2_0.event)

	arg_2_0.destroyPage:SetCardClickCallBack(function(arg_21_0)
		arg_2_0.blacklist[arg_21_0.shipVO:getGroupId()] = true

		local var_21_0 = table.indexof(arg_2_0.selectedIds, arg_21_0.shipVO.id)

		if var_21_0 and var_21_0 > 0 then
			table.remove(arg_2_0.selectedIds, var_21_0)
		end

		arg_2_0:updateDestroyRes()
		arg_2_0:updateSelected()
	end)
	arg_2_0.destroyPage:SetConfirmCallBack(function()
		local var_22_0 = {}
		local var_22_1, var_22_2 = arg_2_0:checkDestroyGold()

		if not var_22_2 then
			table.insert(var_22_0, function(arg_23_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("oil_max_tip_title") .. i18n("resource_max_tip_retire_1"),
					onYes = arg_23_0
				})
			end)
		end

		local var_22_3 = underscore.map(arg_2_0.selectedIds, function(arg_24_0)
			return arg_2_0.shipVOsById[arg_24_0]
		end)

		table.insert(var_22_0, function(arg_25_0)
			arg_2_0:checkDestroyShips(var_22_3, arg_25_0)
		end)
		seriesAsync(var_22_0, function()
			arg_2_0:emit(DockyardMediator.ON_DESTROY_SHIPS, arg_2_0.selectedIds)
		end)
	end)

	arg_2_0.destroyConfirmWindow = ShipDestoryConfirmWindow.New(arg_2_0._tf, arg_2_0.event)
end

function var_0_0.isDefaultStatus(arg_27_0)
	return arg_27_0.sortIndex == ShipIndexConst.SortLevel and (not arg_27_0.typeIndex or arg_27_0.typeIndex == ShipIndexConst.TypeAll) and (not arg_27_0.campIndex or arg_27_0.campIndex == ShipIndexConst.CampAll) and (not arg_27_0.rarityIndex or arg_27_0.rarityIndex == ShipIndexConst.RarityAll) and (not arg_27_0.extraIndex or arg_27_0.extraIndex == ShipIndexConst.ExtraAll)
end

function var_0_0.setShipsCount(arg_28_0, arg_28_1, arg_28_2)
	arg_28_0.shipsCount = arg_28_1
	arg_28_0.specialShipCount = arg_28_2
end

function var_0_0.GetCard(arg_29_0, arg_29_1)
	local var_29_0

	if arg_29_0.contextData.selectFriend then
		var_29_0 = DockyardFriend.New(arg_29_1)
	else
		var_29_0 = DockyardShipItem.New(arg_29_1, arg_29_0.contextData.hideTagFlags, arg_29_0.contextData.blockTagFlags)
	end

	return var_29_0
end

function var_0_0.OnClickCard(arg_30_0, arg_30_1)
	if arg_30_1.shipVO then
		if not arg_30_0.selecteEnabled then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_CLICK)

			DockyardScene.value = arg_30_0.shipContainer.value

			arg_30_0.onClick(arg_30_1.shipVO, arg_30_0.shipVOs)
		else
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(table.contains(arg_30_0.selectedIds, arg_30_1.shipVO.id) and SFX_UI_CANCEL or SFX_UI_FORMATION_SELECT)
			arg_30_0:selectShip(arg_30_1.shipVO)
		end
	else
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_CLICK)

		if arg_30_0.callbackQuit then
			arg_30_0.onSelected({}, function()
				arg_30_0:back()
			end)
		elseif not arg_30_1.isLoading then
			arg_30_0.onSelected({})
			arg_30_0:back()
		end
	end
end

function var_0_0.onInitItem(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0:GetCard(arg_32_1)

	var_32_0:updateDetail(arg_32_0.itemDetailType)

	var_32_0.isLoading = true

	onButton(arg_32_0, var_32_0.go, function()
		arg_32_0:OnClickCard(var_32_0)
	end)

	local var_32_1 = GetOrAddComponent(var_32_0.go, "UILongPressTrigger").onLongPressed

	if arg_32_0.contextData.preView == NewBackYardShipInfoLayer.__cname then
		var_32_1:RemoveAllListeners()
		var_32_1:AddListener(function()
			if var_32_0.shipVO then
				arg_32_0.contextData.selectedIds = arg_32_0.selectedIds

				arg_32_0.onClick(var_32_0.shipVO, underscore.select(arg_32_0.shipVOs, function(arg_35_0)
					return arg_35_0
				end), arg_32_0.contextData)
			end
		end)
	else
		var_32_1:RemoveAllListeners()
	end

	arg_32_0.scrollItems[arg_32_1] = var_32_0

	return var_32_0
end

function var_0_0.showEnergyDesc(arg_36_0, arg_36_1, arg_36_2)
	if LeanTween.isTweening(go(arg_36_0.energyDescTF)) then
		LeanTween.cancel(go(arg_36_0.energyDescTF))

		arg_36_0.energyDescTF.localScale = Vector3.one
	end

	setText(arg_36_0.energyDescTextTF, i18n(arg_36_2))

	arg_36_0.energyDescTF.position = arg_36_1

	setActive(arg_36_0.energyDescTF, true)
	LeanTween.scale(arg_36_0.energyDescTF, Vector3.zero, 0.2):setDelay(1):setFrom(Vector3.one):setOnComplete(System.Action(function()
		arg_36_0.energyDescTF.localScale = Vector3.one

		setActive(arg_36_0.energyDescTF, false)
	end))
end

function var_0_0.onUpdateItem(arg_38_0, arg_38_1, arg_38_2)
	local var_38_0 = arg_38_0.scrollItems[arg_38_2] or arg_38_0:onInitItem(arg_38_2)
	local var_38_1 = arg_38_0.shipVOs[arg_38_1 + 1]

	if arg_38_0.contextData.selectFriend then
		var_38_0:update(var_38_1, arg_38_0.friends)
	else
		var_38_0:update(var_38_1)
	end

	if arg_38_0.contextData.mode == DockyardScene.MODE_WORLD then
		var_38_0:updateWorld()
	end

	local var_38_2 = false

	if var_38_0.shipVO then
		for iter_38_0, iter_38_1 in ipairs(arg_38_0.selectedIds) do
			if var_38_0.shipVO.id == iter_38_1 then
				var_38_2 = true

				break
			end
		end
	end

	var_38_0:updateSelected(var_38_2)
	arg_38_0:updateItemBlackBlock(var_38_0)

	var_38_0.isLoading = false

	var_38_0:updateIntimacyEnergy(arg_38_0.contextData.energyDisplay or arg_38_0.sortIndex == ShipIndexConst.SortEnergy)

	local var_38_3 = (arg_38_0.sortIndex == ShipIndexConst.SortIntimacy or arg_38_0.extraIndex == ShipIndexConst.ExtraMarry) and arg_38_0.contextData.mode ~= DockyardScene.MODE_UPGRADE

	var_38_0:updateIntimacy(var_38_3)
end

function var_0_0.onReturnItem(arg_39_0, arg_39_1, arg_39_2)
	if arg_39_0.exited then
		return
	end

	local var_39_0 = arg_39_0.scrollItems[arg_39_2]

	if var_39_0 then
		var_39_0:clear()
	end
end

function var_0_0.updateIndexDatas(arg_40_0)
	arg_40_0.contextData.indexDatas = arg_40_0.contextData.indexDatas or {}
	arg_40_0.contextData.indexDatas.sortIndex = arg_40_0.sortIndex
	arg_40_0.contextData.indexDatas.typeIndex = arg_40_0.typeIndex
	arg_40_0.contextData.indexDatas.campIndex = arg_40_0.campIndex
	arg_40_0.contextData.indexDatas.rarityIndex = arg_40_0.rarityIndex
	arg_40_0.contextData.indexDatas.extraIndex = arg_40_0.extraIndex
end

function var_0_0.initIndexPanel(arg_41_0)
	onButton(arg_41_0, arg_41_0.indexBtn, function()
		local var_42_0 = {
			indexDatas = Clone(arg_41_0.contextData.indexDatas),
			customPanels = {
				minHeight = 650,
				sortIndex = {
					isSort = true,
					mode = CustomIndexLayer.Mode.OR,
					options = ShipIndexConst.SortIndexs,
					names = ShipIndexConst.SortNames
				},
				sortPropertyIndex = {
					blueSeleted = true,
					mode = CustomIndexLayer.Mode.OR,
					options = ShipIndexConst.SortPropertyIndexs,
					names = ShipIndexConst.SortPropertyNames
				},
				typeIndex = {
					blueSeleted = true,
					mode = CustomIndexLayer.Mode.AND,
					options = ShipIndexConst.TypeIndexs,
					names = ShipIndexConst.TypeNames
				},
				campIndex = {
					blueSeleted = true,
					mode = CustomIndexLayer.Mode.AND,
					options = ShipIndexConst.CampIndexs,
					names = ShipIndexConst.CampNames
				},
				rarityIndex = {
					blueSeleted = true,
					mode = CustomIndexLayer.Mode.AND,
					options = ShipIndexConst.RarityIndexs,
					names = ShipIndexConst.RarityNames
				},
				extraIndex = {
					blueSeleted = true,
					mode = CustomIndexLayer.Mode.OR,
					options = ShipIndexConst.ExtraIndexs,
					names = ShipIndexConst.ExtraNames
				},
				layoutPos = Vector2(0, -25)
			},
			groupList = {
				{
					dropdown = false,
					titleTxt = "indexsort_sort",
					titleENTxt = "indexsort_sorteng",
					tags = {
						"sortIndex"
					},
					simpleDropdown = {
						"sortPropertyIndex"
					}
				},
				{
					dropdown = false,
					titleTxt = "indexsort_index",
					titleENTxt = "indexsort_indexeng",
					tags = {
						"typeIndex"
					}
				},
				{
					dropdown = false,
					titleTxt = "indexsort_camp",
					titleENTxt = "indexsort_campeng",
					tags = {
						"campIndex"
					}
				},
				{
					dropdown = false,
					titleTxt = "indexsort_rarity",
					titleENTxt = "indexsort_rarityeng",
					tags = {
						"rarityIndex"
					}
				},
				{
					dropdown = false,
					titleTxt = "indexsort_extraindex",
					titleENTxt = "indexsort_indexeng",
					tags = {
						"extraIndex"
					}
				}
			},
			callback = function(arg_43_0)
				arg_41_0.sortIndex = arg_43_0.sortIndex
				arg_41_0.typeIndex = arg_43_0.typeIndex
				arg_41_0.campIndex = arg_43_0.campIndex
				arg_41_0.rarityIndex = arg_43_0.rarityIndex
				arg_41_0.extraIndex = arg_43_0.extraIndex

				arg_41_0:updateIndexDatas()
				arg_41_0:filter()
			end
		}

		arg_41_0:emit(DockyardMediator.OPEN_DOCKYARD_INDEX, var_42_0)
	end, SFX_PANEL)
	onToggle(arg_41_0, arg_41_0.preferenceBtn, function(arg_44_0)
		if arg_44_0 then
			arg_41_0.commonTag = Ship.PREFERENCE_TAG_COMMON
		else
			arg_41_0.commonTag = Ship.PREFERENCE_TAG_NONE
		end

		arg_41_0:filter()
	end)
end

function var_0_0.setShips(arg_45_0, arg_45_1)
	arg_45_0.shipVOsById = arg_45_1
end

function var_0_0.setPlayer(arg_46_0, arg_46_1)
	arg_46_0.player = arg_46_1

	arg_46_0:updateBarInfo()
end

function var_0_0.setFriends(arg_47_0, arg_47_1)
	arg_47_0.friends = {}

	for iter_47_0, iter_47_1 in pairs(arg_47_1) do
		arg_47_0.friends[iter_47_1.id] = iter_47_1
	end
end

function var_0_0.updateBarInfo(arg_48_0)
	setActive(arg_48_0.bottomTipsText, arg_48_0.contextData.leftTopInfo)
	setText(arg_48_0.bottomTipsText, arg_48_0.contextData.leftTopInfo and i18n("dock_yard_left_tips", arg_48_0.contextData.leftTopInfo) or "")
	setActive(arg_48_0.bottomTipsWithFrame, arg_48_0.contextData.leftTopWithFrameInfo)
	setText(arg_48_0.bottomTipsWithFrame:Find("Text"), arg_48_0.contextData.leftTopWithFrameInfo or "")

	if arg_48_0.contextData.mode == var_0_0.MODE_WORLD or arg_48_0.contextData.mode == var_0_0.MODE_GUILD_BOSS or arg_48_0.contextData.mode == var_0_0.MODE_REMOULD then
		setActive(arg_48_0.leftTipsText, false)
	else
		setActive(arg_48_0.leftTipsText, true)
		arg_48_0:updateCapacityDisplay()
	end
end

function var_0_0.updateCapacityDisplay(arg_49_0)
	setActive(arg_49_0.leftTipsText:Find("plus"), not arg_49_0.isCapacityMeta)
	setActive(arg_49_0.leftTipsText:Find("tip"), arg_49_0.isCapacityMeta)
	setActive(arg_49_0.leftTipsText:Find("switch/off"), not arg_49_0.isCapacityMeta)
	setActive(arg_49_0.leftTipsText:Find("switch/on"), arg_49_0.isCapacityMeta)

	if arg_49_0.isCapacityMeta then
		setText(arg_49_0.leftTipsText:Find("label"), i18n("specialshipyard_name"))
		setText(arg_49_0.leftTipsText:Find("Text"), arg_49_0.specialShipCount)
	else
		setText(arg_49_0.leftTipsText:Find("label"), i18n("ship_dockyardScene_capacity"))
		setText(arg_49_0.leftTipsText:Find("Text"), arg_49_0.shipsCount .. "/" .. arg_49_0.player:getMaxShipBag())
	end
end

function var_0_0.initWorldPanel(arg_50_0)
	onButton(arg_50_0, arg_50_0.worldPanel:Find("btn_repair"), function()
		if #arg_50_0.selectedIds > 0 then
			arg_50_0:repairWorldShip(arg_50_0.shipVOsById[arg_50_0.selectedIds[1]])
		end
	end, SFX_PANEL)
	onButton(arg_50_0, arg_50_0.worldPanel:Find("btn_repair_all"), function()
		local var_52_0 = {}
		local var_52_1 = 0

		for iter_52_0, iter_52_1 in pairs(arg_50_0.shipVOsById) do
			local var_52_2 = WorldConst.FetchWorldShip(iter_52_1.id)

			if var_52_2:IsBroken() or not var_52_2:IsHpFull() then
				table.insert(var_52_0, var_52_2.id)

				var_52_1 = var_52_1 + nowWorld():CalcRepairCost(var_52_2)
			end
		end

		if #var_52_0 == 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("world_ship_repair_no_need"))
		else
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("world_ship_repair_all", var_52_1),
				onYes = function()
					arg_50_0:emit(DockyardMediator.ON_SHIP_REPAIR, var_52_0, var_52_1)
				end
			})
		end
	end, SFX_PANEL)
end

function var_0_0.repairWorldShip(arg_54_0, arg_54_1)
	local var_54_0 = WorldConst.FetchWorldShip(arg_54_1.id)
	local var_54_1 = nowWorld():CalcRepairCost(var_54_0)

	if var_54_0:IsBroken() then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("world_ship_repair_2", arg_54_1:getName(), var_54_1),
			onYes = function()
				arg_54_0:emit(DockyardMediator.ON_SHIP_REPAIR, {
					var_54_0.id
				}, var_54_1)
			end
		})
	elseif not var_54_0:IsHpFull() then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("world_ship_repair_1", arg_54_1:getName(), var_54_1),
			onYes = function()
				arg_54_0:emit(DockyardMediator.ON_SHIP_REPAIR, {
					var_54_0.id
				}, var_54_1)
			end
		})
	else
		pg.TipsMgr.GetInstance():ShowTips(i18n("world_ship_repair_no_need"))
	end
end

function var_0_0.filter(arg_57_0)
	local var_57_0 = arg_57_0:isDefaultStatus() and "shaixuan_off" or "shaixuan_on"

	GetSpriteFromAtlasAsync("ui/dockyardui_atlas", var_57_0, function(arg_58_0)
		setImageSprite(arg_57_0.indexBtn, arg_58_0, true)
	end)

	if arg_57_0.isRemouldOrUpgradeMode then
		arg_57_0:filterForRemouldAndUpgrade()
	else
		arg_57_0:filterCommon()
	end

	local var_57_1 = 0

	if arg_57_0.contextData.quitTeam then
		var_57_1 = var_57_1 + 1

		table.insert(arg_57_0.shipVOs, var_57_1, false)
	end

	if arg_57_0.contextData.priorEquipUpShipIDList then
		local var_57_2 = {}

		for iter_57_0, iter_57_1 in ipairs(arg_57_0.contextData.priorEquipUpShipIDList) do
			var_57_2[iter_57_1] = true
		end

		for iter_57_2 = #arg_57_0.shipVOs, 1, -1 do
			local var_57_3 = type(arg_57_0.shipVOs[iter_57_2]) == "table" and arg_57_0.shipVOs[iter_57_2].id

			if var_57_2[var_57_3] then
				var_57_2[var_57_3] = table.remove(arg_57_0.shipVOs, iter_57_2)
			end
		end

		for iter_57_3, iter_57_4 in ipairs(arg_57_0.contextData.priorEquipUpShipIDList) do
			local var_57_4 = var_57_2[iter_57_4]

			if type(var_57_4) == "table" then
				var_57_1 = var_57_1 + 1

				table.insert(arg_57_0.shipVOs, var_57_1, var_57_4)
			end
		end
	end

	if var_0_0.MODE_OVERVIEW == arg_57_0.contextData.mode and DockyardScene.value then
		arg_57_0:updateShipCount(DockyardScene.value or 0)

		DockyardScene.value = nil
	else
		arg_57_0:updateShipCount(0)
	end
end

function var_0_0.filterForRemouldAndUpgrade(arg_59_0)
	arg_59_0.shipVOs = {}

	local var_59_0 = arg_59_0.isFilterLockForMod
	local var_59_1 = arg_59_0.isFilterLevelForMod

	local function var_59_2(arg_60_0)
		local var_60_0 = true

		if not var_59_0 and arg_60_0.lockState == Ship.LOCK_STATE_LOCK then
			var_60_0 = false
		end

		if not var_59_1 and arg_60_0.level > 1 then
			var_60_0 = false
		end

		return var_60_0
	end

	for iter_59_0, iter_59_1 in pairs(arg_59_0.shipVOsById) do
		if var_59_2(iter_59_1) then
			table.insert(arg_59_0.shipVOs, iter_59_1)
		end
	end

	table.sort(arg_59_0.shipVOs, CompareFuncs({
		function(arg_61_0)
			return arg_61_0.level
		end,
		function(arg_62_0)
			return arg_62_0:isTestShip() and 1 or 0
		end
	}))
end

function var_0_0.filterCommon(arg_63_0)
	arg_63_0.shipVOs = {}

	local var_63_0 = arg_63_0.sortIndex

	local function var_63_1(arg_64_0)
		if arg_63_0.contextData.mode ~= var_0_0.MODE_GUILD_BOSS then
			return true
		end

		if arg_63_0.isShowAssultShips then
			return true
		end

		if not arg_64_0.user then
			return true
		end

		if arg_64_0.user.id == arg_63_0.player.id then
			return true
		end

		return false
	end

	for iter_63_0, iter_63_1 in pairs(arg_63_0.shipVOsById) do
		if arg_63_0.contextData.blockLock and iter_63_1:GetLockState() == Ship.LOCK_STATE_LOCK then
			-- block empty
		elseif arg_63_0.teamTypeFilter and iter_63_1:getTeamType() ~= arg_63_0.teamTypeFilter then
			-- block empty
		elseif ShipIndexConst.filterByType(iter_63_1, arg_63_0.typeIndex) and ShipIndexConst.filterByCamp(iter_63_1, arg_63_0.campIndex) and ShipIndexConst.filterByRarity(iter_63_1, arg_63_0.rarityIndex) and ShipIndexConst.filterByExtra(iter_63_1, arg_63_0.extraIndex) and (arg_63_0.commonTag == Ship.PREFERENCE_TAG_NONE or arg_63_0.commonTag == iter_63_1:GetPreferenceTag()) and var_63_1(iter_63_1) then
			table.insert(arg_63_0.shipVOs, iter_63_1)
		end
	end

	local var_63_2 = getInputText(arg_63_0.nameSearchInput)

	if var_63_2 and var_63_2 ~= "" then
		arg_63_0.shipVOs = underscore.filter(arg_63_0.shipVOs, function(arg_65_0)
			return arg_65_0:IsMatchKey(var_63_2)
		end)
	end

	local var_63_3, var_63_4 = ShipIndexConst.getSortFuncAndName(var_63_0, arg_63_0.selectAsc)

	if (var_63_0 ~= ShipIndexConst.SortIntimacy and true or false) and not defaultValue((arg_63_0.contextData.hideTagFlags or {}).inFleet, ShipStatus.TAG_HIDE_BASE.inFleet) then
		table.insert(var_63_3, 1, function(arg_66_0)
			return arg_66_0:getFlag("inFleet") and 0 or 1
		end)
	end

	if var_63_3 then
		arg_63_0:SortShips(var_63_3)
	end

	arg_63_0:updateSelected()
	setActive(arg_63_0.sortImgAsc, arg_63_0.selectAsc)
	setActive(arg_63_0.sortImgDesc, not arg_63_0.selectAsc)
	setText(arg_63_0:findTF("Image", arg_63_0.sortBtn), i18n(var_63_4))
end

function var_0_0.SortShips(arg_67_0, arg_67_1)
	if pg.NewGuideMgr.GetInstance():IsBusy() then
		local var_67_0 = {
			101171,
			201211,
			401231,
			301051
		}

		arg_67_1 = {
			function(arg_68_0)
				return table.contains(var_67_0, arg_68_0.configId) and 0 or 1
			end
		}
	elseif arg_67_0.isFormTactics then
		table.insert(arg_67_1, 1, function(arg_69_0)
			return arg_69_0:getNation() == Nation.META and 1 or 0
		end)
		table.insert(arg_67_1, 1, function(arg_70_0)
			return arg_70_0:isFullSkillLevel() and 1 or 0
		end)
	elseif arg_67_0.contextData.mode == var_0_0.MODE_OVERVIEW or arg_67_0.contextData.mode == var_0_0.MODE_SELECT then
		table.insert(arg_67_1, 1, function(arg_71_0)
			return -arg_71_0.activityNpc
		end)
	elseif arg_67_0.contextData.mode == var_0_0.MODE_GUILD_BOSS then
		table.insert(arg_67_1, 1, function(arg_72_0)
			return arg_72_0.guildRecommand and 0 or 1
		end)
	end

	table.sort(arg_67_0.shipVOs, CompareFuncs(arg_67_1))
end

function var_0_0.UpdateGuildViewEquipmentsBtn(arg_73_0)
	setActive(arg_73_0.viewEquipmentBtn, arg_73_0.contextData.mode == var_0_0.MODE_GUILD_BOSS and #arg_73_0.selectedIds > 0)
end

function var_0_0.didEnter(arg_74_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_74_0.blurPanel)
	setActive(arg_74_0.stampBtn, getProxy(TaskProxy):mingshiTouchFlagEnabled() and arg_74_0.contextData.mode ~= var_0_0.MODE_GUILD_BOSS)
	arg_74_0:UpdateGuildViewEquipmentsBtn()
	onButton(arg_74_0, arg_74_0.stampBtn, function()
		getProxy(TaskProxy):dealMingshiTouchFlag(1)
	end, SFX_CONFIRM)
	onButton(arg_74_0, arg_74_0:findTF("back", arg_74_0.topPanel), function()
		arg_74_0:back()
	end, SFX_CANCEL)
	onButton(arg_74_0, arg_74_0.sortBtn, function()
		arg_74_0.selectAsc = not arg_74_0.selectAsc

		arg_74_0:filter()
	end, SFX_UI_CLICK)

	if arg_74_0.contextData.mode == var_0_0.MODE_GUILD_BOSS then
		arg_74_0.isShowAssultShips = false

		onToggle(arg_74_0, arg_74_0.assultBtn, function(arg_78_0)
			arg_74_0.isShowAssultShips = arg_78_0

			arg_74_0:filter()
		end, SFX_PANEL)
		triggerToggle(arg_74_0.assultBtn, true)

		arg_74_0.guildShipEquipmentsPage = GuildShipEquipmentsPage.New(arg_74_0._tf, arg_74_0.event)

		arg_74_0.guildShipEquipmentsPage:SetCallBack(function()
			arg_74_0:TriggerCard(-1)
		end, function()
			arg_74_0:TriggerCard(1)
		end)
		onButton(arg_74_0, arg_74_0.viewEquipmentBtn, function()
			local var_81_0 = arg_74_0.selectedIds[#arg_74_0.selectedIds]

			if not var_81_0 then
				return
			end

			local var_81_1 = arg_74_0.shipVOsById[var_81_0]
			local var_81_2 = var_81_1.user

			arg_74_0.guildShipEquipmentsPage:ExecuteAction("Show", var_81_1, var_81_2)
		end, SFX_PANEL)
	end

	local var_74_0 = arg_74_0.attrBtn:GetComponent("Button")

	eachChild(var_74_0, function(arg_82_0)
		setActive(arg_82_0, false)
	end)

	arg_74_0.isFormTactics = arg_74_0.contextData.prevPage == "NewNavalTacticsMediator"

	local var_74_1 = arg_74_0:findTF("off", var_74_0):GetComponent("Image")
	local var_74_2 = arg_74_0:findTF("on", var_74_0):GetComponent("Image")

	if arg_74_0.isFormTactics then
		GetImageSpriteFromAtlasAsync("ui/dockyardui_atlas", "skill_off", var_74_1)
		GetImageSpriteFromAtlasAsync("ui/dockyardui_atlas", "skill_on", var_74_2)
	else
		GetImageSpriteFromAtlasAsync("ui/dockyardui_atlas", "attr_off", var_74_1)
		GetImageSpriteFromAtlasAsync("ui/dockyardui_atlas", "attr_on", var_74_2)
	end

	if arg_74_0.isRemouldOrUpgradeMode then
		local var_74_3 = getProxy(SettingsProxy)

		arg_74_0.isFilterLevelForMod = var_74_3:GetDockYardLevelBtnFlag()

		arg_74_0:OnSwitch(arg_74_0.modLeveFilter, arg_74_0.isFilterLevelForMod, function(arg_83_0)
			arg_74_0.isFilterLevelForMod = arg_83_0

			arg_74_0:filter()
		end)

		arg_74_0.isFilterLockForMod = var_74_3:GetDockYardLockBtnFlag()

		arg_74_0:OnSwitch(arg_74_0.modLockFilter, arg_74_0.isFilterLockForMod, function(arg_84_0)
			arg_74_0.isFilterLockForMod = arg_84_0

			arg_74_0:filter()
		end)
	end

	onButton(arg_74_0, var_74_0, function()
		if not arg_74_0.isFormTactics then
			arg_74_0.itemDetailType = (arg_74_0.itemDetailType + 1) % 4
		else
			arg_74_0.itemDetailType = arg_74_0.itemDetailType == DockyardShipItem.DetailType0 and DockyardShipItem.DetailType3 or DockyardShipItem.DetailType0
		end

		setActive(var_74_2, arg_74_0.itemDetailType ~= DockyardShipItem.DetailType0)
		setActive(var_74_1, arg_74_0.itemDetailType == DockyardShipItem.DetailType0)

		var_74_0.targetGraphic = arg_74_0.itemDetailType == DockyardShipItem.DetailType0 and var_74_1 or var_74_2

		arg_74_0:updateItemDetailType()
	end, SFX_PANEL)
	triggerButton(var_74_0)
	onButton(arg_74_0, arg_74_0.selectPanel:Find("cancel_button"), function()
		if arg_74_0.animating then
			return
		end

		if arg_74_0.contextData.mode == var_0_0.MODE_DESTROY then
			if #arg_74_0.selectedIds > 0 then
				arg_74_0:unselecteAllShips()
				arg_74_0:back()
			else
				arg_74_0:back()
			end
		else
			arg_74_0:back()

			return
		end
	end, SFX_CANCEL)
	onButton(arg_74_0, arg_74_0.selectPanel:Find("confirm_button"), function()
		if arg_74_0.animating then
			return
		end

		if arg_74_0.contextData.mode == var_0_0.MODE_DESTROY then
			local var_87_0, var_87_1 = arg_74_0:checkDestroyGold()

			if not var_87_0 or not var_87_1 then
				if not var_87_0 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_retire"))
				elseif not var_87_0 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_retire"))
				end

				return
			end
		end

		if #arg_74_0.selectedIds < arg_74_0.selectedMin then
			if arg_74_0.leastLimitMsg then
				pg.TipsMgr.GetInstance():ShowTips(arg_74_0.leastLimitMsg)
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("ship_dockyardScene_error_choiseRoleMore", arg_74_0.selectedMin))
			end

			return
		end

		if arg_74_0.contextData.mode == var_0_0.MODE_DESTROY then
			arg_74_0:displayDestroyPanel()
		else
			local var_87_2 = {}

			if arg_74_0.contextData.destroyCheck then
				local var_87_3 = underscore.map(arg_74_0.selectedIds, function(arg_88_0)
					return arg_74_0.shipVOsById[arg_88_0]
				end)

				table.insert(var_87_2, function(arg_89_0)
					arg_74_0:checkDestroyShips(var_87_3, arg_89_0)
				end)
			end

			seriesAsync(var_87_2, function()
				if arg_74_0.confirmSelect then
					arg_74_0.confirmSelect(arg_74_0.selectedIds, function()
						arg_74_0.onSelected(arg_74_0.selectedIds)
						arg_74_0:back()
					end, function()
						arg_74_0:back()
					end)
				elseif arg_74_0.callbackQuit then
					arg_74_0.onSelected(arg_74_0.selectedIds, function()
						arg_74_0:back()
					end)
				else
					arg_74_0.onSelected(arg_74_0.selectedIds)
					arg_74_0:back()
				end
			end)
		end
	end, SFX_CONFIRM)
	onButton(arg_74_0, arg_74_0.selectPanel:Find("quick_select"), function()
		if arg_74_0.animating then
			return
		end

		local var_94_0 = {
			PlayerPrefs.GetInt("QuickSelectRarity1", 3),
			PlayerPrefs.GetInt("QuickSelectRarity2", 4),
			PlayerPrefs.GetInt("QuickSelectRarity3", 2)
		}
		local var_94_1 = 3
		local var_94_2 = {}

		for iter_94_0, iter_94_1 in pairs(var_94_0) do
			if iter_94_1 ~= 0 then
				var_94_2[iter_94_1] = var_94_2[iter_94_1] or var_94_1
				var_94_1 = var_94_1 - 1
			end
		end

		local var_94_3 = getProxy(BayProxy):getShips()
		local var_94_4 = {}
		local var_94_5 = {}

		for iter_94_2, iter_94_3 in pairs(var_94_3) do
			if iter_94_3:isMaxStar() then
				var_94_4[iter_94_3:getGroupId()] = true
			else
				local var_94_6 = iter_94_3:getMaxStar() - iter_94_3:getStar() + 1

				if iter_94_3:GetLockState() == Ship.LOCK_STATE_UNLOCK then
					var_94_6 = var_94_6 + 1
				end

				local var_94_7 = var_94_5[iter_94_3:getGroupId()]

				var_94_5[iter_94_3:getGroupId()] = var_94_7 and var_94_7 < var_94_6 and var_94_7 or var_94_6
			end
		end

		local var_94_8 = _.select(arg_74_0.shipVOs, function(arg_95_0)
			return arg_95_0.configId ~= 100001 and arg_95_0.configId ~= 100011 and arg_95_0:GetLockState() == Ship.LOCK_STATE_UNLOCK and table.contains(var_94_0, arg_95_0:getRarity()) and arg_95_0.level == 1 and not arg_74_0.blacklist[arg_95_0:getGroupId()] and not table.contains(arg_74_0.selectedIds, arg_95_0.id) and not arg_95_0:hasAnyFlag({
				"inFleet",
				"inChapter",
				"inWorld",
				"inEvent",
				"inBackyard",
				"inClass",
				"inTactics",
				"inExercise",
				"inAdmiral",
				"inElite",
				"inActivity",
				"inGuildEvent",
				"inGuildBossEvent"
			})
		end)

		if not _.all(var_94_8, function(arg_96_0)
			return arg_74_0.blacklist[arg_96_0:getGroupId()]
		end) then
			var_94_8 = _.select(var_94_8, function(arg_97_0)
				return not arg_74_0.blacklist[arg_97_0:getGroupId()]
			end)
		elseif #arg_74_0.selectedIds > 0 then
			var_94_8 = {}
		end

		table.sort(var_94_8, function(arg_98_0, arg_98_1)
			local var_98_0 = var_94_2[arg_98_0:getRarity()] or 0
			local var_98_1 = var_94_2[arg_98_1:getRarity()] or 0

			if var_98_0 == var_98_1 then
				if arg_98_0:getGroupId() == arg_98_1:getGroupId() then
					return arg_98_0.createTime > arg_98_1.createTime
				end

				return arg_98_0.configId > arg_98_1.configId
			else
				return var_98_1 < var_98_0
			end
		end)

		local var_94_9 = PlayerPrefs.GetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepNone")
		local var_94_10 = PlayerPrefs.GetString("QuickSelectWithoutMaxstar", "KeepAll")
		local var_94_11 = {}
		local var_94_12 = _.select(var_94_8, function(arg_99_0)
			if var_94_4[arg_99_0:getGroupId()] then
				if var_94_9 == "KeepNone" then
					return true
				elseif var_94_9 == "KeepOne" then
					if not var_94_11[arg_99_0:getGroupId()] then
						var_94_11[arg_99_0:getGroupId()] = true

						return false
					end

					return true
				elseif var_94_9 == "KeepAll" then
					return false
				end
			elseif var_94_10 == "KeepNone" then
				return true
			elseif var_94_10 == "KeepNeeded" then
				if var_94_5[arg_99_0:getGroupId()] > 0 then
					var_94_5[arg_99_0:getGroupId()] = var_94_5[arg_99_0:getGroupId()] - 1

					return false
				end

				return true
			elseif var_94_10 == "KeepAll" then
				return false
			end
		end)
		local var_94_13 = 0
		local var_94_14 = false
		local var_94_15 = false
		local var_94_16 = 0
		local var_94_17 = 0

		for iter_94_4, iter_94_5 in ipairs(arg_74_0.selectedIds) do
			local var_94_18, var_94_19 = arg_74_0.shipVOsById[iter_94_5]:calReturnRes()

			var_94_16 = var_94_16 + var_94_18
			var_94_17 = var_94_17 + var_94_19
		end

		for iter_94_6, iter_94_7 in ipairs(var_94_12) do
			if arg_74_0.selectedMax > 0 and arg_74_0.selectedMax <= #arg_74_0.selectedIds then
				break
			end

			local var_94_20, var_94_21 = iter_94_7:calReturnRes()

			var_94_16 = var_94_16 + var_94_20
			var_94_17 = var_94_17 + var_94_21
			var_94_14 = arg_74_0.player:OilMax(var_94_17)
			var_94_15 = arg_74_0.player:GoldMax(var_94_16)

			if var_94_15 then
				break
			end

			var_94_13 = var_94_13 + 1

			arg_74_0:selectShip(iter_94_7, true)
		end

		if var_94_13 == 0 then
			if var_94_15 then
				if #arg_74_0.selectedIds == 0 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_retire"))
				else
					pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title"))
				end
			elseif #arg_74_0.selectedIds > 0 then
				arg_74_0:displayDestroyPanel()
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("retire_selectzero"))
			end
		elseif var_94_14 then
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("oil_max_tip_title") .. i18n("resource_max_tip_retire_1"),
				onYes = function()
					arg_74_0:displayDestroyPanel()
				end
			})
		else
			arg_74_0:displayDestroyPanel()
		end
	end, SFX_CONFIRM)

	if not arg_74_0.contextData.selectFriend then
		arg_74_0.shipContainer:GetComponentInChildren(typeof(GridLayoutGroup)).constraintCount = 7
	end

	arg_74_0:filter()
	arg_74_0:updateBarInfo()

	if arg_74_0.contextData.mode == var_0_0.MODE_WORLD then
		arg_74_0:initWorldPanel()
	elseif arg_74_0.contextData.mode == var_0_0.MODE_DESTROY and not LOCK_DESTROY_GUIDE then
		pg.SystemGuideMgr.GetInstance():Play(arg_74_0)
	end

	setAnchoredPosition(arg_74_0.topPanel, {
		y = arg_74_0.topPanel.rect.height
	})
	setAnchoredPosition(arg_74_0.selectPanel, {
		y = -1 * arg_74_0.selectPanel.rect.height
	})
	onNextTick(function()
		if arg_74_0.exited then
			return
		end

		arg_74_0:uiStartAnimating()
	end)

	if arg_74_0.contextData.selectShipId then
		arg_74_0.selectedIds = {}

		table.insert(arg_74_0.selectedIds, arg_74_0.contextData.selectShipId)
		arg_74_0:updateSelected()
	end

	arg_74_0.bulinTip = AprilFoolBulinSubView.ShowAprilFoolBulin(arg_74_0)

	onButton(arg_74_0, arg_74_0.settingBtn, function()
		arg_74_0.settingPanel:Load()
		arg_74_0.settingPanel:ActionInvoke("Show")
	end)
	pg.SystemGuideMgr.GetInstance():Play(arg_74_0)
end

function var_0_0.TriggerCard(arg_103_0, arg_103_1)
	local var_103_0 = arg_103_0.selectedIds[1]

	if not var_103_0 then
		return
	end

	local var_103_1

	for iter_103_0, iter_103_1 in ipairs(arg_103_0.shipVOs) do
		if iter_103_1 and iter_103_1.id == var_103_0 then
			var_103_1 = iter_103_0

			break
		end
	end

	if not var_103_1 then
		return
	end

	local var_103_2 = var_103_1
	local var_103_3

	local function var_103_4()
		var_103_2 = var_103_2 + arg_103_1

		local var_104_0 = arg_103_0.shipVOs[var_103_2]

		if not var_104_0 or arg_103_0.checkShip(var_104_0) then
			return var_104_0
		else
			return var_103_4()
		end
	end

	local var_103_5 = var_103_4()

	if not var_103_5 then
		return
	end

	local function var_103_6()
		local var_105_0

		for iter_105_0, iter_105_1 in pairs(arg_103_0.scrollItems) do
			if iter_105_1.shipVO and iter_105_1.go.name ~= "-1" and iter_105_1.shipVO.id == var_103_5.id then
				var_105_0 = iter_105_1

				break
			end
		end

		return var_105_0
	end

	local var_103_7 = var_103_6()

	if var_103_7 then
		local var_103_8 = getBounds(arg_103_0:findTF("main/ship_container"))
		local var_103_9 = getBounds(var_103_7.tr)

		if not var_103_8:Intersects(var_103_9) then
			local var_103_10 = arg_103_1 * (arg_103_0.shipContainer:HeadIndexToValue(7) - arg_103_0.shipContainer:HeadIndexToValue(1))
			local var_103_11 = arg_103_0.shipContainer.value + var_103_10

			arg_103_0.shipContainer:SetNormalizedPosition(var_103_11, 1)
		end
	end

	if not var_103_7 then
		local var_103_12 = (math.ceil(var_103_2 / 7) - math.ceil(var_103_1 / 7)) * (arg_103_0.shipContainer:HeadIndexToValue(21) - arg_103_0.shipContainer:HeadIndexToValue(1))
		local var_103_13 = arg_103_0.shipContainer.value + var_103_12

		arg_103_0.shipContainer:SetNormalizedPosition(var_103_13, 1)

		var_103_7 = var_103_6()
	end

	if var_103_7 then
		triggerButton(var_103_7.tr)

		local var_103_14 = arg_103_0.shipVOsById[var_103_7.shipVO.id]

		arg_103_0.guildShipEquipmentsPage:Refresh(var_103_14, var_103_14.user)
	end
end

function var_0_0.OnSwitch(arg_106_0, arg_106_1, arg_106_2, arg_106_3)
	local function var_106_0()
		setActive(arg_106_1:Find("off"), not arg_106_2)
		setActive(arg_106_1:Find("on"), arg_106_2)
	end

	onButton(arg_106_0, arg_106_1, function()
		arg_106_2 = not arg_106_2

		if arg_106_3 then
			arg_106_3(arg_106_2)
		end

		var_106_0()
	end, SFX_PANEL)
	var_106_0()
end

function var_0_0.onBackPressed(arg_109_0)
	if arg_109_0.destroyConfirmWindow:isShowing() then
		arg_109_0.destroyConfirmWindow:Hide()

		return
	end

	if arg_109_0.destroyPage:isShowing() then
		arg_109_0.destroyPage:Hide()

		return
	end

	if arg_109_0.settingPanel:isShowing() then
		arg_109_0.settingPanel:Hide()

		return
	end

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	arg_109_0:back()
end

function var_0_0.updateShipStatusById(arg_110_0, arg_110_1)
	for iter_110_0, iter_110_1 in pairs(arg_110_0.scrollItems) do
		if iter_110_1.shipVO and iter_110_1.shipVO.id == arg_110_1 then
			iter_110_1:flush(arg_110_0.selectedIds)

			if arg_110_0.contextData.mode == DockyardScene.MODE_WORLD then
				iter_110_1:updateWorld()
			end
		end
	end
end

function var_0_0.checkDestroyGold(arg_111_0, arg_111_1)
	local var_111_0 = 0
	local var_111_1 = 0

	for iter_111_0, iter_111_1 in ipairs(arg_111_0.selectedIds) do
		local var_111_2, var_111_3 = arg_111_0.shipVOsById[iter_111_1]:calReturnRes()

		var_111_0 = var_111_0 + var_111_2
		var_111_1 = var_111_1 + var_111_3
	end

	if arg_111_1 then
		local var_111_4, var_111_5 = arg_111_1:calReturnRes()

		var_111_0 = var_111_0 + var_111_4
		var_111_1 = var_111_1 + var_111_5
	end

	local var_111_6 = arg_111_0.player:OilMax(var_111_1)

	if arg_111_0.player:GoldMax(var_111_0) then
		return false, not var_111_6
	end

	return true, not var_111_6
end

function var_0_0.selectShip(arg_112_0, arg_112_1, arg_112_2)
	local var_112_0 = false
	local var_112_1

	for iter_112_0, iter_112_1 in ipairs(arg_112_0.selectedIds) do
		if iter_112_1 == arg_112_1.id then
			var_112_0 = true
			var_112_1 = iter_112_0

			break
		end
	end

	if not var_112_0 then
		local var_112_2, var_112_3 = arg_112_0.checkShip(arg_112_1, function()
			if not arg_112_0.exited then
				arg_112_0:selectShip(arg_112_1)
			end
		end, arg_112_0.selectedMax == 1 and {} or arg_112_0.selectedIds)

		if not var_112_2 then
			if var_112_3 then
				pg.TipsMgr.GetInstance():ShowTips(var_112_3)
			end

			return
		end

		if arg_112_0.selectedMax == 1 then
			local var_112_4 = arg_112_0.selectedIds[1]

			arg_112_0.selectedIds[1] = arg_112_1.id
		elseif arg_112_0.selectedMax == 0 or #arg_112_0.selectedIds < arg_112_0.selectedMax then
			table.insert(arg_112_0.selectedIds, arg_112_1.id)
			arg_112_0:updateBlackBlocks(arg_112_1)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_dockyardScene_error_choiseRoleLess", arg_112_0.selectedMax))

			return
		end
	else
		local var_112_5, var_112_6 = arg_112_0.onCancelShip(arg_112_1, function()
			if not arg_112_0.exited then
				arg_112_0:selectShip(arg_112_1)
			end
		end, arg_112_0.selectedIds)

		if not var_112_5 then
			if var_112_6 then
				pg.TipsMgr.GetInstance():ShowTips(var_112_6)
			end

			return
		end

		table.remove(arg_112_0.selectedIds, var_112_1)

		if arg_112_0.selectedMax ~= 1 then
			arg_112_0:updateBlackBlocks(arg_112_1)
		end
	end

	arg_112_0:updateSelected()

	if arg_112_0.contextData.mode == var_0_0.MODE_DESTROY then
		arg_112_0:updateDestroyRes()
	elseif arg_112_0.contextData.mode == var_0_0.MODE_MOD then
		arg_112_0:updateModAttr()
	end

	arg_112_0:UpdateGuildViewEquipmentsBtn()
end

function var_0_0.updateBlackBlocks(arg_115_0, arg_115_1)
	if not arg_115_0.contextData.useBlackBlock or not arg_115_1 then
		return
	end

	for iter_115_0, iter_115_1 in pairs(arg_115_0.scrollItems) do
		arg_115_0:updateItemBlackBlock(iter_115_1)
	end
end

function var_0_0.updateItemBlackBlock(arg_116_0, arg_116_1)
	if arg_116_0.contextData.useBlackBlock then
		if arg_116_0.selectedMax == 1 then
			arg_116_1:updateBlackBlock(arg_116_0.contextData.otherSelectedIds)
		else
			arg_116_1:updateBlackBlock(arg_116_0.selectedIds)
		end
	else
		arg_116_1:updateBlackBlock()
	end
end

function var_0_0.unselecteAllShips(arg_117_0)
	arg_117_0.selectedIds = {}

	arg_117_0:updateSelected()
	arg_117_0:updateDestroyRes()
end

function var_0_0.updateSelected(arg_118_0)
	for iter_118_0, iter_118_1 in pairs(arg_118_0.scrollItems) do
		if iter_118_1.shipVO then
			local var_118_0 = false

			for iter_118_2, iter_118_3 in ipairs(arg_118_0.selectedIds) do
				if iter_118_1.shipVO.id == iter_118_3 then
					var_118_0 = true

					break
				end
			end

			iter_118_1:updateSelected(var_118_0)
		end
	end

	if arg_118_0.selectedMax == 0 then
		setText(arg_118_0.selectPanel:Find("bottom_info/bg_input/count"), #arg_118_0.selectedIds)
	else
		local var_118_1 = #arg_118_0.selectedIds

		if arg_118_0.contextData.mode ~= var_0_0.MODE_DESTROY or #arg_118_0.selectedIds == 0 then
			var_118_1 = setColorStr(#arg_118_0.selectedIds, COLOR_WHITE)
		elseif arg_118_0.contextData.mode == var_0_0.MODE_DESTROY then
			var_118_1 = #arg_118_0.selectedIds == 10 and setColorStr(#arg_118_0.selectedIds, COLOR_RED) or setColorStr(#arg_118_0.selectedIds, COLOR_GREEN)
		end

		setText(arg_118_0.selectPanel:Find("bottom_info/bg_input/count"), var_118_1 .. "/" .. arg_118_0.selectedMax)
	end

	if #arg_118_0.selectedIds < arg_118_0.selectedMin then
		setActive(arg_118_0.selectPanel:Find("confirm_button/mask"), true)
	else
		setActive(arg_118_0.selectPanel:Find("confirm_button/mask"), false)
	end

	if arg_118_0.contextData.mode == var_0_0.MODE_MOD then
		arg_118_0:updateModAttr()
	end
end

function var_0_0.updateItemDetailType(arg_119_0)
	for iter_119_0, iter_119_1 in pairs(arg_119_0.scrollItems) do
		iter_119_1:updateDetail(arg_119_0.itemDetailType)
	end

	arg_119_0.shipLayout.anchoredPosition = arg_119_0.shipLayout.anchoredPosition + Vector3(0, 0.001, 0)
end

function var_0_0.closeDestroyMode(arg_120_0)
	setActive(arg_120_0.awardTF, false)
	setActive(arg_120_0.bottomTipsText, true)
end

function var_0_0.updateDestroyRes(arg_121_0)
	if table.getCount(arg_121_0.selectedIds) == 0 then
		arg_121_0:closeDestroyMode()
	else
		setActive(arg_121_0.awardTF, true)
		setActive(arg_121_0.bottomTipsText, false)
	end

	local var_121_0 = _.map(arg_121_0.selectedIds, function(arg_122_0)
		return arg_121_0.shipVOsById[arg_122_0]
	end)
	local var_121_1, var_121_2, var_121_3 = ShipCalcHelper.CalcDestoryRes(var_121_0)
	local var_121_4 = var_121_2 == 0

	if arg_121_0.destroyResList then
		local var_121_5 = (var_121_4 and 1 or 2) + #var_121_3

		arg_121_0.destroyResList:make(function(arg_123_0, arg_123_1, arg_123_2)
			if arg_123_0 == UIItemList.EventUpdate then
				local var_123_0 = ""
				local var_123_1 = 0

				if arg_123_1 == 0 then
					var_123_0, var_123_1 = "Props/gold", var_121_1
				elseif arg_123_1 == 1 then
					if not var_121_4 then
						var_123_0, var_123_1 = "Props/oil", var_121_2
					else
						local var_123_2 = var_121_3[1]

						var_123_0, var_123_1 = Item.getConfigData(var_123_2.id).icon, var_123_2.count
					end
				elseif arg_123_1 > 1 then
					local var_123_3 = var_121_4 and var_121_3[arg_123_1] or var_121_3[arg_123_1 - 1]

					var_123_0, var_123_1 = Item.getConfigData(var_123_3.id).icon, var_123_3.count
				end

				GetImageSpriteFromAtlasAsync(var_123_0, "", arg_123_2:Find("icon"))
				setText(arg_123_2:Find("Text"), "X" .. var_123_1)
			end
		end)
		arg_121_0.destroyResList:align(var_121_5)
	end

	if arg_121_0.destroyPage and arg_121_0.destroyPage:GetLoaded() and arg_121_0.destroyPage:isShowing() then
		arg_121_0.destroyPage:RefreshRes()
	end
end

function var_0_0.setModShip(arg_124_0, arg_124_1)
	arg_124_0.modShip = arg_124_1
end

function var_0_0.updateModAttr(arg_125_0)
	if table.getCount(arg_125_0.selectedIds) == 0 then
		arg_125_0:closeModAttr()
	else
		setActive(arg_125_0.modAttrsTF, true)
		setActive(arg_125_0.bottomTipsText, false)
	end

	local var_125_0 = arg_125_0.contextData.ignoredIds[1]
	local var_125_1 = {}

	for iter_125_0, iter_125_1 in ipairs(arg_125_0.selectedIds) do
		table.insert(var_125_1, arg_125_0.shipVOsById[iter_125_1])
	end

	local var_125_2 = ShipModLayer.getModExpAdditions(arg_125_0.modShip, var_125_1)

	for iter_125_2, iter_125_3 in pairs(ShipModAttr.ID_TO_ATTR) do
		if iter_125_2 ~= ShipModLayer.IGNORE_ID then
			local var_125_3 = arg_125_0.modAttrContainer:Find("attr_" .. iter_125_2)

			setText(var_125_3:Find("value"), var_125_2[iter_125_3])
			setText(var_125_3:Find("name"), ShipModAttr.id2Name(iter_125_2))
		end
	end
end

function var_0_0.closeModAttr(arg_126_0)
	setActive(arg_126_0.modAttrsTF, false)
	setActive(arg_126_0.bottomTipsText, true)
end

function var_0_0.removeShip(arg_127_0, arg_127_1)
	for iter_127_0, iter_127_1 in ipairs(arg_127_0.selectedIds) do
		if iter_127_1 == arg_127_1 then
			table.remove(arg_127_0.selectedIds, iter_127_0)

			break
		end
	end

	for iter_127_2 = #arg_127_0.shipVOs, 1, -1 do
		if arg_127_0.shipVOs[iter_127_2].id == arg_127_1 then
			table.remove(arg_127_0.shipVOs, iter_127_2)

			break
		end
	end

	arg_127_0.shipVOsById[arg_127_1] = nil
end

function var_0_0.updateShipCount(arg_128_0, arg_128_1)
	arg_128_0.shipContainer:SetTotalCount(#arg_128_0.shipVOs, defaultValue(arg_128_1, -1))
	setActive(arg_128_0.listEmptyTF, #arg_128_0.shipVOs <= 0)
end

function var_0_0.ClearShipsBlackBlock(arg_129_0)
	if not arg_129_0.shipVOsById then
		return
	end

	for iter_129_0, iter_129_1 in pairs(arg_129_0.shipVOsById) do
		iter_129_1.blackBlock = false
	end
end

function var_0_0.willExit(arg_130_0)
	arg_130_0:closeDestroyMode()
	arg_130_0:closeModAttr()
	arg_130_0:ClearShipsBlackBlock()

	if arg_130_0.guildShipEquipmentsPage then
		arg_130_0.guildShipEquipmentsPage:Destroy()
	end

	if arg_130_0.settingPanel then
		arg_130_0.settingPanel:Destroy()
	end

	if arg_130_0.destroyPage then
		arg_130_0.destroyPage:Destroy()
	end

	if arg_130_0.destroyConfirmWindow then
		arg_130_0.destroyConfirmWindow:Destroy()
	end

	if arg_130_0.contextData.mode == var_0_0.MODE_MOD then
		-- block empty
	elseif not arg_130_0.contextData.sortData then
		if _G[arg_130_0.contextData.preView] then
			_G[arg_130_0.contextData.preView].sortIndex = arg_130_0.sortIndex
			_G[arg_130_0.contextData.preView].selectAsc = arg_130_0.selectAsc
			_G[arg_130_0.contextData.preView].typeIndex = arg_130_0.typeIndex
			_G[arg_130_0.contextData.preView].campIndex = arg_130_0.campIndex
			_G[arg_130_0.contextData.preView].rarityIndex = arg_130_0.rarityIndex
			_G[arg_130_0.contextData.preView].extraIndex = arg_130_0.extraIndex
			_G[arg_130_0.contextData.preView].commonTag = arg_130_0.commonTag
		else
			DockyardScene.sortIndex = arg_130_0.sortIndex
			DockyardScene.selectAsc = arg_130_0.selectAsc
			DockyardScene.typeIndex = arg_130_0.typeIndex
			DockyardScene.campIndex = arg_130_0.campIndex
			DockyardScene.rarityIndex = arg_130_0.rarityIndex
			DockyardScene.extraIndex = arg_130_0.extraIndex
			DockyardScene.commonTag = arg_130_0.commonTag
		end
	end

	arg_130_0.shipContainer.enabled = false

	for iter_130_0, iter_130_1 in pairs(arg_130_0.scrollItems) do
		iter_130_1:clear()
		GetOrAddComponent(iter_130_1.go, "UILongPressTrigger").onLongPressed:RemoveAllListeners()
	end

	if LeanTween.isTweening(go(arg_130_0.energyDescTF)) then
		setActive(arg_130_0.energyDescTF, false)
		LeanTween.cancel(go(arg_130_0.energyDescTF))
	end

	arg_130_0:cancelAnimating()

	if arg_130_0.isRemouldOrUpgradeMode then
		local var_130_0 = getProxy(SettingsProxy)

		var_130_0:SetDockYardLockBtnFlag(arg_130_0.isFilterLockForMod)
		var_130_0:SetDockYardLevelBtnFlag(arg_130_0.isFilterLevelForMod)
	end

	if arg_130_0.bulinTip then
		arg_130_0.bulinTip:Destroy()

		arg_130_0.bulinTip = nil
	end

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_130_0.blurPanel, arg_130_0._tf)
end

function var_0_0.uiStartAnimating(arg_131_0)
	local var_131_0 = arg_131_0:findTF("back", arg_131_0.topPanel)
	local var_131_1 = 0
	local var_131_2 = 0.3

	if isActive(arg_131_0.selectPanel) then
		shiftPanel(arg_131_0.selectPanel, nil, 0, var_131_2, var_131_1, true, true)
	end
end

function var_0_0.uiExitAnimating(arg_132_0)
	if arg_132_0.contextData.mode == var_0_0.MODE_OVERVIEW then
		-- block empty
	else
		local var_132_0 = 0
		local var_132_1 = 0.3

		shiftPanel(arg_132_0.selectPanel, nil, -1 * arg_132_0.selectPanel.rect.height, var_132_1, var_132_0, true, true)
	end
end

function var_0_0.back(arg_133_0)
	if arg_133_0.exited then
		return
	end

	arg_133_0:closeView()
end

function var_0_0.cancelAnimating(arg_134_0)
	if LeanTween.isTweening(go(arg_134_0.topPanel)) then
		LeanTween.cancel(go(arg_134_0.topPanel))
	end

	if LeanTween.isTweening(go(arg_134_0.selectPanel)) then
		LeanTween.cancel(go(arg_134_0.selectPanel))
	end

	if arg_134_0.tweens then
		cancelTweens(arg_134_0.tweens)
	end
end

function var_0_0.quickExitFunc(arg_135_0)
	seriesAsync({
		function(arg_136_0)
			if arg_135_0.contextData.onQuickHome then
				arg_135_0.contextData.onQuickHome(arg_136_0)
			else
				arg_136_0()
			end
		end,
		function(arg_137_0)
			arg_135_0:emit(var_0_0.ON_HOME)
		end
	})
end

function var_0_0.displayDestroyPanel(arg_138_0)
	arg_138_0.destroyPage:ExecuteAction("Show")
	arg_138_0.destroyPage:ActionInvoke("Refresh", arg_138_0.selectedIds, arg_138_0.shipVOsById)
end

function var_0_0.closeDestroyPanel(arg_139_0)
	if arg_139_0.destroyPage:isShowing() then
		arg_139_0.destroyPage:Hide()
	end
end

function var_0_0.checkDestroyShips(arg_140_0, arg_140_1, arg_140_2)
	local var_140_0 = {}
	local var_140_1, var_140_2 = ShipCalcHelper.GetEliteAndHightLevelShips(arg_140_1)

	if #var_140_1 > 0 or #var_140_2 > 0 then
		table.insert(var_140_0, function(arg_141_0)
			local var_141_0 = false

			if arg_140_0.contextData.mode == var_0_0.MODE_DESTROY then
				var_141_0 = ({
					ShipCalcHelper.CalcDestoryRes(arg_140_1)
				})[4]
			end

			arg_140_0.destroyConfirmWindow:ExecuteAction("Show", var_140_1, var_140_2, var_141_0, arg_141_0)
		end)
	end

	local var_140_3 = underscore.filter(arg_140_1, function(arg_142_0)
		return arg_142_0:getFlag("inElite")
	end)

	if #var_140_3 > 0 then
		table.insert(var_140_0, function(arg_143_0)
			arg_140_0.destroyConfirmWindow:ExecuteAction("ShowEliteTag", var_140_3, arg_143_0)
		end)
	end

	seriesAsync(var_140_0, arg_140_2)
end

return var_0_0

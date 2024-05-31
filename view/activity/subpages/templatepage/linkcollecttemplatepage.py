local var_0_0 = class("LinkCollectTemplatePage", import("view.base.BaseActivityPage"))

var_0_0.DropType2Name = {
	[DROP_TYPE_EQUIP] = "equip",
	[DROP_TYPE_FURNITURE] = "furniture",
	[DROP_TYPE_EQUIPMENT_SKIN] = "equip_skin",
	[DROP_TYPE_SPWEAPON] = "special_weapon"
}

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.btnList = arg_1_0.findTF("btn_list", arg_1_0.bg)
	arg_1_0.itemPanel = arg_1_0.findTF("item_panel", arg_1_0.bg)
	arg_1_0.togglesTF = arg_1_0.findTF("toggles", arg_1_0.itemPanel)
	arg_1_0.content = arg_1_0.findTF("item_list/content", arg_1_0.itemPanel)
	arg_1_0.itemList = UIItemList.New(arg_1_0.content, arg_1_0.findTF("tpl", arg_1_0.content))

	setText(arg_1_0.findTF("tpl/owner/title", arg_1_0.content), i18n("collect_page_got"))

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.guideConfig = pg.activity_limit_item_guide

	arg_2_0.BuildDatas()

def var_0_0.BuildDatas(arg_3_0):
	local var_3_0 = pg.activity_limit_item_guide.get_id_list_by_activity[arg_3_0.activity.id]

	assert(var_3_0, "activity_limit_item_guide not exist activity id. " .. arg_3_0.activity.id)

	arg_3_0.dataList = {}

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		local var_3_1 = {
			id = iter_3_1
		}

		var_3_1.config = arg_3_0.guideConfig[var_3_1.id]
		var_3_1.count = arg_3_0.activity.getKVPList(1, var_3_1.id)

		if var_3_1.config.count_storage == 1:
			var_3_1.count = Drop.New({
				type = var_3_1.config.type,
				id = var_3_1.config.drop_id
			}).getOwnedCount()

		table.insert(arg_3_0.dataList, var_3_1)

def var_0_0.GetTogglesDropTypes(arg_4_0):
	return {
		DROP_TYPE_EQUIP,
		DROP_TYPE_FURNITURE,
		DROP_TYPE_EQUIPMENT_SKIN,
		DROP_TYPE_SPWEAPON
	}

def var_0_0.OnFirstFlush(arg_5_0):
	arg_5_0.itemList.make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate:
			arg_5_0.OnUpdateItem(arg_6_1, arg_6_2))
	arg_5_0.AddTogglesListener()
	arg_5_0.AddSpecialBtnListener()

	arg_5_0.curPage = arg_5_0.curPage or arg_5_0.GetTogglesDropTypes()[1]

	triggerToggle(arg_5_0.toggles[arg_5_0.curPage], True)

def var_0_0.OnUpdateFlush(arg_7_0):
	arg_7_0.BuildDatas()
	arg_7_0.UpdatePage(arg_7_0.curPage)

def var_0_0.AddTogglesListener(arg_8_0):
	arg_8_0.toggles = {}

	local var_8_0 = arg_8_0.GetTogglesDropTypes()

	assert(#var_8_0 == arg_8_0.togglesTF.childCount, "dropType数量与togglesTF子节点数不匹配")

	for iter_8_0, iter_8_1 in ipairs(var_8_0):
		local var_8_1 = arg_8_0.findTF(var_0_0.DropType2Name[iter_8_1], arg_8_0.togglesTF)

		onToggle(arg_8_0, var_8_1, function(arg_9_0)
			if arg_9_0:
				arg_8_0.UpdatePage(iter_8_1), SFX_PANEL)

		arg_8_0.toggles[iter_8_1] = var_8_1

def var_0_0.AddSpecialBtnListener(arg_10_0):
	local var_10_0 = arg_10_0.activity.getConfig("config_client")

	arg_10_0.furnitureThemeBtn = arg_10_0.findTF("furniture_theme", arg_10_0.btnList)

	if arg_10_0.furnitureThemeBtn and var_10_0.furniture_theme_link:
		onButton(arg_10_0, arg_10_0.furnitureThemeBtn, function()
			arg_10_0.DoSkip(var_10_0.furniture_theme_link[1], var_10_0.furniture_theme_link[2]), SFX_PANEL)

	arg_10_0.medalBtn = arg_10_0.findTF("medal", arg_10_0.btnList)

	if arg_10_0.medalBtn and var_10_0.medal_link:
		onButton(arg_10_0, arg_10_0.medalBtn, function()
			arg_10_0.DoSkip(var_10_0.medal_link[1], var_10_0.medal_link[2]), SFX_PANEL)

	arg_10_0.equipSkinBoxBtn = arg_10_0.findTF("equip_skin_box", arg_10_0.btnList)

	if arg_10_0.equipSkinBoxBtn and var_10_0.equipskin_box_link:
		local var_10_1 = Drop.New({
			type = var_10_0.equipskin_box_link.drop_type,
			id = var_10_0.equipskin_box_link.drop_id
		}).getOwnedCount()

		onButton(arg_10_0, arg_10_0.equipSkinBoxBtn, function()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_LIKN_COLLECT_GUIDE,
				show_type = Msgbox4LinkCollectGuide.SHOW_TYPE_NORMAL,
				drop_type = var_10_0.equipskin_box_link.drop_type,
				drop_id = var_10_0.equipskin_box_link.drop_id,
				count = var_10_1,
				skipable_list = var_10_0.equipskin_box_link.list
			}), SFX_PANEL)

def var_0_0.OnUpdateItem(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_0.showDataList[arg_14_1 + 1]
	local var_14_1 = arg_14_0.findTF("icon_mask/icon", arg_14_2)
	local var_14_2 = {
		type = var_14_0.config.type,
		id = var_14_0.config.drop_id
	}

	updateDrop(var_14_1, var_14_2)
	onButton(arg_14_0, var_14_1, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_LIKN_COLLECT_GUIDE,
			show_type = Msgbox4LinkCollectGuide.SHOW_TYPE_LIMIT,
			drop_type = var_14_0.config.type,
			drop_id = var_14_0.config.drop_id,
			count = var_14_0.count,
			count_limit = var_14_0.config.count,
			skipable_list = var_14_0.config.link_params
		}), SFX_PANEL)
	changeToScrollText(arg_14_0.findTF("name_mask/name", arg_14_2), Drop.New({
		type = var_14_0.config.type,
		id = var_14_0.config.drop_id
	}).getName())
	setText(arg_14_0.findTF("owner/number", arg_14_2), var_14_0.count .. "/" .. var_14_0.config.count)

	GetOrAddComponent(arg_14_0.findTF("owner", arg_14_2), typeof(CanvasGroup)).alpha = var_14_0.count == var_14_0.config.count and 0.5 or 1

	setActive(arg_14_0.findTF("got", arg_14_2), var_14_0.count == var_14_0.config.count)
	setActive(arg_14_0.findTF("new", arg_14_2), var_14_0.config.is_new == "1")

def var_0_0.UpdatePage(arg_16_0, arg_16_1):
	arg_16_0.curPage = arg_16_1
	arg_16_0.showDataList = {}

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.dataList):
		if arg_16_0.guideConfig[iter_16_1.id].type == arg_16_1:
			table.insert(arg_16_0.showDataList, iter_16_1)

	table.sort(arg_16_0.showDataList, CompareFuncs({
		function(arg_17_0)
			return arg_17_0.count < arg_17_0.config.count and 0 or 1,
		function(arg_18_0)
			return arg_18_0.config.order,
		function(arg_19_0)
			return arg_19_0.id
	}))
	arg_16_0.itemList.align(#arg_16_0.showDataList)

def var_0_0.DoSkip(arg_20_0, arg_20_1, arg_20_2):
	if arg_20_1 == 2:
		pg.m02.sendNotification(GAME.GO_SCENE, arg_20_2[1], arg_20_2[2] or {})
	elif arg_20_1 == 3:
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = arg_20_2
		})

return var_0_0

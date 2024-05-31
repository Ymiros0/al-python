local var_0_0 = class("TerminalGuardianPage", import("view.base.BaseSubView"))

var_0_0.BIND_LOTTERY_ACT_ID = ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID
var_0_0.config = pg.guardian_template
var_0_0.GUARDIAN_SELECT_CNT = 4

def var_0_0.getUIName(arg_1_0):
	return "TerminalGuardianPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0._tf.name = tostring(OtherworldTerminalLayer.PAGE_GUARDIAN)
	arg_2_0.mainViewTF = arg_2_0.findTF("frame/view")
	arg_2_0.mainViewUIList = UIItemList.New(arg_2_0.findTF("content", arg_2_0.mainViewTF), arg_2_0.findTF("content/tpl", arg_2_0.mainViewTF))
	arg_2_0.selectViewTF = arg_2_0.findTF("frame/select_view")
	arg_2_0.selectBackBtn = arg_2_0.findTF("top/back_btn", arg_2_0.selectViewTF)

	setText(arg_2_0.findTF("top/Text", arg_2_0.selectViewTF), i18n("guardian_select_title"))

	arg_2_0.selectMainTF = arg_2_0.findTF("left", arg_2_0.selectViewTF)
	arg_2_0.selectdIcon = arg_2_0.findTF("icon_bg/Image", arg_2_0.selectMainTF)
	arg_2_0.selectdUnknown = arg_2_0.findTF("icon_bg/unknown", arg_2_0.selectMainTF)
	arg_2_0.selectdName = arg_2_0.findTF("name", arg_2_0.selectMainTF)
	arg_2_0.selectdDesc = arg_2_0.findTF("desc/content/Text", arg_2_0.selectMainTF)
	arg_2_0.selectdSureBtn = arg_2_0.findTF("sure_btn", arg_2_0.selectMainTF)

	setText(arg_2_0.findTF("Text", arg_2_0.selectdSureBtn), i18n("guardian_sure_btn"))

	arg_2_0.selectdCancelBtn = arg_2_0.findTF("cancel_btn", arg_2_0.selectMainTF)

	setText(arg_2_0.findTF("Text", arg_2_0.selectdCancelBtn), i18n("guardian_cancel_btn"))

	arg_2_0.selectdCondition = arg_2_0.findTF("condition", arg_2_0.selectMainTF)
	arg_2_0.selectViewUIList = UIItemList.New(arg_2_0.findTF("right/content", arg_2_0.selectViewTF), arg_2_0.findTF("right/content/tpl", arg_2_0.selectViewTF))

	setText(arg_2_0.findTF("right/content/tpl/active/Text", arg_2_0.selectViewTF), i18n("guardian_active_tip"))

def var_0_0.OnInit(arg_3_0):
	arg_3_0.activity = getProxy(ActivityProxy).getActivityById(var_0_0.BIND_LOTTERY_ACT_ID)

	assert(arg_3_0.activity, "not exist bind lottery act, id" .. var_0_0.BIND_LOTTERY_ACT_ID)
	onButton(arg_3_0, arg_3_0.selectBackBtn, function()
		arg_3_0.CloseSelectView(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.selectdSureBtn, function()
		if #arg_3_0.activeIds >= var_0_0.GUARDIAN_SELECT_CNT:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guardian_sure_limit_tip"))

			return

		table.insert(arg_3_0.activeIds, arg_3_0.selectedId)
		arg_3_0.ChangeActiveIds(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.selectdCancelBtn, function()
		table.removebyvalue(arg_3_0.activeIds, arg_3_0.selectedId)
		arg_3_0.ChangeActiveIds(), SFX_PANEL)
	arg_3_0.InitMainViewUI()
	arg_3_0.InitSelectViewUI()
	arg_3_0.UpdateView()
	arg_3_0.CloseSelectView()

def var_0_0.ChangeActiveIds(arg_7_0):
	arg_7_0.emit(OtherworldTerminalMediator.ON_BUFF_LIST_CHANGE, {
		actId = var_0_0.BIND_LOTTERY_ACT_ID,
		ids = arg_7_0.activeIds
	})

def var_0_0.InitMainViewUI(arg_8_0):
	arg_8_0.mainViewUIList.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = arg_8_0.activeIds[arg_9_1 + 1]
			local var_9_1 = var_9_0 != None

			setActive(arg_8_0.findTF("content", arg_9_2), var_9_1)
			setActive(arg_8_0.findTF("empty", arg_9_2), not var_9_1)

			if var_9_1:
				local var_9_2 = var_0_0.config[var_9_0]

				setText(arg_8_0.findTF("content/name", arg_9_2), var_9_2.guardian_name)
				setText(arg_8_0.findTF("content/desc/content/Text", arg_9_2), var_9_2.guardian_desc)

				local var_9_3 = arg_8_0.findTF("content/icon_mask/Image", arg_9_2)

				GetImageSpriteFromAtlasAsync("shipyardicon/" .. var_9_2.guardian_painting, "", var_9_3, False)

			onButton(arg_8_0, arg_9_2, function()
				arg_8_0.selectedId = var_9_0 or underscore.detect(arg_8_0.allIds, function(arg_11_0)
					return not table.contains(arg_8_0.activeIds, arg_11_0))

				arg_8_0.OpenSelectView(), SFX_PANEL))

def var_0_0.UpdateMainView(arg_12_0):
	arg_12_0.mainViewUIList.align(var_0_0.GUARDIAN_SELECT_CNT)

def var_0_0.InitSelectViewUI(arg_13_0):
	arg_13_0.selectViewUIList.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventInit:
			local var_14_0 = arg_13_0.allIds[arg_14_1 + 1]
			local var_14_1 = var_0_0.config[var_14_0]
			local var_14_2 = arg_13_0.findTF("icon_mask/Image", arg_14_2)

			GetImageSpriteFromAtlasAsync("shipyardicon/" .. var_14_1.guardian_painting, "", var_14_2, True)
			onButton(arg_13_0, arg_14_2, function()
				arg_13_0.selectedId = var_14_0

				arg_13_0.UpdateSelectViewUI(), SFX_PANEL)
		elif arg_14_0 == UIItemList.EventUpdate:
			local var_14_3 = arg_13_0.allIds[arg_14_1 + 1]
			local var_14_4 = var_0_0.config[var_14_3]
			local var_14_5 = table.contains(arg_13_0.unlcokIds, var_14_3)
			local var_14_6 = table.contains(arg_13_0.activeIds, var_14_3)
			local var_14_7 = var_14_4.type == 2 and not var_14_5

			setActive(arg_13_0.findTF("icon_mask/Image", arg_14_2), not var_14_7)
			setActive(arg_13_0.findTF("unknown", arg_14_2), var_14_7)
			setActive(arg_13_0.findTF("lock", arg_14_2), not var_14_5 and not var_14_7)
			setActive(arg_13_0.findTF("active", arg_14_2), var_14_6)
			setActive(arg_13_0.findTF("selected", arg_14_2), var_14_3 == arg_13_0.selectedId))

def var_0_0.UpdateSelectViewUI(arg_16_0):
	local var_16_0 = arg_16_0.selectedId or arg_16_0.allIds[1]
	local var_16_1 = var_0_0.config[var_16_0]
	local var_16_2 = table.contains(arg_16_0.unlcokIds, var_16_0)
	local var_16_3 = table.contains(arg_16_0.activeIds, var_16_0)
	local var_16_4 = var_16_1.type == 2 and not var_16_2

	GetImageSpriteFromAtlasAsync("shipyardicon/" .. var_16_1.guardian_painting, "", arg_16_0.selectdIcon, True)
	setActive(arg_16_0.selectdIcon, not var_16_4)
	setActive(arg_16_0.selectdUnknown, var_16_4)
	setText(arg_16_0.selectdName, var_16_4 and "???" or var_16_1.guardian_name)
	setText(arg_16_0.selectdDesc, var_16_4 and "???" or var_16_1.guardian_desc)

	local var_16_5 = ""

	if var_16_1.type == 1:
		local var_16_6, var_16_7 = ActivityItemPool.GetGuardianLastCount(var_0_0.BIND_LOTTERY_ACT_ID, var_16_0)
		local var_16_8 = var_16_1.guardian_gain[2] - var_16_7

		var_16_5 = string.gsub(var_16_1.guardian_gain_desc, "$1", math.min(var_16_8, var_16_1.guardian_gain[2]))
	elif var_16_1.type == 2:
		var_16_5 = var_16_1.guardian_gain_desc

	setText(arg_16_0.findTF("Text", arg_16_0.selectdCondition), var_16_5)
	setActive(arg_16_0.selectdSureBtn, var_16_2 and not var_16_3)
	setActive(arg_16_0.selectdCancelBtn, var_16_2 and var_16_3)
	setActive(arg_16_0.selectdCondition, not var_16_2)
	arg_16_0.selectViewUIList.align(#arg_16_0.allIds)

def var_0_0.UpdateView(arg_17_0, arg_17_1):
	if arg_17_1:
		arg_17_0.activity = arg_17_1

	arg_17_0.activeIds = _.map(arg_17_0.activity.data2_list, function(arg_18_0)
		return arg_18_0)
	arg_17_0.unlcokIds = ActivityItemPool.GetAllGuardianIdsStatus(var_0_0.BIND_LOTTERY_ACT_ID)
	arg_17_0.allIds = ActivityItemPool.GetAllGuardianIds(var_0_0.BIND_LOTTERY_ACT_ID)

	arg_17_0.UpdateMainView()
	arg_17_0.UpdateSelectViewUI()

def var_0_0.OpenSelectView(arg_19_0):
	setActive(arg_19_0.mainViewTF, False)
	setActive(arg_19_0.selectViewTF, True)
	arg_19_0.UpdateSelectViewUI()

def var_0_0.CloseSelectView(arg_20_0):
	setActive(arg_20_0.mainViewTF, True)
	setActive(arg_20_0.selectViewTF, False)
	arg_20_0.UpdateMainView()

def var_0_0.OnDestroy(arg_21_0):
	return

return var_0_0

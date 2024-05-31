local var_0_0 = class("MailScene", import("view.base.BaseUI"))
local var_0_1 = 592
local var_0_2 = 125
local var_0_3 = 9

def var_0_0.getUIName(arg_1_0):
	return "MailUI"

def var_0_0.ResUISettings(arg_2_0):
	return False

var_0_0.optionsPath = {
	"adapt/top/option"
}

def var_0_0.quickExitFunc(arg_3_0):
	local var_3_0 = {}

	if arg_3_0.proxy.totalExist > MAIL_COUNT_LIMIT:
		table.insert(var_3_0, function(arg_4_0)
			arg_3_0.ShowDoubleConfiremationMsgBox({
				type = MailProxy.MailMessageBoxType.ShowTips,
				content = i18n("warning_mail_max_4", arg_3_0.proxy.totalExist),
				onYes = arg_4_0
			}))

	seriesAsync(var_3_0, function()
		arg_3_0.emit(var_0_0.ON_HOME))

def var_0_0.init(arg_6_0):
	arg_6_0.proxy = getProxy(MailProxy)
	arg_6_0.rtAdapt = arg_6_0._tf.Find("adapt")

	setText(arg_6_0.rtAdapt.Find("top/title"), i18n("mail_title_new"))
	setText(arg_6_0.rtAdapt.Find("top/title/Text"), i18n("mail_title_English"))
	onButton(arg_6_0, arg_6_0.rtAdapt.Find("top/back_btn"), function()
		local var_7_0 = {}

		if arg_6_0.proxy.totalExist > MAIL_COUNT_LIMIT:
			table.insert(var_7_0, function(arg_8_0)
				arg_6_0.ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("warning_mail_max_4", arg_6_0.proxy.totalExist),
					onYes = arg_8_0
				}))

		seriesAsync(var_7_0, function()
			arg_6_0.closeView()), SFX_CANCEL)

	arg_6_0.rtLabels = arg_6_0.rtAdapt.Find("left_length/frame/tagRoot")

	eachChild(arg_6_0.rtLabels, function(arg_10_0)
		local var_10_0

		if arg_10_0.name == "mail":
			toggleName = "mail_mail_page"
		elif arg_10_0.name == "store":
			toggleName = "mail_storeroom_page"
		elif arg_10_0.name == "collection":
			toggleName = "mail_boxroom_page"

		setText(arg_10_0.Find("unSelect/Text"), i18n(toggleName))
		setText(arg_10_0.Find("selected/Text"), i18n(toggleName))
		onToggle(arg_6_0, arg_10_0, function(arg_11_0)
			if arg_11_0:
				arg_6_0.SetPage(arg_10_0.name), SFX_PANEL))

	local var_6_0 = arg_6_0.rtAdapt.Find("main/content/left/head")

	arg_6_0.rightSelect = var_6_0.Find("rightSelect")
	arg_6_0.rtToggles = arg_6_0.rightSelect.Find("toggle")

	eachChild(arg_6_0.rtToggles, function(arg_12_0)
		local var_12_0

		if arg_12_0.name == "btn_all":
			toggleName = "mail_all_page"
		elif arg_12_0.name == "btn_important":
			toggleName = "mail_important_page"
		elif arg_12_0.name == "btn_rare":
			toggleName = "mail_rare_page"

		setText(arg_12_0.Find("unselect/Text"), i18n(toggleName))
		setText(arg_12_0.Find("select/Text"), i18n(toggleName)))
	onToggle(arg_6_0, arg_6_0.rtToggles.Find("btn_all"), function(arg_13_0)
		if arg_13_0:
			if arg_6_0.mailToggle == "all":
				return

			arg_6_0.selectMailId = None

			arg_6_0.UpdateMailList("all", 0), SFX_PANEL)
	onToggle(arg_6_0, arg_6_0.rtToggles.Find("btn_important"), function(arg_14_0)
		if arg_14_0:
			local var_14_0 = {}

			if not arg_6_0.proxy.importantIds:
				table.insert(var_14_0, function(arg_15_0)
					arg_6_0.emit(MailMediator.ON_REQUIRE, "important", arg_15_0))

			seriesAsync(var_14_0, function()
				if arg_6_0.mailToggle == "important":
					return

				arg_6_0.selectMailId = None

				arg_6_0.UpdateMailList("important", 0)), SFX_PANEL)
	onToggle(arg_6_0, arg_6_0.rtToggles.Find("btn_rare"), function(arg_17_0)
		if arg_17_0:
			local var_17_0 = {}

			if not arg_6_0.proxy.rareIds:
				table.insert(var_17_0, function(arg_18_0)
					arg_6_0.emit(MailMediator.ON_REQUIRE, "rare", arg_18_0))

			seriesAsync(var_17_0, function()
				if arg_6_0.mailToggle == "rare":
					return

				arg_6_0.selectMailId = None

				arg_6_0.UpdateMailList("rare", 0)), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtAdapt.Find("top/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("mail_tip")
		}), SFX_PANEL)

	arg_6_0.rtSearch = var_6_0.Find("search")
	arg_6_0.rtCollectionInput = arg_6_0.rtSearch.Find("input/InputField")

	setText(arg_6_0.rtCollectionInput.Find("Placeholder"), i18n("mail_search_new"))
	onInputEndEdit(arg_6_0, arg_6_0.rtCollectionInput, function()
		arg_6_0.collectionFilterStr = getInputText(arg_6_0.rtCollectionInput)

		if arg_6_0.mailToggle == "collection":
			arg_6_0.UpdateMailList(arg_6_0.mailToggle, 0))

	arg_6_0.collectionFilterStr = ""
	arg_6_0.rtToggleCollectionSort = arg_6_0.rtSearch.Find("sort")

	setText(arg_6_0.rtToggleCollectionSort.Find("Text"), i18n("mail_receive_time"))
	onToggle(arg_6_0, arg_6_0.rtToggleCollectionSort, function(arg_22_0)
		arg_6_0.collectionSortToggle = arg_22_0

		if arg_6_0.mailToggle == "collection":
			arg_6_0.UpdateMailList(arg_6_0.mailToggle, 0), SFX_PANEL)
	triggerToggle(arg_6_0.rtToggleCollectionSort, False)

	local var_6_1 = arg_6_0.rtAdapt.Find("main/content")

	arg_6_0.rtMailLeft = var_6_1.Find("left/left_content")
	arg_6_0.rtTip = arg_6_0.rtMailLeft.Find("top/tip")
	arg_6_0.rtMailCount = arg_6_0.rtMailLeft.Find("top/count")
	arg_6_0.Scrollbar = arg_6_0.rtMailLeft.Find("middle/Scrollbar").GetComponent("Scrollbar")
	arg_6_0.lsrMailList = arg_6_0.rtMailLeft.Find("middle/container").GetComponent("LScrollRect")

	function arg_6_0.lsrMailList.onUpdateItem(arg_23_0, arg_23_1)
		arg_23_0 = arg_23_0 + 1

		local var_23_0 = tf(arg_23_1)
		local var_23_1 = arg_6_0.filterMails[arg_23_0]

		if var_23_1.id == 0:
			GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).alpha = 0
			GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).blocksRaycasts = False

			arg_6_0.RequrereNextToIndex(arg_23_0)

			return

		if arg_6_0.tplMailDic[var_23_0]:
			arg_6_0.mailTplDic[arg_6_0.tplMailDic[var_23_0]] = None

		arg_6_0.mailTplDic[var_23_1.id] = var_23_0
		arg_6_0.tplMailDic[var_23_0] = var_23_1.id

		onToggle(arg_6_0, var_23_0, function(arg_24_0)
			if arg_24_0:
				if arg_6_0.selectMailId != var_23_1.id:
					arg_6_0.UpdateMailContent(var_23_1)
			elif var_23_1.id == arg_6_0.selectMailId:
				arg_6_0.UpdateMailContent(None), SFX_PANEL)

		GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).alpha = 1
		GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).blocksRaycasts = True

		arg_6_0.UpdateMailTpl(var_23_1)

	arg_6_0.mailTplDic = {}
	arg_6_0.tplMailDic = {}
	arg_6_0.rtBtnLeftManager = arg_6_0.rtMailLeft.Find("bottom/btn_managerMail")

	onButton(arg_6_0, arg_6_0.rtBtnLeftManager, function()
		arg_6_0.mailMgrSubView.ExecuteAction("Show"), SFX_PANEL)

	arg_6_0.rtBtnLeftDeleteAll = arg_6_0.rtMailLeft.Find("bottom/btn_deleteMail")

	onButton(arg_6_0, arg_6_0.rtBtnLeftDeleteAll, function()
		seriesAsync({
			function(arg_27_0)
				arg_6_0.ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("main_mailLayer_quest_clear"),
					onYes = arg_27_0
				})
		}, function()
			arg_6_0.emit(MailMediator.ON_OPERATION, {
				cmd = "delete",
				filter = {
					type = "all"
				}
			})), SFX_CANCEL)

	arg_6_0.rtBtnLeftMoveAll = arg_6_0.rtMailLeft.Find("bottom/btn_moveAll")

	onButton(arg_6_0, arg_6_0.rtBtnLeftMoveAll, function()
		seriesAsync({
			function(arg_30_0)
				arg_6_0.ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_moveto_markroom_2"),
					onYes = arg_30_0
				})
		}, function()
			arg_6_0.emit(MailMediator.ON_OPERATION, {
				cmd = "move",
				filter = {
					type = "ids",
					list = underscore.rest(arg_6_0.proxy.importantIds, 1)
				}
			})), SFX_CANCEL)

	arg_6_0.rtBtnLeftGetAll = arg_6_0.rtMailLeft.Find("bottom/btn_getAll")

	onButton(arg_6_0, arg_6_0.rtBtnLeftGetAll, function()
		local var_32_0 = {}

		if arg_6_0.mailToggle == "important":
			var_32_0 = underscore.rest(arg_6_0.proxy.importantIds, 1)
		elif arg_6_0.mailToggle == "rare":
			var_32_0 = underscore.rest(arg_6_0.proxy.rareIds, 1)
		else
			assert(False)

		arg_6_0.emit(MailMediator.ON_OPERATION, {
			cmd = "attachment",
			filter = {
				type = "ids",
				list = var_32_0
			}
		}), SFX_CANCEL)

	arg_6_0.rtBtnLeftDeleteCollection = arg_6_0.rtMailLeft.Find("bottom/btn_deleteCollection")

	onButton(arg_6_0, arg_6_0.rtBtnLeftDeleteCollection, function()
		if not arg_6_0.selectMailId:
			return

		assert(arg_6_0.selectMailId)

		local var_33_0 = arg_6_0.proxy.getCollecitonMail(arg_6_0.selectMailId)

		seriesAsync({
			function(arg_34_0)
				arg_6_0.ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_markroom_delete", var_33_0.title),
					onYes = arg_34_0
				})
		}, function()
			arg_6_0.emit(MailMediator.ON_DELETE_COLLECTION, arg_6_0.selectMailId)), SFX_CANCEL)

	arg_6_0.rtMailRight = var_6_1.Find("right")
	arg_6_0.rtBtnRightMove = arg_6_0.rtMailRight.Find("bottom/btn_move")

	onButton(arg_6_0, arg_6_0.rtBtnRightMove, function()
		assert(arg_6_0.selectMailId)
		seriesAsync({
			function(arg_37_0)
				arg_6_0.ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_moveto_markroom_1"),
					onYes = arg_37_0
				})
		}, function()
			arg_6_0.emit(MailMediator.ON_OPERATION, {
				noAttachTip = True,
				cmd = "move",
				filter = {
					type = "ids",
					list = {
						arg_6_0.selectMailId
					}
				}
			})), SFX_PANEL)

	arg_6_0.rtBtnRightGet = arg_6_0.rtMailRight.Find("bottom/btn_get")

	onButton(arg_6_0, arg_6_0.rtBtnRightGet, function()
		assert(arg_6_0.selectMailId)
		arg_6_0.emit(MailMediator.ON_OPERATION, {
			noAttachTip = True,
			cmd = "attachment",
			filter = {
				type = "ids",
				list = {
					arg_6_0.selectMailId
				}
			}
		}), SFX_PANEL)

	arg_6_0.rtMailEmpty = var_6_1.Find("empty")
	arg_6_0.rtStore = var_6_1.Find("store")
	arg_6_0.mailMgrSubView = MailMgrWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.storeUpgradeSubView = StoreUpgradeWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.mailConfirmationSubView = MailConfirmationWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.mailOverflowWindowSubView = MailOverflowWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)

	setText(arg_6_0.rtBtnLeftDeleteAll.Find("Text"), i18n("mail_deleteread_button"))
	setText(arg_6_0.rtBtnLeftManager.Find("Text"), i18n("mail_manage_button"))
	setText(arg_6_0.rtBtnLeftMoveAll.Find("Text"), i18n("mail_move_button"))
	setText(arg_6_0.rtBtnLeftGetAll.Find("Text"), i18n("mail_get_oneclick"))
	setText(arg_6_0.rtBtnLeftDeleteCollection.Find("Text"), i18n("mail_delet_button"))
	setText(arg_6_0.rtBtnRightMove.Find("Text"), i18n("mail_moveone_button"))
	setText(arg_6_0.rtBtnRightGet.Find("Text"), i18n("mail_getone_button"))
	setText(arg_6_0.rtMailRight.Find("main/title/matter/on/Text"), i18n("mail_toggle_on"))
	setText(arg_6_0.rtMailRight.Find("main/title/matter/off/Text"), i18n("mail_toggle_off"))
	arg_6_0.InitResBar()

def var_0_0.SetPage(arg_40_0, arg_40_1):
	if arg_40_0.page == arg_40_1:
		return

	arg_40_0.page = arg_40_1

	setActive(arg_40_0.rightSelect, arg_40_1 == "mail")
	setActive(arg_40_0.rtSearch, arg_40_1 == "collection")
	setActive(arg_40_0.rtStore, arg_40_1 == "store")

	if arg_40_1 == "store":
		setActive(arg_40_0.rtMailEmpty, False)
		setActive(arg_40_0.rtMailLeft, False)
		setActive(arg_40_0.rtMailRight, False)

		arg_40_0.mailToggle = None

		arg_40_0.UpdateStore()
		setText(arg_40_0.rtTip, i18n("mail_storeroom_tips"))
	elif arg_40_1 == "mail":
		triggerToggle(arg_40_0.rtToggles.Find("btn_all"), True)
		setText(arg_40_0.rtTip, i18n("warning_mail_max_5"))
	elif arg_40_1 == "collection":
		local var_40_0 = {}

		if not arg_40_0.proxy.collectionIds:
			table.insert(var_40_0, function(arg_41_0)
				arg_40_0.emit(MailMediator.ON_REQUIRE, "collection", arg_41_0))

		seriesAsync(var_40_0, function()
			arg_40_0.selectMailId = None

			arg_40_0.UpdateMailList("collection", 0))
		setText(arg_40_0.rtTip, i18n("mail_markroom_tip"))

def var_0_0.didEnter(arg_43_0):
	onNextTick(function()
		arg_43_0.lsrMailList.enabled = True

		triggerToggle(arg_43_0.rtLabels.Find("mail"), True))

def var_0_0.RequrereNextToIndex(arg_45_0, arg_45_1):
	if arg_45_0.mailToggle == "all" and not arg_45_0.inRequire and #arg_45_0.proxy.ids < arg_45_0.proxy.totalExist and arg_45_1 > #arg_45_0.proxy.ids:
		arg_45_0.inRequire = True

		pg.UIMgr.GetInstance().LoadingOn()
		arg_45_0.emit(MailMediator.ON_REQUIRE, arg_45_1, function()
			arg_45_0.inRequire = None

			if arg_45_0.mailToggle == "all":
				arg_45_0.UpdateMailList(arg_45_0.mailToggle)

			pg.UIMgr.GetInstance().LoadingOff())

def var_0_0.UpdateMailList(arg_47_0, arg_47_1, arg_47_2):
	arg_47_0.mailToggle = arg_47_1

	local var_47_0, var_47_1 = switch(arg_47_1, {
		def all:()
			return arg_47_0.proxy.ids, string.format("<color=%s>%d</color>/<color=%s>%d</color>", arg_47_0.proxy.totalExist > MAIL_COUNT_LIMIT and COLOR_RED or COLOR_WHITE, arg_47_0.proxy.totalExist, "#181E32", MAIL_COUNT_LIMIT),
		def important:()
			return arg_47_0.proxy.importantIds, string.format("<color=#FFFFFF>%d</color>", #arg_47_0.proxy.importantIds),
		def rare:()
			return arg_47_0.proxy.rareIds, string.format("<color=#FFFFFF>%d</color>", #arg_47_0.proxy.rareIds),
		def collection:()
			return arg_47_0.proxy.collectionIds, string.format("<color=#FFFFFF>%d</color>/%d", #arg_47_0.proxy.collectionIds, getProxy(PlayerProxy).getRawData().getConfig("max_markmail"))
	})

	if arg_47_1 == "collection":
		arg_47_0.filterMails = arg_47_0.proxy.GetCollectionMails(var_47_0)

		if arg_47_0.collectionFilterStr:
			arg_47_0.filterMails = underscore.filter(arg_47_0.filterMails, function(arg_52_0)
				return arg_52_0.IsMatchKey(arg_47_0.collectionFilterStr))

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_53_0)
				return (arg_47_0.collectionSortToggle and 1 or -1) * arg_53_0.id
		}))
	elif arg_47_1 == "all":
		arg_47_0.filterMails = arg_47_0.proxy.GetMails(var_47_0)

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_54_0)
				return -arg_54_0.id
		}))

		for iter_47_0 = #var_47_0 + 1, arg_47_0.proxy.totalExist:
			table.insert(arg_47_0.filterMails, {
				id = 0
			})
	else
		arg_47_0.filterMails = arg_47_0.proxy.GetMails(var_47_0)

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_55_0)
				return -arg_55_0.id
		}))

	if arg_47_0.mailToggle == "all" and #arg_47_0.proxy.ids < arg_47_0.proxy.totalExist and #arg_47_0.proxy.ids < SINGLE_MAIL_REQUIRE_SIZE:
		arg_47_0.inRequire = True

		arg_47_0.emit(MailMediator.ON_REQUIRE, "next", function()
			if arg_47_0.mailToggle == "all":
				arg_47_0.UpdateMailList(arg_47_0.mailToggle)

			arg_47_0.inRequire = None)
	elif #arg_47_0.filterMails == 0:
		setActive(arg_47_0.rtMailLeft, False)
		setActive(arg_47_0.rtMailRight, False)
		setActive(arg_47_0.rtMailEmpty, True)

		if arg_47_0.mailToggle == "collection":
			setText(arg_47_0.rtMailEmpty.Find("Text"), i18n("emptymarkroom_tip_mailboxui"))
			setText(arg_47_0.rtMailEmpty.Find("Text_en"), i18n("emptymarkroom_tip_mailboxui_en"))
		else
			setText(arg_47_0.rtMailEmpty.Find("Text"), i18n("empty_tip_mailboxui"))
			setText(arg_47_0.rtMailEmpty.Find("Text_en"), i18n("empty_tip_mailboxui_en"))
	else
		setActive(arg_47_0.rtMailLeft, True)
		setActive(arg_47_0.rtMailRight, True)
		setActive(arg_47_0.rtMailEmpty, False)

		if not arg_47_0.selectMailId:
			arg_47_0.UpdateMailContent(arg_47_0.filterMails[1])

		arg_47_0.lsrMailList.SetTotalCount(#arg_47_0.filterMails, arg_47_2 or -1)
		setText(arg_47_0.rtMailCount, var_47_1)
		setActive(arg_47_0.rtBtnLeftManager, arg_47_0.mailToggle == "all")
		setActive(arg_47_0.rtBtnLeftMoveAll, arg_47_0.mailToggle == "important")
		setActive(arg_47_0.rtBtnLeftDeleteCollection, arg_47_0.mailToggle == "collection")
		setActive(arg_47_0.rtBtnLeftDeleteAll, arg_47_0.mailToggle == "all" or arg_47_0.mailToggle == "rare")
		setActive(arg_47_0.rtBtnLeftGetAll, arg_47_0.mailToggle == "important" or arg_47_0.mailToggle == "rare")

def var_0_0.UpdateMailTpl(arg_57_0, arg_57_1):
	local var_57_0 = arg_57_0.mailTplDic[arg_57_1.id]

	if not var_57_0:
		return

	local var_57_1 = var_57_0.Find("content")

	setActive(var_57_1.Find("icon/no_attachment"), #arg_57_1.attachments == 0)
	setActive(var_57_1.Find("icon/IconTpl"), #arg_57_1.attachments > 0)

	if #arg_57_1.attachments > 0:
		updateDrop(var_57_1.Find("icon/IconTpl"), arg_57_1.attachments[1])

	setText(var_57_1.Find("info/title/Text"), shortenString(arg_57_1.title, 10))
	setActive(var_57_1.Find("info/title/mark"), arg_57_1.importantFlag and arg_57_0.mailToggle != "collection")
	setText(var_57_1.Find("info/time/Text"), os.date("%Y-%m-%d", arg_57_1.date))
	setActive(var_57_1.Find("info/time/out_time"), False)

	local var_57_2 = #arg_57_1.attachments > 0 and arg_57_1.attachFlag

	setActive(var_57_0.Find("got_mark"), arg_57_0.mailToggle != "collection" and var_57_2)
	setText(var_57_0.Find("got_mark/got_text"), i18n("mail_reward_got"))
	triggerToggle(var_57_0, arg_57_0.selectMailId == arg_57_1.id)

	local var_57_3 = arg_57_1.readFlag or arg_57_0.mailToggle == "collection"

	setActive(var_57_0.Find("hasread_bg"), var_57_3)
	setActive(var_57_0.Find("noread_bg"), not var_57_3)

	local var_57_4 = SummerFeastScene.TransformColor(var_57_3 and "FFFFFF" or "181E32")

	setTextColor(var_57_1.Find("info/title/Text"), var_57_4)
	setTextColor(var_57_1.Find("info/time/Text"), var_57_4)

def var_0_0.UpdateMailContent(arg_58_0, arg_58_1):
	eachChild(arg_58_0.rtMailRight, function(arg_59_0)
		setActive(arg_59_0, tobool(arg_58_1)))

	if not arg_58_1:
		arg_58_0.selectMailId = None

		return

	arg_58_0.selectMailId = arg_58_1.id

	changeToScrollText(arg_58_0.rtMailRight.Find("main/title/info/Text"), i18n2(arg_58_1.title))
	setText(arg_58_0.rtMailRight.Find("main/from/Text"), arg_58_1.sender)
	setText(arg_58_0.rtMailRight.Find("main/time/Text"), os.date("%Y-%m-%d", arg_58_1.date))
	setText(arg_58_0.rtMailRight.Find("main/view/content/text/Text"), arg_58_1.content)

	local var_58_0 = arg_58_0.rtMailRight.Find("main/title/matter")

	setActive(var_58_0, arg_58_0.mailToggle != "collection")

	if arg_58_0.mailToggle != "collection":
		onToggle(arg_58_0, arg_58_0.rtMailRight.Find("main/title/matter"), function(arg_60_0)
			if arg_60_0 != arg_58_1.importantFlag:
				arg_58_0.emit(MailMediator.ON_OPERATION, {
					cmd = arg_60_0 and "important" or "unimportant",
					filter = {
						type = "ids",
						list = {
							arg_58_1.id
						}
					}
				}), SFX_CONFIRM)
		triggerToggle(arg_58_0.rtMailRight.Find("main/title/matter"), arg_58_1.importantFlag)

	local var_58_1 = arg_58_0.rtMailRight.Find("main/view/content/attachment")

	setText(var_58_1.Find("got/Text"), i18n("main_mailLayer_attachTaken"))
	setActive(var_58_1, #arg_58_1.attachments > 0)

	if #arg_58_1.attachments > 0:
		local var_58_2 = var_58_1.Find("content")

		UIItemList.StaticAlign(var_58_2, var_58_2.Find("IconTpl"), #arg_58_1.attachments, function(arg_61_0, arg_61_1, arg_61_2)
			arg_61_1 = arg_61_1 + 1

			if arg_61_0 == UIItemList.EventUpdate:
				local var_61_0 = arg_58_1.attachments[arg_61_1]

				updateDrop(arg_61_2, var_61_0)
				onButton(arg_58_0, arg_61_2, function()
					arg_58_0.emit(var_0_0.ON_DROP, var_61_0), SFX_PANEL))

		local var_58_3 = arg_58_0.mailToggle == "collection" or arg_58_1.attachFlag

		setCanvasGroupAlpha(var_58_2, var_58_3 and 0.5 or 1)
		setActive(var_58_1.Find("got"), var_58_3)

	setActive(arg_58_0.rtBtnRightMove, arg_58_0.mailToggle != "collection")
	setActive(arg_58_0.rtBtnRightGet, arg_58_0.mailToggle != "collection" and not arg_58_1.attachFlag)

	if arg_58_0.mailToggle != "collection" and not arg_58_1.readFlag:
		arg_58_0.emit(MailMediator.ON_OPERATION, {
			cmd = "read",
			ignoreTips = True,
			filter = {
				type = "ids",
				list = {
					arg_58_1.id
				}
			}
		})

def var_0_0.UpdateOperationDeal(arg_63_0, arg_63_1, arg_63_2, arg_63_3):
	if #arg_63_2 == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("mail_manage_3"))
	elif not arg_63_3:
		local var_63_0 = switch(arg_63_1, {
			def delete:()
				return i18n("main_mailMediator_mailDelete"),
			def attachment:()
				return i18n("main_mailMediator_attachTaken"),
			def read:()
				return i18n("main_mailMediator_mailread"),
			def move:()
				return i18n("main_mailMediator_mailmove")
		})

		if var_63_0:
			pg.TipsMgr.GetInstance().ShowTips(var_63_0)

	local var_63_1 = {}

	for iter_63_0, iter_63_1 in ipairs(arg_63_2):
		var_63_1[iter_63_1] = True

	arg_63_0.UpdateMailList(arg_63_0.mailToggle)

	if var_63_1[arg_63_0.selectMailId]:
		arg_63_0.UpdateMailContent(underscore.detect(arg_63_0.filterMails, function(arg_68_0)
			return arg_68_0.id == arg_63_0.selectMailId))

def var_0_0.UpdateCollectionDelete(arg_69_0, arg_69_1):
	arg_69_0.UpdateMailList(arg_69_0.mailToggle)

	if arg_69_0.selectMailId == arg_69_1:
		arg_69_0.UpdateMailContent(None)

def var_0_0.UpdateStore(arg_70_0):
	arg_70_0.withdrawal = {
		gold = 0,
		oil = 0
	}

	local var_70_0 = getProxy(PlayerProxy).getRawData()
	local var_70_1 = pg.mail_storeroom[var_70_0.mailStoreLevel]

	setText(arg_70_0.rtStore.Find("gold/Text/count"), string.format("%d/%d", var_70_0.getResource(PlayerConst.ResStoreGold), var_70_1.gold_store))

	local var_70_2 = var_70_0.IsStoreLevelMax()
	local var_70_3 = arg_70_0.rtStore.Find("bottom/btn_extend")

	SetActive(var_70_3, not var_70_2)
	onButton(arg_70_0, var_70_3, function()
		if var_70_2:
			pg.TipsMgr.GetInstance().ShowTips(i18n("mail_storeroom_noextend"))
		else
			arg_70_0.storeUpgradeSubView.ExecuteAction("Show"), SFX_PANEL)

	local var_70_4 = arg_70_0.rtStore.Find("bottom/btn_get")

	onButton(arg_70_0, var_70_4, function()
		arg_70_0.emit(MailMediator.ON_WITHDRAWAL, arg_70_0.withdrawal), SFX_CONFIRM)

	local function var_70_5()
		local var_73_0 = arg_70_0.withdrawal.oil != 0 or arg_70_0.withdrawal.gold != 0

		setButtonEnabled(var_70_4, var_73_0)
		setGray(var_70_4, not var_73_0)

	var_70_5()

	for iter_70_0, iter_70_1 in pairs({
		{
			"oil",
			PlayerConst.ResOil,
			PlayerConst.ResStoreOil,
			"#0173FF",
			"max_oil"
		},
		{
			"gold",
			PlayerConst.ResGold,
			PlayerConst.ResStoreGold,
			"#FF9C01",
			"max_gold"
		}
	}):
		local var_70_6, var_70_7, var_70_8, var_70_9, var_70_10 = unpack(iter_70_1)
		local var_70_11 = pg.gameset[var_70_10].key_value - var_70_0.getResource(var_70_7)
		local var_70_12 = math.max(var_70_11, 0)
		local var_70_13 = var_70_0.getResource(var_70_8)

		setText(arg_70_0.rtStore.Find(var_70_6 .. "/tips"), i18n("mail_reward_tips"))
		setText(arg_70_0.rtStore.Find(var_70_6 .. "/Text/count"), string.format("<color=%s>%d</color>/%d", var_70_9, var_70_13, var_70_1[var_70_6 .. "_store"]))

		local var_70_14 = arg_70_0.rtStore.Find(var_70_6 .. "/calc")
		local var_70_15 = var_70_14.Find("count/count")

		setText(var_70_15.Find("tip"), i18n("mail_storeroom_resourcetaken"))
		setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])
		onInputEndEdit(arg_70_0, var_70_15, function()
			local var_74_0 = getInputText(var_70_15)

			if var_74_0 == "" or var_74_0 == None:
				var_74_0 = 0

			local var_74_1 = math.clamp(tonumber(var_74_0), 0, var_70_13)

			if var_74_1 >= var_70_12:
				var_74_1 = var_70_12

				pg.TipsMgr.GetInstance().ShowTips(i18n("resource_max_tip_storeroom"))

			if arg_70_0.withdrawal[var_70_6] != var_74_1:
				arg_70_0.withdrawal[var_70_6] = var_74_1

				var_70_5()

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6]))
		pressPersistTrigger(var_70_14.Find("count/left"), 0.5, function()
			if arg_70_0.withdrawal[var_70_6] == 0:
				return

			arg_70_0.withdrawal[var_70_6] = math.max(arg_70_0.withdrawal[var_70_6] - 100, 0)

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])

			if arg_70_0.withdrawal[var_70_6] == 0:
				var_70_5(), None, True, True, 0.15, SFX_PANEL)
		pressPersistTrigger(var_70_14.Find("count/right"), 0.5, function()
			if arg_70_0.withdrawal[var_70_6] >= var_70_12:
				pg.TipsMgr.GetInstance().ShowTips(i18n("resource_max_tip_storeroom"))

				return

			if arg_70_0.withdrawal[var_70_6] == var_70_13:
				return

			local var_76_0 = arg_70_0.withdrawal[var_70_6]

			arg_70_0.withdrawal[var_70_6] = math.min(arg_70_0.withdrawal[var_70_6] + 100, var_70_13)

			if arg_70_0.withdrawal[var_70_6] >= var_70_12:
				arg_70_0.withdrawal[var_70_6] = var_70_12

				pg.TipsMgr.GetInstance().ShowTips(i18n("resource_max_tip_storeroom"))

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])

			if var_76_0 == 0:
				var_70_5(), None, True, True, 0.15, SFX_PANEL)
		onButton(arg_70_0, var_70_14.Find("max"), function()
			arg_70_0.withdrawal[var_70_6] = getProxy(PlayerProxy).getRawData().ResLack(var_70_6, var_70_13)

			if arg_70_0.withdrawal[var_70_6] >= var_70_12:
				arg_70_0.withdrawal[var_70_6] = var_70_12

				pg.TipsMgr.GetInstance().ShowTips(i18n("resource_max_tip_storeroom"))

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])
			var_70_5(), SFX_PANEL)

def var_0_0.onBackPressed(arg_78_0):
	if arg_78_0.mailMgrSubView.isShowing():
		arg_78_0.mailMgrSubView.Hide()
	elif arg_78_0.storeUpgradeSubView.isShowing():
		arg_78_0.storeUpgradeSubView.Hide()
	elif arg_78_0.mailConfirmationSubView.isShowing():
		arg_78_0.mailConfirmationSubView.Hide()
	elif arg_78_0.mailOverflowWindowSubView.isShowing():
		arg_78_0.mailOverflowWindowSubView.Hide()
	else
		triggerButton(arg_78_0.rtAdapt.Find("top/back_btn"))

def var_0_0.willExit(arg_79_0):
	arg_79_0.mailMgrSubView.Destroy()
	arg_79_0.storeUpgradeSubView.Destroy()
	arg_79_0.mailConfirmationSubView.Destroy()
	arg_79_0.mailOverflowWindowSubView.Destroy()

def var_0_0.ShowDoubleConfiremationMsgBox(arg_80_0, arg_80_1):
	if arg_80_1.type == MailProxy.MailMessageBoxType.OverflowConfirm:
		arg_80_0.mailOverflowWindowSubView.ExecuteAction("Show", arg_80_1)
	else
		arg_80_0.mailConfirmationSubView.ExecuteAction("Show", arg_80_1)

def var_0_0.InitResBar(arg_81_0):
	arg_81_0.resBar = arg_81_0._tf.Find("adapt/top/res")
	arg_81_0.goldMax = arg_81_0.resBar.Find("gold/max").GetComponent(typeof(Text))
	arg_81_0.goldValue = arg_81_0.resBar.Find("gold/Text").GetComponent(typeof(Text))
	arg_81_0.oilMax = arg_81_0.resBar.Find("oil/max").GetComponent(typeof(Text))
	arg_81_0.oilValue = arg_81_0.resBar.Find("oil/Text").GetComponent(typeof(Text))
	arg_81_0.gemValue = arg_81_0.resBar.Find("gem/Text").GetComponent(typeof(Text))

	onButton(arg_81_0, arg_81_0.resBar.Find("gold"), function()
		pg.playerResUI.ClickGold(), SFX_PANEL)
	onButton(arg_81_0, arg_81_0.resBar.Find("oil"), function()
		pg.playerResUI.ClickOil(), SFX_PANEL)
	onButton(arg_81_0, arg_81_0.resBar.Find("gem"), function()
		pg.playerResUI.ClickGem(), SFX_PANEL)
	arg_81_0.UpdateRes()

def var_0_0.UpdateRes(arg_85_0):
	local var_85_0 = getProxy(PlayerProxy).getRawData()

	PlayerResUI.StaticFlush(var_85_0, arg_85_0.goldMax, arg_85_0.goldValue, arg_85_0.oilMax, arg_85_0.oilValue, arg_85_0.gemValue)

return var_0_0

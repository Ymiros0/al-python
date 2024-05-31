local var_0_0 = class("MailScene", import("view.base.BaseUI"))
local var_0_1 = 592
local var_0_2 = 125
local var_0_3 = 9

function var_0_0.getUIName(arg_1_0)
	return "MailUI"
end

function var_0_0.ResUISettings(arg_2_0)
	return false
end

var_0_0.optionsPath = {
	"adapt/top/option"
}

function var_0_0.quickExitFunc(arg_3_0)
	local var_3_0 = {}

	if arg_3_0.proxy.totalExist > MAIL_COUNT_LIMIT then
		table.insert(var_3_0, function(arg_4_0)
			arg_3_0:ShowDoubleConfiremationMsgBox({
				type = MailProxy.MailMessageBoxType.ShowTips,
				content = i18n("warning_mail_max_4", arg_3_0.proxy.totalExist),
				onYes = arg_4_0
			})
		end)
	end

	seriesAsync(var_3_0, function()
		arg_3_0:emit(var_0_0.ON_HOME)
	end)
end

function var_0_0.init(arg_6_0)
	arg_6_0.proxy = getProxy(MailProxy)
	arg_6_0.rtAdapt = arg_6_0._tf:Find("adapt")

	setText(arg_6_0.rtAdapt:Find("top/title"), i18n("mail_title_new"))
	setText(arg_6_0.rtAdapt:Find("top/title/Text"), i18n("mail_title_English"))
	onButton(arg_6_0, arg_6_0.rtAdapt:Find("top/back_btn"), function()
		local var_7_0 = {}

		if arg_6_0.proxy.totalExist > MAIL_COUNT_LIMIT then
			table.insert(var_7_0, function(arg_8_0)
				arg_6_0:ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("warning_mail_max_4", arg_6_0.proxy.totalExist),
					onYes = arg_8_0
				})
			end)
		end

		seriesAsync(var_7_0, function()
			arg_6_0:closeView()
		end)
	end, SFX_CANCEL)

	arg_6_0.rtLabels = arg_6_0.rtAdapt:Find("left_length/frame/tagRoot")

	eachChild(arg_6_0.rtLabels, function(arg_10_0)
		local var_10_0

		if arg_10_0.name == "mail" then
			toggleName = "mail_mail_page"
		elseif arg_10_0.name == "store" then
			toggleName = "mail_storeroom_page"
		elseif arg_10_0.name == "collection" then
			toggleName = "mail_boxroom_page"
		end

		setText(arg_10_0:Find("unSelect/Text"), i18n(toggleName))
		setText(arg_10_0:Find("selected/Text"), i18n(toggleName))
		onToggle(arg_6_0, arg_10_0, function(arg_11_0)
			if arg_11_0 then
				arg_6_0:SetPage(arg_10_0.name)
			end
		end, SFX_PANEL)
	end)

	local var_6_0 = arg_6_0.rtAdapt:Find("main/content/left/head")

	arg_6_0.rightSelect = var_6_0:Find("rightSelect")
	arg_6_0.rtToggles = arg_6_0.rightSelect:Find("toggle")

	eachChild(arg_6_0.rtToggles, function(arg_12_0)
		local var_12_0

		if arg_12_0.name == "btn_all" then
			toggleName = "mail_all_page"
		elseif arg_12_0.name == "btn_important" then
			toggleName = "mail_important_page"
		elseif arg_12_0.name == "btn_rare" then
			toggleName = "mail_rare_page"
		end

		setText(arg_12_0:Find("unselect/Text"), i18n(toggleName))
		setText(arg_12_0:Find("select/Text"), i18n(toggleName))
	end)
	onToggle(arg_6_0, arg_6_0.rtToggles:Find("btn_all"), function(arg_13_0)
		if arg_13_0 then
			if arg_6_0.mailToggle == "all" then
				return
			end

			arg_6_0.selectMailId = nil

			arg_6_0:UpdateMailList("all", 0)
		end
	end, SFX_PANEL)
	onToggle(arg_6_0, arg_6_0.rtToggles:Find("btn_important"), function(arg_14_0)
		if arg_14_0 then
			local var_14_0 = {}

			if not arg_6_0.proxy.importantIds then
				table.insert(var_14_0, function(arg_15_0)
					arg_6_0:emit(MailMediator.ON_REQUIRE, "important", arg_15_0)
				end)
			end

			seriesAsync(var_14_0, function()
				if arg_6_0.mailToggle == "important" then
					return
				end

				arg_6_0.selectMailId = nil

				arg_6_0:UpdateMailList("important", 0)
			end)
		end
	end, SFX_PANEL)
	onToggle(arg_6_0, arg_6_0.rtToggles:Find("btn_rare"), function(arg_17_0)
		if arg_17_0 then
			local var_17_0 = {}

			if not arg_6_0.proxy.rareIds then
				table.insert(var_17_0, function(arg_18_0)
					arg_6_0:emit(MailMediator.ON_REQUIRE, "rare", arg_18_0)
				end)
			end

			seriesAsync(var_17_0, function()
				if arg_6_0.mailToggle == "rare" then
					return
				end

				arg_6_0.selectMailId = nil

				arg_6_0:UpdateMailList("rare", 0)
			end)
		end
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtAdapt:Find("top/help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("mail_tip")
		})
	end, SFX_PANEL)

	arg_6_0.rtSearch = var_6_0:Find("search")
	arg_6_0.rtCollectionInput = arg_6_0.rtSearch:Find("input/InputField")

	setText(arg_6_0.rtCollectionInput:Find("Placeholder"), i18n("mail_search_new"))
	onInputEndEdit(arg_6_0, arg_6_0.rtCollectionInput, function()
		arg_6_0.collectionFilterStr = getInputText(arg_6_0.rtCollectionInput)

		if arg_6_0.mailToggle == "collection" then
			arg_6_0:UpdateMailList(arg_6_0.mailToggle, 0)
		end
	end)

	arg_6_0.collectionFilterStr = ""
	arg_6_0.rtToggleCollectionSort = arg_6_0.rtSearch:Find("sort")

	setText(arg_6_0.rtToggleCollectionSort:Find("Text"), i18n("mail_receive_time"))
	onToggle(arg_6_0, arg_6_0.rtToggleCollectionSort, function(arg_22_0)
		arg_6_0.collectionSortToggle = arg_22_0

		if arg_6_0.mailToggle == "collection" then
			arg_6_0:UpdateMailList(arg_6_0.mailToggle, 0)
		end
	end, SFX_PANEL)
	triggerToggle(arg_6_0.rtToggleCollectionSort, false)

	local var_6_1 = arg_6_0.rtAdapt:Find("main/content")

	arg_6_0.rtMailLeft = var_6_1:Find("left/left_content")
	arg_6_0.rtTip = arg_6_0.rtMailLeft:Find("top/tip")
	arg_6_0.rtMailCount = arg_6_0.rtMailLeft:Find("top/count")
	arg_6_0.Scrollbar = arg_6_0.rtMailLeft:Find("middle/Scrollbar"):GetComponent("Scrollbar")
	arg_6_0.lsrMailList = arg_6_0.rtMailLeft:Find("middle/container"):GetComponent("LScrollRect")

	function arg_6_0.lsrMailList.onUpdateItem(arg_23_0, arg_23_1)
		arg_23_0 = arg_23_0 + 1

		local var_23_0 = tf(arg_23_1)
		local var_23_1 = arg_6_0.filterMails[arg_23_0]

		if var_23_1.id == 0 then
			GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).alpha = 0
			GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).blocksRaycasts = false

			arg_6_0:RequrereNextToIndex(arg_23_0)

			return
		end

		if arg_6_0.tplMailDic[var_23_0] then
			arg_6_0.mailTplDic[arg_6_0.tplMailDic[var_23_0]] = nil
		end

		arg_6_0.mailTplDic[var_23_1.id] = var_23_0
		arg_6_0.tplMailDic[var_23_0] = var_23_1.id

		onToggle(arg_6_0, var_23_0, function(arg_24_0)
			if arg_24_0 then
				if arg_6_0.selectMailId ~= var_23_1.id then
					arg_6_0:UpdateMailContent(var_23_1)
				end
			elseif var_23_1.id == arg_6_0.selectMailId then
				arg_6_0:UpdateMailContent(nil)
			end
		end, SFX_PANEL)

		GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).alpha = 1
		GetOrAddComponent(arg_23_1, typeof(CanvasGroup)).blocksRaycasts = true

		arg_6_0:UpdateMailTpl(var_23_1)
	end

	arg_6_0.mailTplDic = {}
	arg_6_0.tplMailDic = {}
	arg_6_0.rtBtnLeftManager = arg_6_0.rtMailLeft:Find("bottom/btn_managerMail")

	onButton(arg_6_0, arg_6_0.rtBtnLeftManager, function()
		arg_6_0.mailMgrSubView:ExecuteAction("Show")
	end, SFX_PANEL)

	arg_6_0.rtBtnLeftDeleteAll = arg_6_0.rtMailLeft:Find("bottom/btn_deleteMail")

	onButton(arg_6_0, arg_6_0.rtBtnLeftDeleteAll, function()
		seriesAsync({
			function(arg_27_0)
				arg_6_0:ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("main_mailLayer_quest_clear"),
					onYes = arg_27_0
				})
			end
		}, function()
			arg_6_0:emit(MailMediator.ON_OPERATION, {
				cmd = "delete",
				filter = {
					type = "all"
				}
			})
		end)
	end, SFX_CANCEL)

	arg_6_0.rtBtnLeftMoveAll = arg_6_0.rtMailLeft:Find("bottom/btn_moveAll")

	onButton(arg_6_0, arg_6_0.rtBtnLeftMoveAll, function()
		seriesAsync({
			function(arg_30_0)
				arg_6_0:ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_moveto_markroom_2"),
					onYes = arg_30_0
				})
			end
		}, function()
			arg_6_0:emit(MailMediator.ON_OPERATION, {
				cmd = "move",
				filter = {
					type = "ids",
					list = underscore.rest(arg_6_0.proxy.importantIds, 1)
				}
			})
		end)
	end, SFX_CANCEL)

	arg_6_0.rtBtnLeftGetAll = arg_6_0.rtMailLeft:Find("bottom/btn_getAll")

	onButton(arg_6_0, arg_6_0.rtBtnLeftGetAll, function()
		local var_32_0 = {}

		if arg_6_0.mailToggle == "important" then
			var_32_0 = underscore.rest(arg_6_0.proxy.importantIds, 1)
		elseif arg_6_0.mailToggle == "rare" then
			var_32_0 = underscore.rest(arg_6_0.proxy.rareIds, 1)
		else
			assert(false)
		end

		arg_6_0:emit(MailMediator.ON_OPERATION, {
			cmd = "attachment",
			filter = {
				type = "ids",
				list = var_32_0
			}
		})
	end, SFX_CANCEL)

	arg_6_0.rtBtnLeftDeleteCollection = arg_6_0.rtMailLeft:Find("bottom/btn_deleteCollection")

	onButton(arg_6_0, arg_6_0.rtBtnLeftDeleteCollection, function()
		if not arg_6_0.selectMailId then
			return
		end

		assert(arg_6_0.selectMailId)

		local var_33_0 = arg_6_0.proxy:getCollecitonMail(arg_6_0.selectMailId)

		seriesAsync({
			function(arg_34_0)
				arg_6_0:ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_markroom_delete", var_33_0.title),
					onYes = arg_34_0
				})
			end
		}, function()
			arg_6_0:emit(MailMediator.ON_DELETE_COLLECTION, arg_6_0.selectMailId)
		end)
	end, SFX_CANCEL)

	arg_6_0.rtMailRight = var_6_1:Find("right")
	arg_6_0.rtBtnRightMove = arg_6_0.rtMailRight:Find("bottom/btn_move")

	onButton(arg_6_0, arg_6_0.rtBtnRightMove, function()
		assert(arg_6_0.selectMailId)
		seriesAsync({
			function(arg_37_0)
				arg_6_0:ShowDoubleConfiremationMsgBox({
					type = MailProxy.MailMessageBoxType.ShowTips,
					content = i18n("mail_moveto_markroom_1"),
					onYes = arg_37_0
				})
			end
		}, function()
			arg_6_0:emit(MailMediator.ON_OPERATION, {
				noAttachTip = true,
				cmd = "move",
				filter = {
					type = "ids",
					list = {
						arg_6_0.selectMailId
					}
				}
			})
		end)
	end, SFX_PANEL)

	arg_6_0.rtBtnRightGet = arg_6_0.rtMailRight:Find("bottom/btn_get")

	onButton(arg_6_0, arg_6_0.rtBtnRightGet, function()
		assert(arg_6_0.selectMailId)
		arg_6_0:emit(MailMediator.ON_OPERATION, {
			noAttachTip = true,
			cmd = "attachment",
			filter = {
				type = "ids",
				list = {
					arg_6_0.selectMailId
				}
			}
		})
	end, SFX_PANEL)

	arg_6_0.rtMailEmpty = var_6_1:Find("empty")
	arg_6_0.rtStore = var_6_1:Find("store")
	arg_6_0.mailMgrSubView = MailMgrWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.storeUpgradeSubView = StoreUpgradeWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.mailConfirmationSubView = MailConfirmationWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)
	arg_6_0.mailOverflowWindowSubView = MailOverflowWindow.New(arg_6_0._tf, arg_6_0.event, arg_6_0.contextData)

	setText(arg_6_0.rtBtnLeftDeleteAll:Find("Text"), i18n("mail_deleteread_button"))
	setText(arg_6_0.rtBtnLeftManager:Find("Text"), i18n("mail_manage_button"))
	setText(arg_6_0.rtBtnLeftMoveAll:Find("Text"), i18n("mail_move_button"))
	setText(arg_6_0.rtBtnLeftGetAll:Find("Text"), i18n("mail_get_oneclick"))
	setText(arg_6_0.rtBtnLeftDeleteCollection:Find("Text"), i18n("mail_delet_button"))
	setText(arg_6_0.rtBtnRightMove:Find("Text"), i18n("mail_moveone_button"))
	setText(arg_6_0.rtBtnRightGet:Find("Text"), i18n("mail_getone_button"))
	setText(arg_6_0.rtMailRight:Find("main/title/matter/on/Text"), i18n("mail_toggle_on"))
	setText(arg_6_0.rtMailRight:Find("main/title/matter/off/Text"), i18n("mail_toggle_off"))
	arg_6_0:InitResBar()
end

function var_0_0.SetPage(arg_40_0, arg_40_1)
	if arg_40_0.page == arg_40_1 then
		return
	end

	arg_40_0.page = arg_40_1

	setActive(arg_40_0.rightSelect, arg_40_1 == "mail")
	setActive(arg_40_0.rtSearch, arg_40_1 == "collection")
	setActive(arg_40_0.rtStore, arg_40_1 == "store")

	if arg_40_1 == "store" then
		setActive(arg_40_0.rtMailEmpty, false)
		setActive(arg_40_0.rtMailLeft, false)
		setActive(arg_40_0.rtMailRight, false)

		arg_40_0.mailToggle = nil

		arg_40_0:UpdateStore()
		setText(arg_40_0.rtTip, i18n("mail_storeroom_tips"))
	elseif arg_40_1 == "mail" then
		triggerToggle(arg_40_0.rtToggles:Find("btn_all"), true)
		setText(arg_40_0.rtTip, i18n("warning_mail_max_5"))
	elseif arg_40_1 == "collection" then
		local var_40_0 = {}

		if not arg_40_0.proxy.collectionIds then
			table.insert(var_40_0, function(arg_41_0)
				arg_40_0:emit(MailMediator.ON_REQUIRE, "collection", arg_41_0)
			end)
		end

		seriesAsync(var_40_0, function()
			arg_40_0.selectMailId = nil

			arg_40_0:UpdateMailList("collection", 0)
		end)
		setText(arg_40_0.rtTip, i18n("mail_markroom_tip"))
	end
end

function var_0_0.didEnter(arg_43_0)
	onNextTick(function()
		arg_43_0.lsrMailList.enabled = true

		triggerToggle(arg_43_0.rtLabels:Find("mail"), true)
	end)
end

function var_0_0.RequrereNextToIndex(arg_45_0, arg_45_1)
	if arg_45_0.mailToggle == "all" and not arg_45_0.inRequire and #arg_45_0.proxy.ids < arg_45_0.proxy.totalExist and arg_45_1 > #arg_45_0.proxy.ids then
		arg_45_0.inRequire = true

		pg.UIMgr.GetInstance():LoadingOn()
		arg_45_0:emit(MailMediator.ON_REQUIRE, arg_45_1, function()
			arg_45_0.inRequire = nil

			if arg_45_0.mailToggle == "all" then
				arg_45_0:UpdateMailList(arg_45_0.mailToggle)
			end

			pg.UIMgr.GetInstance():LoadingOff()
		end)
	end
end

function var_0_0.UpdateMailList(arg_47_0, arg_47_1, arg_47_2)
	arg_47_0.mailToggle = arg_47_1

	local var_47_0, var_47_1 = switch(arg_47_1, {
		all = function()
			return arg_47_0.proxy.ids, string.format("<color=%s>%d</color>/<color=%s>%d</color>", arg_47_0.proxy.totalExist > MAIL_COUNT_LIMIT and COLOR_RED or COLOR_WHITE, arg_47_0.proxy.totalExist, "#181E32", MAIL_COUNT_LIMIT)
		end,
		important = function()
			return arg_47_0.proxy.importantIds, string.format("<color=#FFFFFF>%d</color>", #arg_47_0.proxy.importantIds)
		end,
		rare = function()
			return arg_47_0.proxy.rareIds, string.format("<color=#FFFFFF>%d</color>", #arg_47_0.proxy.rareIds)
		end,
		collection = function()
			return arg_47_0.proxy.collectionIds, string.format("<color=#FFFFFF>%d</color>/%d", #arg_47_0.proxy.collectionIds, getProxy(PlayerProxy):getRawData():getConfig("max_markmail"))
		end
	})

	if arg_47_1 == "collection" then
		arg_47_0.filterMails = arg_47_0.proxy:GetCollectionMails(var_47_0)

		if arg_47_0.collectionFilterStr then
			arg_47_0.filterMails = underscore.filter(arg_47_0.filterMails, function(arg_52_0)
				return arg_52_0:IsMatchKey(arg_47_0.collectionFilterStr)
			end)
		end

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_53_0)
				return (arg_47_0.collectionSortToggle and 1 or -1) * arg_53_0.id
			end
		}))
	elseif arg_47_1 == "all" then
		arg_47_0.filterMails = arg_47_0.proxy:GetMails(var_47_0)

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_54_0)
				return -arg_54_0.id
			end
		}))

		for iter_47_0 = #var_47_0 + 1, arg_47_0.proxy.totalExist do
			table.insert(arg_47_0.filterMails, {
				id = 0
			})
		end
	else
		arg_47_0.filterMails = arg_47_0.proxy:GetMails(var_47_0)

		table.sort(arg_47_0.filterMails, CompareFuncs({
			function(arg_55_0)
				return -arg_55_0.id
			end
		}))
	end

	if arg_47_0.mailToggle == "all" and #arg_47_0.proxy.ids < arg_47_0.proxy.totalExist and #arg_47_0.proxy.ids < SINGLE_MAIL_REQUIRE_SIZE then
		arg_47_0.inRequire = true

		arg_47_0:emit(MailMediator.ON_REQUIRE, "next", function()
			if arg_47_0.mailToggle == "all" then
				arg_47_0:UpdateMailList(arg_47_0.mailToggle)
			end

			arg_47_0.inRequire = nil
		end)
	elseif #arg_47_0.filterMails == 0 then
		setActive(arg_47_0.rtMailLeft, false)
		setActive(arg_47_0.rtMailRight, false)
		setActive(arg_47_0.rtMailEmpty, true)

		if arg_47_0.mailToggle == "collection" then
			setText(arg_47_0.rtMailEmpty:Find("Text"), i18n("emptymarkroom_tip_mailboxui"))
			setText(arg_47_0.rtMailEmpty:Find("Text_en"), i18n("emptymarkroom_tip_mailboxui_en"))
		else
			setText(arg_47_0.rtMailEmpty:Find("Text"), i18n("empty_tip_mailboxui"))
			setText(arg_47_0.rtMailEmpty:Find("Text_en"), i18n("empty_tip_mailboxui_en"))
		end
	else
		setActive(arg_47_0.rtMailLeft, true)
		setActive(arg_47_0.rtMailRight, true)
		setActive(arg_47_0.rtMailEmpty, false)

		if not arg_47_0.selectMailId then
			arg_47_0:UpdateMailContent(arg_47_0.filterMails[1])
		end

		arg_47_0.lsrMailList:SetTotalCount(#arg_47_0.filterMails, arg_47_2 or -1)
		setText(arg_47_0.rtMailCount, var_47_1)
		setActive(arg_47_0.rtBtnLeftManager, arg_47_0.mailToggle == "all")
		setActive(arg_47_0.rtBtnLeftMoveAll, arg_47_0.mailToggle == "important")
		setActive(arg_47_0.rtBtnLeftDeleteCollection, arg_47_0.mailToggle == "collection")
		setActive(arg_47_0.rtBtnLeftDeleteAll, arg_47_0.mailToggle == "all" or arg_47_0.mailToggle == "rare")
		setActive(arg_47_0.rtBtnLeftGetAll, arg_47_0.mailToggle == "important" or arg_47_0.mailToggle == "rare")
	end
end

function var_0_0.UpdateMailTpl(arg_57_0, arg_57_1)
	local var_57_0 = arg_57_0.mailTplDic[arg_57_1.id]

	if not var_57_0 then
		return
	end

	local var_57_1 = var_57_0:Find("content")

	setActive(var_57_1:Find("icon/no_attachment"), #arg_57_1.attachments == 0)
	setActive(var_57_1:Find("icon/IconTpl"), #arg_57_1.attachments > 0)

	if #arg_57_1.attachments > 0 then
		updateDrop(var_57_1:Find("icon/IconTpl"), arg_57_1.attachments[1])
	end

	setText(var_57_1:Find("info/title/Text"), shortenString(arg_57_1.title, 10))
	setActive(var_57_1:Find("info/title/mark"), arg_57_1.importantFlag and arg_57_0.mailToggle ~= "collection")
	setText(var_57_1:Find("info/time/Text"), os.date("%Y-%m-%d", arg_57_1.date))
	setActive(var_57_1:Find("info/time/out_time"), false)

	local var_57_2 = #arg_57_1.attachments > 0 and arg_57_1.attachFlag

	setActive(var_57_0:Find("got_mark"), arg_57_0.mailToggle ~= "collection" and var_57_2)
	setText(var_57_0:Find("got_mark/got_text"), i18n("mail_reward_got"))
	triggerToggle(var_57_0, arg_57_0.selectMailId == arg_57_1.id)

	local var_57_3 = arg_57_1.readFlag or arg_57_0.mailToggle == "collection"

	setActive(var_57_0:Find("hasread_bg"), var_57_3)
	setActive(var_57_0:Find("noread_bg"), not var_57_3)

	local var_57_4 = SummerFeastScene.TransformColor(var_57_3 and "FFFFFF" or "181E32")

	setTextColor(var_57_1:Find("info/title/Text"), var_57_4)
	setTextColor(var_57_1:Find("info/time/Text"), var_57_4)
end

function var_0_0.UpdateMailContent(arg_58_0, arg_58_1)
	eachChild(arg_58_0.rtMailRight, function(arg_59_0)
		setActive(arg_59_0, tobool(arg_58_1))
	end)

	if not arg_58_1 then
		arg_58_0.selectMailId = nil

		return
	end

	arg_58_0.selectMailId = arg_58_1.id

	changeToScrollText(arg_58_0.rtMailRight:Find("main/title/info/Text"), i18n2(arg_58_1.title))
	setText(arg_58_0.rtMailRight:Find("main/from/Text"), arg_58_1.sender)
	setText(arg_58_0.rtMailRight:Find("main/time/Text"), os.date("%Y-%m-%d", arg_58_1.date))
	setText(arg_58_0.rtMailRight:Find("main/view/content/text/Text"), arg_58_1.content)

	local var_58_0 = arg_58_0.rtMailRight:Find("main/title/matter")

	setActive(var_58_0, arg_58_0.mailToggle ~= "collection")

	if arg_58_0.mailToggle ~= "collection" then
		onToggle(arg_58_0, arg_58_0.rtMailRight:Find("main/title/matter"), function(arg_60_0)
			if arg_60_0 ~= arg_58_1.importantFlag then
				arg_58_0:emit(MailMediator.ON_OPERATION, {
					cmd = arg_60_0 and "important" or "unimportant",
					filter = {
						type = "ids",
						list = {
							arg_58_1.id
						}
					}
				})
			end
		end, SFX_CONFIRM)
		triggerToggle(arg_58_0.rtMailRight:Find("main/title/matter"), arg_58_1.importantFlag)
	end

	local var_58_1 = arg_58_0.rtMailRight:Find("main/view/content/attachment")

	setText(var_58_1:Find("got/Text"), i18n("main_mailLayer_attachTaken"))
	setActive(var_58_1, #arg_58_1.attachments > 0)

	if #arg_58_1.attachments > 0 then
		local var_58_2 = var_58_1:Find("content")

		UIItemList.StaticAlign(var_58_2, var_58_2:Find("IconTpl"), #arg_58_1.attachments, function(arg_61_0, arg_61_1, arg_61_2)
			arg_61_1 = arg_61_1 + 1

			if arg_61_0 == UIItemList.EventUpdate then
				local var_61_0 = arg_58_1.attachments[arg_61_1]

				updateDrop(arg_61_2, var_61_0)
				onButton(arg_58_0, arg_61_2, function()
					arg_58_0:emit(var_0_0.ON_DROP, var_61_0)
				end, SFX_PANEL)
			end
		end)

		local var_58_3 = arg_58_0.mailToggle == "collection" or arg_58_1.attachFlag

		setCanvasGroupAlpha(var_58_2, var_58_3 and 0.5 or 1)
		setActive(var_58_1:Find("got"), var_58_3)
	end

	setActive(arg_58_0.rtBtnRightMove, arg_58_0.mailToggle ~= "collection")
	setActive(arg_58_0.rtBtnRightGet, arg_58_0.mailToggle ~= "collection" and not arg_58_1.attachFlag)

	if arg_58_0.mailToggle ~= "collection" and not arg_58_1.readFlag then
		arg_58_0:emit(MailMediator.ON_OPERATION, {
			cmd = "read",
			ignoreTips = true,
			filter = {
				type = "ids",
				list = {
					arg_58_1.id
				}
			}
		})
	end
end

function var_0_0.UpdateOperationDeal(arg_63_0, arg_63_1, arg_63_2, arg_63_3)
	if #arg_63_2 == 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("mail_manage_3"))
	elseif not arg_63_3 then
		local var_63_0 = switch(arg_63_1, {
			delete = function()
				return i18n("main_mailMediator_mailDelete")
			end,
			attachment = function()
				return i18n("main_mailMediator_attachTaken")
			end,
			read = function()
				return i18n("main_mailMediator_mailread")
			end,
			move = function()
				return i18n("main_mailMediator_mailmove")
			end
		})

		if var_63_0 then
			pg.TipsMgr.GetInstance():ShowTips(var_63_0)
		end
	end

	local var_63_1 = {}

	for iter_63_0, iter_63_1 in ipairs(arg_63_2) do
		var_63_1[iter_63_1] = true
	end

	arg_63_0:UpdateMailList(arg_63_0.mailToggle)

	if var_63_1[arg_63_0.selectMailId] then
		arg_63_0:UpdateMailContent(underscore.detect(arg_63_0.filterMails, function(arg_68_0)
			return arg_68_0.id == arg_63_0.selectMailId
		end))
	end
end

function var_0_0.UpdateCollectionDelete(arg_69_0, arg_69_1)
	arg_69_0:UpdateMailList(arg_69_0.mailToggle)

	if arg_69_0.selectMailId == arg_69_1 then
		arg_69_0:UpdateMailContent(nil)
	end
end

function var_0_0.UpdateStore(arg_70_0)
	arg_70_0.withdrawal = {
		gold = 0,
		oil = 0
	}

	local var_70_0 = getProxy(PlayerProxy):getRawData()
	local var_70_1 = pg.mail_storeroom[var_70_0.mailStoreLevel]

	setText(arg_70_0.rtStore:Find("gold/Text/count"), string.format("%d/%d", var_70_0:getResource(PlayerConst.ResStoreGold), var_70_1.gold_store))

	local var_70_2 = var_70_0:IsStoreLevelMax()
	local var_70_3 = arg_70_0.rtStore:Find("bottom/btn_extend")

	SetActive(var_70_3, not var_70_2)
	onButton(arg_70_0, var_70_3, function()
		if var_70_2 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("mail_storeroom_noextend"))
		else
			arg_70_0.storeUpgradeSubView:ExecuteAction("Show")
		end
	end, SFX_PANEL)

	local var_70_4 = arg_70_0.rtStore:Find("bottom/btn_get")

	onButton(arg_70_0, var_70_4, function()
		arg_70_0:emit(MailMediator.ON_WITHDRAWAL, arg_70_0.withdrawal)
	end, SFX_CONFIRM)

	local function var_70_5()
		local var_73_0 = arg_70_0.withdrawal.oil ~= 0 or arg_70_0.withdrawal.gold ~= 0

		setButtonEnabled(var_70_4, var_73_0)
		setGray(var_70_4, not var_73_0)
	end

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
	}) do
		local var_70_6, var_70_7, var_70_8, var_70_9, var_70_10 = unpack(iter_70_1)
		local var_70_11 = pg.gameset[var_70_10].key_value - var_70_0:getResource(var_70_7)
		local var_70_12 = math.max(var_70_11, 0)
		local var_70_13 = var_70_0:getResource(var_70_8)

		setText(arg_70_0.rtStore:Find(var_70_6 .. "/tips"), i18n("mail_reward_tips"))
		setText(arg_70_0.rtStore:Find(var_70_6 .. "/Text/count"), string.format("<color=%s>%d</color>/%d", var_70_9, var_70_13, var_70_1[var_70_6 .. "_store"]))

		local var_70_14 = arg_70_0.rtStore:Find(var_70_6 .. "/calc")
		local var_70_15 = var_70_14:Find("count/count")

		setText(var_70_15:Find("tip"), i18n("mail_storeroom_resourcetaken"))
		setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])
		onInputEndEdit(arg_70_0, var_70_15, function()
			local var_74_0 = getInputText(var_70_15)

			if var_74_0 == "" or var_74_0 == nil then
				var_74_0 = 0
			end

			local var_74_1 = math.clamp(tonumber(var_74_0), 0, var_70_13)

			if var_74_1 >= var_70_12 then
				var_74_1 = var_70_12

				pg.TipsMgr.GetInstance():ShowTips(i18n("resource_max_tip_storeroom"))
			end

			if arg_70_0.withdrawal[var_70_6] ~= var_74_1 then
				arg_70_0.withdrawal[var_70_6] = var_74_1

				var_70_5()
			end

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])
		end)
		pressPersistTrigger(var_70_14:Find("count/left"), 0.5, function()
			if arg_70_0.withdrawal[var_70_6] == 0 then
				return
			end

			arg_70_0.withdrawal[var_70_6] = math.max(arg_70_0.withdrawal[var_70_6] - 100, 0)

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])

			if arg_70_0.withdrawal[var_70_6] == 0 then
				var_70_5()
			end
		end, nil, true, true, 0.15, SFX_PANEL)
		pressPersistTrigger(var_70_14:Find("count/right"), 0.5, function()
			if arg_70_0.withdrawal[var_70_6] >= var_70_12 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("resource_max_tip_storeroom"))

				return
			end

			if arg_70_0.withdrawal[var_70_6] == var_70_13 then
				return
			end

			local var_76_0 = arg_70_0.withdrawal[var_70_6]

			arg_70_0.withdrawal[var_70_6] = math.min(arg_70_0.withdrawal[var_70_6] + 100, var_70_13)

			if arg_70_0.withdrawal[var_70_6] >= var_70_12 then
				arg_70_0.withdrawal[var_70_6] = var_70_12

				pg.TipsMgr.GetInstance():ShowTips(i18n("resource_max_tip_storeroom"))
			end

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])

			if var_76_0 == 0 then
				var_70_5()
			end
		end, nil, true, true, 0.15, SFX_PANEL)
		onButton(arg_70_0, var_70_14:Find("max"), function()
			arg_70_0.withdrawal[var_70_6] = getProxy(PlayerProxy):getRawData():ResLack(var_70_6, var_70_13)

			if arg_70_0.withdrawal[var_70_6] >= var_70_12 then
				arg_70_0.withdrawal[var_70_6] = var_70_12

				pg.TipsMgr.GetInstance():ShowTips(i18n("resource_max_tip_storeroom"))
			end

			setInputText(var_70_15, arg_70_0.withdrawal[var_70_6])
			var_70_5()
		end, SFX_PANEL)
	end
end

function var_0_0.onBackPressed(arg_78_0)
	if arg_78_0.mailMgrSubView:isShowing() then
		arg_78_0.mailMgrSubView:Hide()
	elseif arg_78_0.storeUpgradeSubView:isShowing() then
		arg_78_0.storeUpgradeSubView:Hide()
	elseif arg_78_0.mailConfirmationSubView:isShowing() then
		arg_78_0.mailConfirmationSubView:Hide()
	elseif arg_78_0.mailOverflowWindowSubView:isShowing() then
		arg_78_0.mailOverflowWindowSubView:Hide()
	else
		triggerButton(arg_78_0.rtAdapt:Find("top/back_btn"))
	end
end

function var_0_0.willExit(arg_79_0)
	arg_79_0.mailMgrSubView:Destroy()
	arg_79_0.storeUpgradeSubView:Destroy()
	arg_79_0.mailConfirmationSubView:Destroy()
	arg_79_0.mailOverflowWindowSubView:Destroy()
end

function var_0_0.ShowDoubleConfiremationMsgBox(arg_80_0, arg_80_1)
	if arg_80_1.type == MailProxy.MailMessageBoxType.OverflowConfirm then
		arg_80_0.mailOverflowWindowSubView:ExecuteAction("Show", arg_80_1)
	else
		arg_80_0.mailConfirmationSubView:ExecuteAction("Show", arg_80_1)
	end
end

function var_0_0.InitResBar(arg_81_0)
	arg_81_0.resBar = arg_81_0._tf:Find("adapt/top/res")
	arg_81_0.goldMax = arg_81_0.resBar:Find("gold/max"):GetComponent(typeof(Text))
	arg_81_0.goldValue = arg_81_0.resBar:Find("gold/Text"):GetComponent(typeof(Text))
	arg_81_0.oilMax = arg_81_0.resBar:Find("oil/max"):GetComponent(typeof(Text))
	arg_81_0.oilValue = arg_81_0.resBar:Find("oil/Text"):GetComponent(typeof(Text))
	arg_81_0.gemValue = arg_81_0.resBar:Find("gem/Text"):GetComponent(typeof(Text))

	onButton(arg_81_0, arg_81_0.resBar:Find("gold"), function()
		pg.playerResUI:ClickGold()
	end, SFX_PANEL)
	onButton(arg_81_0, arg_81_0.resBar:Find("oil"), function()
		pg.playerResUI:ClickOil()
	end, SFX_PANEL)
	onButton(arg_81_0, arg_81_0.resBar:Find("gem"), function()
		pg.playerResUI:ClickGem()
	end, SFX_PANEL)
	arg_81_0:UpdateRes()
end

function var_0_0.UpdateRes(arg_85_0)
	local var_85_0 = getProxy(PlayerProxy):getRawData()

	PlayerResUI.StaticFlush(var_85_0, arg_85_0.goldMax, arg_85_0.goldValue, arg_85_0.oilMax, arg_85_0.oilValue, arg_85_0.gemValue)
end

return var_0_0

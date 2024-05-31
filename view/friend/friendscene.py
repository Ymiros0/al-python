local var_0_0 = class("FriendScene", import("..base.BaseUI"))

var_0_0.FRIEND_PAGE = 1
var_0_0.SEARCH_PAGE = 2
var_0_0.REQUEST_PAGE = 3
var_0_0.BLACKLIST_PAGE = 4

def var_0_0.getUIName(arg_1_0):
	return "FriendUI"

def var_0_0.setFriendVOs(arg_2_0, arg_2_1):
	arg_2_0.friendVOs = arg_2_1

def var_0_0.setPlayer(arg_3_0, arg_3_1):
	arg_3_0.playerVO = arg_3_1

def var_0_0.setRequests(arg_4_0, arg_4_1):
	arg_4_0.requestVOs = arg_4_1

def var_0_0.setSearchResult(arg_5_0, arg_5_1):
	arg_5_0.searchResultVOs = arg_5_1

def var_0_0.removeSearchResult(arg_6_0, arg_6_1):
	local var_6_0 = _.select(arg_6_0.searchResultVOs, function(arg_7_0)
		return arg_7_0.id != arg_6_1)

	arg_6_0.setSearchResult(var_6_0)

def var_0_0.setBlackList(arg_8_0, arg_8_1):
	if arg_8_1:
		arg_8_0.blackVOs = {}

		for iter_8_0, iter_8_1 in pairs(arg_8_1 or {}):
			table.insert(arg_8_0.blackVOs, iter_8_1)

def var_0_0.init(arg_9_0):
	arg_9_0.pages = arg_9_0.findTF("pages")
	arg_9_0.togglesTF = arg_9_0.findTF("blur_panel/adapt/left_length/frame/tagRoot")
	arg_9_0.pages = {
		FriendListPage.New(arg_9_0.pages, arg_9_0.event, arg_9_0.contextData),
		FriendSearchPage.New(arg_9_0.pages, arg_9_0.event),
		FriendRequestPage.New(arg_9_0.pages, arg_9_0.event),
		FriendBlackListPage.New(arg_9_0.pages, arg_9_0.event)
	}
	arg_9_0.toggles = {}

	for iter_9_0 = 1, arg_9_0.togglesTF.childCount:
		arg_9_0.toggles[iter_9_0] = arg_9_0.togglesTF.GetChild(iter_9_0 - 1)

		onToggle(arg_9_0, arg_9_0.toggles[iter_9_0], function(arg_10_0)
			if arg_10_0:
				arg_9_0.switchPage(iter_9_0), SFX_PANEL)

	arg_9_0.chatTipContainer = arg_9_0.toggles[1].Find("count")
	arg_9_0.chatTip = arg_9_0.toggles[1].Find("count/Text").GetComponent(typeof(Text))
	arg_9_0.listEmptyTF = arg_9_0.findTF("empty")

	setActive(arg_9_0.listEmptyTF, False)

	arg_9_0.listEmptyTxt = arg_9_0.findTF("Text", arg_9_0.listEmptyTF)

def var_0_0.didEnter(arg_11_0):
	onButton(arg_11_0, arg_11_0.findTF("blur_panel/adapt/top/back_btn"), function()
		arg_11_0.emit(var_0_0.ON_BACK), SOUND_BACK)

	local var_11_0 = arg_11_0.contextData.initPage or 1

	triggerToggle(arg_11_0.toggles[var_11_0], True)
	arg_11_0.updateRequestTip()

def var_0_0.wrapData(arg_13_0):
	return {
		friendVOs = arg_13_0.friendVOs,
		requestVOs = arg_13_0.requestVOs,
		searchResults = arg_13_0.searchResultVOs,
		blackVOs = arg_13_0.blackVOs,
		playerVO = arg_13_0.playerVO
	}

def var_0_0.updateEmpty(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = {}
	local var_14_1 = ""

	if arg_14_1 == var_0_0.FRIEND_PAGE:
		var_14_0 = arg_14_2.friendVOs
		var_14_1 = i18n("list_empty_tip_friendui")
	elif arg_14_1 == var_0_0.SEARCH_PAGE:
		var_14_0 = arg_14_2.searchResults
		var_14_1 = i18n("list_empty_tip_friendui_search")
	elif arg_14_1 == var_0_0.REQUEST_PAGE:
		var_14_0 = arg_14_2.requestVOs
		var_14_1 = i18n("list_empty_tip_friendui_request")
	elif arg_14_1 == var_0_0.BLACKLIST_PAGE:
		var_14_0 = arg_14_2.blackVOs
		var_14_1 = i18n("list_empty_tip_friendui_black")

	setActive(arg_14_0.listEmptyTF, not var_14_0 or #var_14_0 <= 0)
	setText(arg_14_0.listEmptyTxt, var_14_1)

def var_0_0.switchPage(arg_15_0, arg_15_1):
	if arg_15_0.page:
		arg_15_0.page.ExecuteAction("Hide")

	local var_15_0 = arg_15_0.pages[arg_15_1]
	local var_15_1 = arg_15_0.wrapData()

	var_15_0.ExecuteAction("Show")
	var_15_0.ExecuteAction("UpdateData", var_15_1)

	arg_15_0.page = var_15_0

	arg_15_0.updateEmpty(arg_15_1, var_15_1)

def var_0_0.updatePage(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.pages[arg_16_1]

	if arg_16_0.page and var_16_0 == arg_16_0.page:
		local var_16_1 = arg_16_0.wrapData()

		arg_16_0.page.ExecuteAction("UpdateData", var_16_1)
		arg_16_0.updateEmpty(arg_16_1, var_16_1)

def var_0_0.updateChatNotification(arg_17_0, arg_17_1):
	setActive(arg_17_0.chatTipContainer, arg_17_1 > 0)

	arg_17_0.chatTip.text = arg_17_1

def var_0_0.updateRequestTip(arg_18_0):
	setActive(arg_18_0.toggles[3].Find("tip"), #arg_18_0.requestVOs > 0)

def var_0_0.willExit(arg_19_0):
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.pages):
		iter_19_1.Destroy()

return var_0_0

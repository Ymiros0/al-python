local var_0_0 = class("FriendRequestPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "FriendRequestUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.requestPanel = arg_2_0.findTF("request_panel")
	arg_2_0.requestTopTF = arg_2_0.findTF("request_view_top")
	arg_2_0.refuseAllBtn = arg_2_0.findTF("refuse_all_btn", arg_2_0.requestTopTF)

def var_0_0.OnInit(arg_3_0):
	arg_3_0.refuseMsgBox = FriendRefusePage.New(arg_3_0._tf, arg_3_0.event)

	onButton(arg_3_0, arg_3_0.refuseAllBtn, function()
		arg_3_0.emit(FriendMediator.REFUSE_ALL_REQUEST), SFX_PANEL)

def var_0_0.UpdateData(arg_5_0, arg_5_1):
	arg_5_0.requestVOs = arg_5_1.requestVOs or {}

	if not arg_5_0.isInit:
		arg_5_0.isInit = True

		arg_5_0.isInitRequestPage()
	else
		arg_5_0.sortRequest()

def var_0_0.isInitRequestPage(arg_6_0):
	arg_6_0.requestItems = {}
	arg_6_0.requestRect = arg_6_0.requestPanel.Find("mask/view").GetComponent("LScrollRect")

	function arg_6_0.requestRect.onInitItem(arg_7_0)
		arg_6_0.onInitItem(arg_7_0)

	function arg_6_0.requestRect.onUpdateItem(arg_8_0, arg_8_1)
		arg_6_0.onUpdateItem(arg_8_0, arg_8_1)

	arg_6_0.sortRequest()

def var_0_0.sortRequest(arg_9_0):
	arg_9_0.requestRect.SetTotalCount(#arg_9_0.requestVOs, -1)

def var_0_0.onInitItem(arg_10_0, arg_10_1):
	local var_10_0 = FriendRequestCard.New(arg_10_1)

	onButton(arg_10_0, var_10_0.acceptBtn, function()
		if var_10_0.friendVO:
			arg_10_0.emit(FriendMediator.ACCEPT_REQUEST, var_10_0.friendVO.id), SFX_PANEL)
	onButton(arg_10_0, var_10_0.refuseBtn, function()
		if var_10_0.friendVO:
			arg_10_0.refuseMsgBox.ExecuteAction("Show", i18n("refuse_friend"), i18n("refuse_and_add_into_bl"), function(arg_13_0)
				arg_10_0.emit(FriendMediator.REFUSE_REQUEST, var_10_0.friendVO, arg_13_0)))
	onButton(arg_10_0, var_10_0.resumeBtn, function()
		arg_10_0.emit(FriendMediator.OPEN_RESUME, var_10_0.friendVO.id), SFX_PANEL)

	arg_10_0.requestItems[arg_10_1] = var_10_0

def var_0_0.onUpdateItem(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_0.requestItems[arg_15_2]

	if not var_15_0:
		arg_15_0.onInitItem(arg_15_2)

		var_15_0 = arg_15_0.requestItems[arg_15_2]

	local var_15_1 = arg_15_0.requestVOs[arg_15_1 + 1]

	var_15_0.update(var_15_1.player, var_15_1.timestamp, var_15_1.content)

def var_0_0.OnDestroy(arg_16_0):
	for iter_16_0, iter_16_1 in pairs(arg_16_0.requestItems or {}):
		iter_16_1.dispose()

	arg_16_0.refuseMsgBox.Destroy()

return var_0_0

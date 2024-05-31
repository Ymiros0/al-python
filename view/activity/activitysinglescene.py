local var_0_0 = class("ActivitySingleScene", import("..base.BaseUI"))

var_0_0.EXIT = "exit"

def var_0_0.preload(arg_1_0, arg_1_1):
	arg_1_1()

def var_0_0.getUIName(arg_2_0):
	return "ActivitySingleUI"

def var_0_0.init(arg_3_0):
	arg_3_0.shareData = ActivityShareData.New()
	arg_3_0.pageContainer = arg_3_0._tf

	pg.UIMgr.GetInstance().OverlayPanel(arg_3_0._tf)

def var_0_0.didEnter(arg_4_0):
	arg_4_0.bind(var_0_0.EXIT, function(arg_5_0)
		arg_4_0.emit(var_0_0.ON_BACK))

def var_0_0.setPlayer(arg_6_0, arg_6_1):
	arg_6_0.shareData.SetPlayer(arg_6_1)

def var_0_0.setFlagShip(arg_7_0, arg_7_1):
	arg_7_0.shareData.SetFlagShip(arg_7_1)

def var_0_0.updateTaskLayers(arg_8_0):
	if not arg_8_0.activity:
		return

	arg_8_0.updateActivity(arg_8_0.activity)

def var_0_0.selectActivity(arg_9_0, arg_9_1):
	arg_9_0.activity = arg_9_1

	local var_9_0 = arg_9_1.getConfig("page_info")

	if var_9_0.class_name and not arg_9_1.isEnd():
		arg_9_0.actPage = import("view.activity.subPages." .. var_9_0.class_name).New(arg_9_0.pageContainer, arg_9_0.event, arg_9_0.contextData)

		if arg_9_0.actPage.UseSecondPage(arg_9_1):
			arg_9_0.actPage.SetUIName(var_9_0.ui_name2)
		else
			arg_9_0.actPage.SetUIName(var_9_0.ui_name)

		arg_9_0.actPage.SetShareData(arg_9_0.shareData)
		arg_9_0.actPage.Load()
		arg_9_0.actPage.ActionInvoke("Flush", arg_9_0.activity)
		arg_9_0.actPage.ActionInvoke("ShowOrHide", True)

def var_0_0.updateActivity(arg_10_0, arg_10_1):
	if ActivityConst.PageIdLink[arg_10_1.id]:
		arg_10_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.PageIdLink[arg_10_1.id])

	if arg_10_1.isShow() and not arg_10_1.isEnd() and arg_10_0.activity and arg_10_0.activity.id == arg_10_1.id:
		arg_10_0.activity = arg_10_1

		arg_10_0.actPage.ActionInvoke("Flush", arg_10_1)

def var_0_0.onBackPressed(arg_11_0):
	arg_11_0.actPage.ActionInvoke("onBackPressed")
	arg_11_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.willExit(arg_12_0):
	arg_12_0.shareData = None

	if arg_12_0.actPage:
		arg_12_0.actPage.Destroy()

	pg.UIMgr.GetInstance().UnOverlayPanel(arg_12_0._tf)

return var_0_0

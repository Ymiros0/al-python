local var_0_0 = class("EducateTargetPanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "EducateTargetPanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.contentTF = arg_2_0.findTF("content")

	onButton(arg_2_0, arg_2_0.contentTF, function()
		arg_2_0.emit(EducateBaseUI.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateTargetMediator,
			viewComponent = EducateTargetLayer
		})), SFX_PANEL)

	arg_2_0.taskTpl = arg_2_0.findTF("tpl", arg_2_0.contentTF)

	setActive(arg_2_0.taskTpl, False)

	arg_2_0.listBg = arg_2_0.findTF("task_list/bg", arg_2_0.contentTF)
	arg_2_0.lineTF = arg_2_0.findTF("task_list/line", arg_2_0.contentTF)
	arg_2_0.mainTF = arg_2_0.findTF("task_list/main", arg_2_0.contentTF)

	setText(arg_2_0.findTF("title/Image/Text", arg_2_0.mainTF), i18n("child_task_system_type3"))

	arg_2_0.mainTaskUIList = UIItemList.New(arg_2_0.findTF("list", arg_2_0.mainTF), arg_2_0.taskTpl)

	arg_2_0.mainTaskUIList.make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventUpdate:
			arg_2_0.updateTaskItem(arg_4_1, arg_4_2, "main"))

	arg_2_0.otherTF = arg_2_0.findTF("task_list/other", arg_2_0.contentTF)

	setText(arg_2_0.findTF("title/Image/Text", arg_2_0.otherTF), i18n("child_task_system_type2"))

	arg_2_0.otherTaskUIList = UIItemList.New(arg_2_0.findTF("list", arg_2_0.otherTF), arg_2_0.taskTpl)

	arg_2_0.otherTaskUIList.make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate:
			arg_2_0.updateTaskItem(arg_5_1, arg_5_2, "other"))
	arg_2_0.Flush()

def var_0_0.updateTaskItem(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	local var_6_0 = arg_6_3 == "main" and arg_6_0.mainTaskVOs[arg_6_1 + 1] or arg_6_0.otherTaskVOs[arg_6_1 + 1]
	local var_6_1 = string.format("(%s)", var_6_0.GetProgress() .. "/" .. var_6_0.GetFinishNum())

	setText(arg_6_0.findTF("progress", arg_6_2), var_6_1)

	local var_6_2 = GetPerceptualSize(var_6_1)

	if PLATFORM_CODE == PLATFORM_JP:
		var_6_2 = var_6_2 + 2

	setText(arg_6_0.findTF("desc", arg_6_2), shortenString(var_6_0.getConfig("name"), 11 - var_6_2))

def var_0_0.Flush(arg_7_0):
	if not arg_7_0.GetLoaded():
		return

	arg_7_0.taskProxy = getProxy(EducateProxy).GetTaskProxy()

	setActive(arg_7_0.findTF("target_btn/tip", arg_7_0.contentTF), arg_7_0.taskProxy.IsShowOtherTasksTip())

	arg_7_0.mainTaskVOs = arg_7_0.taskProxy.FilterByGroup(arg_7_0.taskProxy.GetMainTasksForShow())

	if not arg_7_0.taskProxy.CanGetTargetAward():
		arg_7_0.otherTaskVOs = {}
	else
		arg_7_0.otherTaskVOs = arg_7_0.taskProxy.FilterByGroup(arg_7_0.taskProxy.GetTargetTasksForShow(), True)

	setActive(arg_7_0.mainTF, #arg_7_0.mainTaskVOs > 0)
	arg_7_0.mainTaskUIList.align(#arg_7_0.mainTaskVOs)

	local var_7_0 = #arg_7_0.mainTaskVOs
	local var_7_1 = 3 - var_7_0

	setActive(arg_7_0.otherTF, #arg_7_0.otherTaskVOs > 0)

	local var_7_2 = var_7_1 < #arg_7_0.otherTaskVOs and var_7_1 or #arg_7_0.otherTaskVOs

	arg_7_0.otherTaskUIList.align(var_7_2)
	setActive(arg_7_0.listBg, var_7_0 > 0 or var_7_2 > 0)
	setActive(arg_7_0.lineTF, var_7_0 > 0 and var_7_2 > 0)

def var_0_0.SetPosLeft(arg_8_0):
	setLocalPosition(arg_8_0.contentTF, Vector2(-650, 0))

def var_0_0.SetPosRight(arg_9_0):
	setLocalPosition(arg_9_0.contentTF, Vector2(0, 0))

def var_0_0.OnDestroy(arg_10_0):
	return

return var_0_0

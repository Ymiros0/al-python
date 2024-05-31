local var_0_0 = class("EducateMediator", import(".base.EducateContextMediator"))

var_0_0.ON_DEFAULT_TARGET_SET = "EducateMediator.ON_DEFAULT_TARGET_SET"
var_0_0.ON_UPGRADE_FAVOR = "EducateMediator.ON_UPGRADE_FAVOR"
var_0_0.ON_SPECIAL_EVENT_TRIGGER = "EducateMediator.ON_SPECIAL_EVENT_TRIGGER"
var_0_0.ON_EVENT_TRIGGER = "EducateMediator.ON_EVENT_TRIGGER"
var_0_0.ON_GET_EVENT = "EducateMediator.ON_GET_EVENT"
var_0_0.ON_EXECTUE_PLANS = "EducateMediator.ON_EXECTUE_PLANS"
var_0_0.ON_ENDING_TRIGGER = "EducateMediator.ON_ENDING_TRIGGER"
var_0_0.ON_GAME_RESET = "EducateMediator.ON_GAME_RESET"
var_0_0.ENTER_VIRTUAL_STAGE = "EducateMediator.ENTER_VIRTUAL_STAGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_DEFAULT_TARGET_SET, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.EDUCATE_SET_TARGET, {
			id = arg_2_1.id,
			callback = arg_2_1.callback
		}))
	arg_1_0.bind(var_0_0.ON_UPGRADE_FAVOR, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.EDUCATE_UPGRADE_FAVOR, {
			callback = arg_3_1
		}))
	arg_1_0.bind(var_0_0.ON_SPECIAL_EVENT_TRIGGER, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.EDUCATE_TRIGGER_SPEC_EVENT, {
			eventId = arg_4_1.id,
			callback = arg_4_1.callback
		}))
	arg_1_0.bind(var_0_0.ON_EVENT_TRIGGER, function(arg_5_0, arg_5_1)
		arg_1_0.sendNotification(GAME.EDUCATE_TRIGGER_EVENT, {
			eventId = arg_5_1.id,
			callback = arg_5_1.callback
		}))
	arg_1_0.bind(var_0_0.ON_GET_EVENT, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.EDUCATE_GET_EVENTS, {
			callback = arg_6_1
		}))
	arg_1_0.bind(var_0_0.ON_EXECTUE_PLANS, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.EDUCATE_EXECUTE_PLANS, {
			callback = arg_7_1
		}))
	arg_1_0.bind(var_0_0.ON_ENDING_TRIGGER, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(GAME.EDUCATE_TRIGGER_END, {
			id = getProxy(EducateProxy).GetEndingResult()
		}))
	arg_1_0.bind(var_0_0.ON_GAME_RESET, function(arg_9_0, arg_9_1)
		arg_1_0.sendNotification(GAME.EDUCATE_RESET))
	arg_1_0.bind(var_0_0.ENTER_VIRTUAL_STAGE, function(arg_10_0, arg_10_1)
		arg_1_0.viewComponent.updateResPanel()
		arg_1_0.viewComponent.updatePaintingUI()
		arg_1_0.viewComponent.updateArchivePanel()
		arg_1_0.viewComponent.PlayBGM())

def var_0_0.listNotificationInterests(arg_11_0):
	return {
		EducateProxy.RESOURCE_UPDATED,
		EducateProxy.ATTR_UPDATED,
		EducateProxy.TIEM_UPDATED,
		EducateProxy.TIME_WEEKDAY_UPDATED,
		EducateProxy.BUFF_ADDED,
		EducateTaskProxy.TASK_UPDATED,
		GAME.EDUCATE_UPGRADE_FAVOR_DONE,
		GAME.EDUCATE_TRIGGER_SPEC_EVENT_DONE,
		GAME.EDUCATE_TRIGGER_EVENT_DONE,
		GAME.EDUCATE_SET_TARGET_DONE,
		GAME.EDUCATE_TRIGGER_END_DONE,
		GAME.EDUCATE_RESET_DONE,
		GAME.EDUCATE_REFRESH_DONE,
		GAME.EDUCATE_EXECUTE_PLANS_DONE,
		GAME.EDUCATE_SUBMIT_TASK_DONE,
		GAME.EDUCATE_GET_TARGET_AWARD_DONE,
		EducateProxy.GUIDE_CHECK,
		EducateProxy.MAIN_SCENE_ADD_LAYER,
		EducateProxy.POLAROID_ADDED,
		EducateProxy.MEMORY_ADDED,
		EducateTaskProxy.TASK_ADDED,
		EducateTaskProxy.TASK_REMOVED,
		EducateProxy.CLEAR_NEW_TIP
	}

def var_0_0.handleNotification(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_1.getName()
	local var_12_1 = arg_12_1.getBody()

	if var_12_0 == EducateProxy.RESOURCE_UPDATED:
		arg_12_0.viewComponent.updateResPanel()
		arg_12_0.viewComponent.updateTargetPanel()
	elif var_12_0 == EducateProxy.ATTR_UPDATED:
		arg_12_0.viewComponent.updateArchivePanel()
		arg_12_0.viewComponent.updateTargetPanel()
	elif var_12_0 == EducateProxy.TIEM_UPDATED:
		arg_12_0.viewComponent.updateDatePanel()
		arg_12_0.viewComponent.updateTargetPanel()
		arg_12_0.viewComponent.updatePaintingData()
	elif var_12_0 == EducateProxy.TIME_WEEKDAY_UPDATED:
		arg_12_0.viewComponent.updateWeekDay(var_12_1.weekDay)
	elif var_12_0 == EducateProxy.BUFF_ADDED:
		arg_12_0.viewComponent.updateArchivePanel()

		if not pg.NewStoryMgr.GetInstance().IsPlayed("tb_10"):
			arg_12_0.viewComponent.showArchivePanel()

		arg_12_0.viewComponent.OnCheckGuide()
	elif var_12_0 == EducateTaskProxy.TASK_UPDATED:
		arg_12_0.viewComponent.updateTargetPanel()
	elif var_12_0 == GAME.EDUCATE_UPGRADE_FAVOR_DONE:
		arg_12_0.viewComponent.ShowFavorUpgrade(var_12_1.drops, var_12_1.performs, var_12_1.cb)
	elif var_12_0 == GAME.EDUCATE_TRIGGER_SPEC_EVENT_DONE:
		if var_12_1.type == EducateSpecialEvent.TYPE_BUBBLE_MIND or var_12_1.type == EducateSpecialEvent.TYPE_BUBBLE_DISCOUNT:
			arg_12_0.viewComponent.ShowSpecialEvent(var_12_1.id, var_12_1.drops, var_12_1.cb)
	elif var_12_0 == GAME.EDUCATE_TRIGGER_EVENT_DONE:
		if pg.child_event[var_12_1.id].type == EducateEvent.TYPE_BUBBLE:
			arg_12_0.viewComponent.ShowEvent(var_12_1.id, var_12_1.drops, var_12_1.cb)
	elif var_12_0 == GAME.EDUCATE_SET_TARGET_DONE:
		arg_12_0.addSubLayers(Context.New({
			mediator = EducateTargetMediator,
			viewComponent = EducateTargetLayer
		}))
		arg_12_0.viewComponent.updateBottomPanel()
		arg_12_0.viewComponent.updateDatePanel()
		arg_12_0.viewComponent.updateTargetPanel()
		arg_12_0.viewComponent.updateMindTip()
		arg_12_0.viewComponent.OnCheckGuide()
	elif var_12_0 == GAME.EDUCATE_TRIGGER_END_DONE:
		arg_12_0.viewComponent.updateBottomPanel()
		arg_12_0.viewComponent.updateDatePanel()
		arg_12_0.viewComponent.updateTargetPanel()
		arg_12_0.viewComponent.updateMindTip()
		arg_12_0.viewComponent.OnCheckGuide()
	elif var_12_0 == GAME.EDUCATE_RESET_DONE or var_12_0 == GAME.EDUCATE_REFRESH_DONE:
		arg_12_0.viewComponent.emit(EducateBaseUI.EDUCATE_CHANGE_SCENE, SCENE.EDUCATE)
	elif var_12_0 == GAME.EDUCATE_EXECUTE_PLANS_DONE:
		local var_12_2 = var_12_1.isSkip

		arg_12_0.playPlansPerform(var_12_2, var_12_1)
	elif var_12_0 == GAME.EDUCATE_SUBMIT_TASK_DONE:
		arg_12_0.viewComponent.updateTargetPanel()
		arg_12_0.viewComponent.updateMindTip()
	elif var_12_0 == GAME.EDUCATE_GET_TARGET_AWARD_DONE:
		arg_12_0.viewComponent.updateTargetPanel()
	elif var_12_0 == EducateProxy.GUIDE_CHECK:
		if var_12_1.view == arg_12_0.viewComponent.__cname:
			arg_12_0.viewComponent.OnCheckGuide()
	elif var_12_0 == EducateProxy.MAIN_SCENE_ADD_LAYER:
		arg_12_0.addSubLayers(var_12_1)
	elif var_12_0 == EducateProxy.POLAROID_ADDED or var_12_0 == EducateProxy.MEMORY_ADDED:
		arg_12_0.viewComponent.updateBookNewTip()
	elif var_12_0 == EducateTaskProxy.TASK_ADDED or var_12_0 == EducateTaskProxy.TASK_REMOVED:
		arg_12_0.viewComponent.updateMindNewTip()
		arg_12_0.viewComponent.updateTargetPanel()
	elif var_12_0 == EducateProxy.CLEAR_NEW_TIP:
		if var_12_1.index == EducateTipHelper.NEW_MEMORY or var_12_1.index == EducateTipHelper.NEW_POLAROID:
			arg_12_0.viewComponent.updateBookNewTip()
		elif var_12_1.index == EducateTipHelper.NEW_MIND_TASK:
			arg_12_0.viewComponent.updateMindNewTip()

def var_0_0.playPlansPerform(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = {}

	table.insert(var_13_0, function(arg_14_0)
		arg_13_0.addSubLayers(Context.New({
			viewComponent = EducateCalendarLayer,
			mediator = EducateCalendarMediator,
			data = {
				onExit = arg_14_0
			}
		})))

	if not EducateConst.FORCE_SKIP_PLAN_PERFORM:
		table.insert(var_13_0, function(arg_15_0)
			arg_13_0.addSubLayers(Context.New({
				viewComponent = EducateSchedulePerformLayer,
				mediator = EducateSchedulePerformMediator,
				data = {
					gridData = arg_13_2.gridData,
					plan_results = arg_13_2.plan_results,
					events = arg_13_2.events,
					skip = arg_13_1,
					onExit = arg_15_0
				}
			})))

	table.insert(var_13_0, function(arg_16_0)
		arg_13_0.addSubLayers(Context.New({
			viewComponent = EducateScheduleResultLayer,
			mediator = EducateScheduleResultMediator,
			data = {
				plan_results = arg_13_2.plan_results,
				onExit = arg_16_0
			}
		})))
	seriesAsync(var_13_0, function()
		arg_13_0.viewComponent.FlushView())

return var_0_0

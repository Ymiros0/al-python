local var_0_0 = class("CastleMainMediator", import("..base.ContextMediator"))

var_0_0.CASTLE_ACT_OP = "castle act op"
var_0_0.ADD_ITEM = "add item"
var_0_0.UPDATE_ACTIVITY = "update activity"
var_0_0.CASTLE_FIRST_STORY_OP_DONE = "castle first story op:ne"
var_0_0.ON_TASK_SUBMIT = "on task submit"
var_0_0.UPDATE_GUIDE = "CastleMainMediator.UPDATE_GUIDE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.CASTLE_ACT_OP, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.CASTLE_ACT_OP, arg_2_1))
	arg_1_0.bind(var_0_0.ON_TASK_SUBMIT, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_3_1
		}))
	arg_1_0.bind(var_0_0.ADD_ITEM, function(arg_4_0, arg_4_1)
		return)
	arg_1_0.bind(var_0_0.UPDATE_ACTIVITY, function(arg_5_0, arg_5_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 2,
			activity_id = arg_5_1.id
		}))
	arg_1_0.bind(var_0_0.UPDATE_GUIDE, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.STORY_UPDATE, {
			storyId = arg_6_1
		}))

def var_0_0.initNotificationHandleDic(arg_7_0):
	arg_7_0.handleDic = {
		[GAME.CASTLE_STORY_OP_DONE] = function(arg_8_0, arg_8_1)
			local var_8_0 = arg_8_1.getBody()

			arg_8_0.viewComponent.StoryActEnd(var_8_0.number[1]),
		[GAME.CASTLE_DICE_OP_DONE] = function(arg_9_0, arg_9_1)
			local var_9_0 = arg_9_1.getBody()

			arg_9_0.viewComponent.RollDice(var_9_0.number[1], var_9_0.number[2]),
		[GAME.CASTLE_FIRST_STORY_OP_DONE] = function(arg_10_0, arg_10_1)
			arg_10_0.viewComponent.FirstStory(),
		[GAME.SUBMIT_TASK_DONE] = function(arg_11_0, arg_11_1)
			local var_11_0 = arg_11_1.getBody()

			arg_11_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_11_0, function()
				arg_11_0.viewComponent.UpdateFlush())
	}

return var_0_0

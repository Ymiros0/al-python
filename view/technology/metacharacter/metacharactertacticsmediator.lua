local var_0_0 = class("MetaCharacterTacticsMediator", import("...base.ContextMediator"))

var_0_0.GO_TASK = "MetaCharacterTacticsMediator:GO_TASK"
var_0_0.ON_SUBMIT = "MetaCharacterTacticsMediator:ON_SUBMIT"
var_0_0.ON_TRIGGER = "MetaCharacterTacticsMediator:ON_TRIGGER"
var_0_0.ON_SKILL = "MetaCharacterTacticsMediator:ON_SKILL"
var_0_0.ON_QUICK = "MetaCharacterTacticsMediator:ON_QUICK"

function var_0_0.register(arg_1_0)
	arg_1_0:requestTacticsData()
	arg_1_0:bindEvent()
end

function var_0_0.listNotificationInterests(arg_2_0)
	return {
		GAME.TACTICS_META_INFO_REQUEST_DONE,
		GAME.TACTICS_META_UNLOCK_SKILL_DONE,
		GAME.TACTICS_META_SWITCH_SKILL_DONE,
		GAME.TACTICS_META_LEVELUP_SKILL_DONE,
		GAME.META_QUICK_TACTICS_DONE
	}
end

function var_0_0.handleNotification(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:getName()
	local var_3_1 = arg_3_1:getBody()

	if var_3_0 == GAME.TACTICS_META_INFO_REQUEST_DONE then
		local var_3_2 = var_3_1

		arg_3_0.viewComponent:setTacticsData(var_3_2)
		arg_3_0.viewComponent:updateTacticsRedTag()
		arg_3_0.viewComponent:updateExpPanel()
		arg_3_0.viewComponent:updateMain()
		arg_3_0.viewComponent:updateSkillTFLearning()
	elseif var_3_0 == GAME.TACTICS_META_UNLOCK_SKILL_DONE then
		local var_3_3 = arg_3_0.viewComponent:isAllSkillLock()

		arg_3_0.viewComponent:updateData()
		arg_3_0.viewComponent:updateSkillListPanel()
		arg_3_0.viewComponent:updateMain()

		if var_3_3 then
			arg_3_0.viewComponent:tryLearnSkillAfterFirstUnlock()
		end

		arg_3_0.viewComponent:closeUnlockSkillPanel()
	elseif var_3_0 == GAME.TACTICS_META_SWITCH_SKILL_DONE then
		local var_3_4 = var_3_1.skillID
		local var_3_5 = var_3_1.leftSwitchCount

		arg_3_0.viewComponent:switchTacticsSkillData(var_3_4, var_3_5)
		arg_3_0.viewComponent:updateExpPanel()
		arg_3_0.viewComponent:updateTaskPanel(var_3_4)
		arg_3_0.viewComponent:updateSkillTFLearning()
	elseif var_3_0 == GAME.TACTICS_META_LEVELUP_SKILL_DONE then
		local var_3_6 = var_3_1.skillID
		local var_3_7 = var_3_1.leftSwitchCount

		arg_3_0.viewComponent:updateData()
		arg_3_0.viewComponent:levelupTacticsSkillData(var_3_6, var_3_7)
		arg_3_0.viewComponent:updateTacticsRedTag()
		arg_3_0.viewComponent:updateSkillListPanel()
		arg_3_0.viewComponent:updateTaskPanel(var_3_6)
	elseif var_3_0 == GAME.META_QUICK_TACTICS_DONE then
		local var_3_8 = var_3_1.skillID
		local var_3_9 = var_3_1.skillExp

		if var_3_1.isLevelUp then
			arg_3_0.viewComponent:clearTaskInfo(var_3_8)
		end

		arg_3_0.viewComponent:updateSkillExp(var_3_8, var_3_9)
		arg_3_0.viewComponent:updateData()
		arg_3_0.viewComponent:updateTacticsRedTag()
		arg_3_0.viewComponent:updateSkillListPanel()
		arg_3_0.viewComponent:updateTaskPanel(var_3_8)
	end
end

function var_0_0.bindEvent(arg_4_0)
	arg_4_0:bind(var_0_0.ON_QUICK, function(arg_5_0, arg_5_1, arg_5_2)
		arg_4_0:addSubLayers(Context.New({
			mediator = MetaQuickTacticsMediator,
			viewComponent = MetaQuickTacticsLayer,
			data = {
				shipID = arg_5_1,
				skillID = arg_5_2
			}
		}))
	end)
end

function var_0_0.requestTacticsData(arg_6_0)
	arg_6_0:sendNotification(GAME.TACTICS_META_INFO_REQUEST, {
		id = arg_6_0.contextData.shipID
	})
end

return var_0_0

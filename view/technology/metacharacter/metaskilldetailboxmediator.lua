local var_0_0 = class("MetaSkillDetailBoxMediator", import("...base.ContextMediator"))

function var_0_0.register(arg_1_0)
	return
end

function var_0_0.listNotificationInterests(arg_2_0)
	return {
		GAME.TACTICS_META_UNLOCK_SKILL_DONE,
		GAME.TACTICS_META_SWITCH_SKILL_DONE
	}
end

function var_0_0.handleNotification(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:getName()
	local var_3_1 = arg_3_1:getBody()

	if var_3_0 == GAME.TACTICS_META_UNLOCK_SKILL_DONE or var_3_0 == GAME.TACTICS_META_SWITCH_SKILL_DONE then
		if var_3_0 == GAME.TACTICS_META_SWITCH_SKILL_DONE then
			local var_3_2 = arg_3_0.contextData.expInfoList

			if var_3_2 and #var_3_2 > 0 then
				local var_3_3 = arg_3_0.contextData.metaShipID
				local var_3_4

				for iter_3_0, iter_3_1 in ipairs(var_3_2) do
					if iter_3_1.shipID == var_3_3 and iter_3_1.isUpLevel and iter_3_1.isMaxLevel then
						var_3_4 = iter_3_0
					end
				end

				if var_3_4 then
					var_3_2[var_3_4].isUpLevel = false
					var_3_2[var_3_4].isMaxLevel = false
				end
			end
		end

		arg_3_0.viewComponent:updateSkillList()
	end
end

return var_0_0

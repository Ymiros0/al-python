local var_0_0 = class("KwxyKrTracker")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	return
end

function var_0_0.Tracking(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4)
	if arg_2_1 == TRACKING_TUTORIAL_COMPLETE_1 then
		pg.SdkMgr.GetInstance():CompletedTutorial()
		pg.SdkMgr.GetInstance():UnlockAchievement()
	elseif arg_2_1 == TRACKING_USER_LEVELUP then
		pg.SdkMgr.GetInstance():SdkLevelUp(arg_2_4, arg_2_3)
	end
end

return var_0_0

local var_0_0 = class("SurveyStateCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	pg.ConnectionMgr.GetInstance():Send(11027, {
		survey_id = var_1_0.surveyID
	}, 11028, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(ActivityProxy):setSurveyState(arg_2_0.result)
		elseif arg_2_0.result > 0 then
			getProxy(ActivityProxy):setSurveyState(arg_2_0.result)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0

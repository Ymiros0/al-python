local var_0_0 = class("SurveyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(11025, {
		survey_id = var_1_0.surveyID
	}, 11026, function(arg_2_0)
		if arg_2_0.result == 0:
			print(var_1_0.surveyID, var_1_0.surveyUrlStr)
			pg.SdkMgr.GetInstance().Survey(var_1_0.surveyUrlStr)

			if IsUnityEditor:
				Application.OpenURL(var_1_0.surveyUrlStr)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0

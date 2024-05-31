local var_0_0 = class("SurveyPage", import("...base.BaseActivityPage"))

def var_0_0.SetEnterTag(arg_1_0):
	PlayerPrefs.SetInt("survey_enter_" .. tostring(arg_1_0), 1)

def var_0_0.IsEverEnter(arg_2_0):
	return PlayerPrefs.HasKey("survey_enter_" .. tostring(arg_2_0))

def var_0_0.ClearEnterTag(arg_3_0):
	PlayerPrefs.DeleteKey("survey_enter_" .. tostring(arg_3_0))

def var_0_0.OnInit(arg_4_0):
	arg_4_0.bg = arg_4_0.findTF("BG")
	arg_4_0.bguo = arg_4_0.findTF("BGUO")
	arg_4_0.goBtn = arg_4_0.findTF("GO")
	arg_4_0.awardTF = arg_4_0.findTF("Award")
	arg_4_0.itemTF = arg_4_0.findTF("Award/IconTpl")
	arg_4_0.maskTF = arg_4_0.findTF("Award/Mask")
	arg_4_0.actProxy = getProxy(ActivityProxy)
	arg_4_0.isOpen, arg_4_0.surveyID = arg_4_0.actProxy.isSurveyOpen()

	if arg_4_0.isOpen:
		arg_4_0.isDone = arg_4_0.actProxy.isSurveyDone()

	setActive(arg_4_0.bg, True)
	setActive(arg_4_0.bguo, False)
	setActive(arg_4_0.goBtn, True)

def var_0_0.OnFirstFlush(arg_5_0):
	setActive(arg_5_0.maskTF, arg_5_0.isDone == True)
	setActive(arg_5_0.goBtn, not arg_5_0.isDone)

	local var_5_0 = pg.survey_data_template[arg_5_0.surveyID].bonus[1]
	local var_5_1 = {
		type = var_5_0[1],
		id = var_5_0[2],
		count = var_5_0[3]
	}

	updateDrop(arg_5_0.itemTF, var_5_1)
	onButton(arg_5_0, arg_5_0.itemTF, function()
		arg_5_0.emit(BaseUI.ON_DROP, var_5_1), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.goBtn, function()
		pg.m02.sendNotification(GAME.SURVEY_REQUEST, {
			surveyID = arg_5_0.surveyID,
			surveyUrlStr = getSurveyUrl(arg_5_0.surveyID)
		})

		if IsUnityEditor:
			var_0_0.ClearEnterTag(arg_5_0.surveyID), SFX_PANEL)
	var_0_0.SetEnterTag(arg_5_0.surveyID)

return var_0_0

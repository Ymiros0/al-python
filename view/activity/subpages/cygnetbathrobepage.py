local var_0_0 = class("CygnetBathrobePage", import("...base.BaseActivityPage"))

var_0_0.MAX_COUNT = 7

def var_0_0.OnInit(arg_1_0):
	arg_1_0.drawBtn = arg_1_0.findTF("DrawBtn")
	arg_1_0.resultTF = arg_1_0.findTF("ResultImg")
	arg_1_0.resultImgLittle = arg_1_0.findTF("Little", arg_1_0.resultTF)
	arg_1_0.resultImgMiddle = arg_1_0.findTF("Middle", arg_1_0.resultTF)
	arg_1_0.resultImgBig = arg_1_0.findTF("Big", arg_1_0.resultTF)
	arg_1_0.progressTF = arg_1_0.findTF("Progress")
	arg_1_0.progressText = arg_1_0.findTF("Progress/ProgressText")
	arg_1_0.gotImg = arg_1_0.findTF("GotImg")
	arg_1_0.awardPanel = arg_1_0.findTF("AwardPanel")
	arg_1_0.itemTpl = arg_1_0.findTF("itemTpl", arg_1_0.awardPanel)
	arg_1_0.resultTextTF = arg_1_0.findTF("ResultImg", arg_1_0.awardPanel)
	arg_1_0.resultTextLittle = arg_1_0.findTF("ResultImg/Little", arg_1_0.awardPanel)
	arg_1_0.resultTextMiddle = arg_1_0.findTF("ResultImg/Middle", arg_1_0.awardPanel)
	arg_1_0.resultTextBig = arg_1_0.findTF("ResultImg/Big", arg_1_0.awardPanel)
	arg_1_0.itemTplContainer = arg_1_0.findTF("AwardList", arg_1_0.awardPanel)
	arg_1_0.animTF = arg_1_0.findTF("Anim")

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.progressNum = arg_2_0.activity.data1
	arg_2_0.resultNum = arg_2_0.activity.data2
	arg_2_0.awardDayList = arg_2_0.activity.data1_list
	arg_2_0.isFinished = arg_2_0.progressNum > var_0_0.MAX_COUNT
	arg_2_0.isAvailable = not (arg_2_0.resultNum > 0)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.drawBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_3_0.activity.id
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_5_0):
	setActive(arg_5_0.drawBtn, arg_5_0.isAvailable)
	setActive(arg_5_0.resultTF, not arg_5_0.isAvailable)

	if not arg_5_0.isAvailable:
		for iter_5_0 = 1, arg_5_0.resultTF.childCount:
			setActive(arg_5_0.resultTF.GetChild(iter_5_0 - 1), iter_5_0 == arg_5_0.resultNum)

	setActive(arg_5_0.progressTF, not arg_5_0.isFinished)
	setActive(arg_5_0.gotImg, arg_5_0.isFinished)

	if not arg_5_0.isFinished:
		setText(arg_5_0.progressText, arg_5_0.progressNum .. "/" .. var_0_0.MAX_COUNT)

	local var_5_0 = arg_5_0.activity.getConfig("config_data")[2]

	if var_5_0:
		local var_5_1 = _.filter(var_5_0, function(arg_6_0)
			for iter_6_0, iter_6_1 in ipairs(arg_5_0.activity.data1_list):
				if iter_6_1 == arg_6_0[1]:
					return False

			return True)

		for iter_5_1, iter_5_2 in ipairs(var_5_1):
			if arg_5_0.progressNum == iter_5_2[1]:
				arg_5_0.emit(ActivityMediator.EVENT_OPERATION, {
					cmd = 2,
					activity_id = arg_5_0.activity.id,
					arg1 = iter_5_2[1]
				})

				return

def var_0_0.OnDestroy(arg_7_0):
	return

def var_0_0.showLotteryAwardResult(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	GetComponent(arg_8_0.animTF, typeof(DftAniEvent)).SetEndEvent(function(arg_9_0)
		setActive(arg_8_0.animTF, False)
		setActive(arg_8_0.awardPanel, True)

		for iter_9_0 = 1, arg_8_0.resultTextTF.childCount:
			setActive(arg_8_0.resultTextTF.GetChild(iter_9_0 - 1), iter_9_0 == arg_8_2)

		removeAllChildren(arg_8_0.itemTplContainer)

		for iter_9_1, iter_9_2 in ipairs(arg_8_1):
			local var_9_0 = cloneTplTo(arg_8_0.itemTpl, arg_8_0.itemTplContainer)
			local var_9_1 = {
				type = iter_9_2.type,
				id = iter_9_2.id,
				count = iter_9_2.count
			}

			updateDrop(var_9_0, var_9_1)
			onButton(arg_8_0, var_9_0, function()
				arg_8_0.emit(BaseUI.ON_DROP, var_9_1), SFX_PANEL)

		arg_8_0.emit(ActivityMainScene.LOCK_ACT_MAIN, False)
		arg_8_3()
		onButton(arg_8_0, arg_8_0.awardPanel, function()
			setActive(arg_8_0.awardPanel, False)))
	setActive(arg_8_0.animTF, True)
	arg_8_0.emit(ActivityMainScene.LOCK_ACT_MAIN, True)

def var_0_0.IsTip():
	local var_12_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.CYGNET_BATHROBE_PAGE_ID)

	if var_12_0 and not var_12_0.isEnd():
		return var_12_0.data2 <= 0

return var_0_0

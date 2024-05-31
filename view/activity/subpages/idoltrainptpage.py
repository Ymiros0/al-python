local var_0_0 = class("IdolTrainPtPage", import(".TemplatePage.PtTemplatePage"))
local var_0_1 = {
	"dafeng_idol",
	"tashigan_idol",
	"daiduo_idol",
	"daqinghuayu_idol",
	"baerdimo_idol",
	"luoen_idol",
	"guanghui_idol",
	"edu_idol"
}

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.skills = arg_1_0.findTF("skill", arg_1_0.bg)
	arg_1_0.skillBtns = {}

	eachChild(arg_1_0.skills, function(arg_2_0)
		table.insert(arg_1_0.skillBtns, arg_2_0))

	arg_1_0.getGreyBtn = arg_1_0.findTF("get_grey_btn", arg_1_0.bg)
	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)
	arg_1_0.idol1 = arg_1_0.findTF("idol1", arg_1_0.bg)
	arg_1_0.idol2 = arg_1_0.findTF("idol2", arg_1_0.bg)
	arg_1_0.buffInfoBox = arg_1_0.findTF("BuffInfoBox")
	arg_1_0.mask = arg_1_0.findTF("mengban", arg_1_0.buffInfoBox)
	arg_1_0.buffWindow = arg_1_0.findTF("panel", arg_1_0.buffInfoBox)
	arg_1_0.buffName = arg_1_0.findTF("title/name", arg_1_0.buffWindow)
	arg_1_0.titleLv = arg_1_0.findTF("title/lv", arg_1_0.buffWindow)
	arg_1_0.titleIcon = arg_1_0.findTF("title/icon", arg_1_0.buffWindow)
	arg_1_0.buffTip = arg_1_0.findTF("content/tip", arg_1_0.buffWindow)
	arg_1_0.desc = arg_1_0.findTF("content/desc", arg_1_0.buffWindow)
	arg_1_0.buffAwardTF = arg_1_0.findTF("award_bg/award", arg_1_0.buffWindow)
	arg_1_0.trainWindow = arg_1_0.findTF("IdolTrainWindow")
	arg_1_0.trainTitle = arg_1_0.findTF("panel/title/Text", arg_1_0.trainWindow)
	arg_1_0.trainBtn = arg_1_0.findTF("panel/train_btn", arg_1_0.trainWindow)
	arg_1_0.trainSkills = arg_1_0.findTF("panel/skills", arg_1_0.trainWindow)
	arg_1_0.trainSkillBtns = {}

	eachChild(arg_1_0.trainSkills, function(arg_3_0)
		table.insert(arg_1_0.trainSkillBtns, arg_3_0))

	arg_1_0.info = arg_1_0.findTF("panel/info", arg_1_0.trainWindow)
	arg_1_0.curBuff = arg_1_0.findTF("preview/current", arg_1_0.info)
	arg_1_0.nextBuff = arg_1_0.findTF("preview/next", arg_1_0.info)
	arg_1_0.msgBox = arg_1_0.findTF("MsgBox")
	arg_1_0.msgIcon = arg_1_0.findTF("panel/title/icon", arg_1_0.msgBox)
	arg_1_0.msgContent = arg_1_0.findTF("panel/content", arg_1_0.msgBox)
	arg_1_0.msgBoxMask = arg_1_0.findTF("mengban", arg_1_0.msgBox)
	arg_1_0.cancelBtn = arg_1_0.findTF("panel/cancel_btn", arg_1_0.msgBox)
	arg_1_0.confirmBtn = arg_1_0.findTF("panel/confirm_btn", arg_1_0.msgBox)
	arg_1_0.tipPanel = arg_1_0.findTF("Tip")

def var_0_0.OnFirstFlush(arg_4_0):
	var_0_0.super.OnFirstFlush(arg_4_0)
	removeOnButton(arg_4_0.getBtn)
	onButton(arg_4_0, arg_4_0.getBtn, function()
		local var_5_0 = {}
		local var_5_1 = arg_4_0.ptData.GetAward()
		local var_5_2 = getProxy(PlayerProxy).getData()

		if var_5_1.type == DROP_TYPE_RESOURCE and var_5_1.id == PlayerConst.ResGold and var_5_2.GoldMax(var_5_1.count):
			table.insert(var_5_0, function(arg_6_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("gold_max_tip_title") .. i18n("award_max_warning"),
					onYes = arg_6_0
				}))

		seriesAsync(var_5_0, function()
			local var_7_0, var_7_1 = arg_4_0.ptData.GetResProgress()

			arg_4_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_4_0.ptData.GetId(),
				arg1 = var_7_1
			})

			if arg_4_0.ptData.CanTrain():
				arg_4_0.showTrianPanel()

			arg_4_0.playIdolAni()), SFX_PANEL)
	removeOnButton(arg_4_0.battleBtn)
	onButton(arg_4_0, arg_4_0.battleBtn, function()
		local var_8_0
		local var_8_1

		if arg_4_0.activity.getConfig("config_client") != "":
			var_8_0 = arg_4_0.activity.getConfig("config_client").linkActID

			if var_8_0:
				var_8_1 = getProxy(ActivityProxy).getActivityById(var_8_0)

		if not var_8_0:
			arg_4_0.emit(ActivityMediator.BATTLE_OPERA)
		elif var_8_1 and not var_8_1.isEnd():
			arg_4_0.emit(ActivityMediator.BATTLE_OPERA)
		else
			arg_4_0.showTip(i18n("common_activity_end")), SFX_PANEL)
	arg_4_0.hideBuffInfoBox()
	onButton(arg_4_0, arg_4_0.mask, function()
		arg_4_0.hideBuffInfoBox(), SFX_PANEL)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.skillBtns):
		onButton(arg_4_0, iter_4_1, function()
			for iter_10_0, iter_10_1 in ipairs(arg_4_0.ptData.GetCurBuffInfos()):
				if iter_4_0 == iter_10_1.group:
					arg_4_0.showBuffInfoBox(iter_10_1), SFX_PANEL)

	local var_4_0, var_4_1 = arg_4_0.getRandomName()

	pg.UIMgr.GetInstance().LoadingOn()
	PoolMgr.GetInstance().GetSpineChar(var_4_0, True, function(arg_11_0)
		pg.UIMgr.GetInstance().LoadingOff()

		arg_4_0.prefab1 = var_4_0
		arg_4_0.model1 = arg_11_0
		tf(arg_11_0).localScale = Vector3(1, 1, 1)

		arg_11_0.GetComponent("SpineAnimUI").SetAction("stand2", 0)
		setParent(arg_11_0, arg_4_0.idol1))
	pg.UIMgr.GetInstance().LoadingOn()
	PoolMgr.GetInstance().GetSpineChar(var_4_1, True, function(arg_12_0)
		pg.UIMgr.GetInstance().LoadingOff()

		arg_4_0.prefab2 = var_4_1
		arg_4_0.model2 = arg_12_0
		tf(arg_12_0).localScale = Vector3(1, 1, 1)

		arg_12_0.GetComponent("SpineAnimUI").SetAction("stand2", 0)
		setParent(arg_12_0, arg_4_0.idol2))

def var_0_0.OnUpdateFlush(arg_13_0):
	local var_13_0 = arg_13_0.ptData.CanTrain()

	if var_13_0 and var_13_0 <= arg_13_0.ptData.level:
		arg_13_0.showTrianPanel()

	local var_13_1, var_13_2, var_13_3 = arg_13_0.ptData.GetLevelProgress()
	local var_13_4, var_13_5, var_13_6 = arg_13_0.ptData.GetResProgress()

	setText(arg_13_0.step, setColorStr("PHASE  " .. var_13_1 .. "/", COLOR_WHITE) .. var_13_2)
	setText(arg_13_0.progress, (var_13_6 >= 1 and setColorStr(var_13_4 .. "/", COLOR_WHITE) or var_13_4 .. "/") .. var_13_5)
	setSlider(arg_13_0.slider, 0, 1, var_13_6)

	local var_13_7 = arg_13_0.ptData.CanGetAward()
	local var_13_8 = arg_13_0.ptData.CanGetNextAward()
	local var_13_9 = arg_13_0.ptData.CanGetMorePt()
	local var_13_10 = arg_13_0.ptData.CanTrain()

	setActive(arg_13_0.battleBtn, var_13_9 and not var_13_7 and var_13_8)
	setActive(arg_13_0.getBtn, var_13_7)
	setActive(arg_13_0.getGreyBtn, not var_13_7)
	setActive(arg_13_0.gotBtn, not var_13_8 and not var_13_10)

	local var_13_11 = arg_13_0.ptData.GetAward()

	updateDrop(arg_13_0.awardTF, var_13_11)
	onButton(arg_13_0, arg_13_0.awardTF, function()
		arg_13_0.emit(BaseUI.ON_DROP, var_13_11), SFX_PANEL)

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.ptData.GetCurBuffInfos()):
		setActive(arg_13_0.findTF("lv1", arg_13_0.skillBtns[iter_13_1.group]), False)
		setActive(arg_13_0.findTF("lv2", arg_13_0.skillBtns[iter_13_1.group]), False)
		setActive(arg_13_0.findTF("lv3", arg_13_0.skillBtns[iter_13_1.group]), False)

		if iter_13_1.next:
			setActive(arg_13_0.findTF("lv" .. iter_13_1.lv, arg_13_0.skillBtns[iter_13_1.group]), True)
		else
			setActive(arg_13_0.findTF("lv3", arg_13_0.skillBtns[iter_13_1.group]), True)

		local var_13_12 = pg.benefit_buff_template[iter_13_1.id].icon

		setImageSprite(arg_13_0.findTF("icon", arg_13_0.skillBtns[iter_13_1.group]), LoadSprite(var_13_12))

	onButton(arg_13_0, arg_13_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("practise_idol_help")
		}), SFX_PANEL)

def var_0_0.showTrianPanel(arg_16_0):
	setActive(arg_16_0.trainWindow, True)
	setText(arg_16_0.trainTitle, i18n("upgrade_idol_tip"))

	local var_16_0 = arg_16_0.ptData.GetCurBuffInfos()

	arg_16_0.selectIndex = None
	arg_16_0.selectBuffId = None
	arg_16_0.selectBuffLv = None
	arg_16_0.selectNewBuffId = None

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.trainSkillBtns):
		onButton(arg_16_0, iter_16_1, function()
			for iter_17_0, iter_17_1 in ipairs(var_16_0):
				if iter_16_0 == iter_17_1.group:
					if iter_17_1.next:
						arg_16_0.selectIndex = iter_16_0
						arg_16_0.selectBuffId = iter_17_1.id
						arg_16_0.selectNewBuffId = iter_17_1.next
						arg_16_0.selectBuffLv = iter_17_1.lv
					else
						arg_16_0.selectIndex = None
						arg_16_0.selectBuffId = None
						arg_16_0.selectNewBuffId = None
						arg_16_0.selectBuffLv = None

			arg_16_0.flushTrainPanel(), SFX_PANEL)

	onButton(arg_16_0, arg_16_0.trainBtn, function()
		arg_16_0.showMsgBox(), SFX_PANEL)
	arg_16_0.flushTrainPanel()

def var_0_0.hideTrianPanel(arg_19_0):
	setActive(arg_19_0.trainWindow, False)

def var_0_0.flushTrainPanel(arg_20_0):
	local var_20_0 = arg_20_0.ptData.GetCurBuffInfos()

	if var_20_0:
		for iter_20_0, iter_20_1 in ipairs(var_20_0):
			setActive(arg_20_0.findTF("lv1", arg_20_0.trainSkillBtns[iter_20_1.group]), False)
			setActive(arg_20_0.findTF("lv2", arg_20_0.trainSkillBtns[iter_20_1.group]), False)
			setActive(arg_20_0.findTF("lv3", arg_20_0.trainSkillBtns[iter_20_1.group]), False)

			if iter_20_1.next:
				setActive(arg_20_0.findTF("lv" .. iter_20_1.lv, arg_20_0.trainSkillBtns[iter_20_1.group]), True)
			else
				setActive(arg_20_0.findTF("lv3", arg_20_0.trainSkillBtns[iter_20_1.group]), True)

			local var_20_1 = pg.benefit_buff_template[iter_20_1.id].icon

			setImageSprite(arg_20_0.findTF("icon", arg_20_0.trainSkillBtns[iter_20_1.group]), LoadSprite(var_20_1))
			setText(arg_20_0.findTF("name", arg_20_0.trainSkillBtns[iter_20_1.group]), shortenString(pg.benefit_buff_template[iter_20_1.id].name, 7))

	for iter_20_2, iter_20_3 in ipairs(arg_20_0.trainSkillBtns):
		if iter_20_2 == arg_20_0.selectIndex:
			setActive(arg_20_0.findTF("selected", iter_20_3), True)
			setActive(arg_20_0.findTF("name", iter_20_3), True)
		else
			setActive(arg_20_0.findTF("selected", iter_20_3), False)
			setActive(arg_20_0.findTF("name", iter_20_3), False)

	if arg_20_0.selectIndex:
		setActive(arg_20_0.info, True)
		setActive(arg_20_0.trainBtn, True)
		setText(arg_20_0.curBuff, "Lv." .. arg_20_0.selectBuffLv .. pg.benefit_buff_template[arg_20_0.selectBuffId].desc)
		setText(arg_20_0.nextBuff, "Lv." .. arg_20_0.selectBuffLv + 1 .. pg.benefit_buff_template[arg_20_0.selectNewBuffId].desc)
	else
		setActive(arg_20_0.info, False)
		setActive(arg_20_0.trainBtn, False)

def var_0_0.showBuffInfoBox(arg_21_0, arg_21_1):
	local var_21_0 = pg.benefit_buff_template[arg_21_1.id].name

	setText(arg_21_0.buffName, var_21_0)
	setText(arg_21_0.desc, pg.benefit_buff_template[arg_21_1.id].desc)
	setText(arg_21_0.buffTip, i18n("upgrade_introduce_tip", var_21_0))

	local var_21_1 = pg.benefit_buff_template[arg_21_1.id].icon

	setImageSprite(arg_21_0.titleIcon, LoadSprite(var_21_1))

	local var_21_2 = arg_21_1.award

	updateDrop(arg_21_0.buffAwardTF, var_21_2)
	onButton(arg_21_0, arg_21_0.buffAwardTF, function()
		arg_21_0.emit(BaseUI.ON_DROP, var_21_2), SFX_PANEL)

	if arg_21_1.next:
		setText(arg_21_0.titleLv, "Lv." .. arg_21_1.lv)
		setActive(arg_21_0.findTF("icon_bg/got_mask", arg_21_0.buffAwardTF), False)
	else
		setText(arg_21_0.titleLv, "MAX")
		setActive(arg_21_0.findTF("icon_bg/got_mask", arg_21_0.buffAwardTF), True)
		removeOnButton(arg_21_0.buffAwardTF)

	setActive(arg_21_0.buffInfoBox, True)

def var_0_0.hideBuffInfoBox(arg_23_0):
	setActive(arg_23_0.buffInfoBox, False)

def var_0_0.OnDestroy(arg_24_0):
	if arg_24_0.prefab1 and arg_24_0.model1:
		PoolMgr.GetInstance().ReturnSpineChar(arg_24_0.prefab1, arg_24_0.model1)

		arg_24_0.prefab1 = None
		arg_24_0.model1 = None

	if arg_24_0.prefab2 and arg_24_0.model2:
		PoolMgr.GetInstance().ReturnSpineChar(arg_24_0.prefab2, arg_24_0.model2)

		arg_24_0.prefab2 = None
		arg_24_0.model2 = None

def var_0_0.getRandomName(arg_25_0):
	local var_25_0 = math.random(#var_0_1)
	local var_25_1

	while var_25_1 == var_25_0 or not var_25_1:
		var_25_1 = math.random(#var_0_1)

	return var_0_1[var_25_0], var_0_1[var_25_1]

def var_0_0.playIdolAni(arg_26_0):
	if arg_26_0.model1:
		arg_26_0.model1.GetComponent("SpineAnimUI").SetAction("idol", 0)

	if arg_26_0.model2:
		arg_26_0.model2.GetComponent("SpineAnimUI").SetAction("idol", 0)

def var_0_0.showMsgBox(arg_27_0):
	if arg_27_0.selectBuffId:
		setActive(arg_27_0.msgBox, True)

		local var_27_0 = pg.benefit_buff_template[arg_27_0.selectBuffId].icon

		setImageSprite(arg_27_0.msgIcon, LoadSprite(var_27_0))

		local var_27_1 = pg.benefit_buff_template[arg_27_0.selectBuffId].name

		setText(arg_27_0.msgContent, i18n("practise_idol_tip", var_27_1))
		onButton(arg_27_0, arg_27_0.msgBoxMask, function()
			arg_27_0.hideMsgBox(), SFX_PANEL)
		onButton(arg_27_0, arg_27_0.cancelBtn, function()
			arg_27_0.hideMsgBox(), SFX_PANEL)
		onButton(arg_27_0, arg_27_0.confirmBtn, function()
			arg_27_0.hideMsgBox()
			arg_27_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 3,
				activity_id = arg_27_0.ptData.GetId(),
				arg1 = arg_27_0.ptData.CanTrain(),
				arg2 = arg_27_0.selectNewBuffId,
				oldBuffId = arg_27_0.selectBuffId
			})
			arg_27_0.hideTrianPanel()
			arg_27_0.showTip(i18n("upgrade_complete_tip")), SFX_PANEL)

def var_0_0.hideMsgBox(arg_31_0):
	setActive(arg_31_0.msgBox, False)

def var_0_0.showTip(arg_32_0, arg_32_1):
	local var_32_0 = cloneTplTo(arg_32_0.tipPanel, arg_32_0._tf)

	setActive(var_32_0, True)
	setText(arg_32_0.findTF("Text", var_32_0), arg_32_1)

	var_32_0.transform.localScale = Vector3(0, 0.1, 1)

	LeanTween.scale(var_32_0, Vector3(1.8, 0.1, 1), 0.1).setUseEstimatedTime(True)
	LeanTween.scale(var_32_0, Vector3(1.1, 1.1, 1), 0.1).setDelay(0.1).setUseEstimatedTime(True)

	local var_32_1 = GetOrAddComponent(var_32_0, "CanvasGroup")

	Timer.New(function()
		if IsNil(var_32_0):
			return

		LeanTween.scale(var_32_0, Vector3(0.1, 1.5, 1), 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
			LeanTween.scale(var_32_0, Vector3.zero, 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
				Destroy(var_32_0))))), 3).Start()

return var_0_0

local var_0_0 = class("TrophyGalleryLayer", import("..base.BaseUI"))

var_0_0.Filter = {
	"all",
	"claimed",
	"unclaim"
}

def var_0_0.getUIName(arg_1_0):
	return "TrophyGalleryUI"

def var_0_0.setTrophyGroups(arg_2_0, arg_2_1):
	arg_2_0.trophyGroups = arg_2_1

def var_0_0.setTrophyList(arg_3_0, arg_3_1):
	arg_3_0.trophyList = arg_3_1

def var_0_0.init(arg_4_0):
	arg_4_0._bg = arg_4_0.findTF("bg")
	arg_4_0._blurPanel = arg_4_0.findTF("blur_panel")
	arg_4_0._topPanel = arg_4_0.findTF("adapt/top", arg_4_0._blurPanel)
	arg_4_0._backBtn = arg_4_0._topPanel.Find("back_btn")
	arg_4_0._helpBtn = arg_4_0._topPanel.Find("help_btn")
	arg_4_0._center = arg_4_0.findTF("bg/taskBGCenter")
	arg_4_0._trophyUpperTpl = arg_4_0.getTpl("trophy_upper", arg_4_0._center)
	arg_4_0._trophyLowerTpl = arg_4_0.getTpl("trophy_lower", arg_4_0._center)
	arg_4_0._trophyContainer = arg_4_0.findTF("bg/taskBGCenter/right_panel/Grid")
	arg_4_0._scrllPanel = arg_4_0.findTF("bg/taskBGCenter/right_panel")
	arg_4_0._scrollView = arg_4_0._scrllPanel.GetComponent("LScrollRect")
	arg_4_0._trophyDetailPanel = TrophyDetailPanel.New(arg_4_0.findTF("trophyPanel"), arg_4_0._tf)
	arg_4_0._filterBtn = arg_4_0.findTF("filter/toggle", arg_4_0._topPanel)
	arg_4_0._trophyCounter = arg_4_0.findTF("filter/counter/Text", arg_4_0._topPanel)
	arg_4_0._reminderRes = arg_4_0.findTF("bg/resource")
	arg_4_0._trophyTFList = {}

def var_0_0.didEnter(arg_5_0):
	pg.LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_5_0._tf, {
		weight = LayerWeightConst.SECOND_LAYER
	})
	onButton(arg_5_0, arg_5_0._backBtn, function()
		arg_5_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0._filterBtn, function()
		arg_5_0.onFilter(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0._helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.medal_help_tip.tip
		}), SFX_PANEL)

	arg_5_0._filterIndex = 0

	triggerButton(arg_5_0._filterBtn)
	arg_5_0.updateTrophyCounter()

def var_0_0.updateTrophyList(arg_9_0):
	arg_9_0._trophyTFList = {}

	removeAllChildren(arg_9_0._trophyContainer)

	local var_9_0 = var_0_0.Filter[arg_9_0._filterIndex]
	local var_9_1 = 0

	for iter_9_0, iter_9_1 in pairs(arg_9_0.trophyGroups):
		local var_9_2

		if var_9_0 == "all":
			var_9_2 = True
		elif var_9_0 == "claimed":
			var_9_2 = iter_9_1.getMaxClaimedTrophy() != None
		elif var_9_0 == "unclaim":
			var_9_2 = not iter_9_1.getProgressTrophy().isClaimed()

		if var_9_2:
			local var_9_3

			if math.fmod(var_9_1, 2) == 0:
				var_9_3 = arg_9_0._trophyUpperTpl
			else
				var_9_3 = arg_9_0._trophyLowerTpl

			local var_9_4 = cloneTplTo(var_9_3, arg_9_0._trophyContainer)
			local var_9_5 = TrophyView.New(var_9_4)

			if var_9_0 == "all":
				var_9_5.UpdateTrophyGroup(iter_9_1)
			elif var_9_0 == "claimed":
				var_9_5.ClaimForm(iter_9_1)
			elif var_9_0 == "unclaim":
				var_9_5.ProgressingForm(iter_9_1)

			local var_9_6 = var_9_5.GetTrophyClaimTipsID()

			var_9_5.SetTrophyReminder(Instantiate(arg_9_0._reminderRes.Find(var_9_6)))

			arg_9_0._trophyTFList[iter_9_0] = var_9_5
			var_9_1 = var_9_1 + 1

			onButton(arg_9_0, var_9_4.transform.Find("frame"), function()
				local var_10_0 = arg_9_0.trophyGroups[iter_9_0]
				local var_10_1 = var_10_0.getProgressTrophy()

				if var_10_1.canClaimed() and not var_10_1.isClaimed():
					if not var_9_5.IsPlaying():
						arg_9_0.emit(TrophyGalleryMediator.ON_TROPHY_CLAIM, var_10_1.id)
				else
					arg_9_0.openTrophyDetail(var_10_0, var_10_1))

def var_0_0.PlayTrophyClaim(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.trophyGroups[arg_11_1]
	local var_11_1 = arg_11_0._trophyTFList[arg_11_1]
	local var_11_2 = Instantiate(arg_11_0._reminderRes.Find("claim_fx"))

	var_11_1.PlayClaimAnima(var_11_0, var_11_2, function()
		arg_11_0.updateTrophyByGroup(arg_11_1)
		arg_11_0.updateTrophyCounter())

def var_0_0.updateTrophyByGroup(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.trophyGroups[arg_13_1]

	arg_13_0._trophyTFList[arg_13_1].UpdateTrophyGroup(var_13_0)

def var_0_0.openTrophyDetail(arg_14_0, arg_14_1, arg_14_2):
	arg_14_0._trophyDetailPanel.SetTrophyGroup(arg_14_1)
	arg_14_0._trophyDetailPanel.UpdateTrophy(arg_14_2)
	arg_14_0._trophyDetailPanel.SetActive(True)

def var_0_0.updateTrophyCounter(arg_15_0):
	local var_15_0 = 0

	for iter_15_0, iter_15_1 in pairs(arg_15_0.trophyList):
		if iter_15_1.isClaimed() and not iter_15_1.isHide():
			var_15_0 = var_15_0 + 1

	setText(arg_15_0._trophyCounter, var_15_0)

def var_0_0.onFilter(arg_16_0):
	arg_16_0._filterIndex = arg_16_0._filterIndex + 1

	if arg_16_0._filterIndex > #var_0_0.Filter:
		arg_16_0._filterIndex = 1

	for iter_16_0 = 1, #var_0_0.Filter:
		setActive(arg_16_0._filterBtn.GetChild(iter_16_0 - 1), iter_16_0 == arg_16_0._filterIndex)

	arg_16_0.updateTrophyList()

def var_0_0.onBackPressed(arg_17_0):
	if arg_17_0._trophyDetailPanel.IsActive():
		arg_17_0._trophyDetailPanel.SetActive(False)
	else
		var_0_0.super.onBackPressed(arg_17_0)

def var_0_0.willExit(arg_18_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_18_0._blurPanel, arg_18_0._tf)
	arg_18_0._trophyDetailPanel.Dispose()

return var_0_0

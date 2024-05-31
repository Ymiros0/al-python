local var_0_0 = class("WinConditionDisplayPanel", BaseSubView)

def var_0_0.getUIName(arg_1_0):
	return "WinConditionDisplayPanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.listTF = arg_2_0._tf.Find("window/bg/awards/awardList")
	arg_2_0.closeBtn = arg_2_0._tf.Find("window/top/btnBack")
	arg_2_0.winCondtitle = arg_2_0.findTF("window/bg/winCond/title/text")

	setText(arg_2_0.winCondtitle, i18n("text_win_condition"))

	arg_2_0.winCondDesc = arg_2_0.findTF("window/bg/winCond/desc")
	arg_2_0.loseCondtitle = arg_2_0.findTF("window/bg/loseCond/title/text")

	setText(arg_2_0.loseCondtitle, i18n("text_lose_condition"))

	arg_2_0.loseCondDesc = arg_2_0.findTF("window/bg/loseCond/desc")
	arg_2_0.rewardList = arg_2_0.findTF("window/bg/awards")
	arg_2_0.rewardtip = arg_2_0.findTF("text", arg_2_0.rewardList)

	setText(arg_2_0.rewardtip, i18n("desc_defense_reward"))

	arg_2_0.rewardWord = arg_2_0.findTF("desc", arg_2_0.rewardList)

	setText(arg_2_0.rewardWord, i18n("word_reward"))

	arg_2_0.rewardCond = arg_2_0.findTF("cond", arg_2_0.rewardList)

	setText(arg_2_0.rewardCond, i18n("text_rest_HP"))
	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.Hide(), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.closeBtn, function()
		arg_2_0.Hide(), SFX_PANEL)

local var_0_1 = {
	"s",
	"a",
	"b"
}

def var_0_0.UpdateList(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	local var_5_0

	if #arg_5_3 == 3:
		arg_5_0.listTF.GetChild(1).gameObject.SetActive(True)
		arg_5_0.listTF.GetChild(2).gameObject.SetActive(True)
		arg_5_0.listTF.GetChild(3).gameObject.SetActive(True)

		var_5_0 = {
			3,
			2,
			1
		}
	elif #arg_5_3 == 2:
		arg_5_0.listTF.GetChild(1).gameObject.SetActive(True)
		arg_5_0.listTF.GetChild(2).gameObject.SetActive(False)
		arg_5_0.listTF.GetChild(3).gameObject.SetActive(True)

		var_5_0 = {
			3,
			1
		}
	elif #arg_5_3 == 1:
		arg_5_0.listTF.GetChild(1).gameObject.SetActive(False)
		arg_5_0.listTF.GetChild(2).gameObject.SetActive(True)
		arg_5_0.listTF.GetChild(3).gameObject.SetActive(False)

		var_5_0 = {
			2
		}

	local var_5_1 = False

	for iter_5_0 = 1, #arg_5_3:
		local var_5_2 = arg_5_0.listTF.GetChild(var_5_0[iter_5_0])
		local var_5_3 = tostring(arg_5_2[iter_5_0] - 1)

		if arg_5_2[iter_5_0] - 1 != arg_5_2[iter_5_0 + 1]:
			var_5_3 = tostring(arg_5_2[iter_5_0 + 1]) .. "-" .. var_5_3

		setText(var_5_2.Find("text"), var_5_3)

		local var_5_4 = arg_5_3[iter_5_0]

		updateDrop(var_5_2.Find("award"), var_5_4, {
			hideName = True
		})
		onButton(arg_5_0, var_5_2.Find("award"), function()
			arg_5_0.emit(BaseUI.ON_DROP, var_5_4), SFX_PANEL)

		local var_5_5 = not var_5_1 and arg_5_4 >= arg_5_2[iter_5_0 + 1]

		var_5_1 = var_5_1 or arg_5_4 >= arg_5_2[iter_5_0 + 1]

		setActive(var_5_2.Find("mask"), not var_5_5)

def var_0_0.Enter(arg_7_0, arg_7_1):
	setText(arg_7_0.winCondDesc, i18n(arg_7_1.getConfig("win_condition_display")))
	setText(arg_7_0.loseCondDesc, i18n(arg_7_1.getConfig("lose_condition_display")))

	local var_7_0 = arg_7_1.getPlayType() == ChapterConst.TypeDefence

	setActive(arg_7_0.rewardList, var_7_0)

	if var_7_0:
		arg_7_0.UpdateRewardList(arg_7_1)

	arg_7_0.Show()
	Canvas.ForceUpdateCanvases()

def var_0_0.UpdateRewardList(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.id
	local var_8_1 = pg.chapter_defense[var_8_0]

	if not var_8_1:
		return

	local var_8_2 = Clone(var_8_1.score)

	table.insert(var_8_2, 1, var_8_1.port_hp + 1)

	local var_8_3 = {}

	for iter_8_0, iter_8_1 in ipairs(var_0_1):
		local var_8_4 = var_8_1["evaluation_display_" .. iter_8_1]

		if #var_8_4 > 0:
			table.insert(var_8_3, {
				type = var_8_4[1],
				id = var_8_4[2],
				count = var_8_4[3]
			})

	arg_8_0.UpdateList(var_8_1, var_8_2, var_8_3, arg_8_1.BaseHP)

return var_0_0

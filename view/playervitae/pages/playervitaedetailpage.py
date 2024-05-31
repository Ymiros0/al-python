local var_0_0 = class("PlayerVitaeDetailPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "PlayerVitaeDetailPage"

def var_0_0.OnPlayerNameChange(arg_2_0, arg_2_1):
	arg_2_0.player = arg_2_1
	arg_2_0.nameTxt.text = arg_2_1.name

def var_0_0.OnLoaded(arg_3_0):
	arg_3_0.medalTpl = arg_3_0.findTF("medalList/tpl")
	arg_3_0.emblemIcon = arg_3_0.findTF("power/medal").GetComponent(typeof(Image))
	arg_3_0.emblemTxt = arg_3_0.findTF("power/medal_text").GetComponent(typeof(Image))
	arg_3_0.highestEmblem = arg_3_0.findTF("power/rank").GetComponent(typeof(Text))
	arg_3_0.powerTxt = arg_3_0.findTF("power/power").GetComponent(typeof(Text))
	arg_3_0.collectionTxt = arg_3_0.findTF("power/collection").GetComponent(typeof(Text))
	arg_3_0.modityNameBtn = arg_3_0.findTF("info/name")
	arg_3_0.nameTxt = arg_3_0.findTF("info/name/Text").GetComponent(typeof(Text))
	arg_3_0.idTxt = arg_3_0.findTF("info/uid").GetComponent(typeof(Text))
	arg_3_0.levelTxt = arg_3_0.findTF("info/level").GetComponent(typeof(Text))
	arg_3_0.expTxt = arg_3_0.findTF("info/exp").GetComponent(typeof(Text))
	arg_3_0.statisticTpl = arg_3_0.findTF("statistics/tpl")
	arg_3_0.shareBtn = arg_3_0.findTF("btn_share")
	arg_3_0.attireBtn = arg_3_0.findTF("btn_attire")
	arg_3_0.attireBtnTip = arg_3_0.attireBtn.Find("tip")
	arg_3_0.inputField = arg_3_0.findTF("greet/InputField")
	arg_3_0.writeBtn = arg_3_0.findTF("greet/write_btn")
	arg_3_0.animPanels = {
		arg_3_0.findTF("info"),
		arg_3_0.findTF("power"),
		arg_3_0.findTF("statistics"),
		arg_3_0.findTF("greet")
	}

	setText(arg_3_0.findTF("power/collection_label"), i18n("friend_resume_collection_rate"))
	setText(arg_3_0.findTF("power/power_label"), i18n("friend_resume_fleet_gs"))
	setText(arg_3_0.findTF("info/title_name"), i18n("friend_resume_title"))
	setText(arg_3_0.findTF("statistics/title_name"), i18n("friend_resume_data_title"))
	setText(arg_3_0.findTF("greet/InputField/Placeholder"), i18n("player_manifesto_placeholder"))
	arg_3_0.MatchResolution()

def var_0_0.PreCalcAspect(arg_4_0, arg_4_1):
	return arg_4_0.rect.height / arg_4_1

def var_0_0.MatchResolution(arg_5_0):
	local var_5_0 = var_0_0.PreCalcAspect(arg_5_0._parentTf, arg_5_0._tf.rect.height)

	arg_5_0._tf.localScale = Vector3(var_5_0, var_5_0, 1)

def var_0_0.OnInit(arg_6_0):
	onButton(arg_6_0, arg_6_0.modityNameBtn, function()
		local var_7_0, var_7_1 = arg_6_0.player.canModifyName()

		if not var_7_0:
			pg.TipsMgr.GetInstance().ShowTips(var_7_1)

			return

		arg_6_0.contextData.renamePage.ExecuteAction("Show", arg_6_0.player), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.writeBtn, function()
		activateInputField(arg_6_0.inputField), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.shareBtn, function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeAdmira), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.attireBtn, function()
		arg_6_0.emit(PlayerVitaeMediator.ON_ATTIRE), SFX_PANEL)
	setActive(arg_6_0.attireBtnTip, _.any(getProxy(AttireProxy).needTip(), function(arg_11_0)
		return arg_11_0 == True))
	onInputEndEdit(arg_6_0, arg_6_0.inputField, function(arg_12_0)
		if wordVer(arg_12_0) > 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("playerinfo_mask_word"))
			activateInputField(arg_6_0.inputField)

			return

		if not arg_12_0 or arg_6_0.manifesto == arg_12_0:
			return

		arg_6_0.manifesto = arg_12_0

		arg_6_0.emit(PlayerVitaeMediator.CHANGE_MANIFESTO, arg_12_0))
	arg_6_0._tf.SetAsFirstSibling()

def var_0_0.Show(arg_13_0, arg_13_1, arg_13_2):
	var_0_0.super.Show(arg_13_0)

	arg_13_0.player = arg_13_1

	arg_13_0.UpdateMedals()
	arg_13_0.UpdatePower()
	arg_13_0.UpdateInfo()
	arg_13_0.UpdateStatistics()

	if arg_13_2:
		arg_13_0.DoEnterAnimation()

def var_0_0.DoEnterAnimation(arg_14_0):
	for iter_14_0, iter_14_1 in ipairs(arg_14_0.animPanels):
		local var_14_0 = iter_14_1.localPosition.x
		local var_14_1 = iter_14_0 * 0.05
		local var_14_2 = 0.2 + (iter_14_0 - 1) * 0.05

		iter_14_1.localPosition = Vector3(var_14_0 + 800, iter_14_1.localPosition.y, 0)

		LeanTween.moveLocalX(iter_14_1.gameObject, var_14_0, var_14_2).setDelay(var_14_1).setEase(LeanTweenType.easeInOutSine)

def var_0_0.UpdateMedals(arg_15_0):
	local var_15_0 = arg_15_0.player.displayTrophyList
	local var_15_1 = math.min(5, #var_15_0)
	local var_15_2 = 353
	local var_15_3 = 30

	for iter_15_0 = 1, var_15_1:
		local var_15_4 = iter_15_0 == 1 and arg_15_0.medalTpl or cloneTplTo(arg_15_0.medalTpl, arg_15_0.medalTpl.parent)
		local var_15_5 = pg.medal_template[var_15_0[var_15_1 - iter_15_0 + 1]]

		LoadSpriteAsync("medal/s_" .. var_15_5.icon, function(arg_16_0)
			if arg_15_0.exited:
				return

			local var_16_0 = var_15_4.Find("icon").GetComponent(typeof(Image))

			var_16_0.sprite = arg_16_0

			var_16_0.SetNativeSize())

		local var_15_6 = var_15_2 - (iter_15_0 - 1) * (var_15_3 + var_15_4.sizeDelta.x)

		var_15_4.anchoredPosition = Vector2(var_15_6, var_15_4.anchoredPosition.y)

	setActive(arg_15_0.medalTpl, var_15_1 != 0)

def var_0_0.UpdatePower(arg_17_0):
	local var_17_0 = getProxy(MilitaryExerciseProxy).RawGetSeasonInfo()
	local var_17_1 = SeasonInfo.getEmblem(var_17_0.score, var_17_0.rank)

	LoadSpriteAsync("emblem/" .. var_17_1, function(arg_18_0)
		arg_17_0.emblemIcon.sprite = arg_18_0

		arg_17_0.emblemIcon.SetNativeSize())
	LoadSpriteAsync("emblem/n_" .. var_17_1, function(arg_19_0)
		if arg_17_0.exited:
			return

		arg_17_0.emblemTxt.sprite = arg_19_0

		arg_17_0.emblemTxt.SetNativeSize())

	local var_17_2 = math.max(arg_17_0.player.maxRank, 1)
	local var_17_3 = pg.arena_data_rank[math.min(var_17_2, 14)]

	arg_17_0.highestEmblem.text = i18n("friend_resume_title_metal") .. var_17_3.name

	getProxy(BayProxy).GetBayPowerRootedAsyn(function(arg_20_0)
		if arg_17_0.exited:
			return

		arg_17_0.powerTxt.text = math.floor(arg_20_0))

	arg_17_0.collectionTxt.text = getProxy(CollectionProxy).getCollectionRate() * 100 .. "%"

def var_0_0.UpdateInfo(arg_21_0):
	arg_21_0.nameTxt.text = arg_21_0.player.name
	arg_21_0.idTxt.text = arg_21_0.player.id
	arg_21_0.levelTxt.text = "LV." .. arg_21_0.player.level

	local var_21_0 = getConfigFromLevel1(pg.user_level, arg_21_0.player.level).exp

	arg_21_0.expTxt.text = arg_21_0.player.exp .. "/" .. var_21_0

	local var_21_1 = arg_21_0.player.GetManifesto()

	setInputText(arg_21_0.inputField, var_21_1)

def var_0_0.UpdateStatistics(arg_22_0):
	local var_22_0 = arg_22_0.GetDisplayStatisticsData()
	local var_22_1 = 2
	local var_22_2 = Vector2(355, 25)
	local var_22_3 = arg_22_0.statisticTpl.anchoredPosition
	local var_22_4 = arg_22_0.statisticTpl.sizeDelta.x

	for iter_22_0 = 1, #var_22_0, var_22_1:
		local var_22_5 = var_22_3.y - (iter_22_0 - 1) * var_22_2.y

		for iter_22_1 = 1, var_22_1:
			local var_22_6 = iter_22_1 == 1 and iter_22_0 == 1 and arg_22_0.statisticTpl or cloneTplTo(arg_22_0.statisticTpl, arg_22_0.statisticTpl.parent)
			local var_22_7 = var_22_0[iter_22_0 + (iter_22_1 - 1)]

			setText(var_22_6, i18n(var_22_7[1]))
			setText(var_22_6.Find("value"), var_22_7[2])

			local var_22_8 = var_22_3.x + (iter_22_1 - 1) * var_22_2.x

			var_22_6.anchoredPosition = Vector2(var_22_8, var_22_5)

def var_0_0.GetDisplayStatisticsData(arg_23_0):
	local var_23_0 = arg_23_0.player
	local var_23_1 = string.format("%0.1f", var_23_0.winCount / math.max(var_23_0.attackCount, 1) * 100) .. "%"
	local var_23_2 = string.format("%0.1f", var_23_0.pvp_win_count / math.max(var_23_0.pvp_attack_count, 1) * 100) .. "%"

	return {
		{
			"friend_resume_ship_count",
			var_23_0.shipCount
		},
		{
			"friend_event_count",
			var_23_0.collect_attack_count
		},
		{
			"friend_resume_attack_count",
			var_23_0.attackCount
		},
		{
			"friend_resume_manoeuvre_count",
			var_23_0.pvp_attack_count
		},
		{
			"friend_resume_attack_win_rate",
			var_23_1
		},
		{
			"friend_resume_manoeuvre_win_rate",
			var_23_2
		}
	}

def var_0_0.OnDestroy(arg_24_0):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.animPanels):
		if LeanTween.isTweening(iter_24_1.gameObject):
			LeanTween.cancel(iter_24_1.gameObject)

	arg_24_0.exited = True

return var_0_0

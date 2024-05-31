local var_0_0 = class("BattleActivityBossResultLayer", import(".BattleResultLayer"))

def var_0_0.showRightBottomPanel(arg_1_0):
	local var_1_0 = arg_1_0._blurConatiner.Find("activitybossConfirmPanel")

	setActive(var_1_0, True)
	var_0_0.super.showRightBottomPanel(arg_1_0)
	SetActive(arg_1_0._rightBottomPanel, False)

	local var_1_1 = arg_1_0.contextData.system
	local var_1_2 = var_1_1 != SYSTEM_BOSS_EXPERIMENT

	setActive(var_1_0.Find("playAgain"), var_1_2)
	onButton(arg_1_0, var_1_0.Find("statisticsBtn"), function()
		setActive(var_1_0.Find("playAgain"), arg_1_0._atkBG.gameObject.activeSelf and var_1_2)
		triggerButton(arg_1_0._statisticsBtn), SFX_PANEL)
	setText(var_1_0.Find("confirmBtn/Image"), i18n("text_confirm"))
	onButton(arg_1_0, var_1_0.Find("confirmBtn"), function()
		triggerButton(arg_1_0._confirmBtn), SFX_CONFIRM)
	setText(var_1_0.Find("confirmBtn/Image"), i18n("text_confirm"))
	setText(var_1_0.Find("playAgain/Image"), i18n("re_battle"))
	setText(var_1_0.Find("playAgain/bonus/title"), i18n("expedition_extra_drop_tip"))

	local var_1_3 = getProxy(FleetProxy).getActivityFleets()[arg_1_0.contextData.actId]
	local var_1_4 = var_1_0.Find("playAgain/bonus")
	local var_1_5 = var_1_0.Find("playAgain/ticket")
	local var_1_6 = getProxy(ActivityProxy).getActivityById(arg_1_0.contextData.actId)
	local var_1_7 = arg_1_0.contextData.stageId
	local var_1_8 = var_1_6.getConfig("config_id")
	local var_1_9 = pg.activity_event_worldboss[var_1_8]
	local var_1_10 = var_1_9.ticket
	local var_1_11 = var_1_6.GetStageBonus(var_1_7)
	local var_1_12 = var_1_6.IsOilLimit(var_1_7)
	local var_1_13 = 0
	local var_1_14 = var_1_9.use_oil_limit[arg_1_0.contextData.mainFleetId]

	;(function(arg_4_0, arg_4_1)
		local var_4_0 = arg_4_0.GetCostSum().oil

		if arg_4_1 > 0:
			var_4_0 = math.min(var_4_0, var_1_14[1])

		var_1_13 = var_1_13 + var_4_0)(var_1_3[arg_1_0.contextData.mainFleetId], var_1_12 and var_1_14[1] or 0)
	setText(var_1_0.Find("playAgain/Text"), var_1_13)

	local var_1_15
	local var_1_16

	setActive(var_1_4, var_1_11 > 0)
	setActive(var_1_5, var_1_11 <= 0)
	setText(var_1_4.Find("Text"), var_1_11)

	if var_1_11 <= 0:
		local var_1_17 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = var_1_10
		}).getIcon()
		local var_1_18 = GetSpriteFromAtlas(var_1_17, "")

		setImageSprite(var_1_5.Find("icon"), var_1_18)

		local var_1_19 = getProxy(PlayerProxy).getRawData().getResource(var_1_10)

		var_1_16 = getProxy(SettingsProxy).isTipActBossExchangeTicket() == 1
		var_1_15 = var_1_19 > 0

		local var_1_20 = 1
		local var_1_21 = var_1_5.Find("checkbox")

		if var_1_1 == SYSTEM_BOSS_EXPERIMENT:
			var_1_20 = 0

			triggerToggle(var_1_21, False)
			setToggleEnabled(var_1_21, False)
		elif var_1_1 == SYSTEM_HP_SHARE_ACT_BOSS:
			triggerToggle(var_1_21, True)
			setToggleEnabled(var_1_21, False)
		elif var_1_1 == SYSTEM_ACT_BOSS:
			setToggleEnabled(var_1_21, var_1_15)
			triggerToggle(var_1_21, var_1_15 and var_1_16)

		var_1_19 = var_1_19 < var_1_20 and setColorStr(var_1_19, COLOR_RED) or var_1_19

		setText(var_1_5.Find("Text"), var_1_20 .. "/" .. var_1_19)
		onToggle(arg_1_0, var_1_21, function(arg_5_0)
			var_1_16 = arg_5_0

			getProxy(SettingsProxy).setActBossExchangeTicketTip(arg_5_0 and 1 or 0), SFX_PANEL, SFX_CANCEL)

	onButton(arg_1_0, var_1_0.Find("playAgain"), function()
		if arg_1_0.contextData.isLastBonus:
			arg_1_0.PassMsgbox("lastBonus", {
				content = i18n("expedition_drop_use_out")
			})

			return

		if var_1_1 == SYSTEM_HP_SHARE_ACT_BOSS and not var_1_15:
			pg.m02.sendNotification(GAME.GO_BACK)
			pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noTicket"))

			return

		local var_6_0 = pg.battle_cost_template[arg_1_0.contextData.system].oil_cost > 0
		local var_6_1 = getProxy(PlayerProxy).getRawData().oil

		if var_6_0 and var_6_1 < var_1_13:
			arg_1_0.PassMsgbox("oil", var_1_13)

			return

		if getProxy(BayProxy).getShipCount() >= getProxy(PlayerProxy).getRawData().getMaxShipBag():
			arg_1_0.PassMsgbox("shipCapacity")

			return

		local var_6_2 = var_1_3[arg_1_0.contextData.mainFleetId]

		if _.any(_.values(var_6_2.ships), function(arg_7_0)
			local var_7_0 = getProxy(BayProxy).getShipById(arg_7_0)

			return var_7_0 and var_7_0.energy == Ship.ENERGY_LOW):
			arg_1_0.PassMsgbox("energy", var_6_2)

			return

		if var_1_1 == SYSTEM_ACT_BOSS and var_1_15 and var_1_16:
			pg.m02.sendNotification(GAME.ACT_BOSS_EXCHANGE_TICKET, {
				stageId = var_1_7
			})

			return

		arg_1_0.emit(NewBattleResultMediator.REENTER_STAGE))

def var_0_0.PassMsgbox(arg_8_0, arg_8_1, arg_8_2):
	getProxy(ContextProxy).GetPrevContext(1).data.msg = {
		type = arg_8_1,
		param = arg_8_2
	}

	pg.m02.sendNotification(GAME.GO_BACK)

def var_0_0.HideConfirmPanel(arg_9_0):
	local var_9_0 = arg_9_0._blurConatiner.Find("activitybossConfirmPanel")

	setActive(var_9_0, False)

return var_0_0

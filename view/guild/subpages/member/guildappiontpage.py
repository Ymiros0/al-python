local var_0_0 = class("GuildAppiontPage", import(".GuildMemberBasePage"))

def var_0_0.getUIName(arg_1_0):
	return "GuildAppiontPage"

local var_0_1 = {
	"commander",
	"deputyCommander",
	"picked",
	"normal"
}

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.dutyContainer = arg_2_0.findTF("frame/duty")
	arg_2_0.print = arg_2_0.findTF("frame/prints/print").GetComponent(typeof(Image))
	arg_2_0.confirmBtn = arg_2_0.findTF("frame/confirm_btn")
	arg_2_0.nameTF = arg_2_0.findTF("frame/info/name/Text", arg_2_0._tf).GetComponent(typeof(Text))
	arg_2_0.iconTF = arg_2_0.findTF("frame/info/shipicon/icon", arg_2_0._tf).GetComponent(typeof(Image))
	arg_2_0.starsTF = arg_2_0.findTF("frame/info/shipicon/stars", arg_2_0._tf)
	arg_2_0.starTF = arg_2_0.findTF("frame/info/shipicon/stars/star", arg_2_0._tf)
	arg_2_0.levelTF = arg_2_0.findTF("frame/info/level/Text", arg_2_0._tf).GetComponent(typeof(Text))
	arg_2_0.circle = arg_2_0.findTF("frame/info/shipicon/frame", arg_2_0._tf)
	arg_2_0.toggles = arg_2_0.findTF("frame/duty").GetComponent(typeof(ToggleGroup))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.ShouldShow(arg_5_0):
	return arg_5_0.memberVO.id != arg_5_0.playerVO.id

def var_0_0.OnShow(arg_6_0):
	local var_6_0 = arg_6_0.playerVO
	local var_6_1 = arg_6_0.memberVO
	local var_6_2 = arg_6_0.guildVO
	local var_6_3 = var_6_2.getDutyByMemberId(var_6_0.id)
	local var_6_4 = var_6_2.getEnableDuty(var_6_3, var_6_1.duty)
	local var_6_5 = var_6_2.getAssistantMaxCount()
	local var_6_6 = var_6_2.getAssistantCount()
	local var_6_7

	for iter_6_0, iter_6_1 in ipairs(var_0_1):
		local var_6_8 = arg_6_0.dutyContainer.Find(iter_6_1)
		local var_6_9 = var_6_8.Find("Text")
		local var_6_10 = False

		if var_6_1.duty == iter_6_0:
			setText(var_6_9, i18n("guild_duty_tip_1"))

			var_6_10 = True
		elif not table.contains(var_6_4, iter_6_0):
			if var_6_5 <= var_6_6 and iter_6_0 == 2:
				setText(var_6_9, i18n("guild_deputy_commander_cnt_is_full"))
			else
				setText(var_6_9, i18n("guild_duty_tip_2"))

			var_6_10 = True

		setActive(var_6_9, not table.contains(var_6_4, iter_6_0))

		if var_6_3 == GuildConst.DUTY_COMMANDER and iter_6_0 == 2 and not var_6_10:
			if var_6_5 <= var_6_6:
				setText(var_6_9, i18n("guild_deputy_commander_cnt_is_full"))
			else
				setText(var_6_9, i18n("guild_deputy_commander_cnt", var_6_6, var_6_5))

			setActive(var_6_9, True)

		setToggleEnabled(var_6_8, table.contains(var_6_4, iter_6_0))
		onToggle(arg_6_0, var_6_8, function(arg_7_0)
			if arg_7_0:
				var_6_7 = iter_6_0
				arg_6_0.selectedToggle = var_6_8, SFX_PANEL)

	local var_6_11 = arg_6_0.dutyContainer.Find("commander/Image2")

	if var_6_3 == GuildConst.DUTY_COMMANDER and var_6_1.duty > GuildConst.DUTY_DEPUTY_COMMANDER:
		onButton(arg_6_0, var_6_11, function()
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_duty_shoule_be_deputy_commander")), SFX_PANEL)
	else
		local var_6_12 = var_6_11.GetComponent(typeof(Button))

		if not IsNil(var_6_12):
			Object.Destroy(var_6_12)

	local var_6_13 = var_6_2.getFaction()

	if var_6_13 == GuildConst.FACTION_TYPE_BLHX:
		arg_6_0.print.color = Color.New(0.4235294117647059, 0.6313725490196078, 0.9568627450980393)
	elif var_6_13 == GuildConst.FACTION_TYPE_CSZZ:
		arg_6_0.print.color = Color.New(0.9568627450980393, 0.44313725490196076, 0.42745098039215684)

	arg_6_0.nameTF.text = var_6_1.name

	local var_6_14 = AttireFrame.attireFrameRes(var_6_1, var_6_1.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, var_6_1.propose)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_6_14, var_6_14, True, function(arg_9_0)
		if IsNil(arg_6_0._tf):
			return

		if arg_6_0.circle:
			arg_9_0.name = var_6_14
			findTF(arg_9_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_9_0, arg_6_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_6_14, var_6_14, arg_9_0))

	local var_6_15 = pg.ship_data_statistics[var_6_1.icon]
	local var_6_16 = Ship.New({
		configId = var_6_1.icon,
		skin_id = var_6_1.skinId
	})

	LoadSpriteAsync("qicon/" .. var_6_16.getPainting(), function(arg_10_0)
		if not IsNil(arg_6_0.iconTF):
			arg_6_0.iconTF.sprite = arg_10_0)

	local var_6_17 = arg_6_0.starsTF.childCount

	for iter_6_2 = var_6_17, var_6_15.star - 1:
		cloneTplTo(arg_6_0.starTF, arg_6_0.starsTF)

	for iter_6_3 = 1, var_6_17:
		local var_6_18 = arg_6_0.starsTF.GetChild(iter_6_3 - 1)

		setActive(var_6_18, iter_6_3 <= var_6_15.star)

	arg_6_0.levelTF.text = "Lv." .. var_6_1.level

	onButton(arg_6_0, arg_6_0.confirmBtn, function()
		local function var_11_0()
			arg_6_0.emit(GuildMemberMediator.SET_DUTY, var_6_1.id, var_6_7)
			arg_6_0.Hide()

		if var_6_3 == GuildConst.DUTY_COMMANDER and var_6_7 == GuildConst.DUTY_COMMANDER:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("guild_transfer_president_confirm", var_6_1.name),
				onYes = var_11_0
			})
		else
			var_11_0(), SFX_CONFIRM)

def var_0_0.Hide(arg_13_0):
	arg_13_0.toggles.SetAllTogglesOff()
	var_0_0.super.Hide(arg_13_0)

return var_0_0

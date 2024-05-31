local var_0_0 = class("GuildFirePage", import(".GuildMemberBasePage"))

def var_0_0.getUIName(arg_1_0):
	return "GuildFirePage"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.fireconfirmBtn = arg_2_0.findTF("frame/confirm_btn")
	arg_2_0.firecancelBtn = arg_2_0.findTF("frame/cancel_btn")
	arg_2_0.firenameTF = arg_2_0.findTF("frame/info/name/Text", arg_2_0._tf).GetComponent(typeof(Text))
	arg_2_0.fireiconTF = arg_2_0.findTF("frame/info/shipicon/icon", arg_2_0._tf).GetComponent(typeof(Image))
	arg_2_0.fireduty = arg_2_0.findTF("frame/duty").GetComponent(typeof(Image))
	arg_2_0.firestarsTF = arg_2_0.findTF("frame/info/shipicon/stars", arg_2_0._tf)
	arg_2_0.firestarTF = arg_2_0.findTF("frame/info/shipicon/stars/star", arg_2_0._tf)
	arg_2_0.firelevelTF = arg_2_0.findTF("frame/info/level/Text", arg_2_0._tf).GetComponent(typeof(Text))
	arg_2_0.circle = arg_2_0.findTF("frame/info/shipicon/frame", arg_2_0._tf)

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.firecancelBtn, function()
		arg_3_0.Hide(), SFX_CONFIRM)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_CONFIRM)

def var_0_0.OnShow(arg_6_0):
	local var_6_0 = arg_6_0.guildVO
	local var_6_1 = arg_6_0.playerVO
	local var_6_2 = arg_6_0.memberVO

	arg_6_0.firenameTF.text = var_6_2.name

	local var_6_3 = AttireFrame.attireFrameRes(var_6_2, var_6_2.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, var_6_2.propose)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_6_3, var_6_3, True, function(arg_7_0)
		if IsNil(arg_6_0._tf):
			return

		if arg_6_0.circle:
			arg_7_0.name = var_6_3
			findTF(arg_7_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_7_0, arg_6_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_6_3, var_6_3, arg_7_0))

	local var_6_4 = pg.ship_data_statistics[var_6_2.icon]
	local var_6_5 = Ship.New({
		configId = var_6_2.icon,
		skin_id = var_6_2.skinId
	})

	LoadSpriteAsync("qicon/" .. var_6_5.getPainting(), function(arg_8_0)
		if not IsNil(arg_6_0.fireiconTF):
			arg_6_0.fireiconTF.sprite = arg_8_0)

	local var_6_6 = GetSpriteFromAtlas("dutyicon", "icon_" .. var_6_2.duty)

	arg_6_0.fireduty.sprite = var_6_6

	local var_6_7 = arg_6_0.firestarsTF.childCount

	for iter_6_0 = var_6_7, var_6_4.star - 1:
		cloneTplTo(arg_6_0.firestarTF, arg_6_0.firestarsTF)

	for iter_6_1 = 1, var_6_7:
		local var_6_8 = arg_6_0.firestarsTF.GetChild(iter_6_1 - 1)

		setActive(var_6_8, iter_6_1 <= var_6_4.star)

	arg_6_0.firelevelTF.text = "Lv." .. var_6_2.level

	onButton(arg_6_0, arg_6_0.fireconfirmBtn, function()
		if var_6_2.id == var_6_1.id:
			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("guild_fire_tip"),
			def onYes:()
				arg_6_0.emit(GuildMemberMediator.FIRE, var_6_2.id)
				arg_6_0.Hide()
		}), SFX_CONFIRM)

return var_0_0

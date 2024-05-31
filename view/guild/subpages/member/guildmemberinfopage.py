local var_0_0 = class("GuildMemberInfoPage", import(".GuildMemberBasePage"))

def var_0_0.getUIName(arg_1_0):
	return "GuildMemberInfoPage"

local var_0_1 = {
	{
		value = "shipCount",
		type = 1,
		tag = i18n("friend_resume_ship_count")
	},
	{
		type = 3,
		tag = i18n("friend_resume_collection_rate"),
		value = {
			"collectionCount"
		}
	},
	{
		value = "attackCount",
		type = 1,
		tag = i18n("friend_resume_attack_count")
	},
	{
		type = 2,
		tag = i18n("friend_resume_attack_win_rate"),
		value = {
			"attackCount",
			"winCount"
		}
	},
	{
		value = "pvp_attack_count",
		type = 1,
		tag = i18n("friend_resume_manoeuvre_count")
	},
	{
		type = 2,
		tag = i18n("friend_resume_manoeuvre_win_rate"),
		value = {
			"pvp_attack_count",
			"pvp_win_count"
		}
	},
	{
		value = "collect_attack_count",
		type = 1,
		tag = i18n("friend_event_count")
	}
}

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.infonameTF = arg_2_0.findTF("frame/info/name/Text").GetComponent(typeof(Text))
	arg_2_0.infoiconTF = arg_2_0.findTF("frame/info/shipicon/icon").GetComponent(typeof(Image))
	arg_2_0.infoduty = arg_2_0.findTF("frame/duty").GetComponent(typeof(Image))
	arg_2_0.infostarsTF = arg_2_0.findTF("frame/info/shipicon/stars")
	arg_2_0.infostarTF = arg_2_0.findTF("frame/info/shipicon/stars/star")
	arg_2_0.infolevelTF = arg_2_0.findTF("frame/info/level/Text").GetComponent(typeof(Text))
	arg_2_0.circle = arg_2_0.findTF("frame/info/shipicon/frame")
	arg_2_0.resumeInfo = arg_2_0.findTF("frame/content")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_CONFIRM)

def var_0_0.Show(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	arg_5_0.guildVO = arg_5_1
	arg_5_0.playerVO = arg_5_2
	arg_5_0.memberVO = arg_5_3

	arg_5_0.emit(GuildMemberMediator.OPEN_DESC_INFO, arg_5_3)

	if arg_5_4:
		arg_5_4()

def var_0_0.Flush(arg_6_0, arg_6_1):
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	setActive(arg_6_0._tf, True)
	arg_6_0._tf.SetAsLastSibling()
	arg_6_0.onShowCallBack(arg_6_0.buttonPos)

	local var_6_0 = arg_6_0.guildVO
	local var_6_1 = arg_6_0.memberVO

	arg_6_0.infonameTF.text = var_6_1.name

	local var_6_2 = AttireFrame.attireFrameRes(var_6_1, var_6_1.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, var_6_1.propose)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_6_2, var_6_2, True, function(arg_7_0)
		if IsNil(arg_6_0._tf):
			return

		if arg_6_0.circle:
			arg_7_0.name = var_6_2
			findTF(arg_7_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_7_0, arg_6_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_6_2, var_6_2, arg_7_0))

	local var_6_3 = pg.ship_data_statistics[var_6_1.icon]
	local var_6_4 = Ship.New({
		configId = var_6_1.icon,
		skin_id = var_6_1.skinId
	})

	LoadSpriteAsync("qicon/" .. var_6_4.getPainting(), function(arg_8_0)
		if not IsNil(arg_6_0.infoiconTF):
			arg_6_0.infoiconTF.sprite = arg_8_0)

	local var_6_5 = GetSpriteFromAtlas("dutyicon", "icon_" .. var_6_1.duty)

	arg_6_0.infoduty.sprite = var_6_5

	local var_6_6 = arg_6_0.infostarsTF.childCount

	for iter_6_0 = var_6_6, var_6_3.star - 1:
		cloneTplTo(arg_6_0.infostarTF, arg_6_0.infostarsTF)

	for iter_6_1 = 1, var_6_6:
		local var_6_7 = arg_6_0.infostarsTF.GetChild(iter_6_1 - 1)

		setActive(var_6_7, iter_6_1 <= var_6_3.star)

	arg_6_0.infolevelTF.text = "Lv." .. var_6_1.level

	for iter_6_2, iter_6_3 in ipairs(var_0_1):
		local var_6_8 = arg_6_0.resumeInfo.GetChild(iter_6_2 - 1)

		setText(var_6_8.Find("tag"), iter_6_3.tag)

		local var_6_9 = var_6_8.Find("tag (1)")

		if iter_6_3.type == 1:
			setText(var_6_9, arg_6_1[iter_6_3.value])
		elif iter_6_3.type == 2:
			local var_6_10 = math.max(arg_6_1[iter_6_3.value[1]], 1)
			local var_6_11 = math.max(arg_6_1[iter_6_3.value[2]], 0)

			setText(var_6_9, string.format("%0.2f", var_6_11 / var_6_10 * 100) .. "%")
		elif iter_6_3.type == 3:
			local var_6_12 = arg_6_1[iter_6_3.value[1]] or 1

			setText(var_6_9, string.format("%0.2f", var_6_12 / getProxy(CollectionProxy).getCollectionTotal() * 100) .. "%")

return var_0_0

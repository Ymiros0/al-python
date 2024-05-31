local var_0_0 = class("resumeLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "resumeUI"

def var_0_0.setPlayerVO(arg_2_0, arg_2_1):
	arg_2_0.player = arg_2_1

def var_0_0.init(arg_3_0):
	arg_3_0.frame = arg_3_0.findTF("frame")
	arg_3_0.resumeIcon = arg_3_0.findTF("frame/window/info/circle/head")
	arg_3_0.resumeStars = arg_3_0.findTF("frame/window/info/circle/head/stars")
	arg_3_0.resumeStarTpl = arg_3_0.findTF("frame/window/info/circle/head/star")
	arg_3_0.resumeLv = arg_3_0.findTF("frame/window/info/player_info/level_bg/level").GetComponent(typeof(Text))
	arg_3_0.resumeName = arg_3_0.findTF("frame/window/info/player_info/name_bg/name").GetComponent(typeof(Text))
	arg_3_0.resumeInfo = arg_3_0.findTF("frame/window/summary/content")
	arg_3_0.resumeEmblem = arg_3_0.findTF("frame/window/info/rank_bg/rank/Image")
	arg_3_0.resumeEmblemLabel = arg_3_0.findTF("frame/window/info/rank_bg/rank/label")
	arg_3_0.resumeMedalList = arg_3_0.findTF("frame/window/medalList/container")
	arg_3_0.resumeMedalTpl = arg_3_0.findTF("frame/window/medal_tpl")
	arg_3_0.closeBtn = arg_3_0.findTF("frame/window/title_bg/close_btn")
	arg_3_0.circle = arg_3_0.findTF("frame/window/info/circle/head/frame")
	arg_3_0.titleText = arg_3_0.findTF("frame/title/label_cn/text")

	local var_3_0 = i18n("friend_resume_title_detail")

	if var_3_0:
		setText(arg_3_0.titleText, var_3_0)

def var_0_0.didEnter(arg_4_0):
	arg_4_0.display(arg_4_0.player)
	onButton(arg_4_0, arg_4_0._tf, function()
		arg_4_0.emit(var_0_0.ON_CLOSE), SOUND_BACK)

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

def var_0_0.display(arg_6_0, arg_6_1):
	if arg_6_0.contextData.parent:
		setParent(arg_6_0._tf, arg_6_0.contextData.parent)
	else
		pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf, False, {
			weight = LayerWeightConst.SECOND_LAYER
		})

	local var_6_0 = SeasonInfo.getMilitaryRank(arg_6_1.score, arg_6_1.rank)
	local var_6_1 = SeasonInfo.getEmblem(arg_6_1.score, arg_6_1.rank)

	LoadImageSpriteAsync("emblem/" .. var_6_1, arg_6_0.resumeEmblem)
	LoadImageSpriteAsync("emblem/n_" .. var_6_1, arg_6_0.resumeEmblemLabel)

	arg_6_0.resumeName.text = arg_6_1.name
	arg_6_0.resumeLv.text = "Lv." .. arg_6_1.level

	LoadSpriteAsync("qicon/" .. arg_6_1.getPainting(), function(arg_7_0)
		if not IsNil(arg_6_0.resumeIcon):
			local var_7_0 = arg_6_0.resumeIcon.GetComponent(typeof(Image))

			var_7_0.color = Color.white
			var_7_0.sprite = arg_7_0 or LoadSprite("heroicon/unknown"))

	local var_6_2 = AttireFrame.attireFrameRes(arg_6_1, arg_6_1.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, arg_6_1.propose)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_6_2, var_6_2, True, function(arg_8_0)
		if IsNil(arg_6_0._tf):
			return

		if arg_6_0.circle:
			arg_8_0.name = var_6_2
			findTF(arg_8_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_8_0, arg_6_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_6_2, var_6_2, arg_8_0))

	local var_6_3 = pg.ship_data_statistics[arg_6_1.icon]
	local var_6_4 = Ship.New({
		configId = var_6_3.id
	})
	local var_6_5 = arg_6_0.resumeStars.childCount
	local var_6_6 = var_6_4.getStar()

	for iter_6_0 = var_6_5, var_6_6 - 1:
		cloneTplTo(arg_6_0.resumeStarTpl, arg_6_0.resumeStars)

	local var_6_7 = arg_6_0.resumeStars.childCount

	for iter_6_1 = 0, var_6_7 - 1:
		arg_6_0.resumeStars.GetChild(iter_6_1).gameObject.SetActive(iter_6_1 < var_6_3.star)

	removeAllChildren(arg_6_0.resumeMedalList)

	for iter_6_2 = 1, 5:
		local var_6_8 = cloneTplTo(arg_6_0.resumeMedalTpl, arg_6_0.resumeMedalList)

		setActive(arg_6_0.findTF("empty", var_6_8), iter_6_2 > #arg_6_1.displayTrophyList)

		if iter_6_2 <= #arg_6_1.displayTrophyList:
			setActive(arg_6_0.findTF("icon", var_6_8), True)

			local var_6_9 = pg.medal_template[arg_6_1.displayTrophyList[iter_6_2]]

			LoadImageSpriteAsync("medal/" .. var_6_9.icon, arg_6_0.findTF("icon", var_6_8), True)

	for iter_6_3, iter_6_4 in ipairs(var_0_1):
		local var_6_10 = arg_6_0.resumeInfo.GetChild(iter_6_3 - 1)

		setText(var_6_10.Find("tag"), iter_6_4.tag)

		local var_6_11 = var_6_10.Find("value")

		if iter_6_4.type == 1:
			setText(var_6_11, arg_6_0.player[iter_6_4.value])
		elif iter_6_4.type == 2:
			local var_6_12 = math.max(arg_6_0.player[iter_6_4.value[1]], 1)
			local var_6_13 = math.max(arg_6_0.player[iter_6_4.value[2]], 0)

			setText(var_6_11, string.format("%0.2f", var_6_13 / var_6_12 * 100) .. "%")
		elif iter_6_4.type == 3:
			local var_6_14 = arg_6_0.player[iter_6_4.value[1]] or 1

			setText(var_6_11, string.format("%0.2f", var_6_14 / getProxy(CollectionProxy).getCollectionTotal() * 100) .. "%")

def var_0_0.willExit(arg_9_0):
	if arg_9_0.contextData.parent:
		-- block empty
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_9_0._tf, pg.UIMgr.GetInstance().UIMain)

	if arg_9_0.circle.childCount > 0:
		local var_9_0 = arg_9_0.circle.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_9_0.name, var_9_0.name, var_9_0)

return var_0_0

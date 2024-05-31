﻿local var_0_0 = class("ChatBubbleWorldBoss")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.interactable = defaultValue(arg_1_2, true)
	arg_1_0.nameTF = findTF(arg_1_0.tf, "desc/name"):GetComponent("Text")
	arg_1_0.face = findTF(arg_1_0.tf, "face/content")
	arg_1_0.circle = findTF(arg_1_0.tf, "shipicon/frame")
	arg_1_0.timeTF = findTF(arg_1_0.tf, "time"):GetComponent("Text")
	arg_1_0.headTF = findTF(arg_1_0.tf, "shipicon/icon"):GetComponent("Image")
	arg_1_0.stars = findTF(arg_1_0.tf, "shipicon/stars")
	arg_1_0.star = findTF(arg_1_0.stars, "star")
	arg_1_0.dutyTF = findTF(arg_1_0.tf, "desc/duty")
	arg_1_0.channel = findTF(arg_1_0.tf, "desc/channel")
	arg_1_0.chatframe = findTF(arg_1_0.tf, "chat_fram")
	arg_1_0.chatContent = findTF(arg_1_0.tf, "chat_fram/Text"):GetComponent("Text")
	arg_1_0.chatframeSel = findTF(arg_1_0.tf, "chat_fram/sel")
	arg_1_0.chatframeUnsel = findTF(arg_1_0.tf, "chat_fram/unsel")

	setActive(arg_1_0.chatframeSel, true)
	setActive(arg_1_0.chatframeUnsel, false)
end

function var_0_0.update(arg_2_0, arg_2_1)
	if arg_2_0.data == arg_2_1 then
		return
	end

	arg_2_0.data = arg_2_1

	local var_2_0 = false
	local var_2_1 = arg_2_1.player

	if var_2_1.icon == 0 then
		var_2_1.icon = 101171
	end

	local var_2_2 = var_2_1.propose

	arg_2_0.nameTF.text = var_2_1.name

	local var_2_3 = arg_2_1.timestamp
	local var_2_4 = getOfflineTimeStamp(var_2_3)

	arg_2_0.timeTF.text = var_2_4

	local var_2_5 = pg.ship_data_statistics[var_2_1.icon]
	local var_2_6 = Ship.New({
		configId = var_2_5.id
	})
	local var_2_7 = arg_2_0.stars.childCount
	local var_2_8 = var_2_6:getStar()

	for iter_2_0 = var_2_7, var_2_8 - 1 do
		cloneTplTo(arg_2_0.star, arg_2_0.stars)
	end

	local var_2_9 = arg_2_0.stars.childCount

	for iter_2_1 = 0, var_2_9 - 1 do
		arg_2_0.stars:GetChild(iter_2_1).gameObject:SetActive(iter_2_1 < var_2_5.star)
	end

	if arg_2_0.channel then
		local var_2_10 = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_2_1.type) .. "_1920")

		setImageSprite(arg_2_0.channel, var_2_10, true)
	end

	arg_2_0.headTF.color = Color.New(1, 1, 1, 0)

	LoadSpriteAsync("qicon/" .. var_2_1:getPainting(), function(arg_3_0)
		if not IsNil(arg_2_0.headTF) then
			arg_2_0.headTF.color = Color.white
			arg_2_0.headTF.sprite = arg_3_0 or LoadSprite("heroicon/unknown")
		end
	end)

	if arg_2_0.dutyTF then
		setActive(arg_2_0.dutyTF, var_2_1.duty)

		if var_2_1.duty then
			local var_2_11 = GetSpriteFromAtlas("dutyicon", var_2_1.duty)

			setImageSprite(arg_2_0.dutyTF, var_2_11, true)
		end
	end

	local var_2_12 = AttireFrame.attireFrameRes(var_2_1, var_2_0, AttireConst.TYPE_ICON_FRAME, var_2_2)

	PoolMgr.GetInstance():GetPrefab("IconFrame/" .. var_2_12, var_2_12, true, function(arg_4_0)
		if IsNil(arg_2_0.tf) then
			return
		end

		if arg_2_0.circle and arg_2_0.data then
			arg_4_0.name = var_2_12
			findTF(arg_4_0.transform, "icon"):GetComponent(typeof(Image)).raycastTarget = false

			setParent(arg_4_0, arg_2_0.circle, false)
		else
			PoolMgr.GetInstance():ReturnPrefab("IconFrame/" .. var_2_12, var_2_12, arg_4_0)
		end
	end)

	local var_2_13 = arg_2_1.args.wordBossId

	onButton(nil, arg_2_0.chatframe, function()
		if not arg_2_0.interactable then
			pg.TipsMgr.GetInstance():ShowTips(i18n("world_boss_inbattle"))

			return
		end

		if arg_2_1.args.isDeath then
			arg_2_0:SetGray()
			pg.TipsMgr.GetInstance():ShowTips(i18n("world_boss_none"))

			return
		end

		pg.WorldBossTipMgr.GetInstance():OnClick("", var_2_13, arg_2_1.args.lastTime, function()
			arg_2_0:SetGray()
		end)
	end, SFX_PANEL)

	if arg_2_1.args.isDeath then
		arg_2_0:SetGray()
	end

	arg_2_0.chatContent.text = i18n("world_boss_ad", arg_2_1.args.bossName, arg_2_1.args.level)
end

function var_0_0.SetGray(arg_7_0)
	setActive(arg_7_0.chatframeSel, false)
	setActive(arg_7_0.chatframeUnsel, true)
end

function var_0_0.dispose(arg_8_0)
	removeOnButton(arg_8_0.chatframe)

	if arg_8_0.circle.childCount > 0 then
		local var_8_0 = arg_8_0.circle:GetChild(0).gameObject

		PoolMgr.GetInstance():ReturnPrefab("IconFrame/" .. var_8_0.name, var_8_0.name, var_8_0)
	end
end

return var_0_0

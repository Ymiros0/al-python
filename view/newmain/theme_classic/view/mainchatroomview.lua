﻿local var_0_0 = class("MainChatRoomView", import("...base.MainBaseView"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	local var_1_0 = arg_1_1:Find("item")

	arg_1_0.items = {
		var_1_0
	}
	arg_1_0.tplInitPosY = var_1_0.anchoredPosition.y
	arg_1_0.MAX_COUNT = 4
	arg_1_0.enableBtn = arg_1_1:Find("enable")
	arg_1_0.disableBtn = arg_1_1:Find("disable")
	arg_1_0.btn = arg_1_1:GetComponent(typeof(Button))
	arg_1_0.empty = arg_1_1:Find("empty"):GetComponent(typeof(Text))

	arg_1_0:RegisterEvent(arg_1_2)
end

function var_0_0.RegisterEvent(arg_2_0, arg_2_1)
	arg_2_0:bind(GAME.REMOVE_LAYERS, function(arg_3_0, arg_3_1)
		arg_2_0:OnRemoveLayer(arg_3_1.context)
	end)
	arg_2_0:bind(GAME.ANY_CHAT_MSG_UPDATE, function(arg_4_0)
		arg_2_0:OnUpdateChatMsg()
	end)

	arg_2_0.hideChatFlag = PlayerPrefs.GetInt(HIDE_CHAT_FLAG)

	onButton(arg_2_0, arg_2_0._tf, function()
		if not arg_2_0.hideChatFlag or arg_2_0.hideChatFlag ~= 1 then
			arg_2_0:GoChatView()
		end
	end, SFX_MAIN)
	onButton(arg_2_0, arg_2_0.enableBtn, function()
		arg_2_0:SwitchState()
	end, SFX_MAIN)
	onButton(arg_2_0, arg_2_0.disableBtn, function()
		arg_2_0:SwitchState()
	end, SFX_MAIN)
	arg_2_0:UpdateBtnState()
end

function var_0_0.GoChatView(arg_8_0)
	arg_8_0:emit(NewMainMediator.OPEN_CHATVIEW)
end

function var_0_0.SwitchState(arg_9_0)
	local var_9_0 = arg_9_0.hideChatFlag and arg_9_0.hideChatFlag == 1
	local var_9_1 = var_9_0 and "show_chat_warning" or "hide_chat_warning"

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n(var_9_1),
		onYes = function()
			local var_10_0 = var_9_0 and 0 or 1

			PlayerPrefs.SetInt(HIDE_CHAT_FLAG, var_10_0)

			arg_9_0.hideChatFlag = PlayerPrefs.GetInt(HIDE_CHAT_FLAG)

			arg_9_0:UpdateBtnState()
		end
	})
end

function var_0_0.UpdateBtnState(arg_11_0)
	local var_11_0 = arg_11_0.hideChatFlag and arg_11_0.hideChatFlag == 1

	setActive(arg_11_0.enableBtn, var_11_0)
	setActive(arg_11_0.disableBtn, not var_11_0)

	if var_11_0 then
		arg_11_0:Clear()
	end

	arg_11_0.btn.enabled = not var_11_0
end

function var_0_0.OnRemoveLayer(arg_12_0, arg_12_1)
	if arg_12_1.mediator == NotificationMediator then
		arg_12_0:Update()
	end
end

function var_0_0.OnUpdateChatMsg(arg_13_0)
	arg_13_0:Update()
end

function var_0_0.Init(arg_14_0)
	arg_14_0:Update()
end

function var_0_0.Refresh(arg_15_0)
	arg_15_0:Update()
end

function var_0_0.Update(arg_16_0)
	if arg_16_0.hideChatFlag and arg_16_0.hideChatFlag == 1 then
		return
	end

	local var_16_0 = getProxy(ChatProxy):GetAllTypeChatMessages(arg_16_0.MAX_COUNT)

	arg_16_0:UpdateMessages(var_16_0)
end

function var_0_0.InstantiateMsgTpl(arg_17_0, arg_17_1)
	for iter_17_0 = #arg_17_0.items + 1, arg_17_1 do
		local var_17_0 = Object.Instantiate(arg_17_0.items[1], arg_17_0.items[1].parent)

		table.insert(arg_17_0.items, var_17_0)
	end

	for iter_17_1 = #arg_17_0.items, arg_17_1 + 1, -1 do
		setActive(arg_17_0.items[iter_17_1], false)
	end
end

function var_0_0.UpdateMessages(arg_18_0, arg_18_1)
	arg_18_0:InstantiateMsgTpl(#arg_18_1)

	for iter_18_0 = 1, #arg_18_1 do
		local var_18_0 = arg_18_0.items[iter_18_0]
		local var_18_1 = arg_18_1[iter_18_0]
		local var_18_2 = var_18_0.sizeDelta.y + 14
		local var_18_3 = arg_18_0.tplInitPosY - (iter_18_0 - 1) * var_18_2

		var_18_0.anchoredPosition = Vector2(var_18_0.anchoredPosition.x, var_18_3)

		arg_18_0:UpdateMessage(var_18_0, var_18_1)
	end

	local var_18_4 = PLATFORM_CODE == PLATFORM_JP and #arg_18_1 <= 0 and "ログはありません" or ""

	arg_18_0.empty.text = var_18_4
end

function var_0_0.UpdateMessage(arg_19_0, arg_19_1, arg_19_2)
	setActive(arg_19_1, true)

	findTF(arg_19_1, "channel"):GetComponent("Image").sprite = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_19_2.type) .. "_1920")

	local var_19_0 = findTF(arg_19_1, "text"):GetComponent("RichText")

	if arg_19_2.type == ChatConst.ChannelPublic then
		var_19_0.supportRichText = true

		ChatProxy.InjectPublic(var_19_0, arg_19_2, true)
	elseif arg_19_2:IsWorldBossNotify() then
		var_19_0.supportRichText = true

		local var_19_1 = arg_19_2.args.playerName
		local var_19_2 = arg_19_2.args.bossName
		local var_19_3 = GetPerceptualSize(var_19_1 .. var_19_2) - 18

		if var_19_3 > 0 then
			local var_19_4 = GetPerceptualSize(var_19_2) - var_19_3

			var_19_2 = shortenString(var_19_2, var_19_4)
		end

		var_19_0.text = i18n("ad_4", arg_19_2.args.supportType, var_19_1, var_19_2, arg_19_2.args.level)
	else
		var_19_0.supportRichText = arg_19_2.emojiId ~= nil
		var_19_0.text = arg_19_0:MatchEmoji(var_19_0, arg_19_2)
	end
end

function var_0_0.MatchEmoji(arg_20_0, arg_20_1, arg_20_2)
	local var_20_0 = false
	local var_20_1 = arg_20_2.player.name .. ": " .. arg_20_2.content
	local var_20_2 = false

	for iter_20_0 in string.gmatch(var_20_1, ChatConst.EmojiIconCodeMatch) do
		if table.contains(pg.emoji_small_template.all, tonumber(iter_20_0)) then
			var_20_2 = true

			local var_20_3 = pg.emoji_small_template[tonumber(iter_20_0)]
			local var_20_4 = LoadSprite("emoji/" .. var_20_3.pic .. "_small", nil)

			arg_20_1:AddSprite(iter_20_0, var_20_4)
		end
	end

	if not arg_20_2.emojiId then
		var_20_1 = var_20_2 and shortenString(var_20_1, 16) or shortenString(var_20_1, 20)
	end

	return (string.gsub(var_20_1, ChatConst.EmojiIconCodeMatch, function(arg_21_0)
		if table.contains(pg.emoji_small_template.all, tonumber(arg_21_0)) then
			return string.format("<icon name=%s w=0.7 h=0.7/>", arg_21_0)
		end
	end))
end

function var_0_0.Clear(arg_22_0)
	for iter_22_0, iter_22_1 in ipairs(arg_22_0.items) do
		setActive(iter_22_1, false)
	end
end

function var_0_0.GetDirection(arg_23_0)
	return Vector2(1, 0)
end

return var_0_0

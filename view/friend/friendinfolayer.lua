local var_0_0 = class("FriendInfoLayer", import("..base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "FriendInfoUI"
end

function var_0_0.setFriend(arg_2_0, arg_2_1)
	arg_2_0.friend = arg_2_1
end

function var_0_0.setFriendProxy(arg_3_0, arg_3_1)
	arg_3_0.friendProxy = arg_3_1
end

local var_0_1 = {
	"OPEN_RESUME",
	"OPEND_FRIEND",
	"OPEN_BACKYARD",
	"TOGGLE_BLACK",
	"OPEN_INFORM"
}

function var_0_0.init(arg_4_0)
	if arg_4_0.contextData.form == NotificationLayer.FORM_BATTLE then
		setParent(arg_4_0._tf, arg_4_0.contextData.parent)
	elseif arg_4_0.contextData.form == NotificationLayer.FORM_MAIN then
		pg.UIMgr.GetInstance():BlurPanel(arg_4_0._tf, false, {
			groupName = arg_4_0:getGroupNameFromData(),
			weight = LayerWeightConst.SECOND_LAYER
		})
	else
		pg.UIMgr.GetInstance():OverlayPanel(arg_4_0._tf, {
			groupName = arg_4_0:getGroupNameFromData(),
			weight = LayerWeightConst.SECOND_LAYER
		})
	end

	arg_4_0.frame = arg_4_0:findTF("frame")
	arg_4_0.iconTF = arg_4_0:findTF("frame/left_bg/icon_bg/frame/icon"):GetComponent(typeof(Image))
	arg_4_0.starsTF = arg_4_0:findTF("frame/left_bg/icon_bg/stars")
	arg_4_0.starTF = arg_4_0:findTF("frame/left_bg/icon_bg/stars/star")
	arg_4_0.playerNameTF = arg_4_0:findTF("frame/left_bg/name_bg/Text"):GetComponent(typeof(Text))
	arg_4_0.levelTF = arg_4_0:findTF("frame/left_bg/icon_bg/lv/Text"):GetComponent(typeof(Text))
	arg_4_0.resumeEmblem = arg_4_0:findTF("frame/left_bg/emblem")
	arg_4_0.resumeRank = arg_4_0:findTF("frame/left_bg/emblem/Text"):GetComponent(typeof(Text))
	arg_4_0.informPanel = arg_4_0:findTF("inform_panel")
	arg_4_0.toggleTpl = arg_4_0:findTF("inform_panel/frame/window/main/Toggle")
	arg_4_0.buttonTpl = arg_4_0:findTF("inform_panel/frame/window/main/button")
	arg_4_0.toggleContainer = arg_4_0:findTF("inform_panel/frame/window/main/toggles")
	arg_4_0.confirmBtn = arg_4_0:findTF("frame/window/buttons/confirm_btn", arg_4_0.informPanel)
	arg_4_0.cancelBtn = arg_4_0:findTF("frame/window/buttons/cancel_btn", arg_4_0.informPanel)
	arg_4_0.backBtn = arg_4_0:findTF("inform_panel/frame/window/top/btnBack")
	arg_4_0.nameTF = arg_4_0:findTF("inform_panel/frame/window/name"):GetComponent(typeof(Text))

	if arg_4_0.contextData.pos then
		if arg_4_0.contextData.backyardView then
			local var_4_0 = arg_4_0:findTF("frame_for_backyard")

			var_4_0.position = arg_4_0.contextData.pos
			var_4_0.localPosition = Vector3(var_4_0.localPosition.x, var_4_0.localPosition.y, 0)
		else
			arg_4_0.height = arg_4_0._tf.rect.height
			arg_4_0.frame.position = arg_4_0.contextData.pos

			local var_4_1 = arg_4_0.frame.localPosition
			local var_4_2 = -1 * (arg_4_0.height / 2 - arg_4_0.frame.sizeDelta.y)
			local var_4_3 = var_4_2 >= var_4_1.y and var_4_2 or var_4_1.y

			arg_4_0.frame.localPosition = Vector3(var_4_1.x, var_4_3, 0)
		end
	end
end

function var_0_0.didEnter(arg_5_0)
	arg_5_0:Init()
	onButton(arg_5_0, arg_5_0._tf, function()
		arg_5_0:emit(var_0_0.ON_CLOSE)
	end, SOUND_BACK)
end

function var_0_0.Init(arg_7_0)
	local var_7_0 = arg_7_0.contextData.backyardView

	arg_7_0:initInfo()
	setActive(arg_7_0:findTF("frame_for_backyard"), var_7_0)
	setActive(arg_7_0:findTF("frame"), not var_7_0)

	local var_7_1

	if var_7_0 then
		var_7_1 = arg_7_0:findTF("frame_for_backyard/right_bg")
	else
		var_7_1 = arg_7_0:findTF("frame/right_bg")
	end

	arg_7_0.btnTFs = {}

	for iter_7_0, iter_7_1 in ipairs(var_0_1) do
		local var_7_2 = var_7_1:GetChild(iter_7_0 - 1)

		setActive(var_7_2, true)
		onButton(arg_7_0, var_7_2, function()
			if iter_7_1 == "" then
				return
			end

			if iter_7_1 == "OPEN_INFORM" then
				local var_8_0 = arg_7_0.friend.id .. arg_7_0.contextData.msg
				local var_8_1 = getProxy(ChatProxy)

				if not table.contains(var_8_1.informs, var_8_0) then
					arg_7_0:openInfromPanel()
				else
					pg.TipsMgr.GetInstance():ShowTips(i18n("chat_msg_inform"))
				end
			else
				arg_7_0:emit(FriendInfoMediator[iter_7_1])
			end
		end)

		arg_7_0.btnTFs[iter_7_0] = var_7_2
	end

	setActive(arg_7_0.btnTFs[5], arg_7_0.contextData.msg)
	setButtonEnabled(arg_7_0.btnTFs[2], not arg_7_0.friendProxy:isFriend(arg_7_0.friend.id))
	arg_7_0:updateBlack()

	if arg_7_0.contextData.form == NotificationLayer.FORM_BATTLE then
		setActive(arg_7_0.btnTFs[3], false)

		local var_7_3 = arg_7_0:findTF("frame")
		local var_7_4 = var_7_3.sizeDelta

		var_7_3.sizeDelta = Vector2(var_7_4.x, var_7_4.y - 66.7)
	end

	setActive(arg_7_0:findTF("frame/left_bg", false))
end

function var_0_0.openInfromPanel(arg_9_0)
	setActive(arg_9_0.informPanel, true)

	if not arg_9_0.isInitInform then
		arg_9_0.isInitInform = true

		arg_9_0:initInform()
	end
end

function var_0_0.initInform(arg_10_0)
	arg_10_0.informInfoForBackYard = {}

	local var_10_0
	local var_10_1 = arg_10_0.contextData.backyardView

	if var_10_1 then
		arg_10_0.nameTF.text = i18n("inform_player", arg_10_0.friend.name) .. i18n("backyard_theme_inform_them", arg_10_0.contextData.msg)

		local var_10_2 = require("ShareCfg.InformForBackYardThemeTemplateCfg")

		for iter_10_0, iter_10_1 in ipairs(var_10_2) do
			local var_10_3 = cloneTplTo(arg_10_0.buttonTpl, arg_10_0.toggleContainer)

			var_10_3:Find("Label"):GetComponent("Text").text = iter_10_1.content

			local var_10_4 = false

			onButton(arg_10_0, var_10_3, function()
				var_10_4 = not var_10_4

				setActive(var_10_3:Find("Background/Checkmark"), var_10_4)

				if var_10_4 then
					table.insert(arg_10_0.informInfoForBackYard, iter_10_0)
				elseif table.contains(arg_10_0.informInfoForBackYard, iter_10_0) then
					table.removebyvalue(arg_10_0.informInfoForBackYard, iter_10_0)
				end
			end)
		end
	else
		arg_10_0.nameTF.text = i18n("inform_player", arg_10_0.friend.name)

		local var_10_5 = require("ShareCfg.informCfg")

		for iter_10_2, iter_10_3 in ipairs(var_10_5) do
			local var_10_6 = cloneTplTo(arg_10_0.toggleTpl, arg_10_0.toggleContainer)

			var_10_6:Find("Label"):GetComponent("Text").text = iter_10_3.content

			onToggle(arg_10_0, var_10_6, function(arg_12_0)
				if arg_12_0 then
					arg_10_0.informInfo = iter_10_3.content
				end
			end)
		end
	end

	onButton(arg_10_0, arg_10_0.confirmBtn, function()
		if not arg_10_0.contextData.msg then
			pg.TipsMgr.GetInstance():ShowTips(i18n("inform_chat_msg"))

			return
		end

		if var_10_1 then
			if #arg_10_0.informInfoForBackYard == 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("inform_select_type"))

				return
			end

			arg_10_0:emit(FriendInfoMediator.INFORM_BACKYARD, arg_10_0.friend.id, arg_10_0.informInfoForBackYard, arg_10_0.contextData.msg, arg_10_0.friend.name)
		else
			if not arg_10_0.informInfo then
				pg.TipsMgr.GetInstance():ShowTips(i18n("inform_select_type"))

				return
			end

			arg_10_0:emit(FriendInfoMediator.INFORM, arg_10_0.friend.id, arg_10_0.informInfo, arg_10_0.contextData.msg)
		end
	end)
	onButton(arg_10_0, arg_10_0.cancelBtn, function()
		arg_10_0:closeInfromPanel()
	end)
	onButton(arg_10_0, arg_10_0.backBtn, function()
		arg_10_0:closeInfromPanel()
	end)
end

function var_0_0.closeInfromPanel(arg_16_0)
	setActive(arg_16_0.informPanel, false)

	arg_16_0.informInfo = nil
end

function var_0_0.initInfo(arg_17_0)
	assert(arg_17_0.friend, "self.friend is nil")

	local var_17_0 = pg.ship_data_statistics[arg_17_0.friend.icon]

	assert(var_17_0, "shipCfg is nil >> id ==" .. arg_17_0.friend.icon)

	local var_17_1 = pg.ship_skin_template[var_17_0.skin_id]

	assert(var_17_1, "skinCfg is nil >> id ==" .. var_17_0.skin_id)
	LoadSpriteAsync("qicon/" .. var_17_1.painting, function(arg_18_0)
		if not IsNil(arg_17_0.iconTF) then
			if not arg_18_0 then
				arg_17_0.iconTF.sprite = GetSpriteFromAtlas("heroicon/unknown", "")
			else
				arg_17_0.iconTF.sprite = arg_18_0
			end
		end
	end)

	for iter_17_0 = arg_17_0.starsTF.childCount, var_17_0.star - 1 do
		cloneTplTo(arg_17_0.starTF, arg_17_0.starsTF)
	end

	for iter_17_1 = 1, var_17_0.star do
		local var_17_2 = arg_17_0.starsTF:GetChild(iter_17_1 - 1)

		setActive(var_17_2, iter_17_1 <= var_17_0.star)
	end

	arg_17_0.playerNameTF.text = arg_17_0.friend.name
	arg_17_0.levelTF.text = arg_17_0.friend.level

	local var_17_3 = SeasonInfo.getMilitaryRank(arg_17_0.friend.score, arg_17_0.friend.rank)
	local var_17_4 = SeasonInfo.getEmblem(arg_17_0.friend.score, arg_17_0.friend.rank)

	LoadImageSpriteAsync("emblem/" .. var_17_4, arg_17_0.resumeEmblem)
end

function var_0_0.updateBlack(arg_19_0)
	local var_19_0 = arg_19_0.friendProxy:getBlackPlayerById(arg_19_0.friend.id) ~= nil

	setActive(findTF(arg_19_0.btnTFs[4], "black"), not var_19_0)
	setActive(findTF(arg_19_0.btnTFs[4], "unblack"), var_19_0)
end

function var_0_0.willExit(arg_20_0)
	return
end

return var_0_0

pg = pg or {}
pg.ToastMgr = singletonClass("ToastMgr")

local var_0_0 = pg.ToastMgr
local var_0_1 = require("Mgr/Pool/PoolPlural")

var_0_0.TYPE_ATTIRE = "Attire"
var_0_0.TYPE_TECPOINT = "Tecpoint"
var_0_0.TYPE_TROPHY = "Trophy"
var_0_0.TYPE_META = "Meta"
var_0_0.TYPE_CRUSING = "Crusing"
var_0_0.TYPE_VOTE = "Vote"
var_0_0.TYPE_EMOJI = "Emoji"
var_0_0.ToastInfo = {
	[var_0_0.TYPE_ATTIRE] = {
		Attire = "attire_tpl"
	},
	[var_0_0.TYPE_TECPOINT] = {
		Buff = "buff_tpl",
		Point = "point_tpl"
	},
	[var_0_0.TYPE_TROPHY] = {
		Trophy = "trophy_tpl"
	},
	[var_0_0.TYPE_META] = {
		MetaLevel = "meta_level_tpl",
		MetaExp = "meta_exp_tpl"
	},
	[var_0_0.TYPE_CRUSING] = {
		Crusing = "crusing_pt_tpl"
	},
	[var_0_0.TYPE_VOTE] = {
		Vote = "vote_tpl"
	},
	[var_0_0.TYPE_EMOJI] = {
		Emoji = "emoji_tpl"
	}
}

function var_0_0.Init(arg_1_0, arg_1_1)
	PoolMgr.GetInstance():GetUI("ToastUI", true, function(arg_2_0)
		arg_1_0._go = arg_2_0

		arg_1_0._go:SetActive(false)

		arg_1_0._tf = arg_1_0._go.transform
		arg_1_0.container = arg_1_0._tf:Find("container")

		arg_1_0._go.transform:SetParent(pg.UIMgr.GetInstance().OverlayToast, false)

		arg_1_0.pools = {}

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in pairs(var_0_0.ToastInfo) do
			for iter_2_2, iter_2_3 in pairs(iter_2_1) do
				var_2_0[iter_2_2 .. "Tpl"] = iter_2_3
			end
		end

		for iter_2_4, iter_2_5 in pairs(var_2_0) do
			local var_2_1 = arg_1_0._tf:Find("resources/" .. iter_2_5)

			if iter_2_5 == "meta_exp_tpl" then
				local var_2_2 = var_2_1:Find("ExpFull/Tip")

				setText(var_2_2, i18n("meta_toast_fullexp"))

				local var_2_3 = var_2_1:Find("ExpAdd/Tip")

				setText(var_2_3, i18n("meta_toast_tactics"))
			end

			setActive(var_2_1, false)

			local var_2_4 = var_2_1.gameObject

			arg_1_0.pools[iter_2_4] = var_0_1.New(var_2_4, 5)
		end

		arg_1_0:ResetUIDandHistory()

		if arg_1_1 then
			arg_1_1()
		end
	end)
end

function var_0_0.ResetUIDandHistory(arg_3_0)
	arg_3_0.completedJob = 0
	arg_3_0.actionJob = 0
	arg_3_0.buffer = {}
end

function var_0_0.ShowToast(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = #arg_4_0.buffer

	table.insert(arg_4_0.buffer, {
		state = 0,
		type = arg_4_1,
		info = arg_4_2
	})
	setActive(arg_4_0._tf, true)

	if #arg_4_0.buffer == 1 or arg_4_0.buffer[var_4_0].state >= 2 then
		arg_4_0:Toast()
	end
end

function var_0_0.Toast(arg_5_0)
	if arg_5_0.actionJob >= #arg_5_0.buffer then
		return
	end

	if arg_5_0.buffer[arg_5_0.actionJob] and arg_5_0.buffer[arg_5_0.actionJob].state < 2 then
		return
	elseif arg_5_0.buffer[arg_5_0.actionJob] and arg_5_0.buffer[arg_5_0.actionJob].type ~= arg_5_0.buffer[arg_5_0.actionJob + 1].type and arg_5_0.buffer[arg_5_0.actionJob].state < 3 then
		return
	end

	arg_5_0.actionJob = arg_5_0.actionJob + 1

	local var_5_0 = arg_5_0.buffer[arg_5_0.actionJob]
	local var_5_1 = arg_5_0.actionJob

	var_5_0.state = 1

	arg_5_0["Update" .. var_5_0.type](arg_5_0, var_5_0, function()
		var_5_0.state = 2

		arg_5_0:Toast()
	end, function()
		var_5_0.state = 3

		if arg_5_0.buffer[var_5_1 + 1] and arg_5_0.buffer[var_5_1 + 1].state < 1 then
			arg_5_0:Toast()
		end

		arg_5_0.completedJob = arg_5_0.completedJob + 1

		if arg_5_0.completedJob >= #arg_5_0.buffer then
			arg_5_0:ResetUIDandHistory()
			setActive(arg_5_0._tf, false)

			for iter_7_0, iter_7_1 in pairs(arg_5_0.pools) do
				iter_7_1:ClearItems(false)
			end
		end
	end)
end

function var_0_0.GetAndSet(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = arg_8_0.pools[arg_8_1 .. "Tpl"]:Dequeue()

	setActive(var_8_0, true)
	setParent(var_8_0, arg_8_2)
	var_8_0.transform:SetAsLastSibling()

	return var_8_0
end

function var_0_0.UpdateAttire(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
	local var_9_0 = arg_9_0:GetAndSet(arg_9_1.type, arg_9_0.container)
	local var_9_1 = var_9_0:GetComponent(typeof(DftAniEvent))

	var_9_1:SetTriggerEvent(function(arg_10_0)
		if arg_9_2 then
			arg_9_2()
		end

		var_9_1:SetTriggerEvent(nil)
	end)
	var_9_1:SetEndEvent(function(arg_11_0)
		setActive(var_9_0, false)
		arg_9_0.pools[arg_9_1.type .. "Tpl"]:Enqueue(var_9_0)
		var_9_1:SetEndEvent(nil)

		if arg_9_3 then
			arg_9_3()
		end
	end)
	var_9_0:GetComponent(typeof(Animation)):Play("attire")

	local var_9_2 = arg_9_1.info

	assert(isa(var_9_2, AttireFrame))

	local var_9_3 = var_9_2:getType()

	setActive(var_9_0.transform:Find("bg/icon_frame"), var_9_3 == AttireConst.TYPE_ICON_FRAME)
	setActive(var_9_0.transform:Find("bg/chat_frame"), var_9_3 == AttireConst.TYPE_CHAT_FRAME)
	setText(var_9_0.transform:Find("bg/Text"), HXSet.hxLan(var_9_2:getConfig("name")))
end

function var_0_0.UpdateEmoji(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	local var_12_0 = arg_12_0:GetAndSet(arg_12_1.type, arg_12_0.container)
	local var_12_1 = var_12_0:GetComponent(typeof(DftAniEvent))

	var_12_1:SetTriggerEvent(function(arg_13_0)
		if arg_12_2 then
			arg_12_2()
		end

		var_12_1:SetTriggerEvent(nil)
	end)
	var_12_1:SetEndEvent(function(arg_14_0)
		setActive(var_12_0, false)
		arg_12_0.pools[arg_12_1.type .. "Tpl"]:Enqueue(var_12_0)
		var_12_1:SetEndEvent(nil)

		if arg_12_3 then
			arg_12_3()
		end
	end)
	var_12_0:GetComponent(typeof(Animation)):Play("attire")

	local var_12_2 = arg_12_1.info

	setText(var_12_0.transform:Find("bg/label"), i18n("word_emoji_unlock"))
	setText(var_12_0.transform:Find("bg/Text"), i18n("word_get_emoji", var_12_2.item_name))
end

var_0_0.FADE_TIME = 0.4
var_0_0.FADE_OUT_TIME = 1
var_0_0.SHOW_TIME = 1.5
var_0_0.DELAY_TIME = 0.3

function var_0_0.UpdateTecpoint(arg_15_0, arg_15_1, arg_15_2, arg_15_3)
	local var_15_0 = arg_15_1.info
	local var_15_1 = var_15_0.point
	local var_15_2 = var_15_0.typeList
	local var_15_3 = var_15_0.attr
	local var_15_4 = var_15_0.value
	local var_15_5 = arg_15_0:GetAndSet("Point", arg_15_0.container)

	GetComponent(var_15_5.transform, "CanvasGroup").alpha = 0

	setText(findTF(var_15_5, "PointText"), "+" .. var_15_1)

	local var_15_6 = {}

	if var_15_2 then
		for iter_15_0 = 1, #var_15_2 do
			local var_15_7 = arg_15_0:GetAndSet("Buff", arg_15_0.container)

			GetComponent(var_15_7.transform, "CanvasGroup").alpha = 0

			local var_15_8 = var_15_7.transform:Find("TypeImg")
			local var_15_9 = var_15_7.transform:Find("AttrText")
			local var_15_10 = var_15_7.transform:Find("ValueText")
			local var_15_11 = var_15_2[iter_15_0]
			local var_15_12 = GetSpriteFromAtlas("ShipType", "buffitem_tec_" .. var_15_11)

			setImageSprite(var_15_8.transform, var_15_12)
			setText(var_15_9.transform, AttributeType.Type2Name(pg.attribute_info_by_type[var_15_3].name))
			setText(var_15_10.transform, "+" .. var_15_4)

			var_15_6[iter_15_0] = go(var_15_7)
		end
	end

	local function var_15_13()
		if arg_15_2 then
			arg_15_2()
		end

		if arg_15_3 then
			arg_15_3()
		end
	end

	local var_15_14 = go(var_15_5)
	local var_15_15 = GetComponent(var_15_5, "CanvasGroup")

	local function var_15_16(arg_17_0)
		var_15_15.alpha = arg_17_0
	end

	local function var_15_17()
		LeanTween.moveX(rtf(var_15_14), 0, var_0_0.FADE_OUT_TIME)
		LeanTween.value(var_15_14, 1, 0, var_0_0.FADE_OUT_TIME):setOnUpdate(System.Action_float(var_15_16)):setOnComplete(System.Action(function()
			setActive(var_15_5, false)
			arg_15_0.pools.PointTpl:Enqueue(var_15_5)

			if not var_15_2 then
				var_15_13()
			end
		end))
	end

	LeanTween.value(var_15_14, 0, 1, var_0_0.FADE_TIME):setOnUpdate(System.Action_float(var_15_16)):setOnComplete(System.Action(function()
		LeanTween.delayedCall(var_15_14, var_0_0.SHOW_TIME, System.Action(var_15_17))
	end))

	local function var_15_18(arg_21_0, arg_21_1, arg_21_2)
		local var_21_0 = GetComponent(arg_21_0.transform, "CanvasGroup")

		local function var_21_1(arg_22_0)
			var_21_0.alpha = arg_22_0
		end

		local function var_21_2()
			LeanTween.moveX(rtf(arg_21_0), 0, var_0_0.FADE_OUT_TIME)
			LeanTween.value(arg_21_0, 1, 0, var_0_0.FADE_OUT_TIME):setOnUpdate(System.Action_float(var_21_1)):setOnComplete(System.Action(function()
				setActive(arg_21_0, false)
				arg_15_0.pools.BuffTpl:Enqueue(arg_21_0)

				if arg_21_2 then
					var_15_13()
				end
			end))
		end

		LeanTween.value(arg_21_0, 0, 1, var_0_0.FADE_TIME):setOnUpdate(System.Action_float(var_21_1)):setOnComplete(System.Action(function()
			LeanTween.delayedCall(arg_21_0, var_0_0.SHOW_TIME + (var_0_0.FADE_OUT_TIME - var_0_0.DELAY_TIME) * arg_21_1, System.Action(var_21_2))
		end))
	end

	for iter_15_1, iter_15_2 in ipairs(var_15_6) do
		LeanTween.delayedCall(var_15_14, iter_15_1 * var_0_0.DELAY_TIME, System.Action(function()
			var_15_18(iter_15_2, iter_15_1, iter_15_1 == #var_15_6)
		end))
	end
end

function var_0_0.UpdateTrophy(arg_27_0, arg_27_1, arg_27_2, arg_27_3)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_27_1.info.sound or SFX_UI_TIP)

	local var_27_0 = arg_27_0:GetAndSet(arg_27_1.type, arg_27_0.container)
	local var_27_1 = pg.medal_template[arg_27_1.info.id]

	LoadImageSpriteAsync("medal/s_" .. var_27_1.icon, var_27_0.transform:Find("content/icon"), true)
	setText(var_27_0.transform:Find("content/name"), var_27_1.name)
	setText(var_27_0.transform:Find("content/label"), i18n("trophy_achieved"))

	local var_27_2 = var_27_0.transform:Find("content")

	var_27_2.anchoredPosition = Vector2(-550, 0)

	LeanTween.moveX(rtf(var_27_2), 0, 0.5)
	LeanTween.moveX(rtf(var_27_2), -550, 0.5):setDelay(5):setOnComplete(System.Action(function()
		setActive(var_27_0, false)
		arg_27_0.pools[arg_27_1.type .. "Tpl"]:Enqueue(var_27_0)

		if arg_27_3 then
			arg_27_3()
		end
	end))

	if arg_27_2 then
		arg_27_2()
	end
end

function var_0_0.UpdateMeta(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	local var_29_0 = arg_29_1.info
	local var_29_1 = var_29_0.metaShipVO
	local var_29_2 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(var_29_1.configId)
	local var_29_3 = arg_29_0:GetAndSet("MetaExp", arg_29_0.container)
	local var_29_4 = arg_29_0:GetAndSet("MetaLevel", arg_29_0.container)
	local var_29_5 = var_29_3.transform:Find("ShipImg")
	local var_29_6, var_29_7 = MetaCharacterConst.GetMetaCharacterToastPath(var_29_2)

	setImageSprite(var_29_5, LoadSprite(var_29_6, var_29_7))

	local var_29_8 = var_29_3.transform:Find("Progress")
	local var_29_9 = pg.gameset.meta_skill_exp_max.key_value
	local var_29_10 = var_29_0.newDayExp
	local var_29_11 = var_29_0.addDayExp
	local var_29_12 = var_29_9 <= var_29_10

	setSlider(var_29_8, 0, var_29_9, var_29_10)

	local var_29_13 = var_29_0.curSkillID
	local var_29_14 = var_29_0.oldSkillLevel
	local var_29_15 = var_29_0.newSkillLevel
	local var_29_16 = var_29_14 < var_29_15
	local var_29_17 = var_29_3.transform:Find("ExpFull")
	local var_29_18 = var_29_3.transform:Find("ExpAdd")

	if var_29_12 then
		setActive(var_29_17, true)
		setActive(var_29_18, false)
	else
		local var_29_19 = var_29_3.transform:Find("ExpAdd/Value")

		setText(var_29_19, string.format("+%d", var_29_11))
		setActive(var_29_17, false)
		setActive(var_29_18, var_29_16)
	end

	if var_29_16 then
		local var_29_20 = var_29_4.transform:Find("Skill/Icon")
		local var_29_21 = getSkillConfig(var_29_13)

		setImageSprite(var_29_20, LoadSprite("skillicon/" .. var_29_21.icon))

		local var_29_22 = var_29_4.transform:Find("LevelUp")
		local var_29_23 = var_29_4.transform:Find("LevelMax")

		if var_29_15 >= pg.skill_data_template[var_29_13].max_level then
			setActive(var_29_22, false)
			setActive(var_29_23, true)
		else
			local var_29_24 = var_29_4.transform:Find("LevelUp/Value")

			setText(var_29_24, string.format("+%d", var_29_15 - var_29_14))
			setActive(var_29_22, true)
			setActive(var_29_23, false)
		end
	end

	local function var_29_25()
		if arg_29_2 then
			arg_29_2()
		end

		if arg_29_3 then
			arg_29_3()
		end
	end

	local var_29_26 = GetComponent(var_29_3, "CanvasGroup")
	local var_29_27 = GetComponent(var_29_4, "CanvasGroup")

	var_29_26.alpha = 0
	var_29_27.alpha = 0

	if var_29_12 or var_29_16 then
		local function var_29_28(arg_31_0)
			var_29_26.alpha = arg_31_0
		end

		local function var_29_29()
			LeanTween.moveX(rtf(var_29_3.transform), 0, var_0_0.FADE_OUT_TIME)
			LeanTween.value(var_29_3, 1, 0, var_0_0.FADE_OUT_TIME):setOnUpdate(System.Action_float(var_29_28)):setOnComplete(System.Action(function()
				arg_29_0.pools.MetaExpTpl:Enqueue(var_29_3)

				if not var_29_16 then
					arg_29_0.pools.MetaLevelTpl:Enqueue(var_29_4)
					var_29_25()
				end
			end))
		end

		local function var_29_30()
			LeanTween.delayedCall(var_29_3, var_0_0.SHOW_TIME, System.Action(var_29_29))
		end

		LeanTween.value(var_29_3, 0, 1, var_0_0.FADE_TIME):setOnUpdate(System.Action_float(var_29_28)):setOnComplete(System.Action(var_29_30))
	end

	if var_29_16 then
		local function var_29_31(arg_35_0)
			var_29_27.alpha = arg_35_0
		end

		local function var_29_32()
			LeanTween.moveX(rtf(var_29_4.transform), 0, var_0_0.FADE_OUT_TIME)
			LeanTween.value(var_29_4, 1, 0, var_0_0.FADE_OUT_TIME):setOnUpdate(System.Action_float(var_29_31)):setOnComplete(System.Action(function()
				arg_29_0.pools.MetaLevelTpl:Enqueue(var_29_4)
				var_29_25()
			end))
		end

		local function var_29_33()
			LeanTween.delayedCall(var_29_4, var_0_0.SHOW_TIME, System.Action(var_29_32))
		end

		LeanTween.delayedCall(var_29_4, var_0_0.DELAY_TIME, System.Action(function()
			LeanTween.value(var_29_4, 0, 1, var_0_0.FADE_TIME):setOnUpdate(System.Action_float(var_29_31)):setOnComplete(System.Action(var_29_33))
		end))
	end
end

function var_0_0.UpdateCrusing(arg_40_0, arg_40_1, arg_40_2, arg_40_3)
	local var_40_0 = arg_40_1.info
	local var_40_1 = var_40_0.ptId
	local var_40_2 = var_40_0.ptCount

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_40_1.info.sound or SFX_UI_TIP)

	local var_40_3 = tf(arg_40_0:GetAndSet(arg_40_1.type, arg_40_0.container))
	local var_40_4 = Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = var_40_1
	})

	LoadImageSpriteAtlasAsync(var_40_4:getIcon(), "", var_40_3:Find("PointIcon"), true)
	setText(var_40_3:Find("info/name"), var_40_4:getName())
	setText(var_40_3:Find("info/pt"), "+" .. var_40_2)
	setAnchoredPosition(var_40_3, {
		x = var_40_3.rect.width
	})

	local var_40_5 = GetComponent(var_40_3, typeof(CanvasGroup))

	LeanTween.alphaCanvas(var_40_5, 1, 0.5):setFrom(0):setOnComplete(System.Action(function()
		LeanTween.alphaCanvas(var_40_5, 0, 0.5):setDelay(5):setOnComplete(System.Action(function()
			setActive(var_40_3, false)
			arg_40_0.pools[arg_40_1.type .. "Tpl"]:Enqueue(go(var_40_3))

			if arg_40_3 then
				arg_40_3()
			end
		end))

		if arg_40_2 then
			arg_40_2()
		end
	end))
end

function var_0_0.UpdateVote(arg_43_0, arg_43_1, arg_43_2, arg_43_3)
	local var_43_0 = arg_43_1.info
	local var_43_1 = var_43_0.ptId
	local var_43_2 = var_43_0.ptCount
	local var_43_3 = Drop.New({
		type = DROP_TYPE_ITEM,
		id = var_43_1
	})
	local var_43_4 = tf(arg_43_0:GetAndSet(arg_43_1.type, arg_43_0.container))

	LoadImageSpriteAtlasAsync(var_43_3:getIcon(), "", var_43_4:Find("PointIcon"), true)
	setText(var_43_4:Find("info/name"), var_43_3:getName())
	setText(var_43_4:Find("info/pt"), "+" .. var_43_2)
	setAnchoredPosition(var_43_4, {
		x = var_43_4.rect.width
	})

	local var_43_5 = GetComponent(var_43_4, typeof(CanvasGroup))

	LeanTween.alphaCanvas(var_43_5, 1, 0.5):setFrom(0):setOnComplete(System.Action(function()
		LeanTween.alphaCanvas(var_43_5, 0, 0.5):setDelay(5):setOnComplete(System.Action(function()
			setActive(var_43_4, false)
			arg_43_0.pools[arg_43_1.type .. "Tpl"]:Enqueue(go(var_43_4))

			if arg_43_3 then
				arg_43_3()
			end
		end))

		if arg_43_2 then
			arg_43_2()
		end
	end))
end

function var_0_0.Dispose(arg_46_0)
	setActive(arg_46_0._tf, false)
	arg_46_0:ResetUIDandHistory()

	for iter_46_0, iter_46_1 in pairs(arg_46_0.pools) do
		iter_46_1:Clear(false)
	end
end

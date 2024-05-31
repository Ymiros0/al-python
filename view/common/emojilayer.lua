local var_0_0 = class("EmojiLayer", import("..base.BaseUI"))

var_0_0.PageEmojiNums = 8
var_0_0.Frequently_Used_Emoji_Num = 6
var_0_0.True_Emoji_Num_Of_Page = 15

function var_0_0.getUIName(arg_1_0)
	return "EmojiUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.emojiGroup = arg_2_0:findTF("frame/group")
	arg_2_0.emojiType = arg_2_0:findTF("type", arg_2_0.emojiGroup)
	arg_2_0.emojiEvent = arg_2_0:findTF("frame/bg/mask/event")
	arg_2_0.emojiSnap = arg_2_0:findTF("frame/bg/mask/event"):GetComponent("HScrollSnap")

	arg_2_0.emojiSnap:Init()

	arg_2_0.emojiContent = arg_2_0:findTF("content", arg_2_0.emojiSnap)
	arg_2_0.emojiItem = arg_2_0:findTF("item", arg_2_0.emojiSnap)
	arg_2_0.emojiDots = arg_2_0:findTF("frame/dots")
	arg_2_0.emojiIconDots = arg_2_0:findTF("frame/emojiDots")
	arg_2_0.emojiDot = arg_2_0:findTF("dot", arg_2_0.emojiSnap)

	setText(arg_2_0.emojiEvent:Find("null_tpl/Text"), i18n("recently_sticker_placeholder"))
	setActive(arg_2_0.emojiItem, false)
	setActive(arg_2_0.emojiDot, false)

	arg_2_0.emojiIconEvent = arg_2_0:findTF("frame/bg/mask/emojiicon_event")
	arg_2_0.emojiIconSnap = arg_2_0:findTF("frame/bg/mask/emojiicon_event"):GetComponent("HScrollSnap")

	arg_2_0.emojiIconSnap:Init()

	arg_2_0.emojiIconContent = arg_2_0:findTF("content", arg_2_0.emojiIconSnap)
	arg_2_0.emojiIconItem = arg_2_0:findTF("item_emojiicon", arg_2_0.emojiIconSnap)

	setActive(arg_2_0.emojiIconItem, false)

	arg_2_0.parentTr = arg_2_0._tf.parent
	arg_2_0.resource = arg_2_0:findTF("frame/resource")
	arg_2_0.frame = arg_2_0:findTF("frame")
	arg_2_0.frame.position = arg_2_0.contextData.pos or Vector3(0, 0, 0)
	arg_2_0.frame.localPosition = Vector3(arg_2_0.frame.localPosition.x, arg_2_0.frame.localPosition.y, 0)
	arg_2_0.newTag = arg_2_0:findTF("newtag")
	arg_2_0.emojiProxy = getProxy(EmojiProxy)
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:emit(var_0_0.ON_CLOSE)
	end, SFX_CANCEL)
	arg_3_0:display()

	if getProxy(SettingsProxy):IsMellowStyle() then
		setParent(arg_3_0._tf, pg.UIMgr.GetInstance().OverlayMain)
	else
		pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf, false, {
			groupName = arg_3_0:getGroupNameFromData(),
			weight = LayerWeightConst.SECOND_LAYER
		})
	end
end

function var_0_0.display(arg_5_0)
	local var_5_0 = UIItemList.New(arg_5_0.emojiGroup, arg_5_0.emojiType)

	var_5_0:make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate then
			local var_6_0 = ChatConst.EmojiTypes[arg_6_1 + 1]

			setText(arg_6_2:Find("Text"), i18n("emoji_type_" .. var_6_0))

			if arg_5_0.emojiProxy:fliteNewEmojiDataByType()[var_6_0] then
				setActive(arg_6_2:Find("point"), true)
			else
				setActive(arg_6_2:Find("point"), false)
			end

			onToggle(arg_5_0, arg_6_2, function(arg_7_0)
				if arg_7_0 then
					setActive(arg_5_0.emojiDots, var_6_0 ~= ChatConst.EmojiIcon)
					setActive(arg_5_0.emojiIconDots, var_6_0 == ChatConst.EmojiIcon)
					setActive(arg_5_0.emojiEvent, var_6_0 ~= ChatConst.EmojiIcon)
					setActive(arg_5_0.emojiIconEvent, var_6_0 == ChatConst.EmojiIcon)

					if var_6_0 ~= ChatConst.EmojiIcon then
						arg_5_0:filter(var_6_0)
					elseif var_6_0 == ChatConst.EmojiIcon then
						arg_5_0:emojiIconFliter()
					end

					var_5_0:align(#ChatConst.EmojiTypes)
				end
			end, SFX_PANEL)
		end
	end)
	var_5_0:align(#ChatConst.EmojiTypes)
	triggerToggle(arg_5_0.emojiGroup:GetChild(0), true)
end

function var_0_0.filter(arg_8_0, arg_8_1)
	local var_8_0 = _.map(pg.emoji_template.all, function(arg_9_0)
		if pg.emoji_template[arg_9_0].achieve == 0 then
			return pg.emoji_template[arg_9_0]
		end
	end)
	local var_8_1 = arg_8_0.emojiProxy:getNewEmojiIDLIst()
	local var_8_2 = arg_8_0.emojiProxy:fliteNewEmojiDataByType()
	local var_8_3 = arg_8_0.emojiProxy:getExEmojiDataByType(arg_8_1)

	for iter_8_0, iter_8_1 in pairs(var_8_3) do
		table.insert(var_8_0, 1, iter_8_1)
	end

	table.sort(var_8_0, function(arg_10_0, arg_10_1)
		if arg_10_0.index == arg_10_1.index then
			return arg_10_0.id < arg_10_1.id
		end

		return arg_10_0.index < arg_10_1.index
	end)

	if arg_8_1 == ChatConst.EmojiCommon then
		local var_8_4 = getProxy(ChatProxy):getUsedEmoji()
		local var_8_5 = {}

		for iter_8_2, iter_8_3 in pairs(var_8_4) do
			table.insert(var_8_5, {
				id = iter_8_2,
				count = iter_8_3
			})
		end

		table.sort(var_8_5, function(arg_11_0, arg_11_1)
			if arg_11_0.count == arg_11_1.count then
				return arg_11_0.id < arg_11_1.id
			end

			return arg_11_0.count > arg_11_1.count
		end)

		var_8_0 = _.map(var_8_5, function(arg_12_0)
			return pg.emoji_template[arg_12_0.id]
		end)
	else
		var_8_0 = _.filter(var_8_0, function(arg_13_0)
			return table.contains(arg_13_0.type, arg_8_1)
		end)
	end

	if var_8_2[arg_8_1] then
		for iter_8_4, iter_8_5 in pairs(var_8_2[arg_8_1]) do
			table.insert(var_8_0, 1, iter_8_5)
		end
	end

	arg_8_0.tplCaches = arg_8_0.tplCaches or {}

	local var_8_6 = math.ceil(#var_8_0 / var_0_0.PageEmojiNums)

	setActive(arg_8_0.emojiEvent:Find("null_tpl"), var_8_6 == 0)

	for iter_8_6 = arg_8_0.emojiContent.childCount - 1, var_8_6, -1 do
		Destroy(arg_8_0.emojiDots:GetChild(iter_8_6))

		local var_8_7 = arg_8_0.emojiSnap:RemoveChild(iter_8_6)

		var_8_7.transform.localScale = Vector3.one

		var_8_7.transform:SetParent(arg_8_0._tf, false)
		setActive(var_8_7, false)
		arg_8_0:clearItem(var_8_7)
		table.insert(arg_8_0.tplCaches, var_8_7)
	end

	for iter_8_7 = arg_8_0.emojiContent.childCount + 1, var_8_6 do
		local var_8_8

		if #arg_8_0.tplCaches > 0 then
			var_8_8 = table.remove(arg_8_0.tplCaches)
		else
			var_8_8 = Instantiate(arg_8_0.emojiItem)
		end

		setActive(var_8_8, true)
		arg_8_0.emojiSnap:AddChild(var_8_8)
		cloneTplTo(arg_8_0.emojiDot, arg_8_0.emojiDots)
	end

	for iter_8_8 = 0, arg_8_0.emojiContent.childCount - 1 do
		local var_8_9 = arg_8_0.emojiContent:GetChild(iter_8_8)

		arg_8_0:clearItem(var_8_9)

		local var_8_10 = _.slice(var_8_0, iter_8_8 * var_0_0.PageEmojiNums + 1, var_0_0.PageEmojiNums)
		local var_8_11 = GetComponent(var_8_9, typeof(GridLayoutGroup))
		local var_8_12 = UIItemList.New(var_8_9, var_8_9:Find("face"))

		var_8_12:make(function(arg_14_0, arg_14_1, arg_14_2)
			local var_14_0 = var_8_10[arg_14_1 + 1]

			if arg_14_0 == UIItemList.EventUpdate then
				PoolMgr.GetInstance():GetPrefab("emoji/" .. var_14_0.pic, var_14_0.pic, true, function(arg_15_0)
					if not IsNil(arg_14_2) then
						arg_15_0.name = var_14_0.pic
						tf(arg_15_0).sizeDelta = Vector2(var_8_11.cellSize.x, var_8_11.cellSize.y)
						tf(arg_15_0).anchoredPosition = Vector2.zero

						local var_15_0 = arg_15_0:GetComponent("Animator")

						if var_15_0 then
							var_15_0.enabled = false
						end

						local var_15_1 = arg_15_0:GetComponent("CriManaEffectUI")

						if var_15_1 then
							var_15_1:Pause(true)
						end

						setParent(arg_15_0, arg_14_2, false)

						if table.contains(var_8_1, var_14_0.id) then
							cloneTplTo(arg_8_0.newTag, arg_14_2, "newtag")
							arg_8_0.emojiProxy:removeNewEmojiID(var_14_0.id)
						end
					else
						PoolMgr.GetInstance():ReturnPrefab("emoji/" .. var_14_0.pic, var_14_0.pic, arg_15_0)
					end
				end)
				onButton(arg_8_0, arg_14_2, function()
					getProxy(ChatProxy):addUsedEmoji(var_14_0.id)
					arg_8_0.contextData.callback(var_14_0.id)
					triggerButton(arg_8_0._tf)
				end, SFX_PANEL)
			end
		end)
		var_8_12:align(#var_8_10)
	end
end

function var_0_0.emojiIconFliter(arg_17_0)
	local var_17_0 = pg.emoji_small_template
	local var_17_1 = {}
	local var_17_2 = getProxy(ChatProxy):getUsedEmojiIcon()

	for iter_17_0, iter_17_1 in ipairs(var_17_2) do
		table.insert(var_17_1, var_17_0[iter_17_1])
	end

	local var_17_3 = math.ceil((#var_17_0 + #var_17_1) / var_0_0.True_Emoji_Num_Of_Page)

	for iter_17_2 = arg_17_0.emojiIconContent.childCount + 1, var_17_3 do
		cloneTplTo(arg_17_0.emojiDot, arg_17_0.emojiIconDots)
	end

	for iter_17_3 = arg_17_0.emojiIconContent.childCount + 1, var_17_3 do
		local var_17_4 = Instantiate(arg_17_0.emojiIconItem)
		local var_17_5 = arg_17_0:findTF("TitleCommom", var_17_4)
		local var_17_6 = arg_17_0:findTF("TitleAll", var_17_4)
		local var_17_7 = arg_17_0:findTF("CommomIconContainer", var_17_4)
		local var_17_8 = arg_17_0:findTF("AllIconContainer", var_17_4)
		local var_17_9 = GetComponent(var_17_8, "GridLayoutGroup")

		if iter_17_3 == 1 then
			local var_17_10 = arg_17_0:findTF("Icon", var_17_7)
			local var_17_11 = UIItemList.New(var_17_7, var_17_10)

			var_17_11:make(function(arg_18_0, arg_18_1, arg_18_2)
				local var_18_0 = var_17_1[arg_18_1 + 1]

				if arg_18_0 == UIItemList.EventUpdate then
					PoolMgr.GetInstance():GetPrefab("emoji/" .. var_18_0.pic, var_18_0.pic, true, function(arg_19_0)
						if not IsNil(arg_18_2) then
							arg_19_0.name = var_18_0.pic

							setParent(arg_19_0, arg_18_2, false)
							onButton(arg_17_0, arg_19_0, function()
								if arg_17_0.contextData.emojiIconCallback then
									getProxy(ChatProxy):addUsedEmojiIcon(var_18_0.id)
									arg_17_0.contextData.emojiIconCallback(var_18_0.id)
								end
							end, SFX_PANEL)
						end
					end)
				end
			end)
			var_17_11:align(#var_17_1)

			var_17_9.padding.left = 20

			local var_17_12 = arg_17_0:findTF("Icon", var_17_8)
			local var_17_13 = UIItemList.New(var_17_8, var_17_12)

			var_17_13:make(function(arg_21_0, arg_21_1, arg_21_2)
				local var_21_0 = var_17_0[arg_21_1 + 1]

				if arg_21_0 == UIItemList.EventUpdate then
					PoolMgr.GetInstance():GetPrefab("emoji/" .. var_21_0.pic, var_21_0.pic, true, function(arg_22_0)
						if not IsNil(arg_21_2) then
							arg_22_0.name = var_21_0.pic

							setParent(arg_22_0, arg_21_2, false)
							onButton(arg_17_0, arg_22_0, function()
								if arg_17_0.contextData.emojiIconCallback then
									getProxy(ChatProxy):addUsedEmojiIcon(var_21_0.id)
									arg_17_0.contextData.emojiIconCallback(var_21_0.id)
								end
							end, SFX_PANEL)
						end
					end)
				end
			end)
			var_17_13:align(var_0_0.True_Emoji_Num_Of_Page - var_0_0.Frequently_Used_Emoji_Num)
		else
			local var_17_14 = var_0_0.True_Emoji_Num_Of_Page - var_0_0.Frequently_Used_Emoji_Num
			local var_17_15 = _.slice(var_17_0, (iter_17_3 - 2) * var_0_0.True_Emoji_Num_Of_Page + 9 + 1, var_0_0.True_Emoji_Num_Of_Page)

			var_17_9.padding.left = 60

			local var_17_16 = arg_17_0:findTF("Icon", var_17_8)
			local var_17_17 = UIItemList.New(var_17_8, var_17_16)

			var_17_17:make(function(arg_24_0, arg_24_1, arg_24_2)
				local var_24_0 = var_17_15[arg_24_1 + 1]

				if arg_24_0 == UIItemList.EventUpdate then
					PoolMgr.GetInstance():GetPrefab("emoji/" .. var_24_0.pic, var_24_0.pic, true, function(arg_25_0)
						if not IsNil(arg_24_2) then
							arg_25_0.name = var_24_0.pic

							setParent(arg_25_0, arg_24_2, false)
							onButton(arg_17_0, arg_25_0, function()
								if arg_17_0.contextData.emojiIconCallback then
									getProxy(ChatProxy):addUsedEmojiIcon(var_24_0.id)
									arg_17_0.contextData.emojiIconCallback(var_24_0.id)
								end
							end, SFX_PANEL)
						end
					end)
				end
			end)
			var_17_17:align(#var_17_15)
		end

		setActive(var_17_5, iter_17_3 == 1)
		setActive(var_17_6, iter_17_3 == 1)
		setActive(var_17_7, iter_17_3 == 1)
		setActive(var_17_4, true)
		arg_17_0.emojiIconSnap:AddChild(var_17_4)
	end
end

function var_0_0.onBackPressed(arg_27_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_27_0._tf)
end

function var_0_0.clearItem(arg_28_0, arg_28_1)
	eachChild(arg_28_1, function(arg_29_0)
		if arg_29_0.childCount > 0 then
			local var_29_0 = arg_29_0:Find("newtag")

			if var_29_0 then
				Destroy(var_29_0)
			end

			local var_29_1 = arg_29_0:GetChild(0).gameObject

			PoolMgr.GetInstance():ReturnPrefab("emoji/" .. var_29_1.name, var_29_1.name, var_29_1)
		end
	end)
end

function var_0_0.willExit(arg_30_0)
	eachChild(arg_30_0.emojiContent, function(arg_31_0)
		arg_30_0:clearItem(arg_31_0)
	end)
	_.each(arg_30_0.tplCaches, function(arg_32_0)
		arg_30_0:clearItem(arg_32_0)
	end)

	if getProxy(SettingsProxy):IsMellowStyle() then
		setParent(arg_30_0._tf, arg_30_0.parentTr)
	else
		pg.UIMgr.GetInstance():UnblurPanel(arg_30_0._tf)
	end
end

return var_0_0

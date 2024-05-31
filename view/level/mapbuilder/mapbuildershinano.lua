local var_0_0 = import(".MapBuilder")
local var_0_1 = class("MapBuilderShinano", var_0_0)

function var_0_1.Ctor(arg_1_0, ...)
	var_0_1.super.Ctor(arg_1_0, ...)

	arg_1_0.chapterTFsById = {}
	arg_1_0.chaptersInBackAnimating = {}
end

function var_0_1.GetType(arg_2_0)
	return var_0_0.TYPESHINANO
end

function var_0_1.getUIName(arg_3_0)
	return "Shinano_levels"
end

function var_0_1.OnInit(arg_4_0)
	arg_4_0.tpl = arg_4_0._tf:Find("level_tpl")

	setActive(arg_4_0.tpl, false)

	arg_4_0.itemHolder = arg_4_0._tf:Find("items")

	local var_4_0 = arg_4_0._tf:Find("preloadResources"):GetComponent(typeof(ItemList))
	local var_4_1 = Instantiate(var_4_0.prefabItem[0])

	setAnchoredPosition(arg_4_0._tf:Find("rumeng"), tf(var_4_1).anchoredPosition)
	setParent(var_4_1, arg_4_0._tf:Find("rumeng"))
	setAnchoredPosition(var_4_1, Vector2.zero)
	arg_4_0:InitTransformMapBtn(arg_4_0._tf:Find("rumeng"), 1, var_4_0.prefabItem[1])

	local var_4_2 = Instantiate(var_4_0.prefabItem[2])

	setAnchoredPosition(arg_4_0._tf:Find("huigui"), tf(var_4_2).anchoredPosition)
	setParent(var_4_2, arg_4_0._tf:Find("huigui"))
	setAnchoredPosition(var_4_2, Vector2.zero)
	arg_4_0:InitTransformMapBtn(arg_4_0._tf:Find("huigui"), -1, var_4_0.prefabItem[3])
end

function var_0_1.OnShow(arg_5_0)
	setActive(arg_5_0.sceneParent.mainLayer:Find("title_chapter_lines"), true)
	setActive(arg_5_0.sceneParent.topChapter:Find("title_chapter"), true)
	setActive(arg_5_0.sceneParent.topChapter:Find("type_skirmish"), true)
end

function var_0_1.OnHide(arg_6_0)
	setActive(arg_6_0.sceneParent.mainLayer:Find("title_chapter_lines"), false)
	setActive(arg_6_0.sceneParent.topChapter:Find("title_chapter"), false)
	setActive(arg_6_0.sceneParent.topChapter:Find("type_skirmish"), false)
	table.clear(arg_6_0.chaptersInBackAnimating)

	for iter_6_0, iter_6_1 in pairs(arg_6_0.chapterTFsById) do
		local var_6_0 = findTF(iter_6_1, "main/info/bk")

		LeanTween.cancel(rtf(var_6_0))
	end

	var_0_1.super.OnHide(arg_6_0)
end

function var_0_1.TrySwitchNextMap(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0.sceneParent.contextData.mapIdx + arg_7_1
	local var_7_1 = getProxy(ChapterProxy):getMapById(var_7_0)

	if not var_7_1 then
		return
	end

	if var_7_1:getMapType() == Map.ELITE and not var_7_1:isEliteEnabled() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("elite_disable_unusable"))

		return
	end

	local var_7_2, var_7_3 = var_7_1:isUnlock()

	if not var_7_2 then
		pg.TipsMgr.GetInstance():ShowTips(var_7_3)

		return
	end

	return true
end

function var_0_1.InitTransformMapBtn(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	onButton(arg_8_0.sceneParent, arg_8_1, function()
		if arg_8_0.sceneParent:isfrozen() then
			return
		end

		local var_9_0

		seriesAsync({
			function(arg_10_0)
				if not arg_8_0:TrySwitchNextMap(arg_8_2) then
					return
				end

				pg.CriMgr.GetInstance():StopBGM()
				pg.CriMgr.GetInstance():PlaySE_V3("ui-qiehuan")

				var_9_0 = arg_8_0._tf:Find(arg_8_3.name .. "(Clone)") or Instantiate(arg_8_3)

				setParent(var_9_0, arg_8_0._tf)
				setAnchoredPosition(var_9_0, rtf(arg_8_1).anchoredPosition)

				local var_10_0 = arg_8_0.contextData.mapIdx + arg_8_2
				local var_10_1 = Map.bindConfigTable(Map)[var_10_0]

				if var_10_1 and #var_10_1.bg > 0 then
					GetSpriteFromAtlasAsync("levelmap/" .. var_10_1.bg, "", function(arg_11_0)
						return
					end)
				end

				arg_8_0.sceneParent:frozen()
				LeanTween.delayedCall(go(arg_8_1), 2.3, System.Action(arg_10_0))
			end,
			function(arg_12_0)
				arg_8_0.sceneParent:setMap(arg_8_0.contextData.mapIdx + arg_8_2)
				LeanTween.delayedCall(go(arg_8_1), 0.5, System.Action(arg_12_0))
			end,
			function(arg_13_0)
				if not IsNil(var_9_0) then
					Destroy(var_9_0)
				end

				arg_8_0.sceneParent:unfrozen()
			end
		})
	end)
end

function var_0_1.Update(arg_14_0, arg_14_1)
	arg_14_0.float.pivot = Vector2(0.5, 0.5)
	arg_14_0.float.anchoredPosition = Vector2(0, 0)

	local var_14_0 = string.split(arg_14_1:getConfig("name"), "||")

	setText(arg_14_0.sceneParent.chapterName, var_14_0[1])

	local var_14_1 = arg_14_1:getMapTitleNumber()

	arg_14_0.sceneParent.loader:GetSpriteQuiet("chapterno", "chapter" .. var_14_1, arg_14_0.sceneParent.chapterNoTitle, true)
	var_0_1.super.Update(arg_14_0, arg_14_1)
end

function var_0_1.UpdateButtons(arg_15_0)
	arg_15_0.sceneParent:updateDifficultyBtns()
	arg_15_0.sceneParent:updateActivityBtns()
end

function var_0_1.PostUpdateMap(arg_16_0, arg_16_1)
	local var_16_0 = arg_16_0.contextData.map:getConfig("type") == Map.ACT_EXTRA
	local var_16_1 = arg_16_0._tf:Find("rumeng")
	local var_16_2 = arg_16_0._tf:Find("huigui")

	setActive(var_16_1, false)
	setActive(var_16_2, false)

	if not var_16_0 then
		setActive(arg_16_0.sceneParent.btnPrev, false)
		setActive(arg_16_0.sceneParent.btnNext, false)

		local var_16_3 = getProxy(ChapterProxy):getMapById(arg_16_1.id + 1)
		local var_16_4 = getProxy(ChapterProxy):getMapById(arg_16_1.id - 1)

		setActive(var_16_1, var_16_3)
		setActive(var_16_2, var_16_4)
		LeanTween.cancel(go(var_16_1), true)
		LeanTween.cancel(go(var_16_2), true)

		if var_16_3 then
			local var_16_5 = tf(var_16_1).localScale
			local var_16_6 = tf(var_16_1):GetChild(0):Find("Quad"):GetComponent(typeof(MeshRenderer)).sharedMaterial
			local var_16_7 = var_16_6:GetColor("_MainColor")
			local var_16_8 = Clone(var_16_7)
			local var_16_9 = LeanTween.value(go(var_16_1), 0, 1, 0.8):setOnUpdate(System.Action_float(function(arg_17_0)
				var_16_8.a = var_16_7.a * arg_17_0

				var_16_6:SetColor("_MainColor", var_16_8)
			end)):setEase(LeanTweenType.easeInCubic):setOnComplete(System.Action(function()
				var_16_6:SetColor("_MainColor", var_16_7)
			end))

			arg_16_0:RecordTween("rumengAlphaTween", var_16_9.id)
		elseif var_16_4 then
			local var_16_10 = tf(var_16_2).localScale
			local var_16_11 = tf(var_16_2):GetChild(0):Find("Quad"):GetComponent(typeof(MeshRenderer)).sharedMaterial
			local var_16_12 = var_16_11:GetColor("_MainColor")
			local var_16_13 = Clone(var_16_12)
			local var_16_14 = LeanTween.value(go(var_16_2), 0, 1, 0.8):setOnUpdate(System.Action_float(function(arg_19_0)
				var_16_13.a = var_16_12.a * arg_19_0

				var_16_11:SetColor("_MainColor", var_16_13)
			end)):setEase(LeanTweenType.easeInCubic):setOnComplete(System.Action(function()
				var_16_11:SetColor("_MainColor", var_16_12)
			end))

			arg_16_0:RecordTween("huiguiAlphaTween", var_16_14.id)
		end
	end
end

function var_0_1.UpdateMapItems(arg_21_0)
	if not arg_21_0:isShowing() then
		return
	end

	var_0_1.super.UpdateMapItems(arg_21_0)

	local var_21_0 = arg_21_0.data
	local var_21_1 = getProxy(ChapterProxy)

	table.clear(arg_21_0.chapterTFsById)

	local var_21_2 = {}

	for iter_21_0, iter_21_1 in pairs(var_21_0:getChapters()) do
		if (iter_21_1:isUnlock() or iter_21_1:activeAlways()) and (not iter_21_1:ifNeedHide() or var_21_1:GetJustClearChapters(iter_21_1.id)) then
			table.insert(var_21_2, iter_21_1)
		end
	end

	UIItemList.StaticAlign(arg_21_0.itemHolder, arg_21_0.tpl, #var_21_2, function(arg_22_0, arg_22_1, arg_22_2)
		if arg_22_0 == UIItemList.EventUpdate then
			local var_22_0 = var_21_2[arg_22_1 + 1]

			arg_21_0:UpdateMapItem(arg_22_2, var_22_0)

			arg_22_2.name = "Chapter_" .. var_22_0.id
			arg_21_0.chapterTFsById[var_22_0.id] = arg_22_2
		end
	end)

	local var_21_3 = {}

	for iter_21_2, iter_21_3 in pairs(var_21_2) do
		local var_21_4 = iter_21_3:getConfigTable()

		var_21_3[var_21_4.pos_x] = var_21_3[var_21_4.pos_x] or {}

		local var_21_5 = var_21_3[var_21_4.pos_x]

		var_21_5[var_21_4.pos_y] = var_21_5[var_21_4.pos_y] or {}

		local var_21_6 = var_21_5[var_21_4.pos_y]

		table.insert(var_21_6, iter_21_3)
	end

	for iter_21_4, iter_21_5 in pairs(var_21_3) do
		for iter_21_6, iter_21_7 in pairs(iter_21_5) do
			local var_21_7 = {}

			seriesAsync({
				function(arg_23_0)
					local var_23_0 = 0

					for iter_23_0, iter_23_1 in pairs(iter_21_7) do
						if iter_23_1:ifNeedHide() and var_21_1:GetJustClearChapters(iter_23_1.id) and arg_21_0.chapterTFsById[iter_23_1.id] then
							var_23_0 = var_23_0 + 1

							local var_23_1 = arg_21_0.chapterTFsById[iter_23_1.id]

							setActive(var_23_1, true)
							arg_21_0:PlayChapterItemAnimationBackward(var_23_1, iter_23_1, function()
								var_23_0 = var_23_0 - 1

								setActive(var_23_1, false)
								var_21_1:RecordJustClearChapters(iter_23_1.id, nil)

								if var_23_0 <= 0 then
									arg_23_0()
								end
							end)

							var_21_7[iter_23_1.id] = true
						elseif arg_21_0.chapterTFsById[iter_23_1.id] then
							setActive(arg_21_0.chapterTFsById[iter_23_1.id], false)
						end
					end

					if var_23_0 <= 0 then
						arg_23_0()
					end
				end,
				function(arg_25_0)
					local var_25_0 = 0

					for iter_25_0, iter_25_1 in pairs(iter_21_7) do
						if not var_21_7[iter_25_1.id] then
							var_25_0 = var_25_0 + 1

							setActive(arg_21_0.chapterTFsById[iter_25_1.id], true)
							arg_21_0:PlayChapterItemAnimation(arg_21_0.chapterTFsById[iter_25_1.id], iter_25_1, function()
								var_25_0 = var_25_0 - 1

								if var_25_0 <= 0 then
									arg_25_0()
								end
							end)
						end
					end
				end
			})
		end
	end
end

function var_0_1.UpdateMapItem(arg_27_0, arg_27_1, arg_27_2)
	local var_27_0 = arg_27_2:getConfigTable()

	setAnchoredPosition(arg_27_1, {
		x = arg_27_0.mapWidth * var_27_0.pos_x,
		y = arg_27_0.mapHeight * var_27_0.pos_y
	})

	local var_27_1 = findTF(arg_27_1, "main")

	setActive(var_27_1, true)

	local var_27_2 = findTF(var_27_1, "info/bk/fordark")

	setActive(var_27_2, var_27_0.icon_outline == 1)

	local var_27_3 = findTF(var_27_1, "circle/clear_flag")
	local var_27_4 = findTF(var_27_1, "circle/lock")
	local var_27_5 = not arg_27_2.active and not arg_27_2:isUnlock()
	local var_27_6 = findTF(var_27_1, "circle/progress")
	local var_27_7 = findTF(var_27_1, "circle/progress_text")
	local var_27_8 = findTF(var_27_1, "circle/stars")
	local var_27_9 = string.split(var_27_0.name, "|")
	local var_27_10 = var_27_5 and "#737373" or "#FFFFFF"

	setText(findTF(var_27_1, "info/bk/title_form/title_index"), setColorStr(var_27_0.chapter_name .. "  ", var_27_10))
	setText(findTF(var_27_1, "info/bk/title_form/title"), setColorStr(var_27_9[1], var_27_10))
	setText(findTF(var_27_1, "info/bk/title_form/title_en"), setColorStr(var_27_9[2] or "", var_27_10))
	setFillAmount(var_27_6, arg_27_2.progress / 100)
	setText(var_27_7, string.format("%d%%", arg_27_2.progress))
	setActive(var_27_8, arg_27_2:existAchieve())

	if arg_27_2:existAchieve() then
		for iter_27_0, iter_27_1 in ipairs(arg_27_2.achieves) do
			local var_27_11 = ChapterConst.IsAchieved(iter_27_1)
			local var_27_12 = var_27_8:Find("star" .. iter_27_0 .. "/light")

			setActive(var_27_12, var_27_11)
		end
	end

	local var_27_13 = not arg_27_2.active and arg_27_2:isClear()

	setActive(var_27_3, var_27_13)
	setActive(var_27_4, var_27_5)
	setActive(var_27_7, not var_27_13 and not var_27_5)
	arg_27_0:DeleteTween("fighting" .. arg_27_2.id)

	local var_27_14 = findTF(var_27_1, "circle/fighting")

	setText(findTF(var_27_14, "Text"), i18n("tag_level_fighting"))

	local var_27_15 = findTF(var_27_1, "circle/oni")

	setText(findTF(var_27_15, "Text"), i18n("tag_level_oni"))

	local var_27_16 = findTF(var_27_1, "circle/narrative")

	setText(findTF(var_27_16, "Text"), i18n("tag_level_narrative"))
	setActive(var_27_14, false)
	setActive(var_27_15, false)
	setActive(var_27_16, false)

	local var_27_17
	local var_27_18

	if arg_27_2:getConfig("chapter_tag") == 1 then
		var_27_17 = var_27_16
	end

	if arg_27_2.active then
		var_27_17 = arg_27_2:existOni() and var_27_15 or var_27_14
	end

	if var_27_17 then
		setActive(var_27_17, true)

		local var_27_19 = GetOrAddComponent(var_27_17, "CanvasGroup")

		var_27_19.alpha = 1

		arg_27_0:RecordTween("fighting" .. arg_27_2.id, LeanTween.alphaCanvas(var_27_19, 0, 0.5):setFrom(1):setEase(LeanTweenType.easeInOutSine):setLoopPingPong().uniqueId)
	end

	local var_27_20 = findTF(var_27_1, "triesLimit")

	setActive(var_27_20, false)

	if arg_27_2:isTriesLimit() then
		local var_27_21 = arg_27_2:getConfig("count")
		local var_27_22 = var_27_21 - arg_27_2:getTodayDefeatCount() .. "/" .. var_27_21

		setText(var_27_20:Find("label"), i18n("levelScene_chapter_count_tip"))
		setText(var_27_20:Find("Text"), setColorStr(var_27_22, var_27_21 <= arg_27_2:getTodayDefeatCount() and COLOR_RED or COLOR_GREEN))
	end

	local var_27_23 = arg_27_2:GetDailyBonusQuota()
	local var_27_24 = findTF(var_27_1, "mark")

	setActive(var_27_24:Find("bonus"), var_27_23)
	setActive(var_27_24, var_27_23)

	if var_27_23 then
		local var_27_25 = var_27_24:GetComponent(typeof(CanvasGroup))
		local var_27_26 = arg_27_0.sceneParent.contextData.map:getConfig("type") == Map.ACTIVITY_HARD and "bonus_us_hard" or "bonus_us"

		arg_27_0.sceneParent.loader:GetSprite("ui/levelmainscene_atlas", var_27_26, var_27_24:Find("bonus"))
		LeanTween.cancel(go(var_27_24), true)

		local var_27_27 = var_27_24.anchoredPosition.y

		var_27_25.alpha = 0

		LeanTween.value(go(var_27_24), 0, 1, 0.2):setOnUpdate(System.Action_float(function(arg_28_0)
			var_27_25.alpha = arg_28_0

			local var_28_0 = var_27_24.anchoredPosition

			var_28_0.y = var_27_27 * arg_28_0
			var_27_24.anchoredPosition = var_28_0
		end)):setOnComplete(System.Action(function()
			var_27_25.alpha = 1

			local var_29_0 = var_27_24.anchoredPosition

			var_29_0.y = var_27_27
			var_27_24.anchoredPosition = var_29_0
		end)):setEase(LeanTweenType.easeOutSine):setDelay(0.7)
	end

	local var_27_28 = arg_27_2.id

	onButton(arg_27_0.sceneParent, var_27_1, function()
		if arg_27_0:InvokeParent("isfrozen") then
			return
		end

		if arg_27_0.chaptersInBackAnimating[var_27_28] then
			return
		end

		local var_30_0 = getProxy(ChapterProxy):getChapterById(var_27_28)

		if not var_30_0:isUnlock() then
			local var_30_1 = var_30_0:getPrevChapterName()

			pg.TipsMgr.GetInstance():ShowTips(i18n("levelScene_tracking_error_pre", var_30_1))

			return
		end

		if not getProxy(ChapterProxy):getMapById(var_30_0:getConfig("map")):isRemaster() and not var_30_0:inActTime() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("battle_levelScene_close"))

			return
		end

		local var_30_2 = var_30_0:getConfig("unlocklevel")

		if var_30_2 > arg_27_0.sceneParent.player.level then
			pg.TipsMgr.GetInstance():ShowTips(i18n("levelScene_chapter_level_limit", var_30_2))

			return
		end

		local var_30_3 = getProxy(ChapterProxy):getActiveChapter(true)

		if var_30_3 and var_30_3.id ~= var_27_28 then
			arg_27_0:InvokeParent("emit", LevelMediator2.ON_STRATEGYING_CHAPTER)

			return
		end

		if var_30_0.active then
			arg_27_0:InvokeParent("switchToChapter", var_30_0)
		else
			local var_30_4 = arg_27_1.localPosition

			arg_27_0:InvokeParent("displayChapterPanel", var_30_0, Vector3(var_30_4.x - 10, var_30_4.y + 150))
		end
	end, SFX_UI_WEIGHANCHOR_SELECT)
end

function var_0_1.PlayChapterItemAnimation(arg_31_0, arg_31_1, arg_31_2, arg_31_3)
	local var_31_0 = findTF(arg_31_1, "main")
	local var_31_1 = var_31_0:Find("info")
	local var_31_2 = findTF(var_31_0, "circle")
	local var_31_3 = findTF(var_31_0, "info/bk")

	LeanTween.cancel(go(var_31_2))

	var_31_2.localScale = Vector3.zero

	local var_31_4 = LeanTween.scale(var_31_2, Vector3.one, 0.3):setDelay(0.3)

	arg_31_0:RecordTween(var_31_4.uniqueId)
	LeanTween.cancel(go(var_31_3))
	setAnchoredPosition(var_31_3, {
		x = -1 * var_31_1.rect.width
	})
	shiftPanel(var_31_3, 0, nil, 0.4, 0.4, true, true, nil, function()
		if arg_31_2:isTriesLimit() then
			setActive(findTF(var_31_0, "triesLimit"), true)
		end

		if arg_31_3 then
			arg_31_3()
		end
	end)
end

function var_0_1.PlayChapterItemAnimationBackward(arg_33_0, arg_33_1, arg_33_2, arg_33_3)
	local var_33_0 = findTF(arg_33_1, "main")
	local var_33_1 = var_33_0:Find("info")
	local var_33_2 = findTF(var_33_0, "circle")
	local var_33_3 = findTF(var_33_0, "info/bk")

	LeanTween.cancel(go(var_33_2))

	var_33_2.localScale = Vector3.one

	local var_33_4 = LeanTween.scale(go(var_33_2), Vector3.zero, 0.3):setDelay(0.3)

	arg_33_0:RecordTween(var_33_4.uniqueId)

	arg_33_0.chaptersInBackAnimating[arg_33_2.id] = true

	LeanTween.cancel(go(var_33_3))
	setAnchoredPosition(var_33_3, {
		x = 0
	})
	shiftPanel(var_33_3, -1 * var_33_1.rect.width, nil, 0.4, 0.4, true, true, nil, function()
		arg_33_0.chaptersInBackAnimating[arg_33_2.id] = nil

		if arg_33_3 then
			arg_33_3()
		end
	end)

	if arg_33_2:isTriesLimit() then
		setActive(findTF(var_33_0, "triesLimit"), false)
	end
end

function var_0_1.UpdateChapterTF(arg_35_0, arg_35_1)
	local var_35_0 = arg_35_0.chapterTFsById[arg_35_1]

	if var_35_0 then
		local var_35_1 = getProxy(ChapterProxy):getChapterById(arg_35_1)

		arg_35_0:UpdateMapItem(var_35_0, var_35_1)
		arg_35_0:PlayChapterItemAnimation(var_35_0, var_35_1)
	end
end

function var_0_1.AddChapterTF(arg_36_0, arg_36_1)
	local var_36_0 = arg_36_0.data

	if arg_36_0.chapterTFsById[arg_36_1] then
		arg_36_0:UpdateChapterTF(arg_36_1)
	elseif _.contains(var_36_0:GetChapterList(), function(arg_37_0)
		if arg_37_0 ~= arg_36_1 then
			return false
		end

		local var_37_0 = getProxy(ChapterProxy):getChapterById(arg_36_1, true)

		return (var_37_0:isUnlock() or var_37_0:activeAlways()) and not var_37_0:ifNeedHide()
	end) then
		local var_36_1 = getProxy(ChapterProxy):getChapterById(arg_36_1, true)
		local var_36_2 = cloneTplTo(arg_36_0.tpl, arg_36_0.itemHolder, "Chapter_" .. var_36_1.id)

		arg_36_0:UpdateMapItem(var_36_2, var_36_1)

		arg_36_0.chapterTFsById[var_36_1.id] = var_36_2

		arg_36_0:PlayChapterItemAnimation(var_36_2)
	end
end

function var_0_1.TryOpenChapter(arg_38_0, arg_38_1)
	local var_38_0 = arg_38_0.chapterTFsById[arg_38_1]

	if var_38_0 then
		local var_38_1 = var_38_0:Find("main")

		triggerButton(var_38_1)
	end
end

return var_0_1

local var_0_0 = class("GuidePlayer")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tf = arg_1_1
	arg_1_0.bgCg = arg_1_1:Find("BG"):GetComponent(typeof(CanvasGroup))
	arg_1_0.windowContainer = arg_1_1:Find("windows")
	arg_1_0.charContainer = arg_1_1:Find("char")
	arg_1_0.dialogueWindows = pg.NewGuideMgr.GetInstance().dialogueWindows
	arg_1_0.counsellors = pg.NewGuideMgr.GetInstance().counsellors
	arg_1_0.uiFinder = pg.NewGuideMgr.GetInstance().uiFinder
	arg_1_0.uiDuplicator = pg.NewGuideMgr.GetInstance().uiDuplicator
	arg_1_0.uiLoader = pg.NewGuideMgr.GetInstance().uiLoader
	arg_1_0.root = arg_1_1:Find("target")
end

function var_0_0.Execute(arg_2_0, arg_2_1, arg_2_2)
	seriesAsync({
		function(arg_3_0)
			arg_2_0:HideDialogueWindows()
			arg_2_0:UpdateStyle(arg_2_1)
			arg_2_0:DoDelay(arg_2_1, arg_3_0)
		end,
		function(arg_4_0)
			arg_2_0:WaitUntilSceneEnter(arg_2_1, arg_4_0)
		end,
		function(arg_5_0)
			arg_2_0:CheckBaseUI(arg_2_1, arg_5_0)
		end,
		function(arg_6_0)
			arg_2_0:CheckSprite(arg_2_1, arg_6_0)
		end,
		function(arg_7_0)
			arg_2_0:ShowDialogueWindow(arg_2_1, arg_7_0)
		end,
		function(arg_8_0)
			arg_2_0:UpdateHighLight(arg_2_1, arg_8_0)
		end,
		function(arg_9_0)
			arg_2_0:OnExecution(arg_2_1, arg_9_0)
		end,
		function(arg_10_0)
			arg_2_0:RegisterEvent(arg_2_1, arg_10_0)
		end,
		function(arg_11_0)
			arg_2_0:Clear()
			arg_11_0()
		end
	}, arg_2_2)
end

function var_0_0.CheckBaseUI(arg_12_0, arg_12_1, arg_12_2)
	if not arg_12_1:ShouldCheckBaseUI() then
		arg_12_2()

		return
	end

	arg_12_0:SearchUI(arg_12_1:GetBaseUI(), function(arg_13_0)
		if not arg_13_0 then
			pg.NewGuideMgr.GetInstance():Stop()

			return
		end

		arg_12_2()
	end)
end

local function var_0_1(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0:GetComponent(typeof(Image))

	return not (IsNil(var_14_0.sprite) or arg_14_1 and var_14_0.sprite.name == arg_14_1)
end

function var_0_0.CheckSprite(arg_15_0, arg_15_1, arg_15_2)
	if not arg_15_1:ShouldCheckSpriteUI() then
		arg_15_2()

		return
	end

	local var_15_0 = arg_15_1:GetSpriteUI()

	arg_15_0:SearchUI(var_15_0, function(arg_16_0)
		if not arg_16_0 then
			pg.NewGuideMgr.GetInstance():Stop()

			return
		end

		local var_16_0 = var_15_0.childPath and arg_16_0:Find(var_15_0.childPath) or arg_16_0

		arg_15_0:ClearSpriteTimer()

		local var_16_1 = 0
		local var_16_2 = 10

		arg_15_0.spriteTimer = Timer.New(function()
			var_16_1 = var_16_1 + 1

			if var_16_1 == var_16_2 then
				arg_15_0:ClearSpriteTimer()

				return
			end

			if var_0_1(var_16_0, var_15_0.defaultName) then
				arg_15_0:ClearSpriteTimer()
				arg_15_2()
			end
		end, 0.5, -1)

		arg_15_0.spriteTimer:Start()
	end)
end

function var_0_0.ClearSpriteTimer(arg_18_0)
	if arg_18_0.spriteTimer then
		arg_18_0.spriteTimer:Stop()

		arg_18_0.spriteTimer = nil
	end
end

function var_0_0.UpdateStyle(arg_19_0, arg_19_1)
	arg_19_0.bgCg.alpha = arg_19_1:GetAlpha()
end

function var_0_0.DoDelay(arg_20_0, arg_20_1, arg_20_2)
	local var_20_0 = arg_20_1:GetDelay()

	if var_20_0 <= 0 then
		arg_20_2()

		return
	end

	arg_20_0.delayTimer = Timer.New(arg_20_2, var_20_0, 1)

	arg_20_0.delayTimer:Start()
end

function var_0_0.OnSceneEnter(arg_21_0)
	if arg_21_0.waitSceneData and pg.NewGuideMgr.GetInstance():ExistScene(arg_21_0.waitSceneData.sceneName) then
		arg_21_0:ClearWaitUntilSceneTimer()
		arg_21_0.waitSceneData.callback()

		arg_21_0.waitSceneData = nil
	end
end

function var_0_0.WaitUntilSceneEnter(arg_22_0, arg_22_1, arg_22_2)
	if not arg_22_1:ShouldWaitScene() then
		arg_22_2()

		return
	end

	arg_22_0:ClearWaitUntilSceneTimer()

	local var_22_0 = arg_22_1:GetWaitScene()

	if pg.NewGuideMgr.GetInstance():ExistScene(var_22_0) then
		arg_22_2()
	else
		arg_22_0.waitSceneData = {
			sceneName = var_22_0,
			callback = arg_22_2
		}

		arg_22_0:AddWaitUntilSceneTimer()
	end
end

function var_0_0.AddWaitUntilSceneTimer(arg_23_0)
	arg_23_0.waitUntilSceneTimer = Timer.New(function()
		arg_23_0:ClearWaitUntilSceneTimer()
		pg.NewGuideMgr.GetInstance():Stop()
	end, 10, 1)

	arg_23_0.waitUntilSceneTimer:Start()
end

function var_0_0.ClearWaitUntilSceneTimer(arg_25_0)
	if arg_25_0.waitUntilSceneTimer then
		arg_25_0.waitUntilSceneTimer:Stop()

		arg_25_0.waitUntilSceneTimer = nil
	end
end

function var_0_0.ShowDialogueWindow(arg_26_0, arg_26_1, arg_26_2)
	if not arg_26_1:ShouldShowDialogue() then
		arg_26_0:HideDialogueWindows()
		arg_26_2()

		return
	end

	local var_26_0 = {}
	local var_26_1 = arg_26_1:GetDialogueType()

	if not arg_26_0.dialogueWindows[var_26_1] then
		table.insert(var_26_0, function(arg_27_0)
			arg_26_0:LoadDialogueWindow(var_26_1, arg_27_0)
		end)
	end

	table.insert(var_26_0, function(arg_28_0)
		local var_28_0 = arg_26_0.dialogueWindows[var_26_1]

		arg_26_0:UpdateDialogue(arg_26_1, var_28_0, arg_28_0)
	end)
	seriesAsync(var_26_0, arg_26_2)
end

function var_0_0.UpdateDialogue(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	arg_29_0:ActiveDialogueWindow(arg_29_2)

	local var_29_0 = arg_29_1:GetStyleData()

	setText(arg_29_2:Find("content"), var_29_0.text)

	arg_29_2.localScale = var_29_0.scale
	arg_29_2.localPosition = var_29_0.position
	arg_29_2:Find("content").localScale = var_29_0.scale

	local var_29_1 = arg_29_2:Find("hand")

	if not IsNil(var_29_1) then
		var_29_1.localPosition = var_29_0.handPosition
		var_29_1.eulerAngles = var_29_0.handAngle
	end

	local var_29_2 = var_29_0.counsellor

	seriesAsync({
		function(arg_30_0)
			arg_29_0:LoadCounsellor(var_29_2.name, arg_30_0)
		end,
		function(arg_31_0)
			local var_31_0 = arg_29_0.counsellors[var_29_2.name]

			setActive(var_31_0, true)

			var_31_0.localPosition = arg_29_2.localPosition + Vector3(var_29_2.position.x, var_29_2.position.y, 0)
			var_31_0.localScale = Vector3(var_29_2.scale.x, var_29_2.scale.y, 1)

			arg_31_0()
		end
	}, arg_29_3)
end

function var_0_0.LoadCounsellor(arg_32_0, arg_32_1, arg_32_2)
	if not arg_32_0.counsellors[arg_32_1] then
		ResourceMgr.Inst:getAssetAsync("guideitem/" .. arg_32_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_33_0)
			if IsNil(arg_33_0) then
				return
			end

			local var_33_0 = Object.Instantiate(arg_33_0, arg_32_0.charContainer)

			arg_32_0.counsellors[arg_32_1] = var_33_0.transform

			arg_32_2()
		end), true, true)
	else
		arg_32_2()
	end
end

function var_0_0.LoadDialogueWindow(arg_34_0, arg_34_1, arg_34_2)
	ResourceMgr.Inst:getAssetAsync("guideitem/window_" .. arg_34_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_35_0)
		if IsNil(arg_35_0) then
			return
		end

		local var_35_0 = Object.Instantiate(arg_35_0, arg_34_0.windowContainer)

		arg_34_0.dialogueWindows[arg_34_1] = var_35_0.transform

		if arg_34_2 then
			arg_34_2()
		end
	end), true, true)
end

function var_0_0.ActiveDialogueWindow(arg_36_0, arg_36_1)
	for iter_36_0, iter_36_1 in pairs(arg_36_0.dialogueWindows) do
		setActive(iter_36_1, iter_36_1 == arg_36_1)
	end
end

function var_0_0.HideDialogueWindows(arg_37_0)
	for iter_37_0, iter_37_1 in pairs(arg_37_0.dialogueWindows) do
		setActive(iter_37_1, false)
	end
end

local function var_0_2(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
	if arg_38_3.type == GuideStep.HIGH_TYPE_GAMEOBJECT then
		arg_38_0.uiDuplicator:Duplicate(arg_38_2, {
			clearAllEvent = true
		})
	elseif arg_38_3.type == GuideStep.HIGH_TYPE_LINE then
		local var_38_0 = arg_38_1.isWorld and 15 or 55
		local var_38_1 = arg_38_0._tf:InverseTransformPoint(arg_38_2.position)
		local var_38_2 = (arg_38_2.pivot.x - 0.5) * var_38_0
		local var_38_3 = (arg_38_2.pivot.y - 0.5) * var_38_0
		local var_38_4 = Vector2(arg_38_2.sizeDelta.x + var_38_0, arg_38_2.sizeDelta.y + var_38_0)

		arg_38_0.uiLoader:LoadHighLightArea({
			position = Vector3(var_38_1.x, var_38_1.y, 0) + Vector3(var_38_2, var_38_3, 0),
			sizeDelta = var_38_4,
			pivot = arg_38_2.pivot,
			isWorld = arg_38_1.isWorld
		})
	end
end

function var_0_0.UpdateHighLight(arg_39_0, arg_39_1, arg_39_2)
	local var_39_0 = arg_39_1:GetHighLightTarget()

	if #var_39_0 <= 0 then
		arg_39_2()

		return
	end

	local var_39_1 = {}

	for iter_39_0, iter_39_1 in ipairs(var_39_0) do
		table.insert(var_39_1, function(arg_40_0)
			arg_39_0:SearchUI(iter_39_1, function(arg_41_0)
				if not arg_41_0 then
					pg.NewGuideMgr.GetInstance():Stop()

					return
				end

				var_0_2(arg_39_0, arg_39_1, arg_41_0, iter_39_1)
				arg_40_0()
			end)
		end)
	end

	parallelAsync(var_39_1, arg_39_2)
end

function var_0_0.SearchUI(arg_42_0, arg_42_1, arg_42_2)
	arg_42_0.uiFinder:Search({
		path = arg_42_1.path,
		delay = arg_42_1.delay,
		childIndex = arg_42_1.pathIndex,
		conditionData = arg_42_1.conditionData,
		callback = arg_42_2
	})
end

function var_0_0.SearchWithoutDelay(arg_43_0, arg_43_1, arg_43_2)
	arg_43_0.uiFinder:SearchWithoutDelay({
		path = arg_43_1.path,
		delay = arg_43_1.delay,
		childIndex = arg_43_1.pathIndex,
		conditionData = arg_43_1.conditionData,
		callback = arg_43_2
	})
end

function var_0_0.RegisterEvent(arg_44_0, arg_44_1, arg_44_2)
	if arg_44_1:ExistTrigger() then
		removeOnButton(arg_44_0._tf)
		arg_44_2()

		return
	end

	onButton(pg.NewGuideMgr.GetInstance(), arg_44_0._tf, function()
		if arg_44_1:ShouldGoScene() then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE[arg_44_1.sceneName])
			arg_44_2()
		elseif arg_44_1:ShouldTriggerOtherTarget() then
			arg_44_0:SearchUI(arg_44_1:GetOtherTriggerTarget(), function(arg_46_0)
				triggerButton(arg_46_0)
				arg_44_2()
			end)
		else
			arg_44_2()
		end
	end, SFX_PANEL)
end

function var_0_0.NextOne(arg_47_0)
	triggerButton(arg_47_0._tf)
end

function var_0_0.HideCounsellors(arg_48_0)
	for iter_48_0, iter_48_1 in pairs(arg_48_0.counsellors) do
		setActive(iter_48_1, false)
	end
end

function var_0_0.Clear(arg_49_0)
	arg_49_0:HideCounsellors()
	arg_49_0:HideDialogueWindows()
	arg_49_0:ClearSpriteTimer()
	removeOnButton(arg_49_0._tf)
	arg_49_0:OnClear()

	if arg_49_0.delayTimer then
		arg_49_0.delayTimer:Stop()

		arg_49_0.delayTimer = nil
	end

	arg_49_0.uiFinder:Clear()
	arg_49_0.uiDuplicator:Clear()
	arg_49_0.uiLoader:Clear()
end

function var_0_0.OnExecution(arg_50_0, arg_50_1, arg_50_2)
	arg_50_2()
end

function var_0_0.OnClear(arg_51_0)
	return
end

return var_0_0

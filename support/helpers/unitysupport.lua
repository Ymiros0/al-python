function tf(arg_1_0)
	return arg_1_0.transform
end

function go(arg_2_0)
	return tf(arg_2_0).gameObject
end

function rtf(arg_3_0)
	return arg_3_0.transform
end

function findGO(arg_4_0, arg_4_1)
	assert(arg_4_0, "object or transform should exist")

	local var_4_0 = tf(arg_4_0):Find(arg_4_1)

	return var_4_0 and var_4_0.gameObject
end

function findTF(arg_5_0, arg_5_1)
	assert(arg_5_0, "object or transform should exist " .. arg_5_1)

	return (tf(arg_5_0):Find(arg_5_1))
end

function Instantiate(arg_6_0)
	return Object.Instantiate(go(arg_6_0))
end

instantiate = Instantiate

function Destroy(arg_7_0)
	Object.Destroy(go(arg_7_0))
end

destroy = Destroy

function SetActive(arg_8_0, arg_8_1)
	LuaHelper.SetActiveForLua(arg_8_0, tobool(arg_8_1))
end

setActive = SetActive

function isActive(arg_9_0)
	return go(arg_9_0).activeSelf
end

function SetName(arg_10_0, arg_10_1)
	arg_10_0.name = arg_10_1
end

setName = SetName

function SetParent(arg_11_0, arg_11_1, arg_11_2)
	LuaHelper.SetParentForLua(arg_11_0, arg_11_1, tobool(arg_11_2))
end

setParent = SetParent

function setText(arg_12_0, arg_12_1)
	if not arg_12_1 then
		return
	end

	arg_12_0:GetComponent(typeof(Text)).text = tostring(arg_12_1)
end

function setTextEN(arg_13_0, arg_13_1)
	if not arg_13_1 then
		return
	end

	arg_13_1 = splitByWordEN(arg_13_1, arg_13_0)
	arg_13_0:GetComponent(typeof(Text)).text = tostring(arg_13_1)
end

function setBestFitTextEN(arg_14_0, arg_14_1, arg_14_2)
	if not arg_14_1 then
		return
	end

	local var_14_0 = arg_14_0:GetComponent(typeof(RectTransform))
	local var_14_1 = arg_14_0:GetComponent(typeof(Text))
	local var_14_2 = arg_14_2 or 20
	local var_14_3 = var_14_0.rect.width
	local var_14_4 = var_14_0.rect.height

	while var_14_2 > 0 do
		var_14_1.fontSize = var_14_2

		local var_14_5 = splitByWordEN(arg_14_1, arg_14_0)

		var_14_1.text = tostring(var_14_5)

		if var_14_3 >= var_14_1.preferredWidth and var_14_4 >= var_14_1.preferredHeight then
			break
		end

		var_14_2 = var_14_2 - 1
	end
end

function setTextFont(arg_15_0, arg_15_1)
	if not arg_15_1 then
		return
	end

	arg_15_0:GetComponent(typeof(Text)).font = arg_15_1
end

function getText(arg_16_0)
	return arg_16_0:GetComponent(typeof(Text)).text
end

function setInputText(arg_17_0, arg_17_1)
	if not arg_17_1 then
		return
	end

	arg_17_0:GetComponent(typeof(InputField)).text = arg_17_1
end

function getInputText(arg_18_0)
	return arg_18_0:GetComponent(typeof(InputField)).text
end

function onInputEndEdit(arg_19_0, arg_19_1, arg_19_2)
	local var_19_0 = arg_19_1:GetComponent(typeof(InputField)).onEndEdit

	pg.DelegateInfo.Add(arg_19_0, var_19_0)
	var_19_0:RemoveAllListeners()
	var_19_0:AddListener(arg_19_2)
end

function activateInputField(arg_20_0)
	arg_20_0:GetComponent(typeof(InputField)):ActivateInputField()
end

function setButtonText(arg_21_0, arg_21_1, arg_21_2)
	setWidgetText(arg_21_0, arg_21_1, arg_21_2)
end

function setWidgetText(arg_22_0, arg_22_1, arg_22_2)
	arg_22_2 = arg_22_2 or "Text"
	arg_22_2 = findTF(arg_22_0, arg_22_2)

	setText(arg_22_2, arg_22_1)
end

function setWidgetTextEN(arg_23_0, arg_23_1, arg_23_2)
	arg_23_2 = arg_23_2 or "Text"
	arg_23_2 = findTF(arg_23_0, arg_23_2)

	setTextEN(arg_23_2, arg_23_1)
end

local var_0_0
local var_0_1 = true
local var_0_2 = -1

function onButton(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4)
	local var_24_0 = GetOrAddComponent(arg_24_1, typeof(Button))

	assert(var_24_0, "could not found Button component on " .. arg_24_1.name)
	assert(arg_24_2, "callback should exist")

	local var_24_1 = var_24_0.onClick

	pg.DelegateInfo.Add(arg_24_0, var_24_1)
	var_24_1:RemoveAllListeners()
	var_24_1:AddListener(function()
		if var_0_2 == Time.frameCount and Input.touchCount > 1 then
			return
		end

		var_0_2 = Time.frameCount

		if arg_24_3 and var_0_1 then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_24_3)
		end

		arg_24_2()
	end)
end

function removeOnButton(arg_26_0)
	local var_26_0 = arg_26_0:GetComponent(typeof(Button))

	if var_26_0 ~= nil then
		var_26_0.onClick:RemoveAllListeners()
	end
end

function removeAllOnButton(arg_27_0)
	local var_27_0 = arg_27_0:GetComponentsInChildren(typeof(Button))

	for iter_27_0 = 1, var_27_0.Length do
		local var_27_1 = var_27_0[iter_27_0 - 1]

		if var_27_1 ~= nil then
			var_27_1.onClick:RemoveAllListeners()
		end
	end
end

function ClearAllText(arg_28_0)
	local var_28_0 = arg_28_0:GetComponentsInChildren(typeof(Text))

	for iter_28_0 = 1, var_28_0.Length do
		local var_28_1 = var_28_0[iter_28_0 - 1]

		if var_28_1 ~= nil then
			var_28_1.text = ""
		end
	end
end

function onLongPressTrigger(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	local var_29_0 = GetOrAddComponent(arg_29_1, typeof(UILongPressTrigger))

	assert(var_29_0, "could not found UILongPressTrigger component on " .. arg_29_1.name)
	assert(arg_29_2, "callback should exist")

	local var_29_1 = var_29_0.onLongPressed

	pg.DelegateInfo.Add(arg_29_0, var_29_1)
	var_29_1:RemoveAllListeners()
	var_29_1:AddListener(function()
		if arg_29_3 then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_29_3)
		end

		arg_29_2()
	end)
end

function removeOnLongPressTrigger(arg_31_0)
	local var_31_0 = arg_31_0:GetComponent(typeof(UILongPressTrigger))

	if var_31_0 ~= nil then
		var_31_0.onLongPressed:RemoveAllListeners()
	end
end

function setButtonEnabled(arg_32_0, arg_32_1)
	GetComponent(arg_32_0, typeof(Button)).interactable = arg_32_1
end

function setToggleEnabled(arg_33_0, arg_33_1)
	GetComponent(arg_33_0, typeof(Toggle)).interactable = arg_33_1
end

function setSliderEnable(arg_34_0, arg_34_1)
	GetComponent(arg_34_0, typeof(Slider)).interactable = arg_34_1
end

function triggerButton(arg_35_0)
	local var_35_0 = GetComponent(arg_35_0, typeof(Button))

	var_0_1 = false
	var_0_2 = -1

	var_35_0.onClick:Invoke()

	var_0_1 = true
end

local var_0_3 = true

function onToggle(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4)
	local var_36_0 = GetComponent(arg_36_1, typeof(Toggle))

	assert(arg_36_2, "callback should exist")

	local var_36_1 = var_36_0.onValueChanged

	var_36_1:RemoveAllListeners()
	pg.DelegateInfo.Add(arg_36_0, var_36_1)
	var_36_1:AddListener(function(arg_37_0)
		if var_0_3 then
			if arg_37_0 and arg_36_3 and var_36_0.isOn == arg_37_0 then
				arg_36_3 = SFX_UI_TAG

				pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_36_3)
			elseif not arg_37_0 and arg_36_4 then
				pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_36_4)
			end
		end

		arg_36_2(arg_37_0)
	end)

	local var_36_2 = GetComponent(arg_36_1, typeof(UIToggleEvent))

	if not IsNil(var_36_2) then
		var_36_2:Rebind()
	end
end

function removeOnToggle(arg_38_0)
	local var_38_0 = GetComponent(arg_38_0, typeof(Toggle))

	if var_38_0 ~= nil then
		var_38_0.onValueChanged:RemoveAllListeners()
	end
end

function triggerToggle(arg_39_0, arg_39_1)
	local var_39_0 = GetComponent(arg_39_0, typeof(Toggle))

	var_0_3 = false
	arg_39_1 = tobool(arg_39_1)

	if var_39_0.isOn ~= arg_39_1 then
		var_39_0.isOn = arg_39_1
	else
		var_39_0.onValueChanged:Invoke(arg_39_1)
	end

	var_0_3 = true
end

function triggerToggleWithoutNotify(arg_40_0, arg_40_1)
	local var_40_0 = GetComponent(arg_40_0, typeof(Toggle))

	var_0_3 = false
	arg_40_1 = tobool(arg_40_1)

	LuaHelper.ChangeToggleValueWithoutNotify(var_40_0, arg_40_1)

	var_0_3 = true
end

function onSlider(arg_41_0, arg_41_1, arg_41_2)
	local var_41_0 = GetComponent(arg_41_1, typeof(Slider)).onValueChanged

	assert(arg_41_2, "callback should exist")
	var_41_0:RemoveAllListeners()
	pg.DelegateInfo.Add(arg_41_0, var_41_0)
	var_41_0:AddListener(arg_41_2)
end

function setSlider(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	local var_42_0 = GetComponent(arg_42_0, typeof(Slider))

	assert(var_42_0, "slider should exist")

	var_42_0.minValue = arg_42_1
	var_42_0.maxValue = arg_42_2
	var_42_0.value = arg_42_3
end

function eachChild(arg_43_0, arg_43_1)
	local var_43_0 = tf(arg_43_0)

	for iter_43_0 = var_43_0.childCount - 1, 0, -1 do
		arg_43_1(var_43_0:GetChild(iter_43_0))
	end
end

function removeAllChildren(arg_44_0)
	eachChild(arg_44_0, function(arg_45_0)
		tf(arg_45_0).transform:SetParent(nil, false)
		Destroy(arg_45_0)
	end)
end

function scrollTo(arg_46_0, arg_46_1, arg_46_2)
	Canvas.ForceUpdateCanvases()

	local var_46_0 = GetComponent(arg_46_0, typeof(ScrollRect))
	local var_46_1 = Vector2(arg_46_1 or var_46_0.normalizedPosition.x, arg_46_2 or var_46_0.normalizedPosition.y)

	onNextTick(function()
		if not IsNil(arg_46_0) then
			var_46_0.normalizedPosition = var_46_1

			var_46_0.onValueChanged:Invoke(var_46_1)
		end
	end)
end

function scrollToBottom(arg_48_0)
	scrollTo(arg_48_0, 0, 0)
end

function onScroll(arg_49_0, arg_49_1, arg_49_2)
	local var_49_0 = GetComponent(arg_49_1, typeof(ScrollRect)).onValueChanged

	assert(arg_49_2, "callback should exist")
	var_49_0:RemoveAllListeners()
	pg.DelegateInfo.Add(arg_49_0, var_49_0)
	var_49_0:AddListener(arg_49_2)
end

function ClearEventTrigger(arg_50_0)
	arg_50_0:RemovePointClickFunc()
	arg_50_0:RemovePointDownFunc()
	arg_50_0:RemovePointEnterFunc()
	arg_50_0:RemovePointExitFunc()
	arg_50_0:RemovePointUpFunc()
	arg_50_0:RemoveCheckDragFunc()
	arg_50_0:RemoveBeginDragFunc()
	arg_50_0:RemoveDragFunc()
	arg_50_0:RemoveDragEndFunc()
	arg_50_0:RemoveDropFunc()
	arg_50_0:RemoveScrollFunc()
	arg_50_0:RemoveSelectFunc()
	arg_50_0:RemoveUpdateSelectFunc()
	arg_50_0:RemoveMoveFunc()
end

function ClearLScrollrect(arg_51_0)
	arg_51_0.onStart = nil
	arg_51_0.onInitItem = nil
	arg_51_0.onUpdateItem = nil
	arg_51_0.onReturnItem = nil
end

function GetComponent(arg_52_0, arg_52_1)
	return (arg_52_0:GetComponent(arg_52_1))
end

function GetOrAddComponent(arg_53_0, arg_53_1)
	assert(arg_53_0, "objectOrTransform not found: " .. debug.traceback())

	local var_53_0 = arg_53_1

	if type(arg_53_1) == "string" then
		assert(_G[arg_53_1], arg_53_1 .. " not exist in Global")

		var_53_0 = typeof(_G[arg_53_1])
	end

	return LuaHelper.GetOrAddComponentForLua(arg_53_0, var_53_0)
end

function RemoveComponent(arg_54_0, arg_54_1)
	local var_54_0 = arg_54_0:GetComponent(arg_54_1)

	if var_54_0 then
		Object.Destroy(var_54_0)
	end
end

function SetCompomentEnabled(arg_55_0, arg_55_1, arg_55_2)
	local var_55_0 = arg_55_0:GetComponent(arg_55_1)

	assert(var_55_0, "compoment not found")

	var_55_0.enabled = tobool(arg_55_2)
end

function GetInChildren(arg_56_0, arg_56_1)
	local function var_56_0(arg_57_0, arg_57_1)
		if not arg_57_0 then
			return nil
		end

		if arg_57_0.name == arg_57_1 then
			return arg_57_0
		end

		for iter_57_0 = 0, arg_57_0.childCount - 1 do
			local var_57_0 = arg_57_0:GetChild(iter_57_0)

			if arg_57_1 == var_57_0.name then
				return var_57_0
			end

			local var_57_1 = var_56_0(var_57_0, arg_57_1)

			if var_57_1 then
				return var_57_1
			end
		end

		return nil
	end

	return var_56_0(arg_56_0, arg_56_1)
end

function onNextTick(arg_58_0)
	FrameTimer.New(arg_58_0, 1, 1):Start()
end

function onDelayTick(arg_59_0, arg_59_1)
	Timer.New(arg_59_0, arg_59_1, 1):Start()
end

function seriesAsync(arg_60_0, arg_60_1, ...)
	local var_60_0 = 0
	local var_60_1 = #arg_60_0
	local var_60_2

	local function var_60_3(...)
		var_60_0 = var_60_0 + 1

		if var_60_0 <= var_60_1 then
			arg_60_0[var_60_0](var_60_3, ...)
		elseif var_60_0 == var_60_1 + 1 and arg_60_1 then
			arg_60_1(...)
		end
	end

	var_60_3(...)
end

function seriesAsyncExtend(arg_62_0, arg_62_1, ...)
	local var_62_0

	local function var_62_1(...)
		if #arg_62_0 > 0 then
			table.remove(arg_62_0, 1)(var_62_1, ...)
		elseif arg_62_1 then
			arg_62_1(...)
		end
	end

	var_62_1(...)
end

function parallelAsync(arg_64_0, arg_64_1)
	local var_64_0 = #arg_64_0

	local function var_64_1()
		var_64_0 = var_64_0 - 1

		if var_64_0 == 0 and arg_64_1 then
			arg_64_1()
		end
	end

	if var_64_0 > 0 then
		for iter_64_0, iter_64_1 in ipairs(arg_64_0) do
			iter_64_1(var_64_1)
		end
	elseif arg_64_1 then
		arg_64_1()
	end
end

function limitedParallelAsync(arg_66_0, arg_66_1, arg_66_2)
	local var_66_0 = #arg_66_0
	local var_66_1 = var_66_0

	if var_66_1 == 0 then
		arg_66_2()

		return
	end

	local var_66_2 = math.min(arg_66_1, var_66_0)
	local var_66_3

	local function var_66_4()
		var_66_1 = var_66_1 - 1

		if var_66_1 == 0 then
			arg_66_2()
		elseif var_66_2 + 1 <= var_66_0 then
			var_66_2 = var_66_2 + 1

			arg_66_0[var_66_2](var_66_4)
		end
	end

	for iter_66_0 = 1, var_66_2 do
		arg_66_0[iter_66_0](var_66_4)
	end
end

function waitUntil(arg_68_0, arg_68_1)
	local var_68_0

	var_68_0 = FrameTimer.New(function()
		if arg_68_0() then
			arg_68_1()
			var_68_0:Stop()

			return
		end
	end, 1, -1)

	var_68_0:Start()

	return var_68_0
end

function setImageSprite(arg_70_0, arg_70_1, arg_70_2)
	if IsNil(arg_70_0) then
		assert(false)

		return
	end

	local var_70_0 = GetComponent(arg_70_0, typeof(Image))

	if IsNil(var_70_0) then
		return
	end

	var_70_0.sprite = arg_70_1

	if arg_70_2 then
		var_70_0:SetNativeSize()
	end
end

function clearImageSprite(arg_71_0)
	GetComponent(arg_71_0, typeof(Image)).sprite = nil
end

function getImageSprite(arg_72_0)
	local var_72_0 = GetComponent(arg_72_0, typeof(Image))

	return var_72_0 and var_72_0.sprite
end

function tex2sprite(arg_73_0)
	return UnityEngine.Sprite.Create(arg_73_0, UnityEngine.Rect.New(0, 0, arg_73_0.width, arg_73_0.height), Vector2(0.5, 0.5), 100)
end

function setFillAmount(arg_74_0, arg_74_1)
	GetComponent(arg_74_0, typeof(Image)).fillAmount = arg_74_1
end

function string2vector3(arg_75_0)
	local var_75_0 = string.split(arg_75_0, ",")

	return Vector3(var_75_0[1], var_75_0[2], var_75_0[3])
end

function getToggleState(arg_76_0)
	return arg_76_0:GetComponent(typeof(Toggle)).isOn
end

function setLocalPosition(arg_77_0, arg_77_1)
	local var_77_0 = tf(arg_77_0).localPosition

	arg_77_1.x = arg_77_1.x or var_77_0.x
	arg_77_1.y = arg_77_1.y or var_77_0.y
	arg_77_1.z = arg_77_1.z or var_77_0.z
	tf(arg_77_0).localPosition = arg_77_1
end

function setAnchoredPosition(arg_78_0, arg_78_1)
	local var_78_0 = rtf(arg_78_0)
	local var_78_1 = var_78_0.anchoredPosition

	arg_78_1.x = arg_78_1.x or var_78_1.x
	arg_78_1.y = arg_78_1.y or var_78_1.y
	var_78_0.anchoredPosition = arg_78_1
end

function setAnchoredPosition3D(arg_79_0, arg_79_1)
	local var_79_0 = rtf(arg_79_0)
	local var_79_1 = var_79_0.anchoredPosition3D

	arg_79_1.x = arg_79_1.x or var_79_1.x
	arg_79_1.y = arg_79_1.y or var_79_1.y
	arg_79_1.z = arg_79_1.y or var_79_1.z
	var_79_0.anchoredPosition3D = arg_79_1
end

function getAnchoredPosition(arg_80_0)
	return rtf(arg_80_0).anchoredPosition
end

function setLocalScale(arg_81_0, arg_81_1)
	local var_81_0 = tf(arg_81_0).localScale

	arg_81_1.x = arg_81_1.x or var_81_0.x
	arg_81_1.y = arg_81_1.y or var_81_0.y
	arg_81_1.z = arg_81_1.z or var_81_0.z
	tf(arg_81_0).localScale = arg_81_1
end

function setLocalRotation(arg_82_0, arg_82_1)
	local var_82_0 = tf(arg_82_0).localRotation

	arg_82_1.x = arg_82_1.x or var_82_0.x
	arg_82_1.y = arg_82_1.y or var_82_0.y
	arg_82_1.z = arg_82_1.z or var_82_0.z
	tf(arg_82_0).localRotation = arg_82_1
end

function setLocalEulerAngles(arg_83_0, arg_83_1)
	local var_83_0 = tf(arg_83_0).localEulerAngles

	arg_83_1.x = arg_83_1.x or var_83_0.x
	arg_83_1.y = arg_83_1.y or var_83_0.y
	arg_83_1.z = arg_83_1.z or var_83_0.z
	tf(arg_83_0).localEulerAngles = arg_83_1
end

function ActivateInputField(arg_84_0)
	GetComponent(arg_84_0, typeof(InputField)):ActivateInputField()
end

function onInputChanged(arg_85_0, arg_85_1, arg_85_2)
	local var_85_0 = GetComponent(arg_85_1, typeof(InputField)).onValueChanged

	var_85_0:RemoveAllListeners()
	pg.DelegateInfo.Add(arg_85_0, var_85_0)
	var_85_0:AddListener(arg_85_2)
end

function getImageColor(arg_86_0)
	return GetComponent(arg_86_0, typeof(Image)).color
end

function setImageColor(arg_87_0, arg_87_1)
	GetComponent(arg_87_0, typeof(Image)).color = arg_87_1
end

function getImageAlpha(arg_88_0)
	return GetComponent(arg_88_0, typeof(Image)).color.a
end

function setImageAlpha(arg_89_0, arg_89_1)
	local var_89_0 = GetComponent(arg_89_0, typeof(Image))
	local var_89_1 = var_89_0.color

	var_89_1.a = arg_89_1
	var_89_0.color = var_89_1
end

function getImageRaycastTarget(arg_90_0)
	return GetComponent(arg_90_0, typeof(Image)).raycastTarget
end

function setImageRaycastTarget(arg_91_0, arg_91_1)
	GetComponent(arg_91_0, typeof(Image)).raycastTarget = tobool(arg_91_1)
end

function getCanvasGroupAlpha(arg_92_0)
	return GetComponent(arg_92_0, typeof(CanvasGroup)).alpha
end

function setCanvasGroupAlpha(arg_93_0, arg_93_1)
	GetComponent(arg_93_0, typeof(CanvasGroup)).alpha = arg_93_1
end

function setActiveViaLayer(arg_94_0, arg_94_1)
	UIUtil.SetUIActiveViaLayer(go(arg_94_0), arg_94_1)
end

function setActiveViaCG(arg_95_0, arg_95_1)
	UIUtil.SetUIActiveViaCG(go(arg_95_0), arg_95_1)
end

function getTextColor(arg_96_0)
	return GetComponent(arg_96_0, typeof(Text)).color
end

function setTextColor(arg_97_0, arg_97_1)
	GetComponent(arg_97_0, typeof(Text)).color = arg_97_1
end

function getTextAlpha(arg_98_0)
	return GetComponent(arg_98_0, typeof(Text)).color.a
end

function setTextAlpha(arg_99_0, arg_99_1)
	local var_99_0 = GetComponent(arg_99_0, typeof(Text))
	local var_99_1 = var_99_0.color

	var_99_1.a = arg_99_1
	var_99_0.color = var_99_1
end

function setSizeDelta(arg_100_0, arg_100_1)
	local var_100_0 = GetComponent(arg_100_0, typeof(RectTransform))

	if not var_100_0 then
		return
	end

	local var_100_1 = var_100_0.sizeDelta

	var_100_1.x = arg_100_1.x
	var_100_1.y = arg_100_1.y
	var_100_0.sizeDelta = var_100_1
end

function getOutlineColor(arg_101_0)
	return GetComponent(arg_101_0, typeof(Outline)).effectColor
end

function setOutlineColor(arg_102_0, arg_102_1)
	GetComponent(arg_102_0, typeof(Outline)).effectColor = arg_102_1
end

function pressPersistTrigger(arg_103_0, arg_103_1, arg_103_2, arg_103_3, arg_103_4, arg_103_5, arg_103_6, arg_103_7)
	arg_103_6 = defaultValue(arg_103_6, 0.25)

	assert(arg_103_6 > 0, "maxSpeed less than zero")
	assert(arg_103_0, "should exist objectOrTransform")

	local var_103_0 = GetOrAddComponent(arg_103_0, typeof(EventTriggerListener))

	assert(arg_103_2, "should exist callback")

	local var_103_1

	var_103_0:AddPointDownFunc(function()
		var_103_1 = Timer.New(function()
			if arg_103_5 then
				local var_105_0 = math.max(var_103_1.duration - arg_103_1 / 10, arg_103_6)

				var_103_1.duration = var_105_0
			end

			existCall(arg_103_2)
		end, arg_103_1, -1)

		if arg_103_4 then
			var_103_1.func()
		end

		var_103_1:Start()

		if arg_103_7 and var_0_1 then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_103_7)
		end
	end)
	var_103_0:AddPointUpFunc(function()
		var_103_1:Stop()

		var_103_1 = nil

		if arg_103_3 then
			arg_103_3()
		end
	end)

	return var_103_0
end

function getSpritePivot(arg_107_0)
	local var_107_0 = arg_107_0.bounds
	local var_107_1 = -var_107_0.center.x / var_107_0.extents.x / 2 + 0.5
	local var_107_2 = -var_107_0.center.y / var_107_0.extents.y / 2 + 0.5

	return Vector2(var_107_1, var_107_2)
end

function resetAspectRatio(arg_108_0)
	local var_108_0 = GetComponent(arg_108_0, "Image")

	GetComponent(arg_108_0, "AspectRatioFitter").aspectRatio = var_108_0.preferredWidth / var_108_0.preferredHeight
end

function cloneTplTo(arg_109_0, arg_109_1, arg_109_2)
	local var_109_0 = tf(Instantiate(arg_109_0))

	var_109_0:SetParent(tf(arg_109_1), false)
	SetActive(var_109_0, true)

	if arg_109_2 then
		var_109_0.name = arg_109_2
	end

	return var_109_0
end

function setGray(arg_110_0, arg_110_1, arg_110_2)
	if arg_110_1 then
		local var_110_0 = GetOrAddComponent(arg_110_0, "UIGrayScale")

		var_110_0.Recursive = defaultValue(arg_110_2, true)
		var_110_0.enabled = true
	else
		RemoveComponent(arg_110_0, "UIGrayScale")
	end
end

function setBlackMask(arg_111_0, arg_111_1, arg_111_2)
	if arg_111_1 then
		arg_111_2 = arg_111_2 or {}

		local var_111_0 = GetOrAddComponent(arg_111_0, "UIMaterialAdjuster")

		var_111_0.Recursive = tobool(defaultValue(arg_111_2.recursive, true))

		local var_111_1 = Material.New(pg.ShaderMgr.GetInstance():GetShader("M02/Unlit Colored_Alpha_UI"))

		var_111_1:SetColor("_Color", arg_111_2.color or Color(0, 0, 0, 0.2))

		var_111_0.adjusterMaterial = var_111_1
		var_111_0.enabled = true
	else
		RemoveComponent(arg_111_0, "UIMaterialAdjuster")
	end
end

function blockBlackMask(arg_112_0, arg_112_1, arg_112_2)
	if arg_112_1 then
		local var_112_0 = GetOrAddComponent(arg_112_0, "UIMaterialAdjuster")

		var_112_0.Recursive = tobool(defaultValue(arg_112_2, true))
		var_112_0.enabled = false
	else
		RemoveComponent(arg_112_0, "UIMaterialAdjuster")
	end
end

function long2int(arg_113_0)
	local var_113_0, var_113_1 = int64.tonum2(arg_113_0)

	return var_113_0
end

function OnSliderWithButton(arg_114_0, arg_114_1, arg_114_2)
	local var_114_0 = arg_114_1:GetComponent("Slider")

	var_114_0.onValueChanged:RemoveAllListeners()
	pg.DelegateInfo.Add(arg_114_0, var_114_0.onValueChanged)
	var_114_0.onValueChanged:AddListener(arg_114_2)

	local var_114_1 = (var_114_0.maxValue - var_114_0.minValue) * 0.1

	onButton(arg_114_0, arg_114_1:Find("up"), function()
		var_114_0.value = math.clamp(var_114_0.value + var_114_1, var_114_0.minValue, var_114_0.maxValue)
	end, SFX_PANEL)
	onButton(arg_114_0, arg_114_1:Find("down"), function()
		var_114_0.value = math.clamp(var_114_0.value - var_114_1, var_114_0.minValue, var_114_0.maxValue)
	end, SFX_PANEL)
end

function addSlip(arg_117_0, arg_117_1, arg_117_2, arg_117_3, arg_117_4)
	local var_117_0 = GetOrAddComponent(arg_117_1, "EventTriggerListener")
	local var_117_1
	local var_117_2 = 0
	local var_117_3 = 50

	var_117_0:AddPointDownFunc(function()
		var_117_2 = 0
		var_117_1 = nil
	end)
	var_117_0:AddDragFunc(function(arg_119_0, arg_119_1)
		local var_119_0 = arg_119_1.position

		if not var_117_1 then
			var_117_1 = var_119_0
		end

		if arg_117_0 == SLIP_TYPE_HRZ then
			var_117_2 = var_119_0.x - var_117_1.x
		elseif arg_117_0 == SLIP_TYPE_VERT then
			var_117_2 = var_119_0.y - var_117_1.y
		end
	end)
	var_117_0:AddPointUpFunc(function(arg_120_0, arg_120_1)
		if var_117_2 < -var_117_3 then
			if arg_117_3 then
				arg_117_3()
			end
		elseif var_117_2 > var_117_3 then
			if arg_117_2 then
				arg_117_2()
			end
		elseif arg_117_4 then
			arg_117_4()
		end
	end)
end

function getSizeRate()
	local var_121_0 = pg.UIMgr.GetInstance().LevelMain.transform.rect
	local var_121_1 = UnityEngine.Screen

	return Vector2.New(var_121_0.width / var_121_1.width, var_121_0.height / var_121_1.height), var_121_0.width, var_121_0.height
end

function IsUsingWifi()
	return Application.internetReachability == UnityEngine.NetworkReachability.ReachableViaLocalAreaNetwork
end

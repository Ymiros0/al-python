local var_0_0 = class("GuideUIDuplicator")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.caches = {}
	arg_1_0.root = arg_1_1
end

function var_0_0.Duplicate(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = Object.Instantiate(arg_2_1, arg_2_0.root).transform

	setActive(var_2_0, true)
	arg_2_0:InitDuplication(var_2_0, arg_2_1, arg_2_2)

	if arg_2_2 then
		arg_2_0:UpdateSettings(var_2_0, arg_2_1, arg_2_2)
	end

	table.insert(arg_2_0.caches, var_2_0)

	return var_2_0
end

local function var_0_1(arg_3_0)
	return arg_3_0:GetComponent(typeof(Button)) ~= nil or arg_3_0:GetComponent(typeof(Toggle)) ~= nil or arg_3_0:GetComponent(typeof(EventTriggerListener)) ~= nil
end

local function var_0_2(arg_4_0)
	local var_4_0 = arg_4_0:GetComponent(typeof(Button))
	local var_4_1 = arg_4_0:GetComponentsInChildren(typeof(Button))

	for iter_4_0 = 1, var_4_1.Length do
		local var_4_2 = var_4_1[iter_4_0 - 1]

		if var_4_0 ~= var_4_2 then
			var_4_2.enabled = false
		end
	end

	local var_4_3 = arg_4_0:GetComponent(typeof(Toggle))
	local var_4_4 = arg_4_0:GetComponentsInChildren(typeof(Toggle))

	for iter_4_1 = 1, var_4_4.Length do
		local var_4_5 = var_4_4[iter_4_1 - 1]

		if var_4_3 ~= var_4_5 then
			var_4_5.enabled = false
		end
	end

	if var_4_3 then
		setToggleEnabled(arg_4_0, true)
	end
end

local function var_0_3(arg_5_0)
	if LeanTween.isTweening(arg_5_0.gameObject) then
		LeanTween.cancel(arg_5_0.gameObject)
	end

	eachChild(arg_5_0, function(arg_6_0)
		if LeanTween.isTweening(arg_6_0.gameObject) then
			LeanTween.cancel(arg_6_0.gameObject)
		end
	end)
end

function var_0_0.InitDuplication(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	local var_7_0 = arg_7_1:GetComponent(typeof(CanvasGroup))

	if var_7_0 then
		var_7_0.alpha = 1
	end

	local var_7_1 = arg_7_1:GetComponentInChildren(typeof(UnityEngine.UI.Graphic))

	if arg_7_1:GetComponentInChildren(typeof(Canvas)) or var_7_1 == nil then
		GetOrAddComponent(arg_7_1, typeof(Image)).color = Color.New(1, 1, 1, 0)
	end

	if var_7_1 and var_7_1.raycastTarget == false then
		var_7_1.raycastTarget = true
	end

	local var_7_2 = arg_7_1:GetComponent(typeof(Animator))

	if var_7_2 then
		var_7_2.enabled = false
	end

	if var_0_1(arg_7_1) or arg_7_3.clearChildEvent then
		var_0_2(arg_7_1)
	end

	var_0_3(arg_7_1)

	if not arg_7_3.keepScrollTxt then
		local var_7_3 = arg_7_1:GetComponentsInChildren(typeof(ScrollText))

		for iter_7_0 = 1, var_7_3.Length do
			local var_7_4 = var_7_3[iter_7_0 - 1]

			setActive(var_7_4.gameObject, false)
		end
	end

	if arg_7_1:GetComponent(typeof(Canvas)) and arg_7_1:GetComponent(typeof(GraphicRaycaster)) == nil then
		GetOrAddComponent(arg_7_1, typeof(GraphicRaycaster))
	end

	arg_7_1.sizeDelta = arg_7_2.sizeDelta
end

function var_0_0.UpdateSettings(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	if arg_8_3.customPosition then
		arg_8_0:SetCustomPosition(arg_8_1, arg_8_2, arg_8_3)
	else
		arg_8_0:Syn(arg_8_1, arg_8_2, arg_8_3)
	end

	if arg_8_3.clearAllEvent then
		GetOrAddComponent(arg_8_1, typeof(CanvasGroup)).blocksRaycasts = false
	end
end

function var_0_0.SetCustomPosition(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
	if arg_9_3.pos then
		arg_9_1.localPosition = Vector3(arg_9_3.pos.x, arg_9_3.pos.y, arg_9_3.pos.z or 0)
	elseif arg_9_3.isLevelPoint then
		local var_9_0 = pg.UIMgr.GetInstance().levelCameraComp
		local var_9_1 = arg_9_2.transform.parent:TransformPoint(arg_9_2.transform.localPosition)
		local var_9_2 = var_9_0:WorldToScreenPoint(var_9_1)
		local var_9_3 = pg.UIMgr.GetInstance().overlayCameraComp

		arg_9_1.localPosition = LuaHelper.ScreenToLocal(arg_9_0.root, var_9_2, var_9_3)
	else
		arg_9_1.position = arg_9_2.transform.position
		arg_9_1.localPosition = Vector3(arg_9_1.localPosition.x, arg_9_1.localPosition.y, 0)
	end

	local var_9_4 = arg_9_3.scale or 1

	arg_9_1.localScale = Vector3(var_9_4, var_9_4, var_9_4)
	arg_9_1.eulerAngles = arg_9_3.eulerAngles and Vector3(arg_9_3.eulerAngles[1], arg_9_3.eulerAngles[2], arg_9_3.eulerAngles[3]) or Vector3(0, 0, 0)
end

local function var_0_4(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = arg_10_0.root:InverseTransformPoint(arg_10_2.transform.position)

	arg_10_1.localPosition = Vector3(var_10_0.x, var_10_0.y, 0)

	local var_10_1 = arg_10_2.transform.localScale

	arg_10_1.localScale = Vector3(var_10_1.x, var_10_1.y, var_10_1.z)
end

local function var_0_5(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0
	local var_11_1
	local var_11_2 = arg_11_2.image.isChild and arg_11_1:Find(arg_11_2.image.source) or GameObject.Find(arg_11_2.image.source)

	if arg_11_2.image.isRelative then
		var_11_1 = arg_11_2.image.target == "" and arg_11_0 or arg_11_0:Find(arg_11_2.image.target)
	else
		var_11_1 = GameObject.Find(arg_11_2.image.target)
	end

	if IsNil(var_11_2) or IsNil(var_11_1) then
		return
	end

	local var_11_3 = var_11_2:GetComponent(typeof(Image))
	local var_11_4 = var_11_1:GetComponent(typeof(Image))

	if not var_11_3 or not var_11_4 then
		return
	end

	local var_11_5 = var_11_3.sprite
	local var_11_6 = var_11_4.sprite

	if var_11_5 and var_11_6 and var_11_5 ~= var_11_6 then
		var_11_4.enabled = var_11_3.enabled

		setImageSprite(var_11_1, var_11_5)
	end
end

function var_0_0.Syn(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	arg_12_0:RemoveTimer()

	arg_12_0.timer = Timer.New(function()
		var_0_4(arg_12_0, arg_12_1, arg_12_2, arg_12_3)

		if arg_12_3.image then
			var_0_5(arg_12_1, arg_12_2, arg_12_3)
		end
	end, 0.01, -1)

	arg_12_0.timer:Start()
	arg_12_0.timer.func()
end

function var_0_0.RemoveTimer(arg_14_0)
	if arg_14_0.timer then
		arg_14_0.timer:Stop()

		arg_14_0.timer = nil
	end
end

function var_0_0.Clear(arg_15_0)
	if arg_15_0.caches and #arg_15_0.caches > 0 then
		for iter_15_0, iter_15_1 in ipairs(arg_15_0.caches) do
			Object.Destroy(iter_15_1.gameObject)
		end

		arg_15_0.caches = {}
	end

	arg_15_0:RemoveTimer()
end

return var_0_0

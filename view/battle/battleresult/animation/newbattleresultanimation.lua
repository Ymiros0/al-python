local var_0_0 = class("NewBattleResultAnimation")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tf = arg_1_1
	arg_1_0.bgImage = arg_1_0._tf:GetComponent(typeof(Image))
	arg_1_0.paintingTr = arg_1_0._tf:Find("painting/painting")
	arg_1_0.mask = arg_1_0._tf:Find("mask")
	arg_1_0.items = {}
	arg_1_0.paintingPosition = Vector2(698, 0)
	arg_1_0.paintingSizeDelta = Vector2(625, 1080)

	arg_1_0:Start()
end

function var_0_0.CollectionItems(arg_2_0, arg_2_1)
	eachChild(arg_2_0._tf, function(arg_3_0)
		if arg_3_0 ~= arg_2_0.mask then
			table.insert(arg_2_1, {
				position = arg_3_0.position,
				tr = arg_3_0
			})
		end
	end)
end

function var_0_0.Start(arg_4_0)
	if not arg_4_0.handle then
		arg_4_0.handle = UpdateBeat:CreateListener(arg_4_0.Update, arg_4_0)
	end

	UpdateBeat:AddListener(arg_4_0.handle)
end

function var_0_0.Play(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0.setUp = true

	setActive(arg_5_0.mask, true)
	arg_5_0:CollectionItems(arg_5_0.items)
	arg_5_0:MaskItems()
	parallelAsync({
		function(arg_6_0)
			arg_5_0:ZoomMask(arg_6_0)
		end,
		function(arg_7_0)
			if not arg_5_1 then
				return arg_7_0()
			end

			arg_5_0:ZoomPainting(arg_5_1, arg_7_0)
		end
	}, function()
		arg_5_0.setUp = false

		arg_5_0:RevertItems()
		setActive(arg_5_0.mask, false)
		arg_5_0:Clear()
		arg_5_2()
	end)
end

function var_0_0.ZoomPainting(arg_9_0, arg_9_1, arg_9_2)
	local function var_9_0()
		if arg_9_0.exited then
			return
		end

		local var_10_0 = arg_9_0.paintingTr:Find("fitter")

		var_10_0:GetComponent(typeof(PaintingScaler)).enabled = false

		local var_10_1 = arg_9_1.position
		local var_10_2 = arg_9_1.scale
		local var_10_3 = arg_9_1.pivot
		local var_10_4 = var_10_0:GetChild(0)

		arg_9_0:SetPivot(var_10_4, var_10_3)
		LeanTween.value(var_10_4.gameObject, Vector2(var_10_4.position.x, var_10_4.position.y), var_10_1, 0.2):setOnUpdate(System.Action_UnityEngine_Vector2(function(arg_11_0)
			var_10_4.position = Vector3(arg_11_0.x, arg_11_0.y, 0)
			var_10_4.localPosition = Vector3(var_10_4.localPosition.x, var_10_4.localPosition.y, 0)
		end))
		LeanTween.value(var_10_4.gameObject, Vector2(var_10_4.localScale.x, var_10_4.localScale.y), var_10_2, 0.2):setOnUpdate(System.Action_UnityEngine_Vector2(function(arg_12_0)
			var_10_4.localScale = Vector3(arg_12_0.x, arg_12_0.y, 1)
		end)):setOnComplete(System.Action(arg_9_2))
	end

	onNextTick(var_9_0)
end

function var_0_0.SetPivot(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = arg_13_1.rect.size
	local var_13_1 = arg_13_1.pivot - arg_13_2
	local var_13_2 = Vector3(var_13_1.x * var_13_0.x, var_13_1.y * var_13_0.y)

	arg_13_1.pivot = arg_13_2
	arg_13_1.localPosition = arg_13_1.localPosition - var_13_2
end

local function var_0_1(arg_14_0, arg_14_1)
	return arg_14_0:InverseTransformPoint(arg_14_1)
end

function var_0_0.RevertItems(arg_15_0)
	for iter_15_0 = #arg_15_0.items, 1, -1 do
		local var_15_0 = arg_15_0.items[iter_15_0]
		local var_15_1 = var_15_0.tr
		local var_15_2 = var_15_0.position

		setParent(var_15_1, arg_15_0._tf, true)

		var_15_1.localPosition = var_0_1(arg_15_0._tf, var_15_2)
	end
end

function var_0_0.ZoomMask(arg_16_0, arg_16_1)
	LeanTween.value(arg_16_0.mask.gameObject, Vector2(418, 936), Vector2(4180, 2000), 0.4):setOnUpdate(System.Action_UnityEngine_Vector2(function(arg_17_0)
		arg_16_0.mask.sizeDelta = arg_17_0
	end)):setOnComplete(System.Action(arg_16_1))
end

function var_0_0.MaskItems(arg_18_0)
	for iter_18_0 = #arg_18_0.items, 1, -1 do
		local var_18_0 = arg_18_0.items[iter_18_0].tr

		setParent(var_18_0, arg_18_0.mask, true)
	end
end

function var_0_0.Update(arg_19_0)
	if arg_19_0.setUp then
		arg_19_0:SynItemsPosition()
	end
end

function var_0_0.SynItemsPosition(arg_20_0)
	for iter_20_0, iter_20_1 in ipairs(arg_20_0.items) do
		local var_20_0 = iter_20_1.tr
		local var_20_1 = iter_20_1.position

		var_20_0.localPosition = var_0_1(arg_20_0.mask, var_20_1)
	end
end

function var_0_0.Clear(arg_21_0)
	if arg_21_0.handle then
		UpdateBeat:RemoveListener(arg_21_0.handle)

		arg_21_0.handle = nil
	end

	if LeanTween.isTweening(arg_21_0.mask.gameObject) then
		LeanTween.cancel(arg_21_0.mask.gameObject)
	end

	if LeanTween.isTweening(arg_21_0.paintingTr.gameObject) then
		LeanTween.cancel(arg_21_0.paintingTr.gameObject)
	end
end

function var_0_0.Dispose(arg_22_0)
	arg_22_0.exited = true

	arg_22_0:Clear()
end

return var_0_0

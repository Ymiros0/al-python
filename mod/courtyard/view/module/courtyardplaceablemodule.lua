local var_0_0 = class("CourtYardPlaceableModule", import(".CourtYardBaseModule"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.state = 0

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_2
	arg_1_0._tf = arg_1_2.transform
	arg_1_0.data = arg_1_1
	arg_1_0.callbacks = {}
	arg_1_0.iconLoaded = false
	arg_1_0.pudding = false
	arg_1_0.completion = false
	arg_1_0.cg = arg_1_0._tf:GetComponent(typeof(CanvasGroup))
	arg_1_0.rect = arg_1_0:GetView():GetRect()
	arg_1_0.floor = arg_1_0.rect:Find("floor")
	arg_1_0.wall = arg_1_0.rect:Find("wall")
	arg_1_0.mat = arg_1_0.rect:Find("carpet")
	arg_1_0.gridsTF = arg_1_0._tf:Find("grids")
	arg_1_0.childsTF = arg_1_0._tf:Find("childs")
	arg_1_0.interactionTF = arg_1_0._tf:Find("interaction")
	arg_1_0.bones = {}

	local var_1_0 = arg_1_0.data:GetDirection()

	arg_1_0._tf.localScale = Vector3(var_1_0 == 1 and 1 or -1, 1, 1)

	setParent(arg_1_0._tf, arg_1_0:GetParentTF())
	arg_1_0:UpdatePosition(arg_1_0.data:GetPosition(), Vector3.zero)
end

function var_0_0.IsCompletion(arg_2_0)
	return arg_2_0.completion and not arg_2_0.doPuddingAniming
end

function var_0_0.OnIconLoaed(arg_3_0)
	arg_3_0.iconLoaded = true

	if arg_3_0.pudding then
		arg_3_0:PuddingAnim()
	end
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0.dragAgent = CourtYardDragAgent.New(arg_4_0, arg_4_0:GetView():GetRect())
	arg_4_0.completion = true
end

function var_0_0.CreateWhenStoreyInit(arg_5_0)
	arg_5_0:PuddingAnim()
end

function var_0_0.BlocksRaycasts(arg_6_0, arg_6_1)
	return
end

local var_0_1 = "follower_"

function var_0_0.NewBoneFollower(arg_7_0, arg_7_1)
	local var_7_0 = var_0_1 .. arg_7_1
	local var_7_1 = GameObject.New(var_7_0, typeof(RectTransform))
	local var_7_2 = var_7_1.transform

	var_7_2:SetParent(arg_7_0.interactionTF, false)

	local var_7_3 = GetOrAddComponent(var_7_1, typeof(Spine.Unity.BoneFollowerGraphic))

	var_7_3.followLocalScale = true
	var_7_3.skeletonGraphic = arg_7_0:GetSpine():GetComponent("Spine.Unity.SkeletonGraphic")

	var_7_3:SetBone(arg_7_1)

	arg_7_0.bones[var_7_0] = var_7_2

	return var_7_2.transform
end

function var_0_0.FindBoneFollower(arg_8_0, arg_8_1)
	local var_8_0 = var_0_1 .. arg_8_1

	return arg_8_0.bones[var_8_0]
end

function var_0_0.PuddingAnim(arg_9_0)
	if not arg_9_0.iconLoaded then
		arg_9_0.pudding = true

		return
	end

	arg_9_0.doPuddingAniming = true

	local var_9_0 = arg_9_0._tf.localScale.x
	local var_9_1 = arg_9_0._tf.localScale.y

	arg_9_0.normalX, arg_9_0.normalY = var_9_0, var_9_1

	LeanTween.scale(rtf(arg_9_0._tf), Vector3(var_9_0 + 0.2, var_9_1 + 0.2, 1), 0.2):setFrom(0):setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_9_0._tf), Vector3(var_9_0, var_9_1, 1), 0.1):setOnComplete(System.Action(function()
			arg_9_0.doPuddingAniming = false
		end))
	end))

	arg_9_0.pudding = false
end

function var_0_0.CancelPuddingAnim(arg_12_0)
	if arg_12_0.doPuddingAniming then
		LeanTween.cancel(arg_12_0._tf.gameObject)

		arg_12_0._tf.localScale = Vector3(arg_12_0.normalX, arg_12_0.normalY, 1)
		arg_12_0.doPuddingAniming = nil
	end
end

function var_0_0.GetParentTF(arg_13_0)
	if arg_13_0.data:GetDeathType() == CourtYardConst.DEPTH_TYPE_MAT then
		return arg_13_0.mat
	else
		return arg_13_0.floor
	end
end

function var_0_0.GetSpine(arg_14_0)
	assert(false)
end

function var_0_0.GetData(arg_15_0)
	return arg_15_0.data
end

function var_0_0.SetSiblingIndex(arg_16_0, arg_16_1)
	if arg_16_1 ~= arg_16_0._tf:GetSiblingIndex() then
		arg_16_0._tf:SetSiblingIndex(arg_16_1)
	end

	arg_16_0._go.name = arg_16_0.data.id .. "_" .. arg_16_1
end

function var_0_0.SetAsLastSibling(arg_17_0)
	arg_17_0._go.name = arg_17_0.data.id

	arg_17_0._tf:SetAsLastSibling()
end

function var_0_0.SetActive(arg_18_0, arg_18_1)
	setActive(arg_18_0._tf, arg_18_1)
end

function var_0_0.UpdatePosition(arg_19_0, arg_19_1, arg_19_2)
	local var_19_0 = CourtYardCalcUtil.Map2Local(arg_19_1) + (arg_19_2 or Vector3.zero)
	local var_19_1 = CourtYardCalcUtil.TrPosition2LocalPos(arg_19_0:GetParentTF(), arg_19_0._tf.parent, var_19_0)

	arg_19_0._tf.localPosition = var_19_1
end

function var_0_0.OnDispose(arg_20_0)
	for iter_20_0, iter_20_1 in pairs(arg_20_0.bones) do
		if not IsNil(iter_20_1) then
			Object.Destroy(iter_20_1.gameObject)
		end
	end

	arg_20_0.bones = {}

	if arg_20_0.dragAgent then
		arg_20_0.dragAgent:Dispose()

		arg_20_0.dragAgent = nil
	end

	if LeanTween.isTweening(go(arg_20_0._tf)) then
		LeanTween.cancel(go(arg_20_0._tf))
	end
end

function var_0_0.OnDestroy(arg_21_0)
	return
end

function var_0_0.OnBeginDrag(arg_22_0)
	return
end

function var_0_0.OnDragging(arg_23_0, arg_23_1)
	return
end

function var_0_0.OnDragEnd(arg_24_0, arg_24_1)
	return
end

return var_0_0

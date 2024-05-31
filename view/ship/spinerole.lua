local var_0_0 = class("SpineRole")

var_0_0.STATE_EMPTY = 0
var_0_0.STATE_LOADING = 1
var_0_0.STATE_INITED = 2
var_0_0.STATE_DISPOSE = 3

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.state = var_0_0.STATE_EMPTY

	if arg_1_1 then
		arg_1_0.ship = arg_1_1
		arg_1_0.prefabName = arg_1_0.ship:getPrefab()
	end
end

function var_0_0.SetData(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.prefabName = arg_2_1
	arg_2_0.attachmentData = arg_2_2
end

var_0_0.ORBIT_KEY_UI = "orbit_ui"
var_0_0.ORBIT_KEY_SLG = "orbit_slg"

function var_0_0.Load(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if arg_3_2 == nil then
		arg_3_2 = true
	end

	PoolMgr.GetInstance():GetSpineChar(arg_3_0.prefabName, arg_3_2, function(arg_4_0)
		assert(arg_4_0, "没有这个角色的模型  " .. arg_3_0.prefabName)

		if arg_3_0.state == var_0_0.STATE_DISPOSE then
			PoolMgr.GetInstance():ReturnSpineChar(arg_3_0.prefabName, arg_4_0)
		else
			arg_3_0.modelRoot = GameObject.New(arg_3_0.prefabName .. "_root")

			arg_3_0.modelRoot:AddComponent(typeof(RectTransform))

			arg_3_0.model = arg_4_0
			arg_3_0.model.transform.localScale = Vector3.one

			arg_3_0.model.transform:SetParent(arg_3_0.modelRoot.transform, false)

			arg_3_0.model.transform.localPosition = Vector3.zero

			arg_3_0:Init()

			if arg_3_1 then
				arg_3_1()
			end

			arg_3_0:AttachOrbit(arg_3_3)
		end
	end)
end

function var_0_0.Init(arg_5_0)
	arg_5_0.state = var_0_0.STATE_INITED
	arg_5_0._modleGraphic = arg_5_0.model:GetComponent("SkeletonGraphic")
	arg_5_0._modleAnim = arg_5_0.model:GetComponent("SpineAnimUI")
	arg_5_0._attachmentList = {}
	arg_5_0._visible = true
end

function var_0_0.AttachOrbit(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1 or var_0_0.ORBIT_KEY_UI
	local var_6_1 = arg_6_0:GetAttachmentList()

	for iter_6_0, iter_6_1 in pairs(var_6_1) do
		local var_6_2 = iter_6_1[var_6_0]

		if var_6_0 ~= var_0_0.ORBIT_KEY_UI and var_6_2 == "" then
			var_6_2 = iter_6_1.orbit_ui
			var_6_0 = var_0_0.ORBIT_KEY_UI
		end

		if var_6_2 ~= "" then
			local var_6_3 = ys.Battle.BattleResourceManager.GetOrbitPath(var_6_2)

			ResourceMgr.Inst:getAssetAsync(var_6_3, var_6_2, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_7_0)
				if arg_6_0.state == var_0_0.STATE_DISPOSE then
					-- block empty
				else
					local var_7_0 = var_6_0 .. "_bound"
					local var_7_1 = iter_6_1[var_7_0][1]
					local var_7_2 = iter_6_1[var_7_0][2]
					local var_7_3 = Object.Instantiate(arg_7_0)

					var_7_3.transform.localPosition = Vector2(var_7_2[1], var_7_2[2])

					local var_7_4 = SpineAnimUI.AddFollower(var_7_1, arg_6_0.model.transform, var_7_3.transform)

					var_7_3.transform.localScale = Vector3.one
					arg_6_0._attachmentList[var_7_4] = iter_6_1.orbit_hidden_action
					var_7_4:GetComponent("Spine.Unity.BoneFollowerGraphic").followBoneRotation = false

					if iter_6_1.orbit_ui_back == 1 then
						var_7_4:SetParent(arg_6_0.modelRoot.transform, false)
						var_7_4:SetAsFirstSibling()
					else
						var_7_4:SetParent(arg_6_0.modelRoot.transform, false)
						var_7_4:SetAsLastSibling()
					end

					SetActive(var_7_3, arg_6_0._visible)
				end
			end), true, true)
		end
	end
end

function var_0_0.GetAttachmentList(arg_8_0)
	if arg_8_0.ship then
		return arg_8_0.ship:getAttachmentPrefab()
	else
		return arg_8_0.attachmentData or {}
	end
end

function var_0_0.CheckInited(arg_9_0)
	return arg_9_0.state == var_0_0.STATE_INITED
end

function var_0_0.GetName(arg_10_0)
	return arg_10_0.modelRoot.name
end

function var_0_0.SetParent(arg_11_0, arg_11_1)
	if arg_11_0:CheckInited() then
		SetParent(arg_11_0.modelRoot, arg_11_1, false)
	end
end

function var_0_0.SetRaycastTarget(arg_12_0, arg_12_1)
	if arg_12_0:CheckInited() then
		arg_12_0._modleGraphic.raycastTarget = arg_12_1
	end
end

function var_0_0.ModifyName(arg_13_0, arg_13_1)
	if arg_13_0:CheckInited() then
		arg_13_0.modelRoot.name = arg_13_1
	end
end

function var_0_0.SetVisible(arg_14_0, arg_14_1)
	if arg_14_0:CheckInited() then
		arg_14_0._visible = arg_14_1
		arg_14_0._modleGraphic.color = Color.New(1, 1, 1, arg_14_1 and 1 or 0)

		for iter_14_0, iter_14_1 in pairs(arg_14_0._attachmentList) do
			SetActive(iter_14_0, arg_14_1)
		end
	end
end

function var_0_0.SetAction(arg_15_0, arg_15_1)
	if not arg_15_0:CheckInited() then
		return
	end

	arg_15_0._modleAnim:SetAction(arg_15_1, 0)
	arg_15_0:HiddenAttachmentByAction(arg_15_1)
end

function var_0_0.SetActionOnce(arg_16_0, arg_16_1)
	if not arg_16_0:CheckInited() then
		return
	end

	arg_16_0._modleGraphic.AnimationState:SetAnimation(0, arg_16_1, false)
	arg_16_0:HiddenAttachmentByAction(arg_16_1)
end

function var_0_0.SetActionCallBack(arg_17_0, arg_17_1)
	if not arg_17_0:CheckInited() then
		return
	end

	arg_17_0._modleAnim:SetActionCallBack(arg_17_1)
end

function var_0_0.HiddenAttachmentByAction(arg_18_0, arg_18_1)
	for iter_18_0, iter_18_1 in pairs(arg_18_0._attachmentList) do
		SetActive(iter_18_0, not table.contains(iter_18_1, arg_18_1))
	end
end

function var_0_0.SetSizeDelta(arg_19_0, arg_19_1)
	if arg_19_0:CheckInited() then
		rtf(arg_19_0.modelRoot).sizeDelta = arg_19_1
	end
end

function var_0_0.SetLocalScale(arg_20_0, arg_20_1)
	if arg_20_0:CheckInited() then
		arg_20_0.modelRoot.transform.localScale = arg_20_1
	end
end

function var_0_0.SetLocalPos(arg_21_0, arg_21_1)
	if arg_21_0:CheckInited() then
		arg_21_0.modelRoot.transform.localPosition = arg_21_1
	end
end

function var_0_0.SetLayer(arg_22_0, arg_22_1)
	if arg_22_0:CheckInited() then
		pg.ViewUtils.SetLayer(arg_22_0.modelRoot.transform, arg_22_1)
	end
end

function var_0_0.TweenShining(arg_23_0, arg_23_1, arg_23_2, arg_23_3, arg_23_4, arg_23_5, arg_23_6, arg_23_7, arg_23_8, arg_23_9, arg_23_10)
	if arg_23_0:CheckInited() then
		arg_23_0:StopTweenShining()

		local var_23_0 = arg_23_0._modleGraphic.material
		local var_23_1 = LeanTween.value(arg_23_0.modelRoot, arg_23_3, arg_23_4, arg_23_1):setEase(LeanTweenType.easeInOutSine):setOnUpdate(System.Action_float(function(arg_24_0)
			if arg_23_7 then
				var_23_0:SetColor("_Color", Color.Lerp(arg_23_5, arg_23_6, arg_24_0))
			else
				arg_23_0._modleGraphic.color = Color.Lerp(arg_23_5, arg_23_6, arg_24_0)
			end

			existCall(arg_23_9, arg_24_0)
		end)):setOnComplete(System.Action(function()
			arg_23_0._tweenShiningId = nil

			if arg_23_8 then
				if arg_23_7 then
					var_23_0:SetColor("_Color", arg_23_5)
				else
					arg_23_0._modleGraphic.color = arg_23_5
				end
			end

			existCall(arg_23_10)
		end))

		if arg_23_2 then
			var_23_1:setLoopPingPong(arg_23_2)
		end

		arg_23_0._tweenShiningId = var_23_1.uniqueId
	end
end

function var_0_0.StopTweenShining(arg_26_0)
	if arg_26_0:CheckInited() and arg_26_0._tweenShiningId then
		LeanTween.cancel(arg_26_0._tweenShiningId, true)

		arg_26_0._tweenShiningId = nil
	end
end

function var_0_0.ChangeMaterial(arg_27_0, arg_27_1)
	if not arg_27_0:CheckInited() then
		return
	end

	if not arg_27_0._stageMaterial then
		arg_27_0._stageMaterial = arg_27_0._modleGraphic.material
	end

	arg_27_0._modleGraphic.material = arg_27_1
end

function var_0_0.RevertMaterial(arg_28_0)
	if not arg_28_0:CheckInited() then
		return
	end

	if not arg_28_0._stageMaterial then
		return
	end

	arg_28_0._modleGraphic.material = arg_28_0._stageMaterial
end

function var_0_0.CreateInterface(arg_29_0)
	arg_29_0._mouseChild = GameObject("mouseChild")

	arg_29_0._mouseChild.transform:SetParent(arg_29_0.modelRoot.transform, false)

	arg_29_0._mouseChild.transform.localPosition = Vector3.zero
	arg_29_0._modelClick = GetOrAddComponent(arg_29_0._mouseChild, "ModelDrag")
	arg_29_0._modelPress = GetOrAddComponent(arg_29_0._mouseChild, "UILongPressTrigger")
	arg_29_0._dragDelegate = GetOrAddComponent(arg_29_0._mouseChild, "EventTriggerListener")

	arg_29_0._modelClick:Init()

	local var_29_0 = GetOrAddComponent(arg_29_0._mouseChild, typeof(RectTransform))

	var_29_0.pivot = Vector2(0.5, 0)
	var_29_0.anchoredPosition = Vector2(0, 0)
	var_29_0.localScale = Vector2(100, 100)
	var_29_0.sizeDelta = Vector2(3, 3)

	return arg_29_0._modelClick, arg_29_0._modelPress, arg_29_0._dragDelegate
end

function var_0_0.resumeRole(arg_30_0)
	if arg_30_0._modleAnim and arg_30_0._modleAnim:GetAnimationState() then
		arg_30_0._modleAnim:Resume()
	end
end

function var_0_0.GetInterface(arg_31_0)
	return arg_31_0._modelClick, arg_31_0._modelPress, arg_31_0._dragDelegate
end

function var_0_0.EnableInterface(arg_32_0)
	arg_32_0._mouseChild:GetComponent(typeof(Image)).enabled = true
end

function var_0_0.DisableInterface(arg_33_0)
	arg_33_0._mouseChild:GetComponent(typeof(Image)).enabled = false
end

function var_0_0.Dispose(arg_34_0)
	if arg_34_0.state == var_0_0.STATE_INITED then
		arg_34_0:StopTweenShining()
		arg_34_0:RevertMaterial()
		PoolMgr.GetInstance():ReturnSpineChar(arg_34_0.prefabName, arg_34_0.model)
		arg_34_0:SetVisible(true)
		arg_34_0._modleGraphic.material:SetColor("_Color", Color.New(0, 0, 0, 0))

		arg_34_0._modleGraphic.color = Color.New(1, 1, 1, 1)

		for iter_34_0, iter_34_1 in pairs(arg_34_0._attachmentList) do
			Object.Destroy(iter_34_0.gameObject)
		end

		arg_34_0.model = nil
		arg_34_0.prefabName = nil
		arg_34_0.ship = nil
		arg_34_0.attachmentData = nil
		arg_34_0._modleGraphic = nil
		arg_34_0._modleAnim = nil
		arg_34_0._attachmentList = nil
	end

	arg_34_0.state = var_0_0.STATE_DISPOSE
end

return var_0_0

local var_0_0 = class("WSAtlasBottom", import("...BaseEntity"))

var_0_0.Fields = {
	rtBg = "userdata",
	transform = "userdata",
	btnBoss = "userdata",
	btnOverview = "userdata",
	btnCollection = "userdata",
	rtButton = "userdata",
	wsTimer = "table",
	comSilder = "userdata",
	twId = "number",
	btnShop = "userdata",
	btnDailyTask = "userdata"
}
var_0_0.EventUpdateScale = "WSAtlasBottom.EventUpdateScale"

function var_0_0.Setup(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:Init()
end

function var_0_0.Dispose(arg_2_0)
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0:Clear()
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0.transform

	arg_3_0.rtBg = var_3_0:Find("bg")
	arg_3_0.rtButton = var_3_0:Find("button")
	arg_3_0.btnBoss = arg_3_0.rtButton:Find("btn_boss")
	arg_3_0.btnShop = arg_3_0.rtButton:Find("btn_shop")
	arg_3_0.btnOverview = arg_3_0.rtButton:Find("btn_overview")
	arg_3_0.btnCollection = arg_3_0.rtButton:Find("btn_collection")
	arg_3_0.btnDailyTask = arg_3_0.rtButton:Find("btn_daily")
	arg_3_0.comSilder = var_3_0:Find("scale/Slider"):GetComponent("Slider")
	arg_3_0.comSilder.interactable = CAMERA_MOVE_OPEN

	if CAMERA_MOVE_OPEN then
		arg_3_0.comSilder.onValueChanged:AddListener(function(arg_4_0)
			arg_3_0:DispatchEvent(var_0_0.EventUpdateScale, arg_4_0)
		end)
	end
end

function var_0_0.UpdateScale(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if arg_5_2 then
		local var_5_0 = arg_5_0.comSilder.value

		setImageAlpha(arg_5_0.btnOverview, var_5_0)
		setActive(arg_5_0.btnOverview, true)

		arg_5_0.twId = LeanTween.value(go(arg_5_0.comSilder), var_5_0, arg_5_1, WSAtlasWorld.baseDuration):setEase(LeanTweenType.easeInOutSine):setOnUpdate(System.Action_float(function(arg_6_0)
			arg_5_0.comSilder.value = arg_6_0

			setImageAlpha(arg_5_0.btnOverview, arg_6_0)
		end)):setOnComplete(System.Action(function()
			setActive(arg_5_0.btnOverview, arg_5_1 == 1)

			return existCall(arg_5_3)
		end)).uniqueId

		arg_5_0.wsTimer:AddTween(arg_5_0.twId)
	else
		setImageAlpha(arg_5_0.btnOverview, arg_5_1)
		setActive(arg_5_0.btnOverview, arg_5_1 == 1)

		arg_5_0.comSilder.value = arg_5_1

		return existCall(arg_5_3)
	end
end

function var_0_0.CheckIsTweening(arg_8_0)
	return arg_8_0.twId and LeanTween.isTweening(arg_8_0.twId)
end

function var_0_0.SetOverSize(arg_9_0, arg_9_1)
	arg_9_0.rtBg.offsetMin = Vector2(arg_9_1, arg_9_0.rtBg.offsetMin.y)
	arg_9_0.rtBg.offsetMax = Vector2(-arg_9_1, arg_9_0.rtBg.offsetMax.y)
end

return var_0_0

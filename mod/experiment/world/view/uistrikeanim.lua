local var_0_0 = class("UIStrikeAnim", import(".UIAnim"))

var_0_0.Fields = {
	spineAnim = "userdata",
	prefab = "string",
	aniEvent = "userdata",
	char = "userdata",
	transform = "userdata",
	playing = "boolean",
	onTrigger = "function",
	onStart = "function",
	onEnd = "function",
	skelegraph = "userdata",
	painting = "userdata",
	shipVO = "table"
}
var_0_0.EventLoaded = "UIStrikeAnim.EventLoaded"

function var_0_0.Setup(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.prefab = arg_1_1
	arg_1_0.shipVO = arg_1_2
end

function var_0_0.LoadBack(arg_2_0)
	if arg_2_0.transform and arg_2_0.painting and arg_2_0.char then
		arg_2_0:Init()
		arg_2_0:DispatchEvent(var_0_0.EventLoaded)
	end
end

function var_0_0.Load(arg_3_0)
	local var_3_0 = arg_3_0.prefab
	local var_3_1 = PoolMgr.GetInstance()

	var_3_1:GetUI(var_3_0, true, function(arg_4_0)
		if var_3_0 == arg_3_0.prefab then
			arg_3_0.transform = arg_4_0.transform

			arg_3_0:LoadBack()
		else
			var_3_1:ReturnUI(var_3_0, arg_4_0)
		end
	end)
	arg_3_0:ReloadShip(arg_3_0.shipVO)
end

function var_0_0.ReloadShip(arg_5_0, arg_5_1)
	arg_5_0.shipVO = arg_5_1
	arg_5_0.aniEvent = nil
	arg_5_0.painting = nil
	arg_5_0.char = nil

	local var_5_0 = PoolMgr.GetInstance()

	var_5_0.GetInstance():GetPainting(arg_5_1:getPainting(), true, function(arg_6_0)
		arg_5_0.painting = arg_6_0

		ShipExpressionHelper.SetExpression(arg_5_0.painting, arg_5_1:getPainting())
		arg_5_0:LoadBack()
	end)
	var_5_0.GetInstance():GetSpineChar(arg_5_1:getPrefab(), true, function(arg_7_0)
		arg_5_0.char = arg_7_0
		arg_5_0.char.transform.localScale = Vector3.one

		arg_5_0:LoadBack()
	end)
end

function var_0_0.UnloadShipVO(arg_8_0)
	local var_8_0 = arg_8_0.shipVO

	retPaintingPrefab(arg_8_0.transform:Find("mask/painting"), var_8_0:getPainting())
	PoolMgr.GetInstance():ReturnSpineChar(var_8_0:getPrefab(), arg_8_0.char)

	arg_8_0.shipVO = nil
	arg_8_0.painting = nil
	arg_8_0.char = nil
end

function var_0_0.Play(arg_9_0, arg_9_1)
	arg_9_0.playing = true

	function arg_9_0.onStart(arg_10_0)
		arg_9_0.spineAnim:SetAction("attack", 0)

		arg_9_0.skelegraph.freeze = true
	end

	function arg_9_0.onTrigger(arg_11_0)
		arg_9_0.skelegraph.freeze = false

		arg_9_0.spineAnim:SetActionCallBack(function(arg_12_0)
			if arg_12_0 == "action" then
				-- block empty
			elseif arg_12_0 == "finish" then
				arg_9_0.skelegraph.freeze = true
			end
		end)
	end

	arg_9_0.onEnd = arg_9_1

	arg_9_0:Update()
end

function var_0_0.Stop(arg_13_0)
	arg_13_0.playing = false

	arg_13_0:Update()

	if arg_13_0.skelegraph then
		arg_13_0.skelegraph.freeze = false
	end

	arg_13_0:UnloadShipVO()
end

function var_0_0.Init(arg_14_0)
	setActive(arg_14_0.transform, false)

	local var_14_0 = arg_14_0.transform:Find("torpedo")
	local var_14_1 = arg_14_0.transform:Find("mask/painting")
	local var_14_2 = arg_14_0.transform:Find("ship")

	setParent(arg_14_0.painting, var_14_1:Find("fitter"), false)
	setParent(arg_14_0.char, var_14_2, false)
	setActive(var_14_2, false)
	setActive(var_14_0, false)

	arg_14_0.spineAnim = arg_14_0.char:GetComponent("SpineAnimUI")
	arg_14_0.skelegraph = arg_14_0.spineAnim:GetComponent("SkeletonGraphic")
	arg_14_0.aniEvent = arg_14_0.transform:GetComponent("DftAniEvent")

	arg_14_0:Update()
end

return var_0_0

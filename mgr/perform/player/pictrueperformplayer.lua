local var_0_0 = class("StoryPerformPlayer", import(".BasePerformPlayer"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.bgTF = arg_1_0:findTF("bg", arg_1_0._tf)
	arg_1_0.nameTF = arg_1_0:findTF("name", arg_1_0.bgTF)
	arg_1_0.imageCom = arg_1_0:findTF("picture", arg_1_0.bgTF):GetComponent(typeof(Image))
end

function var_0_0.Play(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0:Show()

	if arg_2_0._anim then
		arg_2_0._anim:Play()
	end

	if arg_2_3 then
		setText(arg_2_0.nameTF, arg_2_3)
	end

	local var_2_0 = arg_2_1.param[1] or ""
	local var_2_1 = arg_2_1.param[2] or 3

	setActive(arg_2_0.bgTF, false)
	ResourceMgr.Inst:getAssetAsync("educatepicture/" .. var_2_0, "", typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
		arg_2_0.imageCom.sprite = arg_3_0

		setActive(arg_2_0.bgTF, true)

		arg_2_0.timer = Timer.New(function()
			if arg_2_2 then
				arg_2_2()
			end
		end, var_2_1)

		arg_2_0.timer:Start()
	end), true, true)
end

function var_0_0.Clear(arg_5_0)
	arg_5_0.imageCom.sprite = nil

	if arg_5_0.timer ~= nil then
		arg_5_0.timer:Stop()

		arg_5_0.timer = nil
	end

	setText(arg_5_0.nameTF, "")
	arg_5_0:Hide()
end

return var_0_0

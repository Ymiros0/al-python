local var_0_0 = class("RectKeyTriggerController")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._keyInfo = arg_1_1

	if not arg_1_0.handle then
		arg_1_0.handle = UpdateBeat:CreateListener(arg_1_0.Update, arg_1_0)
	end

	UpdateBeat:AddListener(arg_1_0.handle)
end

function var_0_0.Update(arg_2_0)
	if Application.isEditor then
		if Input.GetKeyDown(KeyCode.A) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.A, true)
		end

		if Input.GetKeyDown(KeyCode.D) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.D, true)
		end

		if Input.GetKeyUp(KeyCode.A) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.A, false)
		end

		if Input.GetKeyUp(KeyCode.D) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.D, false)
		end

		if Input.GetKeyDown(KeyCode.Space) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.Space, true)
		end

		if Input.GetKeyUp(KeyCode.Space) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.Space, false)
		end

		if Input.GetKeyDown(KeyCode.J) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.J, true)
		end

		if Input.GetKeyUp(KeyCode.J) then
			arg_2_0._keyInfo:setKeyPress(KeyCode.J, false)
		end
	end
end

function var_0_0.destroy(arg_3_0)
	if arg_3_0.handle then
		UpdateBeat:RemoveListener(arg_3_0.handle)

		arg_3_0.handle = nil
	end
end

return var_0_0

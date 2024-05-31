local var_0_0 = class("CourtYardFollowInteraction", import(".CourtYardInteraction"))

function var_0_0.OnStepEnd(arg_1_0)
	if arg_1_0:IsCompleteOwnerStep() then
		arg_1_0:DoStep()
	end
end

return var_0_0

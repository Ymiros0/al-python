﻿local var_0_0 = class("GuildBossFormationShipCard")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	tf(arg_1_1).pivot = Vector2(0.5, 0)
	tf(arg_1_1).sizeDelta = Vector2(200, 300)
	tf(arg_1_1).localScale = Vector3(0.6, 0.6, 0.6)
end

function var_0_0.RefreshPosition(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.soltIndex = arg_2_1

	if arg_2_2 then
		arg_2_0:UpdateLocalPosition()
	end
end

function var_0_0.UpdateLocalPosition(arg_3_0)
	local var_3_0 = arg_3_0._go.transform.parent:Find(arg_3_0.soltIndex).localPosition

	arg_3_0:SetLocalPosition(var_3_0)
end

function var_0_0.SetLocalPosition(arg_4_0, arg_4_1)
	arg_4_0._go.transform.localPosition = arg_4_1
end

function var_0_0.GetLocalPosition(arg_5_0)
	return arg_5_0._go.transform.localPosition
end

function var_0_0.GetSoltIndex(arg_6_0)
	return arg_6_0.soltIndex
end

function var_0_0.Update(arg_7_0, arg_7_1, arg_7_2)
	arg_7_0.shipId = arg_7_1.id
	arg_7_0.teamType = arg_7_1:getTeamType()

	arg_7_0:RefreshPosition(arg_7_2, true)
end

function var_0_0.Dispose(arg_8_0)
	if arg_8_0._go then
		tf(arg_8_0._go).pivot = Vector2(0.5, 0.5)
	end

	ClearEventTrigger(GetOrAddComponent(arg_8_0._go, "EventTriggerListener"))
	PoolMgr.GetInstance():ReturnSpineChar(arg_8_0._go.name, arg_8_0._go)
end

return var_0_0

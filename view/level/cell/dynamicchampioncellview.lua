local var_0_0 = import(".DynamicCellView")
local var_0_1 = import(".ChampionCellView")
local var_0_2 = class("DynamicChampionCellView", DecorateClass(var_0_0, var_0_1))

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)
	var_0_1.InitChampionCellTransform(arg_1_0)
end

function var_0_2.GetOrder(arg_2_0)
	return ChapterConst.CellPriorityEnemy
end

function var_0_2.SetActive(arg_3_0, arg_3_1)
	arg_3_0:SetActiveModel(arg_3_1)
end

function var_0_2.SetActiveModel(arg_4_0, arg_4_1)
	arg_4_0:SetSpineVisible(arg_4_1)
	setActive(arg_4_0.tfShadow, arg_4_1)

	for iter_4_0, iter_4_1 in pairs(arg_4_0._extraEffectList) do
		if not IsNil(iter_4_1) then
			setActive(iter_4_1, arg_4_1)
		end
	end
end

function var_0_2.PlayShuiHua()
	return
end

function var_0_2.UpdateChampionCell(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	var_0_1.UpdateChampionCell(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0:RefreshLinePosition(arg_6_1, arg_6_2)
end

function var_0_2.TweenShining(arg_7_0, arg_7_1)
	arg_7_0:StopTween()

	local var_7_0 = arg_7_0:GetSpineRole()

	if not var_7_0 then
		return
	end

	var_7_0:TweenShining(0.5, arg_7_1, 0, 1, Color.New(0, 0, 0, 0), Color.New(1, 1, 1, 1), true, true)
end

function var_0_2.StopTween(arg_8_0)
	if not arg_8_0.tweenId then
		return
	end

	LeanTween.cancel(arg_8_0.tweenId, true)

	arg_8_0.tweenId = nil
end

function var_0_2.Clear(arg_9_0)
	arg_9_0:StopTween()

	if arg_9_0.go then
		LeanTween.cancel(arg_9_0.go)
	end

	var_0_1.Clear(arg_9_0)
end

return var_0_2

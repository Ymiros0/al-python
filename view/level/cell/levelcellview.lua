local var_0_0 = class("LevelCellView")

function var_0_0.Ctor(arg_1_0)
	arg_1_0.go = nil
	arg_1_0.tf = nil
	arg_1_0.orderTable = {}
end

function var_0_0.SetActive(arg_2_0, arg_2_1)
	setActive(arg_2_0.go, arg_2_1)
end

function var_0_0.GetOrder(arg_3_0)
	return ChapterConst.CellPriorityNone
end

function var_0_0.SetLoader(arg_4_0, arg_4_1)
	assert(not arg_4_0.loader, "repeatly Set loader")

	arg_4_0.loader = arg_4_1
end

function var_0_0.GetLoader(arg_5_0)
	arg_5_0.loader = arg_5_0.loader or AutoLoader.New()

	return arg_5_0.loader
end

function var_0_0.ClearLoader(arg_6_0)
	if arg_6_0.loader then
		arg_6_0.loader:Clear()
	end
end

function var_0_0.GetLine(arg_7_0)
	return arg_7_0.line
end

function var_0_0.SetLine(arg_8_0, arg_8_1)
	arg_8_0.line = {
		row = arg_8_1.row,
		column = arg_8_1.column
	}
end

function var_0_0.OverrideCanvas(arg_9_0)
	pg.ViewUtils.SetLayer(tf(arg_9_0.go), Layer.UI)

	arg_9_0.canvas = GetOrAddComponent(arg_9_0.go, typeof(Canvas))
	arg_9_0.canvas.overrideSorting = true
end

function var_0_0.ResetCanvasOrder(arg_10_0)
	if not arg_10_0.canvas then
		return
	end

	local var_10_0 = arg_10_0.line.row * ChapterConst.PriorityPerRow + arg_10_0:GetOrder()

	pg.ViewUtils.SetSortingOrder(arg_10_0.tf, var_10_0)
end

function var_0_0.GetCurrentOrder(arg_11_0)
	return arg_11_0.line.row * ChapterConst.PriorityPerRow + arg_11_0:GetOrder()
end

function var_0_0.AddCanvasOrder(arg_12_0, arg_12_1, arg_12_2)
	arg_12_1 = tf(arg_12_1)

	local var_12_0 = arg_12_1:GetComponents(typeof(Renderer))

	for iter_12_0 = 0, var_12_0.Length - 1 do
		var_12_0[iter_12_0].sortingOrder = (arg_12_0.orderTable[var_12_0[iter_12_0]] or 0) + arg_12_2
	end

	local var_12_1 = arg_12_1:GetComponent(typeof(Canvas))

	if var_12_1 then
		var_12_1.sortingOrder = (arg_12_0.orderTable[var_12_1] or 0) + arg_12_2
	end

	for iter_12_1 = 0, arg_12_1.childCount - 1 do
		arg_12_0:AddCanvasOrder(arg_12_1:GetChild(iter_12_1), arg_12_2)
	end
end

function var_0_0.RecordCanvasOrder(arg_13_0, arg_13_1)
	arg_13_1 = tf(arg_13_1)

	local var_13_0 = arg_13_1:GetComponents(typeof(Renderer))

	for iter_13_0 = 0, var_13_0.Length - 1 do
		local var_13_1 = var_13_0[iter_13_0]

		arg_13_0.orderTable[var_13_0[iter_13_0]] = var_13_0[iter_13_0].sortingOrder
	end

	local var_13_2 = arg_13_1:GetComponent(typeof(Canvas))

	if var_13_2 then
		arg_13_0.orderTable[var_13_2] = var_13_2.sortingOrder
	end

	for iter_13_1 = 0, arg_13_1.childCount - 1 do
		arg_13_0:RecordCanvasOrder(arg_13_1:GetChild(iter_13_1))
	end
end

function var_0_0.RefreshLinePosition(arg_14_0, arg_14_1, arg_14_2)
	if arg_14_2 then
		arg_14_0:SetLine(arg_14_2)
		arg_14_0:ResetCanvasOrder()
	end

	arg_14_0.tf.anchoredPosition = arg_14_1.theme:GetLinePosition(arg_14_0.line.row, arg_14_0.line.column)
end

function var_0_0.Clear(arg_15_0)
	for iter_15_0, iter_15_1 in pairs(arg_15_0.orderTable) do
		if not IsNil(iter_15_0) then
			iter_15_0.sortingOrder = iter_15_1
		end
	end

	table.clear(arg_15_0.orderTable)
	arg_15_0:ClearLoader()
end

return var_0_0

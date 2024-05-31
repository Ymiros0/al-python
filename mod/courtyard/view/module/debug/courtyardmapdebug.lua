local var_0_0 = class("CourtYardMapDebug")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.map = arg_1_1
	arg_1_0.mapGrids = {}
	arg_1_0.r = arg_1_2 and arg_1_2.r or 0
	arg_1_0.g = arg_1_2 and arg_1_2.g or 0
	arg_1_0.b = arg_1_2 and arg_1_2.b or 0

	arg_1_0:Init()
end

function var_0_0.GetView(arg_2_0)
	return arg_2_0.map:GetHost():GetBridge():GetView()
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0:GetView():GetRect():Find("grids")
	local var_3_1 = arg_3_0.map.minSizeX
	local var_3_2 = arg_3_0.map.minSizeY
	local var_3_3 = arg_3_0.map.sizeX
	local var_3_4 = arg_3_0.map.sizeY

	for iter_3_0 = var_3_1, var_3_3 do
		local var_3_5 = {}

		for iter_3_1 = var_3_2, var_3_4 do
			local var_3_6 = arg_3_0:GetView().poolMgr:GetGridPool():Dequeue()

			setParent(var_3_6, var_3_0)

			tf(var_3_6).localScale = Vector3.one
			tf(var_3_6).localPosition = CourtYardCalcUtil.Map2Local(Vector2(iter_3_0, iter_3_1))
			var_3_6:GetComponent(typeof(Image)).color = (iter_3_1 == var_3_4 or iter_3_0 == var_3_3) and Color.New(1, 1, 0, 0.5) or Color.New(0, 1, 0, 1)
			var_3_5[iter_3_1] = var_3_6
		end

		arg_3_0.mapGrids[iter_3_0] = var_3_5
	end

	arg_3_0:Flush()
end

function var_0_0.Flush(arg_4_0)
	local var_4_0 = arg_4_0.map.sizeX
	local var_4_1 = arg_4_0.map.sizeY

	for iter_4_0, iter_4_1 in pairs(arg_4_0.mapGrids) do
		for iter_4_2, iter_4_3 in pairs(iter_4_1) do
			local var_4_2 = arg_4_0.map:IsEmptyPosition(Vector2(iter_4_0, iter_4_2))
			local var_4_3 = iter_4_3:GetComponent(typeof(Image))
			local var_4_4

			if var_4_2 then
				var_4_4 = (iter_4_2 == var_4_1 or iter_4_0 == var_4_0) and Color.New(1, 1, 0, 0.5) or Color.New(0, 1, 0, 1)
			else
				var_4_4 = Color.New(arg_4_0.r, arg_4_0.g, arg_4_0.b, var_4_3.color.a)
			end

			var_4_3.color = var_4_4
		end
	end
end

function var_0_0.Clear(arg_5_0)
	for iter_5_0, iter_5_1 in pairs(arg_5_0.mapGrids) do
		for iter_5_2, iter_5_3 in pairs(iter_5_1) do
			iter_5_3:GetComponent(typeof(Image)).color = Color.New(0, 1, 0, 1)

			arg_5_0:GetView().poolMgr:GetGridPool():Enqueue(iter_5_3)
		end
	end

	arg_5_0.mapGrids = {}
end

function var_0_0.Dispose(arg_6_0)
	arg_6_0:Clear()
end

return var_0_0

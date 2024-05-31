pg = pg or {}

local var_0_0 = pg

var_0_0.FontMgr = singletonClass("FontMgr")

local var_0_1 = var_0_0.FontMgr

function var_0_0.FontMgr.Init(arg_1_0, arg_1_1)
	print("initializing font manager...")

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in pairs({
		crifont = "crifont",
		remfont = "remfont",
		heiti = "zhunyuan",
		treatfont = "treatfont",
		impact = "impact",
		chuanjiadanFont = "chuanjiadanFont",
		explofont = "explofont",
		number = "number",
		countnumber = "countnumber",
		weaponcountfont = "weaponcountfont",
		missfont = "missfont",
		MStiffHei = "MStiffHei",
		weijichuanFont = "weijichuanFont",
		bankgthd = "bankgthd",
		lvnumber = "lvnumber",
		sourcehanserifcn = "sourcehanserifcn-bold_0"
	}) do
		table.insert(var_1_0, function(arg_2_0)
			ResourceMgr.Inst:getAssetAsync("font/" .. iter_1_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
				arg_1_0.fonts[iter_1_0] = arg_3_0

				arg_2_0()
			end), false, false)
		end)
	end

	arg_1_0.fonts = {}

	parallelAsync(var_1_0, function(arg_4_0)
		arg_1_1(arg_4_0)
	end)
end

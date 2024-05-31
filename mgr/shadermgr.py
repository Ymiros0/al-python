pg = pg or {}

local var_0_0 = pg

var_0_0.ShaderMgr = singletonClass("ShaderMgr")

local var_0_1 = var_0_0.ShaderMgr

def var_0_0.ShaderMgr.Init(arg_1_0, arg_1_1):
	print("initializing shader manager...")
	Shader.DisableKeyword("LOW_DEVICE_PERFORMANCE")

	local function var_1_0(arg_2_0)
		ResourceMgr.Inst.LoadShaderAndCached("shader", arg_2_0, False, False)

	local function var_1_1(arg_3_0)
		ResourceMgr.Inst.LoadShaderAndCached("l2dshader", arg_3_0, False, False)

	local function var_1_2(arg_4_0)
		ResourceMgr.Inst.LoadShaderAndCached("spineshader", arg_4_0, False, False)

	local function var_1_3(arg_5_0)
		arg_5_0()

	local function var_1_4(arg_6_0)
		ResourceMgr.Inst.LoadShaderAndCached("builtinpipeline/shaders", arg_6_0, False, False)

	local var_1_5 = {
		var_1_0,
		var_1_1,
		var_1_2,
		var_1_3,
		var_1_4
	}

	parallelAsync(var_1_5, function()
		originalPrint("所有shader加载完成")
		arg_1_1())

def var_0_1.GetShader(arg_8_0, arg_8_1):
	return (ResourceMgr.Inst.GetShader(arg_8_1))

def var_0_1.GetBlurMaterialSync(arg_9_0):
	if arg_9_0.blurMaterial != None:
		return arg_9_0.blurMaterial
	else
		local var_9_0 = arg_9_0.GetShader("Hidden/MobileBlur")

		arg_9_0.blurMaterial = Material.New(var_9_0)

		arg_9_0.blurMaterial.SetVector("_Parameter", Vector4.New(1, -1, 0, 0))

		return arg_9_0.blurMaterial

def var_0_1.BlurTexture(arg_10_0, arg_10_1):
	local var_10_0 = ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "GetTemporary", {
		typeof("System.Int32"),
		typeof("System.Int32"),
		typeof("System.Int32")
	}, {
		Screen.width * 0.25,
		Screen.height * 0.25,
		0
	})
	local var_10_1 = ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "GetTemporary", {
		typeof("System.Int32"),
		typeof("System.Int32"),
		typeof("System.Int32")
	}, {
		Screen.width * 0.25,
		Screen.height * 0.25,
		0
	})

	var_10_0.filterMode = ReflectionHelp.RefGetField(typeof("UnityEngine.FilterMode"), "Bilinear")

	local var_10_2 = arg_10_0.GetBlurMaterialSync()

	ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.Graphics"), "Blit", {
		typeof("UnityEngine.RenderTexture"),
		typeof("UnityEngine.RenderTexture"),
		typeof("UnityEngine.Material"),
		typeof("System.Int32")
	}, {
		arg_10_1,
		var_10_0,
		var_10_2,
		0
	})

	for iter_10_0 = 0, 1:
		var_10_2.SetVector("_Parameter", Vector4.New(1 + iter_10_0, -1 - iter_10_0, 0, 0))
		ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.Graphics"), "Blit", {
			typeof("UnityEngine.RenderTexture"),
			typeof("UnityEngine.RenderTexture"),
			typeof("UnityEngine.Material"),
			typeof("System.Int32")
		}, {
			var_10_0,
			var_10_1,
			var_10_2,
			1
		})
		ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.Graphics"), "Blit", {
			typeof("UnityEngine.RenderTexture"),
			typeof("UnityEngine.RenderTexture"),
			typeof("UnityEngine.Material"),
			typeof("System.Int32")
		}, {
			var_10_1,
			var_10_0,
			var_10_2,
			2
		})

	ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "ReleaseTemporary", {
		typeof("UnityEngine.RenderTexture")
	}, {
		var_10_1
	})

	return var_10_0

def var_0_1.SetSpineUIOutline(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.GetShader("M02/Unlit Colored_Alpha_UI_Outline")
	local var_11_1 = GetComponent(arg_11_1, "SkeletonGraphic")
	local var_11_2 = Material.New(var_11_0)

	var_11_2.SetColor("_OutlineColor", arg_11_2)
	var_11_2.SetFloat("_OutlineWidth", 5.75)
	var_11_2.SetFloat("_ThresholdEnd", 0.2)

	var_11_1.material = var_11_2

def var_0_1.DelSpineUIOutline(arg_12_0, arg_12_1):
	GetComponent(arg_12_1, "SkeletonGraphic").material = None

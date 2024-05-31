local var_0_0 = class("LevelStageAtelierMaterialToast", import("view.base.BaseSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "LevelStageAtelierMaterialToast"

def var_0_0.OnInit(arg_2_0):
	return

def var_0_0.OnLoaded(arg_3_0):
	return

local var_0_1 = 26
local var_0_2 = 47
local var_0_3 = 196

def var_0_0.Play(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.contextData.settings

	setText(arg_4_0._tf.Find("Title"), var_4_0.title)

	local var_4_1 = arg_4_0._tf.Find("Desc")
	local var_4_2 = GetComponent(var_4_1, typeof(Text))
	local var_4_3 = WorldMediaCollectionFileDetailLayer.getTextPreferredHeight(var_4_2, var_4_1.rect.width, var_4_0.desc)
	local var_4_4 = 2

	while var_4_3 > var_0_1 + var_0_2 * (var_4_4 - 1):
		var_4_4 = var_4_4 + 1

	CustomIndexLayer.Clone2Full(arg_4_0._tf.Find("Lines"), var_4_4 + 1)
	setSizeDelta(arg_4_0._tf, {
		x = arg_4_0._tf.sizeDelta.x,
		y = var_0_3 + math.max(var_4_4 - 2, 0) * var_0_2
	})
	setText(var_4_1, var_4_0.desc)

	if var_4_0.icon:
		local var_4_5 = var_4_0.iconScale or 1

		LoadImageSpriteAtlasAsync("ui/ryzaicon_atlas", var_4_0.icon, arg_4_0._tf.Find("Image"))
		setLocalScale(arg_4_0._tf.Find("Image"), {
			x = var_4_5,
			y = var_4_5
		})

	if var_4_0.voice:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_4_0.voice)

	arg_4_0._go.transform.SetParent(pg.UIMgr.GetInstance().OverlayToast, False)
	GetComponent(arg_4_0._tf, typeof(DftAniEvent)).SetEndEvent(function()
		arg_4_0.Destroy()
		existCall(arg_4_1))

def var_0_0.OnDestroy(arg_6_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_6_0._tf)
	LeanTween.cancel(arg_6_0._go)

return var_0_0

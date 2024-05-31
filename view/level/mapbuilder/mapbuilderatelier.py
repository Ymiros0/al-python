local var_0_0 = class("MapBuilderAtelier", import(".MapBuilderNormal"))

def var_0_0.GetType(arg_1_0):
	return MapBuilder.TYPEATELIER

def var_0_0.ShowButtons(arg_2_0):
	var_0_0.super.ShowButtons(arg_2_0)

	local var_2_0 = GetSpriteFromAtlas("ui/levelmainscene_atlas", "btn_lianjin")

	setImageSprite(arg_2_0.sceneParent.actEliteBtn, var_2_0, True)

	local var_2_1 = arg_2_0.data.getConfig("type")

	setActive(arg_2_0.sceneParent.actAtelierBuffBtn, var_2_1 > Map.ACTIVITY_EASY)

def var_0_0.HideButtons(arg_3_0):
	local var_3_0 = GetSpriteFromAtlas("ui/levelmainscene_atlas", "btn_elite")

	setImageSprite(arg_3_0.sceneParent.actEliteBtn, var_3_0, True)
	setActive(arg_3_0.sceneParent.actAtelierBuffBtn, False)
	var_0_0.super.HideButtons(arg_3_0)

return var_0_0

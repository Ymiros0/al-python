local var_0_0 = class("Dorm3dMemorySubView", import("view.base.BaseSubView"))

def var_0_0.OnLoaded(arg_1_0):
	local var_1_0 = arg_1_0._tf.Find("list/container")

	arg_1_0.itemList = UIItemList.New(var_1_0, var_1_0.Find("tpl"))

	arg_1_0.itemList.make(function(arg_2_0, arg_2_1, arg_2_2)
		arg_2_1 = arg_2_1 + 1

		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = arg_1_0.ids[arg_2_1]
			local var_2_1 = pg.dorm3D_recall[var_2_0]
			local var_2_2 = arg_1_0.unlockDic[var_2_1.story_id]

			setText(arg_2_2.Find("name"), var_2_2 and var_2_1.name or string.format("locked.%s", var_2_0))
			GetImageSpriteFromAtlasAsync(string.format("dorm3dmemory/%s_list", var_2_1.image), "", arg_2_2.Find("Image"))
			setImageAlpha(arg_2_2.Find("Image"), var_2_2 and 0.6 or 1)
			onToggle(arg_1_0, arg_2_2, function(arg_3_0)
				if arg_3_0:
					arg_1_0.UpdateDisplay(arg_2_1, var_2_0), SFX_PANEL))

	arg_1_0.rtInfo = arg_1_0._tf.Find("info")

def var_0_0.OnInit(arg_4_0):
	local var_4_0 = arg_4_0.contextData.apartment

	arg_4_0.unlockDic = var_4_0.talkDic

	setText(arg_4_0.rtInfo.Find("count"), string.format("<color=#285cfc>%d</color>/%d", table.getCount(arg_4_0.unlockDic), #var_4_0.getCollectConfig("recall_list")))

	arg_4_0.ids = var_4_0.getCollectConfig("recall_list")

	arg_4_0.itemList.align(#arg_4_0.ids)
	triggerToggle(arg_4_0.itemList.container.GetChild(0), True)

def var_0_0.UpdateDisplay(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_0.rtInfo.Find("content")
	local var_5_1 = pg.dorm3D_recall[arg_5_2]
	local var_5_2 = arg_5_0.unlockDic[var_5_1.story_id]

	GetImageSpriteFromAtlasAsync(string.format("dorm3dmemory/%s_info", var_5_1.image), "", var_5_0.Find("icon"))
	setImageAlpha(var_5_0.Find("icon"), var_5_2 and 1 or 0.25)
	setText(var_5_0.Find("icon/lock/Text"), "wait for unlock")
	setActive(var_5_0.Find("icon/lock"), not var_5_2)
	setActive(var_5_0.Find("icon/play"), var_5_2)
	onButton(arg_5_0, var_5_0.Find("icon/play"), function()
		arg_5_0.emit(Dorm3dCollectionMediator.DO_TALK, var_5_1.story_id), SFX_CONFIRM)
	setText(var_5_0.Find("pro/Text"), "is pro")
	setActive(var_5_0.Find("pro"), var_5_1.type == 2)
	setImageAlpha(var_5_0.Find("name/bg"), var_5_2 and 1 or 0)

	if var_5_2:
		setText(var_5_0.Find("name/number"), string.format("%02d.", arg_5_1))
		setText(var_5_0.Find("name/Text"), var_5_1.name)
		setText(var_5_0.Find("name/Text/en"), "ababababababab")
		setText(var_5_0.Find("desc"), var_5_1.desc)
	else
		setText(var_5_0.Find("name/number"), "")
		setText(var_5_0.Find("name/Text"), string.format("<color=#a9a9a9>locked.%s</color>", arg_5_2))
		setText(var_5_0.Find("name/Text/en"), "")
		setText(var_5_0.Find("desc"), var_5_1.unlock)

def var_0_0.OnDestroy(arg_7_0):
	return

return var_0_0

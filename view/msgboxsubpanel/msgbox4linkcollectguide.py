local var_0_0 = class("Msgbox4LinkCollectGuide", import(".MsgboxSubPanel"))

var_0_0.SHOW_TYPE_NORMAL = 1
var_0_0.SHOW_TYPE_LIMIT = 2
var_0_0.SKIP_TYPE_SCENE = 2
var_0_0.SKIP_TYPE_ACTIVITY = 3

def var_0_0.getUIName(arg_1_0):
	return "Msgbox4LinkCollectGuide"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.title = arg_2_0.findTF("name_mask/name")
	arg_2_0.owner = arg_2_0.findTF("owner")

	setText(arg_2_0.findTF("title", arg_2_0.owner), i18n("collect_page_got"))

	arg_2_0.ownerLimit = arg_2_0.findTF("owner_limit")

	setText(arg_2_0.findTF("title", arg_2_0.ownerLimit), i18n("collect_page_got"))

	arg_2_0.iconTF = arg_2_0.findTF("left/IconTpl")
	arg_2_0.ownTF = arg_2_0.findTF("left/own")
	arg_2_0.detailTF = arg_2_0.findTF("left/detail")
	arg_2_0.desc = arg_2_0.findTF("content/desc")
	arg_2_0.list = arg_2_0.findTF("content/skipable_list")
	arg_2_0.tpl = arg_2_0.findTF("tpl", arg_2_0.list)

def var_0_0.OnRefresh(arg_3_0, arg_3_1):
	arg_3_0.SetWindowSize(Vector2(930, 540))
	setActive(arg_3_0.viewParent._btnContainer, False)

	local var_3_0 = Drop.New({
		type = arg_3_1.drop_type,
		id = arg_3_1.drop_id
	})

	updateDrop(arg_3_0.iconTF, var_3_0)
	UpdateOwnDisplay(arg_3_0.ownTF, var_3_0)
	RegisterDetailButton(arg_3_0.viewParent, arg_3_0.detailTF, var_3_0)

	local var_3_1 = var_3_0.cfg

	changeToScrollText(arg_3_0.title, var_3_1.name)
	setText(arg_3_0.desc, var_3_0.desc)

	if arg_3_1.show_type == var_0_0.SHOW_TYPE_NORMAL:
		setActive(arg_3_0.owner, True)
		setActive(arg_3_0.ownerLimit, False)
		setText(arg_3_0.findTF("Text", arg_3_0.owner), arg_3_1.count)
	elif arg_3_1.show_type == var_0_0.SHOW_TYPE_LIMIT:
		setActive(arg_3_0.owner, False)
		setActive(arg_3_0.ownerLimit, True)
		setText(arg_3_0.findTF("Text", arg_3_0.ownerLimit), arg_3_1.count .. "/" .. (arg_3_1.count_limit or 0))

	UIItemList.StaticAlign(arg_3_0.list, arg_3_0.tpl, #arg_3_1.skipable_list, function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventUpdate:
			local var_4_0 = arg_3_1.skipable_list[arg_4_1 + 1]
			local var_4_1 = var_4_0[1]
			local var_4_2 = var_4_0[2]
			local var_4_3 = var_4_0[3]

			changeToScrollText(arg_3_0.findTF("mask/title", arg_4_2), var_4_3)

			local var_4_4 = arg_3_0.findTF("skip_btn", arg_4_2)

			onButton(arg_3_0, var_4_4, function()
				if var_4_1 == var_0_0.SKIP_TYPE_SCENE:
					pg.m02.sendNotification(GAME.GO_SCENE, var_4_2[1], var_4_2[2] or {})
				elif var_4_1 == var_0_0.SKIP_TYPE_ACTIVITY:
					pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
						id = var_4_2
					})

				arg_3_0.viewParent.hide(), SFX_PANEL)
			Canvas.ForceUpdateCanvases())

return var_0_0

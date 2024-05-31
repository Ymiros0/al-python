local var_0_0 = class("PtAwardWindow")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0.binder = arg_1_2
	arg_1_0.scrollPanel = arg_1_0._tf.Find("window/panel")
	arg_1_0.UIlist = UIItemList.New(arg_1_0._tf.Find("window/panel/list"), arg_1_0._tf.Find("window/panel/list/item"))
	arg_1_0.ptTF = arg_1_0._tf.Find("window/pt")
	arg_1_0.totalTxt = arg_1_0._tf.Find("window/pt/Text").GetComponent(typeof(Text))
	arg_1_0.totalTitleTxt = arg_1_0._tf.Find("window/pt/title").GetComponent(typeof(Text))
	arg_1_0.totalTitleIcon = arg_1_0._tf.Find("window/pt/icon/image").GetComponent(typeof(Image))
	arg_1_0.closeBtn = arg_1_0._tf.Find("window/top/btnBack")
	arg_1_0.ptIcon = arg_1_0._tf.Find("window/pt/icon")

	onButton(arg_1_0.binder, arg_1_0._tf, function()
		arg_1_0.Hide(), SFX_PANEL)
	onButton(arg_1_0.binder, arg_1_0.closeBtn, function()
		arg_1_0.Hide(), SFX_PANEL)

def var_0_0.UpdateList(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4):
	assert(#arg_4_1 == #arg_4_2)
	arg_4_0.UIlist.make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate:
			local var_5_0 = arg_4_1[arg_5_1 + 1]
			local var_5_1 = arg_4_2[arg_5_1 + 1]
			local var_5_2 = GetPerceptualSize(arg_4_0.resTitle)

			setText(arg_5_2.Find("title/Text"), "PHASE " .. arg_5_1 + 1)
			setText(arg_5_2.Find("target/Text"), var_5_1)

			if arg_5_2.Find("target/icon"):
				if arg_4_0.resIcon == "":
					arg_4_0.resIcon = None

				if arg_4_0.resIcon:
					LoadImageSpriteAsync(arg_4_0.resIcon, arg_5_2.Find("target/icon"), False)

				setActive(arg_5_2.Find("target/icon"), arg_4_0.resIcon)
				setActive(arg_5_2.Find("target/mark"), arg_4_0.resIcon)

			setText(arg_5_2.Find("target/title"), arg_4_0.resTitle)

			local var_5_3 = Drop.Create(var_5_0)

			updateDrop(arg_5_2.Find("award"), var_5_3, {
				hideName = True
			})
			onButton(arg_4_0.binder, arg_5_2.Find("award"), function()
				arg_4_0.binder.emit(BaseUI.ON_DROP, var_5_3), SFX_PANEL)
			setActive(arg_5_2.Find("award/mask"), arg_5_1 + 1 <= arg_4_3)

			if not IsNil(arg_5_2.Find("mask")):
				if arg_4_4:
					local var_5_4 = pg.TimeMgr.GetInstance()
					local var_5_5 = arg_4_4[arg_5_1 + 1]

					setActive(arg_5_2.Find("mask"), var_5_5 > var_5_4.GetServerTime())

					local var_5_6 = var_5_4.STimeDescS(var_5_5, "%m")
					local var_5_7 = var_5_4.STimeDescS(var_5_5, "%d")

					setText(arg_5_2.Find("mask/Text"), i18n("unlock_date_tip", var_5_6, var_5_7))
				else
					setActive(arg_5_2.Find("mask"), False))
	arg_4_0.UIlist.align(#arg_4_1)
	scrollTo(arg_4_0.scrollPanel, 0, 1 - arg_4_3 * 166 / (#arg_4_2 * 166 + 20 - 570))

def var_0_0.Show(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.dropList
	local var_7_1 = arg_7_1.targets
	local var_7_2 = arg_7_1.level
	local var_7_3 = arg_7_1.count
	local var_7_4 = arg_7_1.resId
	local var_7_5 = arg_7_1.type
	local var_7_6 = arg_7_1.unlockStamps

	arg_7_0.resIcon = None

	arg_7_0.UpdateTitle(var_7_5)
	arg_7_0.updateResIcon(arg_7_1.resId, arg_7_1.resIcon, arg_7_1.type)
	arg_7_0.UpdateList(var_7_0, var_7_1, var_7_2, var_7_6)

	arg_7_0.totalTxt.text = var_7_3
	arg_7_0.totalTitleTxt.text = arg_7_0.cntTitle

	Canvas.ForceUpdateCanvases()
	setActive(arg_7_0._tf, True)

def var_0_0.UpdateTitle(arg_8_0, arg_8_1):
	local var_8_0 = ""

	if arg_8_1 == 2:
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("pt_cosume", var_8_0), i18n("pt_total_count", i18n("pt_cosume", var_8_0))
		arg_8_0.cntTitle = string.gsub(arg_8_0.cntTitle, "：", "")
	elif arg_8_1 == 3:
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("pt_ship_goal"), i18n("pt_ship_now")
	elif arg_8_1 == 4:
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("cumulative_victory_target_tip"), i18n("cumulative_victory_now_tip")
	elif arg_8_1 == 5:
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("npcfriendly_count"), i18n("npcfriendly_total_count")
	elif arg_8_1 == 6:
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("activity_yanhua_tip2"), i18n("activity_yanhua_tip3")
	else
		arg_8_0.resTitle, arg_8_0.cntTitle = i18n("target_get_tip"), i18n("pt_total_count", var_8_0)
		arg_8_0.cntTitle = string.gsub(arg_8_0.cntTitle, "：", "")

def var_0_0.updateResIcon(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	if arg_9_3 == 2 or arg_9_3 != 3 and arg_9_3 != 4 and arg_9_3 != 5 and arg_9_3 != 6:
		if arg_9_1:
			arg_9_0.resIcon = Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = arg_9_1
			}).getIcon()
		elif arg_9_2:
			arg_9_0.resIcon = arg_9_2

		if arg_9_0.ptIcon and arg_9_0.resIcon and arg_9_0.resIcon != "":
			setActive(arg_9_0.ptIcon, True)
			LoadImageSpriteAsync(arg_9_0.resIcon, arg_9_0.totalTitleIcon, False)
		else
			setActive(arg_9_0.ptIcon, False)

def var_0_0.Hide(arg_10_0):
	setActive(arg_10_0._tf, False)

def var_0_0.Dispose(arg_11_0):
	arg_11_0.Hide()
	removeOnButton(arg_11_0._tf)
	removeOnButton(arg_11_0.closeBtn)

return var_0_0

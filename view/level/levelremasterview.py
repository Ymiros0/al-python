local var_0_0 = class("LevelRemasterView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "LevelRemasterView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.content = arg_2_0.findTF("list/content")
	arg_2_0.item = arg_2_0.content.Find("item")
	arg_2_0.numsTxt = arg_2_0.findTF("nums/text")
	arg_2_0.helpBtn = arg_2_0.findTF("help")

	setActive(arg_2_0.item, False)

	arg_2_0.getRemasterTF = arg_2_0.findTF("getBtn/state_before")
	arg_2_0.gotRemasterTF = arg_2_0.findTF("getBtn/state_after")
	arg_2_0.exToggle = arg_2_0.findTF("toggles/EX")
	arg_2_0.spToggle = arg_2_0.findTF("toggles/SP")

	arg_2_0.bind(LevelUIConst.FLUSH_REMASTER_INFO, function(arg_3_0)
		if not arg_2_0.isShowing():
			return

		arg_2_0.flushOnly())
	arg_2_0.bind(LevelUIConst.FLUSH_REMASTER_TICKET, function(arg_4_0)
		if not arg_2_0.isShowing():
			return

		arg_2_0.updateTicketDisplay())

	local var_2_0 = getProxy(ChapterProxy)
	local var_2_1 = pg.TimeMgr.GetInstance()

	arg_2_0.itemList = UIItemList.New(arg_2_0.content, arg_2_0.item)

	arg_2_0.itemList.make(function(arg_5_0, arg_5_1, arg_5_2)
		arg_5_1 = arg_5_1 + 1

		if arg_5_0 == UIItemList.EventUpdate:
			local var_5_0 = arg_2_0.temp[arg_5_1]

			setActive(arg_5_2.Find("right"), arg_5_1 % 2 > 0)

			local var_5_1 = arg_5_2.Find("bg/icon")
			local var_5_2 = arg_5_2.Find("bg/lock")
			local var_5_3 = arg_5_2.Find("bg/wait")
			local var_5_4 = arg_5_2.Find("bg/tip")

			setActive(var_5_1, False)
			setActive(var_5_2, False)
			setActive(var_5_3, False)
			setActive(var_5_4, False)

			if not var_5_0:
				setActive(var_5_3, True)
				onButton(arg_2_0, var_5_3, function()
					pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_remaster_do_not_open")), SFX_PANEL)
			elif not var_2_1.inTime(var_5_0.time):
				setActive(var_5_2, True)
				onButton(arg_2_0, var_5_2, function()
					pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_remaster_do_not_open")), SFX_PANEL)
			else
				setActive(var_5_1, True)
				GetImageSpriteFromAtlasAsync("activitybanner/" .. var_5_0.bg, "", var_5_1)

				local var_5_5 = var_5_1.Find("info")

				setText(var_5_5.Find("dec1/index"), arg_5_1 < 10 and "0" .. arg_5_1 or arg_5_1)

				local var_5_6 = 0

				for iter_5_0, iter_5_1 in ipairs(var_5_0.config_data):
					if var_2_0.getChapterById(iter_5_1).isClear():
						var_5_6 = math.max(var_5_6, var_5_0.chapter_progress[iter_5_0])

				setText(var_5_5.Find("progress/Text"), var_5_6 .. "%")
				onButton(arg_2_0, var_5_1, function()
					local var_8_0 = (function()
						local var_9_0 = pg.chapter_template[var_5_0.config_data[1]].map

						for iter_9_0, iter_9_1 in ipairs({
							PlayerPrefs.GetInt("remaster_lastmap_" .. var_5_0.id, var_9_0),
							var_9_0
						}):
							if var_2_0.getMapById(iter_9_1).isUnlock():
								return iter_9_1)()

					if var_8_0:
						arg_2_0.onSelectMap(var_8_0)
						arg_2_0.Hide(), SFX_PANEL)

				local var_5_7

				for iter_5_2, iter_5_3 in ipairs(var_5_0.drop_gain):
					if #iter_5_3 > 0 and var_2_0.remasterInfo[iter_5_3[1]][iter_5_2].receive == False:
						var_5_7 = {
							iter_5_2,
							iter_5_3
						}

						break

				local var_5_8 = underscore.rest(var_5_0.drop_display, 1)

				if var_5_7:
					table.insert(var_5_8, 1, var_5_7)
				elif #var_5_0.drop_display_sp > 0:
					var_5_8 = table.mergeArray(var_5_0.drop_display_sp, var_5_8)

				local var_5_9 = var_5_5.Find("content")

				eachChild(var_5_9, function(arg_10_0)
					setActive(arg_10_0, False))

				for iter_5_4, iter_5_5 in ipairs(var_5_8):
					local var_5_10 = iter_5_4 > var_5_9.childCount and cloneTplTo(var_5_9.GetChild(0), var_5_9) or var_5_9.GetChild(iter_5_4 - 1)

					setActive(var_5_10, True)

					if var_5_7 and iter_5_4 == 1:
						local var_5_11 = var_5_7[1]
						local var_5_12, var_5_13, var_5_14, var_5_15 = unpack(var_5_7[2])
						local var_5_16 = var_2_0.remasterInfo[var_5_12][var_5_11]

						setActive(var_5_4, var_5_15 <= var_5_16.count)
						setActive(var_5_10.Find("mark"), var_5_15 > var_5_16.count)
						setActive(var_5_10.Find("Slider"), var_5_15 > var_5_16.count)
						setActive(var_5_10.Find("achieve"), var_5_15 <= var_5_16.count)
						setSlider(var_5_10.Find("Slider"), 0, var_5_15, var_5_16.count)

						local var_5_17 = {
							type = var_5_13,
							id = var_5_14
						}

						updateDrop(var_5_10.Find("IconTpl"), var_5_17)
						onButton(arg_2_0, var_5_10.Find("IconTpl"), function()
							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								hideYes = True,
								hideNo = True,
								type = MSGBOX_TYPE_SINGLE_ITEM,
								drop = var_5_17,
								weight = LayerWeightConst.TOP_LAYER,
								remaster = {
									word = i18n("level_remaster_tip4", pg.chapter_template[var_5_12].chapter_name),
									number = var_5_16.count .. "/" .. var_5_15,
									btn_text = i18n(var_5_16.count < var_5_15 and "level_remaster_tip2" or "level_remaster_tip3"),
									def btn_call:()
										if var_5_16.count < var_5_15:
											local var_12_0 = pg.chapter_template[var_5_12].map
											local var_12_1, var_12_2 = var_2_0.getMapById(var_12_0).isUnlock()

											if not var_12_1:
												pg.TipsMgr.GetInstance().ShowTips(var_12_2)
											else
												arg_2_0.onSelectMap(var_12_0)
												arg_2_0.Hide()
										else
											arg_2_0.emit(LevelMediator2.ON_CHAPTER_REMASTER_AWARD, var_5_12, var_5_11)
								}
							}), SFX_PANEL)
					else
						local var_5_18 = {
							type = iter_5_5[1][1],
							id = iter_5_5[1][2]
						}

						updateDrop(var_5_10.Find("IconTpl"), var_5_18)
						onButton(arg_2_0, var_5_10.Find("IconTpl"), function()
							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								hideYes = True,
								hideNo = True,
								type = MSGBOX_TYPE_SINGLE_ITEM,
								drop = var_5_18,
								weight = LayerWeightConst.TOP_LAYER,
								remaster = {
									word = i18n("level_remaster_tip1") .. iter_5_5[2],
									btn_text = i18n("text_confirm")
								}
							}), SFX_PANEL)
						setActive(var_5_10.Find("mark"), False)
						setActive(var_5_10.Find("Slider"), False)
						setActive(var_5_10.Find("achieve"), False))
	onButton(arg_2_0, arg_2_0.getRemasterTF, function()
		if var_2_0.remasterTickets + pg.gameset.reactivity_ticket_daily.key_value > pg.gameset.reactivity_ticket_max.key_value:
			local var_14_0 = {
				content = i18n("tack_tickets_max_warning", math.max(pg.gameset.reactivity_ticket_max.key_value - var_2_0.remasterTickets, 0)),
				def onYes:()
					arg_2_0.emit(LevelMediator2.ON_CLICK_RECEIVE_REMASTER_TICKETS_BTN)
			}

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_14_0)

			return

		arg_2_0.emit(LevelMediator2.ON_CLICK_RECEIVE_REMASTER_TICKETS_BTN), SFX_PANEL)

def var_0_0.OnDestroy(arg_16_0):
	arg_16_0.onItem = None

	if arg_16_0.isShowing():
		arg_16_0.Hide()

def var_0_0.Show(arg_17_0):
	var_0_0.super.Show(arg_17_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_17_0._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.Hide(arg_18_0):
	var_0_0.super.Hide(arg_18_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_18_0._tf, arg_18_0._parentTf)

def var_0_0.set(arg_19_0, arg_19_1, arg_19_2):
	arg_19_0.templates = {}

	for iter_19_0, iter_19_1 in ipairs(pg.re_map_template.all):
		local var_19_0 = pg.re_map_template[iter_19_1]

		table.insert(arg_19_0.templates, var_19_0)

	arg_19_0.onSelectMap = arg_19_1

	arg_19_0.flush(arg_19_2)

def var_0_0.flush(arg_20_0, arg_20_1):
	onButton(arg_20_0, arg_20_0._tf.Find("bg"), function()
		arg_20_0.Hide(), SFX_CANCEL)
	onButton(arg_20_0, arg_20_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("levelScene_remaster_help_tip")
		}), SFX_PANEL)
	arg_20_0.updateTicketDisplay()

	local var_20_0 = {
		arg_20_0.exToggle,
		arg_20_0.spToggle
	}
	local var_20_1 = getProxy(ChapterProxy)

	for iter_20_0, iter_20_1 in ipairs(var_20_0):
		onToggle(arg_20_0, iter_20_1, function(arg_23_0)
			if arg_23_0:
				arg_20_0.temp = underscore.filter(arg_20_0.templates, function(arg_24_0)
					return arg_24_0.activity_type == iter_20_0)

				table.sort(arg_20_0.temp, CompareFuncs({
					function(arg_25_0)
						for iter_25_0, iter_25_1 in ipairs(arg_25_0.drop_gain):
							if #iter_25_1 > 0:
								local var_25_0, var_25_1, var_25_2, var_25_3 = unpack(iter_25_1)
								local var_25_4 = var_20_1.remasterInfo[var_25_0][iter_25_0]

								if not var_25_4.receive and var_25_3 <= var_25_4.count:
									return 0

						return 1,
					function(arg_26_0)
						return arg_26_0.order
				}))
				arg_20_0.itemList.align(math.max(math.ceil(#arg_20_0.temp / 2) * 2, 4)), SFX_PANEL)

	triggerToggle(var_20_0[arg_20_1 and 2 or 1], True)

def var_0_0.flushOnly(arg_27_0):
	arg_27_0.itemList.align(math.max(math.ceil(#arg_27_0.temp / 2) * 2, 4))

def var_0_0.updateTicketDisplay(arg_28_0):
	local var_28_0 = getProxy(ChapterProxy)
	local var_28_1 = var_28_0.remasterDailyCount > 0

	SetActive(arg_28_0.getRemasterTF, not var_28_1)
	SetActive(arg_28_0.gotRemasterTF, var_28_1)
	setText(arg_28_0.numsTxt, var_28_0.remasterTickets .. "/" .. pg.gameset.reactivity_ticket_max.key_value)

return var_0_0

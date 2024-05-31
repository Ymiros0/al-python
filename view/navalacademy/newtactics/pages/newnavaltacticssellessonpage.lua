﻿local var_0_0 = class("NewNavalTacticsSelLessonPage", import("....base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "NewNavalTacticsLessonPage"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.skillPanel = arg_2_0:findTF("skill")
	arg_2_0.cancelBtn = arg_2_0:findTF("cancel_btn")
	arg_2_0.confirmBtn = arg_2_0:findTF("confirm_btn")
	arg_2_0.toggleGroup = arg_2_0:findTF("items"):GetComponent(typeof(ToggleGroup))
	arg_2_0.lessonNameTxt = arg_2_0:findTF("introl/name"):GetComponent(typeof(Text))
	arg_2_0.lessonDescTxt = arg_2_0:findTF("introl/desc"):GetComponent(typeof(Text))
	arg_2_0.lessonExpTxt = arg_2_0:findTF("introl/exp_Text"):GetComponent(typeof(Text))
	arg_2_0.lessonTimeTxt = arg_2_0:findTF("introl/timer_Text"):GetComponent(typeof(Text))
	arg_2_0.skillCard = NewNavalTacticsAdditionSkillCard.New(arg_2_0:findTF("skill/info"))
	arg_2_0.itemTpls = {
		arg_2_0:findTF("items/scorll/content/item")
	}
	arg_2_0.startPos = arg_2_0.itemTpls[1].anchoredPosition
	arg_2_0.space = Vector2(60, 30)
	arg_2_0.cloumnCnt = 6

	setText(arg_2_0:findTF("introl/exp_label"), i18n("tactics_class_get_exp"))
	setText(arg_2_0:findTF("introl/timer_label"), i18n("tactics_class_spend_time"))
	setText(arg_2_0.confirmBtn:Find("Image"), i18n("tactics_class_start"))
	setText(arg_2_0.cancelBtn:Find("Image"), i18n("tactics_class_cancel"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Cancel()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if not arg_3_0.selLessonId or not arg_3_0.spendTime then
			return
		end

		arg_3_0.student:setLesson(arg_3_0.selLessonId)
		arg_3_0.student:setTime(arg_3_0.spendTime)
		arg_3_0:emit(NewNavalTacticsLayer.ON_LESSON_SELECTED, arg_3_0.student)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.skillPanel, function()
		if not arg_3_0.canBack then
			return
		end

		arg_3_0:emit(NewNavalTacticsLayer.ON_RESEL_SKILL, arg_3_0.student)
	end, SFX_PANEL)
end

function var_0_0.SetHideCallback(arg_7_0, arg_7_1)
	arg_7_0.hideCallback = arg_7_1
end

function var_0_0.Show(arg_8_0, arg_8_1, arg_8_2)
	var_0_0.super.Show(arg_8_0)

	arg_8_0.canBack = defaultValue(arg_8_2, true)

	pg.UIMgr.GetInstance():BlurPanel(arg_8_0._tf)

	if arg_8_1 ~= arg_8_0.student then
		arg_8_0.selLessonId = nil
		arg_8_0.spendTime = nil
		arg_8_0.student = arg_8_1

		arg_8_0:Flush()
	else
		arg_8_0:Flush()
	end
end

function var_0_0.Cancel(arg_9_0)
	arg_9_0:emit(NewNavalTacticsMediator.ON_CANCEL_ADD_STUDENT)
end

function var_0_0.Hide(arg_10_0)
	var_0_0.super.Hide(arg_10_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_10_0._tf, pg.UIMgr.GetInstance().UIMain)

	if arg_10_0.hideCallback then
		arg_10_0.hideCallback()

		arg_10_0.hideCallback = nil
	end
end

function var_0_0.Flush(arg_11_0)
	local var_11_0 = arg_11_0.student
	local var_11_1 = getProxy(BayProxy):RawGetShipById(var_11_0.shipId)
	local var_11_2 = var_11_0:getSkillId(var_11_1)

	arg_11_0:UpdateLessons(var_11_2, var_11_1)
end

function var_0_0.GetLessons(arg_12_0)
	local var_12_0 = getProxy(BagProxy):getItemsByType(Item.LESSON_TYPE)

	table.sort(var_12_0, function(arg_13_0, arg_13_1)
		local var_13_0 = arg_13_0:getConfig("rarity")
		local var_13_1 = arg_13_1:getConfig("rarity")

		if var_13_0 == var_13_1 then
			return arg_13_0.id < arg_13_1.id
		else
			return var_13_1 < var_13_0
		end
	end)

	return var_12_0
end

function var_0_0.UpdateLessons(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0 = arg_14_0:GetLessons()

	for iter_14_0 = 1, #var_14_0 do
		local var_14_1 = arg_14_0.itemTpls[iter_14_0]

		if not var_14_1 then
			local var_14_2 = arg_14_0.itemTpls[1]

			var_14_1 = Object.Instantiate(var_14_2.gameObject, var_14_2.parent).transform
			arg_14_0.itemTpls[iter_14_0] = var_14_1
		end

		setActive(var_14_1, true)
		arg_14_0:UpdateLesson(var_14_1, var_14_0[iter_14_0], arg_14_1, arg_14_2)
	end

	for iter_14_1 = #arg_14_0.itemTpls, #var_14_0 + 1, -1 do
		setActive(arg_14_0.itemTpls[iter_14_1], false)
	end

	if #var_14_0 > 0 then
		arg_14_0.toggleGroup:SetAllTogglesOff()
		triggerToggle(arg_14_0.itemTpls[1], true)
	end
end

function var_0_0.UpdateLesson(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4)
	updateItem(arg_15_1, Item.New({
		id = arg_15_2.id,
		count = arg_15_2.count
	}))
	setText(arg_15_1:Find("icon_bg/count"), arg_15_2.count)

	local var_15_0 = Item.getConfigData(arg_15_2.id)
	local var_15_1 = var_15_0.usage_arg[1]
	local var_15_2 = 100

	if pg.skill_data_template[arg_15_3].type == var_15_0.usage_arg[3] then
		var_15_2 = var_15_2 + var_15_0.usage_arg[4]
	end

	local var_15_3 = var_15_0.usage_arg[2] * (var_15_2 / 100)

	onToggle(arg_15_0, arg_15_1, function(arg_16_0)
		if arg_16_0 then
			arg_15_0.selLessonId = arg_15_2.id
			arg_15_0.spendTime = var_15_1

			arg_15_0:UpdateLessonDesc(arg_15_2.id, var_15_3, var_15_1)
			arg_15_0:UpdateSkill(arg_15_3, var_15_3, arg_15_4)
		end
	end, SFX_PANEL)

	local var_15_4 = var_15_2 == 100 and "" or "EXP" .. var_15_2 .. "%"

	setText(arg_15_1:Find("addition"), var_15_4)
end

function var_0_0.UpdatePosition(arg_17_0, arg_17_1, arg_17_2)
	local var_17_0 = math.ceil(arg_17_2 / arg_17_0.cloumnCnt)
	local var_17_1 = arg_17_2 % arg_17_0.cloumnCnt

	if var_17_1 == 0 then
		var_17_1 = arg_17_0.cloumnCnt
	end

	local var_17_2 = arg_17_0.startPos.y - (var_17_0 - 1) * (arg_17_1.sizeDelta.y + arg_17_0.space.y)
	local var_17_3 = arg_17_0.startPos.x + (var_17_1 - 1) * (arg_17_1.sizeDelta.x + arg_17_0.space.x)

	arg_17_1.anchoredPosition = Vector2(var_17_3, var_17_2)
end

function var_0_0.UpdateLessonDesc(arg_18_0, arg_18_1, arg_18_2, arg_18_3)
	local var_18_0 = Item.getConfigData(arg_18_1)

	arg_18_0.lessonNameTxt.text = var_18_0.name .. "   -"
	arg_18_0.lessonDescTxt.text = var_18_0.display
	arg_18_0.lessonExpTxt.text = arg_18_2
	arg_18_0.lessonTimeTxt.text = pg.TimeMgr.GetInstance():DescCDTime(arg_18_3)
end

function var_0_0.UpdateSkill(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	local var_19_0 = ShipSkill.New(arg_19_3.skills[arg_19_1], arg_19_3.id)

	arg_19_0.skillCard:Update(var_19_0, arg_19_2)
end

function var_0_0.OnDestroy(arg_20_0)
	if arg_20_0:isShowing() then
		arg_20_0:Hide()
	end

	arg_20_0.skillCard:Dispose()

	arg_20_0.skillCard = nil
end

return var_0_0

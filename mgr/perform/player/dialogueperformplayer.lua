﻿local var_0_0 = class("DialoguePerformPlayer", import(".BasePerformPlayer"))

var_0_0.TYPEWRITE_SPEED = 0.05

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.eventTipBig = arg_1_0:findTF("event_tip", arg_1_0._tf)
	arg_1_0.content = arg_1_0:findTF("content", arg_1_0._tf)
	arg_1_0.image = arg_1_0:findTF("Image", arg_1_0.content)
	arg_1_0.nameTF = arg_1_0:findTF("name_bg", arg_1_0.content)
	arg_1_0.nameText = arg_1_0:findTF("name", arg_1_0.nameTF)
	arg_1_0.next = arg_1_0:findTF("next", arg_1_0.content)
	arg_1_0.eventTipSmall = arg_1_0:findTF("event_tip", arg_1_0.content)
	arg_1_0.text = arg_1_0:findTF("Text", arg_1_0.content)
	arg_1_0.text2 = arg_1_0:findTF("Text2", arg_1_0.content)
	arg_1_0.resultTF = arg_1_0:findTF("result", arg_1_0.content)
	arg_1_0.resultTpl = arg_1_0:findTF("tpl", arg_1_0.content)
end

function var_0_0.Play(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:checkName()
	arg_2_0:Show()

	local var_2_0 = arg_2_1.param[1]
	local var_2_1 = pg.child_word[var_2_0]

	assert(var_2_0 and var_2_1, "child_word not exist id: " .. var_2_0)
	setActive(arg_2_0.eventTipBig, arg_2_1.show_event == 1)

	if arg_2_1.show_event == 1 then
		onDelayTick(function()
			if arg_2_0._anim then
				arg_2_0._anim:Play()
			end

			arg_2_0:_play(arg_2_1, var_2_1, arg_2_2)
		end, 0.66)
	else
		setActive(arg_2_0.eventTipBig, false)

		if arg_2_0._anim then
			arg_2_0._anim:Play()
		end

		arg_2_0:_play(arg_2_1, var_2_1, arg_2_2)
	end
end

function var_0_0._play(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	setActive(arg_4_0.eventTipSmall, arg_4_1.show_event == 1)
	setActive(arg_4_0.next, arg_4_1.show_next == 1)

	arg_4_0.drops = arg_4_1.show_drops == 1 and arg_4_1.drops or {}

	local var_4_0 = arg_4_2.char_type ~= EducateConst.WORD_TYPE_CHILD
	local var_4_1 = arg_4_0.text

	setActive(arg_4_0.text, not var_4_0)
	setActive(arg_4_0.text2, var_4_0)
	setActive(arg_4_0.image, not var_4_0)

	if not var_4_0 then
		local var_4_2 = getProxy(EducateProxy):GetCharData():GetPaintingName()

		setImageSprite(arg_4_0.image, LoadSprite("storyicon/" .. var_4_2), true)
	end

	local var_4_3 = var_4_0 and arg_4_0.text2 or arg_4_0.text
	local var_4_4 = arg_4_2.word
	local var_4_5 = string.gsub(var_4_4, "$1", arg_4_0.callName)

	setText(var_4_3, var_4_5)

	local var_4_6 = GetComponent(var_4_3, typeof(Typewriter))

	if arg_4_2.char_type == EducateConst.WORD_TYPE_ASIDE then
		setActive(arg_4_0.nameTF, false)
	else
		setActive(arg_4_0.nameTF, true)

		local var_4_7 = ""

		if arg_4_2.char_type == EducateConst.WORD_TYPE_CHILD then
			var_4_7 = arg_4_0.name
		elseif arg_4_2.char_type == EducateConst.WORD_TYPE_PLAYER then
			var_4_7 = arg_4_0.playerName
		end

		setText(arg_4_0.nameText, var_4_7)
	end

	function var_4_6.endFunc()
		setActive(arg_4_0.resultTF, true)

		local var_5_0 = {}

		for iter_5_0 = 1, #arg_4_0.drops do
			table.insert(var_5_0, function(arg_6_0)
				arg_4_0.resultTF = arg_4_0:findTF("result", arg_4_0.content)
				arg_4_0.resultTpl = arg_4_0:findTF("tpl", arg_4_0.content)

				local var_6_0 = arg_4_0.drops[iter_5_0]
				local var_6_1 = iter_5_0 < arg_4_0.resultTF.childCount and arg_4_0.resultTF:GetChild(iter_5_0 - 1) or cloneTplTo(arg_4_0.resultTpl, arg_4_0.resultTF)

				if var_6_0.type == EducateConst.DROP_TYPE_BUFF then
					setActive(arg_4_0:findTF("icon", var_6_1), false)
					setText(arg_4_0:findTF("name", var_6_1), pg.child_buff[var_6_0.id].name)
					setText(arg_4_0:findTF("value", var_6_1), "")
				else
					setActive(arg_4_0:findTF("icon", var_6_1), true)
					EducateHelper.UpdateDropShowForAttr(var_6_1, var_6_0)
				end

				setActive(var_6_1, true)
				var_6_1:GetComponent(typeof(Animation)):Play("anim_educate_attr_in")
				onDelayTick(function()
					arg_6_0()
				end, 0.033)
			end)
		end

		seriesAsync(var_5_0, function()
			onDelayTick(function()
				setActive(arg_4_0.resultTF, false)
				eachChild(arg_4_0.resultTF, function(arg_10_0)
					setActive(arg_10_0, false)
				end)

				if arg_4_3 then
					arg_4_3()
				end
			end, 1)
		end)
	end

	var_4_6:setSpeed(var_0_0.TYPEWRITE_SPEED)
	var_4_6:Play()
end

function var_0_0.checkName(arg_11_0)
	if not arg_11_0.callName then
		arg_11_0.callName = getProxy(EducateProxy):GetCharData():GetCallName()
	end

	if not arg_11_0.name then
		arg_11_0.name = getProxy(EducateProxy):GetCharData():GetName()
	end

	if not arg_11_0.playerName then
		arg_11_0.playerName = getProxy(PlayerProxy):getRawData():GetName()
	end
end

function var_0_0.Clear(arg_12_0)
	setText(arg_12_0.text, "")
	setText(arg_12_0.text2, "")
	setActive(arg_12_0.eventTipBig, false)
	setActive(arg_12_0.eventTipSmall, false)
	arg_12_0:Hide()
end

return var_0_0

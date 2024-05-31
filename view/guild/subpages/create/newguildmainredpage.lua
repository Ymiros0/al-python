local var_0_0 = class("NewGuildMainRedPage", import("....base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "NewGuildRedUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.nameInput = findTF(arg_2_0._tf, "bg/frame/name_bg/input"):GetComponent(typeof(InputField))
	arg_2_0.manifestoInput = findTF(arg_2_0._tf, "bg/frame/policy_container/input_frame/input"):GetComponent(typeof(InputField))
	arg_2_0.relaxToggle = findTF(arg_2_0._tf, "bg/frame/policy_container/policy/relax")
	arg_2_0.powerToggle = findTF(arg_2_0._tf, "bg/frame/policy_container/policy/power")
	arg_2_0.cancelBtn = findTF(arg_2_0._tf, "bg/frame/cancel_btn")
	arg_2_0.confirmBtn = findTF(arg_2_0._tf, "bg/frame/confirm_btn")
	arg_2_0.costTF = findTF(arg_2_0._tf, "bg/frame/confirm_btn/print_container/Text"):GetComponent(typeof(Text))
end

function var_0_0.OnInit(arg_3_0)
	local var_3_0 = pg.gameset.create_guild_cost.key_value

	arg_3_0.costTF.text = var_3_0

	onInputChanged(arg_3_0, arg_3_0.nameInput, function()
		local var_4_0 = getInputText(arg_3_0.nameInput)
		local var_4_1, var_4_2 = wordVer(var_4_0, {
			isReplace = true
		})

		if var_4_1 > 0 then
			setInputText(arg_3_0.nameInput, var_4_2)
		end
	end)
	onInputChanged(arg_3_0, arg_3_0.manifestoInput, function()
		local var_5_0 = getInputText(arg_3_0.manifestoInput)
		local var_5_1, var_5_2 = wordVer(var_5_0, {
			isReplace = true
		})

		if var_5_1 > 0 then
			setInputText(arg_3_0.manifestoInput, var_5_2)
		end
	end)
	onToggle(arg_3_0, arg_3_0.relaxToggle, function(arg_6_0)
		if arg_6_0 then
			local var_6_0 = GuildConst.POLICY_TYPE_RELAXATION

			arg_3_0.newGuildVO:setPolicy(var_6_0)
		end
	end, SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.powerToggle, function(arg_7_0)
		if arg_7_0 then
			local var_7_0 = GuildConst.POLICY_TYPE_POWER

			arg_3_0.newGuildVO:setPolicy(var_7_0)
		end
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		if arg_3_0.onCancel then
			arg_3_0.onCancel()
		end
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		local var_9_0 = arg_3_0.nameInput.text

		arg_3_0.newGuildVO:setName(var_9_0)

		local var_9_1 = arg_3_0.manifestoInput.text
		local var_9_2 = wordVer(var_9_1)

		arg_3_0.newGuildVO:setManifesto(var_9_1)

		local var_9_3 = arg_3_0.newGuildVO:getName()

		if not var_9_3 or var_9_3 == "" then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_error_noname"))

			return
		end

		if not nameValidityCheck(var_9_3, 0, 20, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"login_newPlayerScene_name_tooLong",
			"err_name_existOtherChar"
		}) then
			return
		end

		if not arg_3_0.newGuildVO:getFaction() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_error_nofaction"))

			return
		end

		if not arg_3_0.newGuildVO:getPolicy() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_error_nopolicy"))

			return
		end

		local var_9_4 = arg_3_0.newGuildVO:getManifesto()

		if not var_9_4 or var_9_4 == "" then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_error_nomanifesto"))

			return
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("guild_create_confirm", var_3_0),
			onYes = function()
				if arg_3_0.playerVO:getTotalGem() < var_3_0 then
					GoShoppingMsgBox(i18n("switch_to_shop_tip_3", i18n("word_gem")), ChargeScene.TYPE_DIAMOND)
				else
					arg_3_0:emit(NewGuildMediator.CREATE, arg_3_0.newGuildVO)
				end
			end
		})
	end, SFX_CONFIRM)
end

function var_0_0.Show(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4)
	arg_11_0.playerVO = arg_11_2

	var_0_0.super.Show(arg_11_0)

	arg_11_0.onCancel = arg_11_4
	arg_11_0.newGuildVO = arg_11_1

	triggerToggle(arg_11_0.relaxToggle, true)

	local var_11_0 = GetOrAddComponent(arg_11_0._tf, "CanvasGroup")

	var_11_0.alpha = 0
	arg_11_0.isPlaying = true

	LeanTween.value(arg_11_0._go, 0, 1, 0.6):setOnUpdate(System.Action_float(function(arg_12_0)
		var_11_0.alpha = arg_12_0
	end)):setOnComplete(System.Action(function()
		arg_11_0.isPlaying = false

		arg_11_3()
	end)):setDelay(0.5)
	arg_11_0._tf:SetSiblingIndex(1)
end

function var_0_0.IsPlaying(arg_14_0)
	return arg_14_0.isPlaying
end

function var_0_0.OnDestroy(arg_15_0)
	return
end

return var_0_0

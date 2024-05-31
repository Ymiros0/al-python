﻿local var_0_0 = class("GuildTechnologyCard")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.view = arg_1_2

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0.titleImg = arg_1_0._tf:Find("title"):GetComponent(typeof(Text))
	arg_1_0.iconImag = arg_1_0._tf:Find("icon"):GetComponent(typeof(Image))
	arg_1_0.levelTxt = arg_1_0._tf:Find("level"):GetComponent(typeof(Text))
	arg_1_0.descTxt = arg_1_0._tf:Find("desc"):GetComponent(typeof(Text))
	arg_1_0.upgradeTF = arg_1_0._tf:Find("upgrade")
	arg_1_0.guildRes = arg_1_0.upgradeTF:Find("cion")
	arg_1_0.guildResTxt = arg_1_0.upgradeTF:Find("cion/Text"):GetComponent(typeof(Text))
	arg_1_0.goldRes = arg_1_0.upgradeTF:Find("gold")
	arg_1_0.goldResTxt = arg_1_0.upgradeTF:Find("gold/Text"):GetComponent(typeof(Text))
	arg_1_0.upgradeBtn = arg_1_0.upgradeTF:Find("upgrade_btn")
	arg_1_0.maxTF = arg_1_0._tf:Find("max")
	arg_1_0.breakoutTF = arg_1_0._tf:Find("breakout")
	arg_1_0.breakoutSlider = arg_1_0._tf:Find("progress"):GetComponent(typeof(Slider))
	arg_1_0.breakoutTxt = arg_1_0._tf:Find("progress/Text"):GetComponent(typeof(Text))
	arg_1_0.livnessTF = arg_1_0.upgradeTF:Find("livness")

	setActive(arg_1_0.breakoutSlider.gameObject, false)
	setActive(arg_1_0.upgradeTF, false)
	setActive(arg_1_0.maxTF, false)
	setActive(arg_1_0.breakoutTF, false)
end

function var_0_0.Update(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_1.group.id
	local var_2_1 = arg_2_1:getConfig("name")

	arg_2_0.titleImg.text = var_2_1
	arg_2_0.iconImag.sprite = GetSpriteFromAtlas("GuildTechnology", var_2_0)

	local var_2_2 = arg_2_1:GetMaxLevel()
	local var_2_3 = arg_2_1:GetLevel()
	local var_2_4 = arg_2_1.group:GetFakeLevel()
	local var_2_5 = math.max(var_2_2, var_2_4)

	if arg_2_1:IsGuildMember() then
		arg_2_0.levelTxt.text = "Lv." .. var_2_3
	else
		local var_2_6 = string.format(" [%s+%s]", var_2_2, math.max(0, var_2_4 - var_2_2))

		arg_2_0.levelTxt.text = "Lv." .. var_2_3 .. "/" .. var_2_5 .. var_2_6
	end

	arg_2_0.descTxt.text = arg_2_1:GetDesc()

	setActive(arg_2_0.maxTF, var_2_5 <= var_2_3)
	setActive(arg_2_0.upgradeTF, var_2_3 < var_2_5)

	local var_2_7 = arg_2_1:_ReachTargetLiveness_()
	local var_2_8 = arg_2_1:CanUpgrade()

	removeOnButton(arg_2_0._tf)

	if var_2_8 then
		var_2_7 = true

		local var_2_9, var_2_10 = arg_2_1:GetConsume()

		arg_2_0.guildResTxt.text = var_2_9
		arg_2_0.goldResTxt.text = var_2_10

		onButton(arg_2_0, arg_2_0._tf, function()
			if var_2_3 >= var_2_5 then
				return
			end

			arg_2_0:DoUprade(arg_2_1)
		end, SFX_PANEL)
	elseif not var_2_7 then
		setText(arg_2_0.livnessTF, i18n("guild_tech_livness_no_enough_label", arg_2_1:GetTargetLivness()))
	end

	setActive(arg_2_0.guildRes, var_2_7)
	setActive(arg_2_0.goldRes, var_2_7)
	setActive(arg_2_0.upgradeBtn, var_2_7)
	setActive(arg_2_0.livnessTF, not var_2_7)

	local var_2_11 = arg_2_2 and arg_2_2.id == var_2_0

	setActive(arg_2_0.breakoutSlider.gameObject, var_2_11)

	if var_2_11 then
		local var_2_12 = arg_2_2:GetTargetProgress()
		local var_2_13 = arg_2_2:GetProgress()

		arg_2_0.breakoutSlider.value = var_2_13 / var_2_12
		arg_2_0.breakoutTxt.text = var_2_13 .. "/" .. var_2_12
	end
end

function var_0_0.DoUprade(arg_4_0, arg_4_1)
	local function var_4_0()
		local var_5_0 = arg_4_1:getConfig("name")
		local var_5_1, var_5_2 = arg_4_1:GetConsume()

		pg.MsgboxMgr:GetInstance():ShowMsgBox({
			content = i18n("guild_tech_consume_tip", var_5_1, var_5_2, var_5_0),
			onYes = function()
				arg_4_0.view:emit(GuildTechnologyMediator.ON_UPGRADE, arg_4_1.group.id)
			end
		})
	end

	local function var_4_1(arg_7_0)
		if arg_4_1:IsRiseInPrice() then
			local var_7_0, var_7_1, var_7_2 = arg_4_1:CanUpgradeBySelf()
			local var_7_3 = i18n("guild_tech_price_inc_tip")

			if var_7_2 and not var_7_1 then
				local var_7_4 = arg_4_1:GetLivenessOffset()

				var_7_3 = i18n("guild_tech_livness_no_enough", var_7_4)
			end

			pg.MsgboxMgr:GetInstance():ShowMsgBox({
				content = var_7_3,
				onYes = arg_7_0
			})
		else
			arg_7_0()
		end
	end

	seriesAsync({
		function(arg_8_0)
			var_4_1(arg_8_0)
		end,
		function(arg_9_0)
			var_4_0()
		end
	})
end

function var_0_0.Destroy(arg_10_0)
	pg.DelegateInfo.Dispose(arg_10_0)
end

return var_0_0

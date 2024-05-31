﻿local var_0_0 = class("BackYardShipCard", import(".BackYardBaseCard"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.info = BackYardFormationCard.New(arg_1_0._go)

	onButton(arg_1_0, arg_1_0._content, function()
		arg_1_0:emit(NewBackYardShipInfoMediator.OPEN_CHUANWU, arg_1_0.type, arg_1_0.ship)
	end, SFX_PANEL)

	arg_1_0.press = GetOrAddComponent(arg_1_0._content, typeof(UILongPressTrigger))

	arg_1_0.press.onLongPressed:RemoveAllListeners()
	arg_1_0.press.onLongPressed:AddListener(function()
		if not arg_1_0.ship then
			return
		end

		arg_1_0:emit(NewBackYardShipInfoMediator.LOOG_PRESS_SHIP, arg_1_0.type, arg_1_0.ship)
	end)
end

function var_0_0.OnFlush(arg_4_0)
	local var_4_0 = arg_4_0.ship
	local var_4_1 = arg_4_0.info

	if not arg_4_0.targteShipId or arg_4_0.targteShipId ~= var_4_0.id then
		var_4_1:update(var_4_0)

		arg_4_0.targteShipId = var_4_0.id
	end

	local var_4_2 = var_4_0:getLevelExpConfig()
	local var_4_3 = arg_4_0:CalcShipAddExpSpeed()
	local var_4_4 = {}
	local var_4_5 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	table.Foreach(var_4_5, function(arg_5_0, arg_5_1)
		if arg_5_1 and not arg_5_1:isEnd() then
			local var_5_0 = arg_5_1:getConfig("config_data")[1][4]

			_.each(arg_5_1:getData1List(), function(arg_6_0)
				var_4_4[arg_6_0] = (var_4_4[arg_6_0] or 0) + var_5_0
			end)
		end
	end)

	local var_4_6 = 0
	local var_4_7 = 0

	for iter_4_0, iter_4_1 in ipairs(getProxy(ActivityProxy):getBackyardEnergyActivityBuffs()) do
		var_4_7 = var_4_7 + tonumber(iter_4_1:getConfig("benefit_effect"))
	end

	if arg_4_0.type == Ship.STATE_TRAIN then
		local var_4_8 = var_4_0:getRecoverEnergyPoint() + Ship.BACKYARD_1F_ENERGY_ADDITION + (var_4_4[var_4_0.id] or 0)

		var_4_1:updateProps({
			{
				i18n("word_lv"),
				var_4_0.level
			},
			{
				i18n("word_next_level"),
				math.max(var_4_2.exp - var_4_0.exp, 0)
			},
			{
				i18n("word_exp_chinese") .. i18n("word_get"),
				var_4_3
			},
			{
				i18n("word_nowenergy"),
				var_4_0.energy
			},
			{
				i18n("word_energy_recov_speed"),
				10 * var_4_8 .. (var_4_7 > 0 and setColorStr("+" .. 10 * var_4_7, COLOR_GREEN) or "") .. "/h"
			}
		})
	elseif arg_4_0.type == Ship.STATE_REST then
		local var_4_9 = var_4_0:getRecoverEnergyPoint() + Ship.BACKYARD_2F_ENERGY_ADDITION + (var_4_4[var_4_0.id] or 0)

		var_4_1:updateProps1({
			{
				i18n("word_lv"),
				var_4_0.level
			},
			{
				i18n("word_nowenergy"),
				var_4_0.energy
			},
			{
				i18n("word_energy_recov_speed"),
				10 * var_4_9 .. (var_4_7 > 0 and setColorStr("+" .. 10 * var_4_7, COLOR_GREEN) or "") .. "/h"
			}
		})
	end

	setActive(var_4_1.propsTr, arg_4_0.type == Ship.STATE_TRAIN)
	setActive(var_4_1.propsTr1, arg_4_0.type == Ship.STATE_REST)
end

function var_0_0.CalcShipAddExpSpeed(arg_7_0)
	local var_7_0 = 0
	local var_7_1 = getProxy(DormProxy):getRawData()
	local var_7_2 = arg_7_0:GetBaseExp(var_7_1)

	return (math.floor(var_7_2 * 3600 / pg.dorm_data_template[var_7_1.id].time))
end

function var_0_0.GetBaseExp(arg_8_0, arg_8_1)
	local var_8_0 = getProxy(PlayerProxy):getRawData()
	local var_8_1 = arg_8_1:GetStateShipCnt(Ship.STATE_TRAIN)

	if var_8_1 <= 0 then
		return 0
	end

	local var_8_2 = pg.dorm_data_template[arg_8_1.id]
	local var_8_3 = BuffHelper.GetBackYardExpBuffs()
	local var_8_4 = 1

	for iter_8_0, iter_8_1 in pairs(var_8_3) do
		if iter_8_1:isActivate() then
			local var_8_5 = iter_8_1:getConfig("benefit_effect")

			var_8_4 = tonumber(var_8_5) / 100 + var_8_4
		end
	end

	local var_8_6 = pg.gameset.dorm_exp_base.key_value
	local var_8_7 = pg.gameset.dorm_exp_ratio_comfort_degree.key_value
	local var_8_8 = pg.gameset["dorm_exp_ratio_by_" .. var_8_1].key_value / 100
	local var_8_9 = arg_8_1:getComfortable()

	return var_8_8 * (var_8_6 + var_8_2.exp * (var_8_9 / (var_8_9 + var_8_7))) * var_8_4 * (1 + 0.05 * var_8_0.level)
end

function var_0_0.OnDispose(arg_9_0)
	arg_9_0.press.onLongPressed:RemoveAllListeners()
	arg_9_0.press.onLongPressed:AddListener(nil)

	if arg_9_0.info then
		arg_9_0.info:clear()
	end
end

return var_0_0

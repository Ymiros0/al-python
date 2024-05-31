﻿local var_0_0 = class("Guild", import(".base.BaseGuild"))
local var_0_1 = pg.guild_technology_template
local var_0_2 = pg.guild_operation_template
local var_0_3 = true

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.member = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.member or {}) do
		local var_1_0 = GuildMember.New(iter_1_1)

		arg_1_0.member[var_1_0.id] = var_1_0
	end

	arg_1_0.logInfo = {}

	for iter_1_2, iter_1_3 in ipairs(arg_1_1.log or {}) do
		local var_1_1 = GuildLogInfo.New(iter_1_3)

		table.insert(arg_1_0.logInfo, var_1_1)
	end

	arg_1_0.events = {}

	for iter_1_4, iter_1_5 in ipairs(var_0_2.all) do
		table.insert(arg_1_0.events, GuildEvent.New({
			id = iter_1_5
		}))
	end

	arg_1_0:updateBaseInfo(arg_1_1)
	arg_1_0:updateExtraInfo(arg_1_1)
	arg_1_0:updateUserInfo({})

	arg_1_0.completion = false
end

function var_0_0.updateBaseInfo(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_1.base or {}

	arg_2_0.id = var_2_0.id
	arg_2_0.policy = var_2_0.policy
	arg_2_0.faction = var_2_0.faction
	arg_2_0.name = var_2_0.name
	arg_2_0.manifesto = var_2_0.manifesto
	arg_2_0.level = var_2_0.level or 1
	arg_2_0.memberCount = var_2_0.member_count or 1
	arg_2_0.announce = var_2_0.announce or ""
	arg_2_0.exp = var_2_0.exp or 0
	arg_2_0.changeFactionTime = var_2_0.change_faction_cd or 0
	arg_2_0.kickLeaderTime = var_2_0.kick_leader_cd or 0
end

function var_0_0.updateExtraInfo(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1.guild_ex or {}

	arg_3_0.capital = var_3_0.capital or 0

	local var_3_1 = GuildTask.New(var_3_0.this_weekly_tasks or {})

	arg_3_0:updateWeeklyTask(var_3_1)

	arg_3_0.benefitFinishTime = var_3_0.benefit_finish_time or 0
	arg_3_0.lastBenefitFinishTime = var_3_0.last_benefit_finish_time or 0
	arg_3_0.technologyGroups = {}

	for iter_3_0, iter_3_1 in pairs(var_0_1.get_id_list_by_group) do
		local var_3_2 = GuildTechnologyGroup.New({
			id = iter_3_0
		})

		arg_3_0.technologyGroups[var_3_2.id] = var_3_2
	end

	for iter_3_2, iter_3_3 in ipairs(var_3_0.technologys or {}) do
		local var_3_3 = var_0_1[iter_3_3.id]

		arg_3_0.technologyGroups[var_3_3.group]:update(iter_3_3)
	end

	arg_3_0.maxMemberCntAddition = 0
	arg_3_0.capitalLogs = {}
	arg_3_0.requestCapitalLogTime = 0
	arg_3_0.retreatCnt = var_3_0.retreat_cnt or 0
	arg_3_0.techCancelCnt = var_3_0.tech_cancel_cnt or 0
	arg_3_0.activeEventCnt = var_3_0.active_event_cnt or 0
	arg_3_0.tipActiveEventCnt = pg.guildset.operation_monthly_time.key_value
end

function var_0_0.SetMaxMemberCntAddition(arg_4_0, arg_4_1)
	arg_4_0.maxMemberCntAddition = arg_4_1
end

function var_0_0.updateUserInfo(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1.user_info or {}

	arg_5_0.donateCount = var_5_0.donate_count or 0
	arg_5_0.benefitTime = var_5_0.benefit_time and var_5_0.benefit_time > 0 and var_5_0.benefit_time or 0
	arg_5_0.weeklyTaskFlag = var_5_0.weekly_task_flag or 0

	arg_5_0:setRefreshWeeklyTaskProgressTime()

	arg_5_0.refreshCaptialTime = 0
	arg_5_0.donateTasks = {}

	for iter_5_0, iter_5_1 in ipairs(var_5_0.donate_tasks or {}) do
		local var_5_1 = GuildDonateTask.New({
			id = iter_5_1
		})

		table.insert(arg_5_0.donateTasks, var_5_1)
	end

	arg_5_0.technologys = {}

	for iter_5_2, iter_5_3 in pairs(var_0_1.get_id_list_by_group) do
		local var_5_2 = arg_5_0.technologyGroups[iter_5_2]
		local var_5_3 = GuildTechnology.New(var_5_2)

		arg_5_0.technologys[iter_5_2] = var_5_3
	end

	for iter_5_4, iter_5_5 in ipairs(var_5_0.tech_id or {}) do
		local var_5_4 = var_0_1[iter_5_5].group
		local var_5_5 = arg_5_0.technologyGroups[var_5_4]

		arg_5_0.technologys[var_5_4]:Update(iter_5_5, var_5_5)
	end

	arg_5_0.extraDonateCnt = var_5_0.extra_donate or 0
	arg_5_0.extraBattleCnt = var_5_0.extra_operation or 0
	arg_5_0.completion = true
end

function var_0_0.IsCompletion(arg_6_0)
	return arg_6_0.completion
end

function var_0_0.AddExtraDonateCnt(arg_7_0, arg_7_1)
	arg_7_0.extraDonateCnt = arg_7_0.extraDonateCnt + arg_7_1
end

function var_0_0.ReduceExtraDonateCnt(arg_8_0, arg_8_1)
	if arg_8_0.extraDonateCnt <= 0 then
		return
	end

	assert(arg_8_1 <= arg_8_0.extraDonateCnt)

	arg_8_0.extraDonateCnt = arg_8_0.extraDonateCnt - arg_8_1
end

function var_0_0.GetExtraDonateCnt(arg_9_0)
	return arg_9_0.extraDonateCnt
end

function var_0_0.AddExtraBattleCnt(arg_10_0, arg_10_1)
	arg_10_0.extraBattleCnt = arg_10_0.extraBattleCnt + arg_10_1
end

function var_0_0.ReduceExtraBattleCnt(arg_11_0, arg_11_1)
	if arg_11_0.extraBattleCnt <= 0 then
		return
	end

	assert(arg_11_1 <= arg_11_0.extraBattleCnt)

	arg_11_0.extraBattleCnt = arg_11_0.extraBattleCnt - arg_11_1
end

function var_0_0.GetExtraBattleCnt(arg_12_0)
	return arg_12_0.extraBattleCnt
end

function var_0_0.StartTech(arg_13_0, arg_13_1)
	local var_13_0 = pg.guild_technology_template[arg_13_1].group

	arg_13_0.technologyGroups[var_13_0]:Start()
end

function var_0_0.GetEvents(arg_14_0)
	return arg_14_0.events
end

function var_0_0.GetEventById(arg_15_0, arg_15_1)
	return _.detect(arg_15_0.events, function(arg_16_0)
		return arg_16_0.id == arg_15_1
	end)
end

function var_0_0.GetActiveEvent(arg_17_0)
	return _.detect(arg_17_0.events, function(arg_18_0)
		return arg_18_0:IsActive()
	end)
end

function var_0_0.CanCancelTech(arg_19_0)
	return arg_19_0.techCancelCnt == 0
end

function var_0_0.UpdateTechCancelCnt(arg_20_0)
	arg_20_0.techCancelCnt = arg_20_0.techCancelCnt + 1
end

function var_0_0.ResetTechCancelCnt(arg_21_0)
	arg_21_0.techCancelCnt = 0
end

function var_0_0.shouldRefreshCaptial(arg_22_0)
	return arg_22_0.refreshCaptialTime < pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.setRefreshCaptialTime(arg_23_0)
	arg_23_0.refreshCaptialTime = pg.TimeMgr.GetInstance():GetServerTime() + GuildConst.REFRESH_CAPITAL_TIME
end

function var_0_0.shouldRefreshWeeklyTaskProgress(arg_24_0)
	return pg.TimeMgr.GetInstance():GetServerTime() >= arg_24_0.weeklyTaskNextRefreshTime
end

function var_0_0.setRefreshWeeklyTaskProgressTime(arg_25_0)
	arg_25_0.weeklyTaskNextRefreshTime = pg.TimeMgr.GetInstance():GetServerTime() + GuildConst.WEEKLY_TASK_PROGRESS_REFRESH_TIME
end

function var_0_0.hasWeeklyTaskFlag(arg_26_0)
	return arg_26_0.weeklyTaskFlag ~= 0
end

function var_0_0.setWeeklyTaskFlag(arg_27_0, arg_27_1)
	arg_27_0.weeklyTaskFlag = arg_27_1
end

function var_0_0.getTechnologyGroups(arg_28_0)
	local var_28_0 = {}

	for iter_28_0, iter_28_1 in pairs(arg_28_0.technologyGroups) do
		table.insert(var_28_0, iter_28_1)
	end

	return var_28_0
end

function var_0_0.getTechnologyGroupById(arg_29_0, arg_29_1)
	return arg_29_0.technologyGroups[arg_29_1]
end

function var_0_0.getActiveTechnologyGroup(arg_30_0)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.technologyGroups) do
		if iter_30_1:isStarting() then
			return iter_30_1
		end
	end
end

function var_0_0.GetTechnologys(arg_31_0)
	return arg_31_0.technologys
end

function var_0_0.getTechnologyById(arg_32_0, arg_32_1)
	return arg_32_0.technologys[arg_32_1]
end

function var_0_0.getTechnologys(arg_33_0)
	local var_33_0 = {}

	for iter_33_0, iter_33_1 in pairs(arg_33_0.technologys) do
		table.insert(var_33_0, iter_33_1)
	end

	return var_33_0
end

function var_0_0.getSupplyConsume(arg_34_0)
	local var_34_0 = pg.guildset.guild_award_consume.key_value
	local var_34_1 = arg_34_0:getSupplyDuration()

	return var_34_0, math.ceil(var_34_1 / 86400)
end

function var_0_0.getSupplyAwardId(arg_35_0)
	return pg.guildset.guild_award_id.key_value
end

function var_0_0.updateSupplyTime(arg_36_0, arg_36_1)
	arg_36_0.benefitTime = arg_36_1
end

function var_0_0.getSupplyCnt(arg_37_0)
	local var_37_0 = 0
	local var_37_1 = pg.TimeMgr.GetInstance():GetServerTime()

	if arg_37_0.benefitFinishTime > 0 then
		var_37_1 = math.min(arg_37_0.benefitFinishTime, var_37_1)
	end

	local var_37_2 = arg_37_0:getSupplyStartTime()

	if arg_37_0.benefitTime == 0 or var_37_2 > arg_37_0.benefitTime then
		var_37_0 = math.ceil((var_37_1 - var_37_2) / 86400)
	else
		local var_37_3 = math.max(0, var_37_1 - arg_37_0.benefitTime)

		var_37_0 = math.floor(var_37_3 / 86400)
	end

	local var_37_4 = arg_37_0:getMemberById(getProxy(PlayerProxy):getRawData().id):GetJoinZeroTime()

	if arg_37_0.lastBenefitFinishTime > 0 and arg_37_0.lastBenefitFinishTime > arg_37_0.benefitTime and var_37_4 <= arg_37_0.lastBenefitFinishTime then
		local var_37_5 = arg_37_0.benefitTime <= 0 and var_37_4 or arg_37_0.benefitTime

		var_37_0 = math.ceil((arg_37_0.lastBenefitFinishTime - var_37_5) / 86400) + var_37_0
	end

	return math.min(var_37_0, GuildConst.MAX_SUPPLY_CNT)
end

function var_0_0.startSupply(arg_38_0, arg_38_1)
	arg_38_0.benefitFinishTime = arg_38_1
end

function var_0_0.GetSupplyEndTime(arg_39_0)
	return arg_39_0.benefitFinishTime
end

function var_0_0.getSupplyLeftCnt(arg_40_0)
	local var_40_0 = pg.TimeMgr.GetInstance():GetServerTime()

	return math.floor((arg_40_0.benefitFinishTime - var_40_0) / 86400)
end

function var_0_0.getSupplyDuration(arg_41_0)
	return pg.guildset.guild_award_duration.key_value
end

function var_0_0.getSupplyStartTime(arg_42_0)
	local var_42_0 = arg_42_0.benefitFinishTime - arg_42_0:getSupplyDuration() + 1
	local var_42_1 = arg_42_0:getMemberById(getProxy(PlayerProxy):getRawData().id):GetJoinZeroTime()

	if var_42_0 < var_42_1 then
		return var_42_1
	else
		return var_42_0
	end
end

function var_0_0.ExistSupply(arg_43_0)
	return arg_43_0.benefitFinishTime > 0 and arg_43_0.benefitFinishTime > pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.isOpenedSupply(arg_44_0)
	return arg_44_0.benefitFinishTime > 0 and (arg_44_0.benefitFinishTime > pg.TimeMgr.GetInstance():GetServerTime() or arg_44_0:getSupplyCnt() > 0)
end

function var_0_0.getSelectableWeeklyTasks(arg_45_0)
	local var_45_0 = {}

	if GuildMember.IsAdministrator(arg_45_0:getSelfDuty()) then
		local var_45_1 = pg.guild_mission_template

		for iter_45_0, iter_45_1 in ipairs(var_45_1.all) do
			local var_45_2 = GuildTask.New({
				progress = 0,
				id = iter_45_1
			})

			table.insert(var_45_0, var_45_2)
		end
	end

	return var_45_0
end

function var_0_0.shouldRequestCapitalLog(arg_46_0)
	if pg.TimeMgr.GetInstance():GetServerTime() - arg_46_0.requestCapitalLogTime > GuildConst.REQUEST_LOG_TIME then
		return true
	end

	return false
end

function var_0_0.updateCapitalLogs(arg_47_0, arg_47_1)
	arg_47_0.capitalLogs = arg_47_1
	arg_47_0.requestCapitalLogTime = pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.getCapitalLogs(arg_48_0)
	return arg_48_0.capitalLogs
end

function var_0_0.getMaxDonateCnt(arg_49_0)
	return pg.guildset.contribution_task_num.key_value
end

function var_0_0.getRemainDonateCnt(arg_50_0)
	return arg_50_0:getMaxDonateCnt() - arg_50_0.donateCount
end

function var_0_0.updateDonateCount(arg_51_0)
	if arg_51_0:getRemainDonateCnt() > 0 then
		arg_51_0.donateCount = arg_51_0.donateCount + 1
	else
		arg_51_0:ReduceExtraDonateCnt(1)
	end
end

function var_0_0.canDonate(arg_52_0)
	return arg_52_0:getRemainDonateCnt() > 0 or arg_52_0.extraDonateCnt > 0
end

function var_0_0.getDonateTasks(arg_53_0)
	return arg_53_0.donateTasks
end

function var_0_0.updateDonateTasks(arg_54_0, arg_54_1)
	arg_54_0.donateTasks = arg_54_1
end

function var_0_0.getDonateTaskById(arg_55_0, arg_55_1)
	return _.detect(arg_55_0.donateTasks, function(arg_56_0)
		return arg_56_0.id == arg_55_1
	end)
end

function var_0_0.updateWeeklyTask(arg_57_0, arg_57_1)
	arg_57_0.weeklyTask = arg_57_1
end

function var_0_0.getWeeklyTask(arg_58_0)
	return arg_58_0.weeklyTask
end

function var_0_0.GetActiveWeeklyTask(arg_59_0)
	if arg_59_0.weeklyTask and arg_59_0.weeklyTask.id ~= 0 then
		return arg_59_0.weeklyTask
	end

	return nil
end

function var_0_0.addCapital(arg_60_0, arg_60_1)
	arg_60_0:updateCapital(arg_60_0.capital + arg_60_1)
end

function var_0_0.updateCapital(arg_61_0, arg_61_1)
	arg_61_0.capital = arg_61_1
end

function var_0_0.consumeCapital(arg_62_0, arg_62_1)
	arg_62_0:updateCapital(arg_62_0.capital - arg_62_1)
end

function var_0_0.getCapital(arg_63_0)
	return arg_63_0.capital
end

function var_0_0.setkickLeaderTime(arg_64_0, arg_64_1)
	arg_64_0.kickLeaderTime = arg_64_1
end

function var_0_0.getKickLeftTime(arg_65_0)
	local var_65_0 = pg.TimeMgr.GetInstance():GetServerTime()

	return arg_65_0.kickLeaderTime - var_65_0
end

function var_0_0.inKickTime(arg_66_0)
	return arg_66_0.kickLeaderTime ~= 0
end

function var_0_0.getAssistantMaxCount(arg_67_0)
	return pg.guild_data_level[arg_67_0.level].assistant_commander
end

function var_0_0.getAssistantCount(arg_68_0)
	local var_68_0 = 0

	for iter_68_0, iter_68_1 in pairs(arg_68_0.member) do
		if iter_68_1.duty == GuildConst.DUTY_DEPUTY_COMMANDER then
			var_68_0 = var_68_0 + 1
		end
	end

	return var_68_0
end

function var_0_0.setMemberCount(arg_69_0, arg_69_1)
	arg_69_0.memberCount = arg_69_1
end

function var_0_0.getSortMember(arg_70_0)
	local var_70_0 = {}

	for iter_70_0, iter_70_1 in pairs(arg_70_0.member) do
		table.insert(var_70_0, iter_70_1)
	end

	return var_70_0
end

function var_0_0.getBgName(arg_71_0)
	if arg_71_0.faction == GuildConst.FACTION_TYPE_BLHX then
		return "bg/bg_guild_blue_n"
	elseif arg_71_0.faction == GuildConst.FACTION_TYPE_CSZZ then
		return "bg/bg_guild_red_n"
	end
end

function var_0_0.addLog(arg_72_0, arg_72_1)
	table.insert(arg_72_0.logInfo, 1, arg_72_1)

	if #arg_72_0.logInfo > 100 then
		table.remove(arg_72_0.logInfo, #arg_72_0.logInfo)
	end
end

function var_0_0.getLogs(arg_73_0)
	return arg_73_0.logInfo
end

function var_0_0.getMemberById(arg_74_0, arg_74_1)
	return arg_74_0.member[arg_74_1]
end

function var_0_0.updateMember(arg_75_0, arg_75_1)
	arg_75_0.member[arg_75_1.id] = arg_75_1
end

function var_0_0.addMember(arg_76_0, arg_76_1)
	arg_76_0.member[arg_76_1.id] = arg_76_1
end

function var_0_0.deleteMember(arg_77_0, arg_77_1)
	arg_77_0.member[arg_77_1] = nil
end

function var_0_0.getDutyByMemberId(arg_78_0, arg_78_1)
	for iter_78_0, iter_78_1 in pairs(arg_78_0.member) do
		if iter_78_1.id == arg_78_1 then
			return iter_78_1.duty
		end
	end
end

function var_0_0.setId(arg_79_0, arg_79_1)
	arg_79_0.id = arg_79_1
end

function var_0_0.setName(arg_80_0, arg_80_1)
	arg_80_0.name = arg_80_1
end

function var_0_0.getPolicyName(arg_81_0)
	return GuildConst.POLICY_NAME[arg_81_0.policy]
end

function var_0_0.getFactionName(arg_82_0)
	return GuildConst.FACTION_NAME[arg_82_0.faction]
end

function var_0_0.getName(arg_83_0)
	return arg_83_0.name
end

function var_0_0.setPolicy(arg_84_0, arg_84_1)
	arg_84_0.policy = arg_84_1
end

function var_0_0.getPolicy(arg_85_0)
	return arg_85_0.policy
end

function var_0_0.setFaction(arg_86_0, arg_86_1)
	arg_86_0.faction = arg_86_1
end

function var_0_0.getFaction(arg_87_0)
	return arg_87_0.faction
end

function var_0_0.setManifesto(arg_88_0, arg_88_1)
	arg_88_0.manifesto = arg_88_1
end

function var_0_0.getManifesto(arg_89_0)
	return arg_89_0.manifesto or ""
end

local var_0_4 = 86400

function var_0_0.inChangefactionTime(arg_90_0)
	local var_90_0 = arg_90_0.changeFactionTime - pg.TimeMgr.GetInstance():GetServerTime()

	if arg_90_0.changeFactionTime ~= 0 and not (var_90_0 < 0) then
		return true
	end
end

function var_0_0.changeFactionLeftTime(arg_91_0)
	local var_91_0 = arg_91_0.changeFactionTime - pg.TimeMgr.GetInstance():GetServerTime()

	return pg.TimeMgr.GetInstance():parseTimeFrom(var_91_0)
end

function var_0_0.getLevelMaxExp(arg_92_0)
	local var_92_0 = pg.guild_data_level

	if not var_92_0[arg_92_0.level] then
		return var_92_0[var_92_0.all[#var_92_0.all]].exp
	else
		return var_92_0[arg_92_0.level].exp
	end
end

function var_0_0.getMaxMember(arg_93_0)
	local var_93_0 = pg.guild_data_level
	local var_93_1 = var_93_0.all[#var_93_0.all]
	local var_93_2 = var_93_0[math.min(arg_93_0.level, var_93_1)].member_num
	local var_93_3 = arg_93_0.maxMemberCntAddition or 0

	return var_93_2 + arg_93_0:GetGuildMemberCntAddition() + var_93_3
end

function var_0_0.updateExp(arg_94_0, arg_94_1)
	arg_94_0.exp = arg_94_1
end

function var_0_0.updateLevel(arg_95_0, arg_95_1)
	arg_95_0.level = arg_95_1
end

function var_0_0.getCommader(arg_96_0)
	for iter_96_0, iter_96_1 in pairs(arg_96_0.member) do
		if iter_96_1.duty == GuildConst.DUTY_COMMANDER then
			return iter_96_1
		end
	end
end

function var_0_0.getCommaderName(arg_97_0)
	local var_97_0 = arg_97_0:getCommader()

	if var_97_0 then
		return var_97_0.name
	else
		return ""
	end
end

function var_0_0.setAnnounce(arg_98_0, arg_98_1)
	arg_98_0.announce = arg_98_1
end

function var_0_0.GetAnnounce(arg_99_0)
	return arg_99_0.announce
end

function var_0_0.getEnableDuty(arg_100_0, arg_100_1, arg_100_2)
	if arg_100_2 == GuildConst.DUTY_RECRUIT then
		return {}
	end

	local var_100_0 = {}

	if arg_100_1 == GuildConst.DUTY_COMMANDER then
		if arg_100_0:getAssistantMaxCount() == arg_100_0:getAssistantCount() then
			var_100_0 = arg_100_2 == GuildConst.DUTY_DEPUTY_COMMANDER and {
				GuildConst.DUTY_COMMANDER,
				GuildConst.DYTY_PICKED,
				GuildConst.DUTY_ORDINARY
			} or {
				GuildConst.DYTY_PICKED,
				GuildConst.DUTY_ORDINARY
			}
		else
			var_100_0 = arg_100_2 == GuildConst.DUTY_DEPUTY_COMMANDER and {
				GuildConst.DUTY_COMMANDER,
				GuildConst.DUTY_DEPUTY_COMMANDER,
				GuildConst.DYTY_PICKED,
				GuildConst.DUTY_ORDINARY
			} or {
				GuildConst.DUTY_DEPUTY_COMMANDER,
				GuildConst.DYTY_PICKED,
				GuildConst.DUTY_ORDINARY
			}
		end
	elseif arg_100_1 == GuildConst.DUTY_DEPUTY_COMMANDER then
		var_100_0 = {
			GuildConst.DYTY_PICKED,
			GuildConst.DUTY_ORDINARY
		}
	end

	for iter_100_0, iter_100_1 in ipairs(var_100_0) do
		if iter_100_1 == arg_100_2 then
			table.remove(var_100_0, iter_100_0)

			break
		end
	end

	return var_100_0
end

function var_0_0.warpChatInfo(arg_101_0, arg_101_1)
	local var_101_0, var_101_1 = wordVer(arg_101_1.content, {
		isReplace = true
	})
	local var_101_2 = GuildMember.New(arg_101_1.player)

	if var_101_2 then
		local var_101_3 = arg_101_0:getDutyByMemberId(var_101_2.id)

		assert(var_101_3, "palyer duty has not been found" .. var_101_2.id)
		var_101_2:setDuty(var_101_3)

		local var_101_4

		string.gsub(var_101_1, ChatConst.EmojiCodeMatch, function(arg_102_0)
			var_101_4 = tonumber(arg_102_0)
		end)

		if var_101_4 then
			local var_101_5 = pg.emoji_template[var_101_4]

			if var_101_5 then
				var_101_1 = var_101_5.desc
			else
				var_101_4 = nil
			end
		end

		return (ChatMsg.New(ChatConst.ChannelGuild, {
			player = var_101_2,
			content = var_101_1,
			emojiId = var_101_4,
			timestamp = arg_101_1.time
		}))
	end
end

function var_0_0.getSelfDuty(arg_103_0)
	local var_103_0 = getProxy(PlayerProxy):getRawData()

	return arg_103_0:getDutyByMemberId(var_103_0.id)
end

function var_0_0.GetOfficePainting(arg_104_0)
	local var_104_0 = arg_104_0:getFaction()

	if var_104_0 == GuildConst.FACTION_TYPE_BLHX then
		return "guild_office_blue"
	elseif var_104_0 == GuildConst.FACTION_TYPE_CSZZ then
		return "guild_office_red"
	end
end

function var_0_0.ShouldShowDonateTip(arg_105_0)
	return arg_105_0:getMaxDonateCnt() > arg_105_0.donateCount
end

function var_0_0.ShouldWeeklyTaskTip(arg_106_0)
	local var_106_0 = arg_106_0.weeklyTask:getState()

	return GuildTask.STATE_EMPTY == var_106_0 and GuildMember.IsAdministrator(arg_106_0:getSelfDuty())
end

function var_0_0.ShouldShowOfficeTip(arg_107_0)
	return arg_107_0:ShouldShowDonateTip() or arg_107_0:ShouldWeeklyTaskTip() or arg_107_0:ShouldShowSupplyTip()
end

function var_0_0.ShouldShowTechTip(arg_108_0)
	local var_108_0 = arg_108_0:getActiveTechnologyGroup()

	return var_108_0 and var_108_0:isMaxLevel() and not arg_108_0:IsFinishAllTechnologyGroup()
end

function var_0_0.IsFinishAllTechnologyGroup(arg_109_0)
	for iter_109_0, iter_109_1 in pairs(arg_109_0.technologyGroups) do
		if not iter_109_1:isMaxLevel() then
			return false
		end
	end

	return true
end

function var_0_0.ShouldShowSupplyTip(arg_110_0)
	local function var_110_0()
		local var_111_0 = getProxy(PlayerProxy):getRawData().id
		local var_111_1 = arg_110_0:getMemberById(var_111_0)

		return not var_111_1:IsRecruit() and not var_111_1:isNewMember()
	end

	local var_110_1 = arg_110_0:getSupplyCnt()

	return arg_110_0:isOpenedSupply() and var_110_1 > 0 and var_110_0()
end

function var_0_0.GetMembers(arg_112_0)
	return arg_112_0.member
end

function var_0_0.GetAllAssaultShip(arg_113_0)
	local var_113_0 = {}

	for iter_113_0, iter_113_1 in pairs(arg_113_0.member) do
		local var_113_1 = iter_113_1:GetAssaultFleet():GetShipList()

		for iter_113_2, iter_113_3 in ipairs(var_113_1) do
			table.insert(var_113_0, iter_113_3)
		end
	end

	return var_113_0
end

function var_0_0.GetRecomForBossEvent(arg_114_0, arg_114_1, arg_114_2, arg_114_3)
	local var_114_0 = {}

	for iter_114_0, iter_114_1 in pairs(arg_114_0.member) do
		if not table.contains(arg_114_3, iter_114_1.id) then
			local var_114_1 = iter_114_1:GetAssaultFleet():GetStrongestShip(arg_114_1)

			if var_114_1 then
				table.insert(var_114_0, var_114_1)
			end
		end
	end

	table.sort(var_114_0, function(arg_115_0, arg_115_1)
		return arg_115_0.level > arg_115_1.level
	end)

	return _.slice(var_114_0, 1, math.min(arg_114_2, #var_114_0))
end

function var_0_0.GetMemberShips(arg_116_0, arg_116_1)
	local var_116_0 = {}
	local var_116_1 = {}
	local var_116_2 = getProxy(PlayerProxy):getRawData().id

	local function var_116_3(arg_117_0)
		return var_116_2 == arg_117_0.id
	end

	for iter_116_0, iter_116_1 in pairs(arg_116_0.member) do
		local var_116_4 = iter_116_1:GetShip()
		local var_116_5 = iter_116_1:IsCommander()

		var_116_4.isCommander = var_116_5

		if var_116_5 or var_116_3(iter_116_1) then
			table.insert(var_116_1, var_116_4)
		else
			table.insert(var_116_0, var_116_4)
		end
	end

	for iter_116_2 = 1, arg_116_1 do
		if #var_116_1 == arg_116_1 then
			break
		end

		local var_116_6 = var_116_0[iter_116_2]

		if var_116_6 then
			table.insert(var_116_1, var_116_6)
		end
	end

	return var_116_1
end

function var_0_0.IsAdministrator(arg_118_0)
	return GuildMember.IsAdministrator(arg_118_0:getSelfDuty())
end

function var_0_0.GetMissionAndAssultFleetShips(arg_119_0)
	local var_119_0 = {}
	local var_119_1 = arg_119_0:GetActiveEvent()

	if var_119_1 and not var_119_1:IsExpired() then
		local var_119_2 = var_119_1:GetJoinShips()

		for iter_119_0, iter_119_1 in ipairs(var_119_2) do
			table.insert(var_119_0, iter_119_1)
		end
	end

	local var_119_3 = getProxy(PlayerProxy):getRawData().id
	local var_119_4 = arg_119_0.member[var_119_3]
	local var_119_5 = var_119_4:GetAssaultFleet()
	local var_119_6 = var_119_4:GetExternalAssaultFleet()
	local var_119_7 = var_119_5:GetShipList()

	for iter_119_2, iter_119_3 in pairs(var_119_7) do
		local var_119_8 = GuildAssaultFleet.GetRealId(iter_119_3.id)

		table.insert(var_119_0, var_119_8)
	end

	local var_119_9 = var_119_6:GetShipList()

	for iter_119_4, iter_119_5 in pairs(var_119_9) do
		local var_119_10 = GuildAssaultFleet.GetRealId(iter_119_5.id)

		table.insert(var_119_0, var_119_10)
	end

	return var_119_0
end

function var_0_0.GetBossMissionShips(arg_120_0)
	local var_120_0 = {}
	local var_120_1 = arg_120_0:GetActiveEvent()

	if var_120_1 and not var_120_1:IsExpired() then
		local var_120_2 = var_120_1:GetBossShipIds()

		for iter_120_0, iter_120_1 in ipairs(var_120_2) do
			table.insert(var_120_0, iter_120_1)
		end
	end

	return var_120_0
end

function var_0_0.ExistCommander(arg_121_0, arg_121_1)
	local var_121_0 = arg_121_0:GetActiveEvent()

	if var_121_0 then
		local var_121_1 = var_121_0:GetBossMission()

		return var_121_1:IsActive() and var_121_1:ExistCommander(arg_121_1)
	end

	return false
end

function var_0_0.IncActiveEventCnt(arg_122_0)
	arg_122_0.activeEventCnt = arg_122_0.activeEventCnt + 1
end

function var_0_0.ResetActiveEventCnt(arg_123_0)
	arg_123_0.activeEventCnt = 0
end

function var_0_0.ShouldTipActiveEvent(arg_124_0)
	return arg_124_0.activeEventCnt + 1 <= arg_124_0.tipActiveEventCnt
end

function var_0_0.GetActiveEventCnt(arg_125_0)
	return arg_125_0.activeEventCnt
end

return var_0_0

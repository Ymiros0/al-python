pg = pg or {}

local var_0_0 = pg

var_0_0.PushNotificationMgr = singletonClass("PushNotificationMgr")

local var_0_1 = var_0_0.PushNotificationMgr

var_0_1.PUSH_TYPE_EVENT = 1
var_0_1.PUSH_TYPE_GOLD = 2
var_0_1.PUSH_TYPE_OIL = 3
var_0_1.PUSH_TYPE_BACKYARD = 4
var_0_1.PUSH_TYPE_SCHOOL = 5
var_0_1.PUSH_TYPE_CLASS = 6
var_0_1.PUSH_TYPE_TECHNOLOGY = 7
var_0_1.PUSH_TYPE_BLUEPRINT = 8
var_0_1.PUSH_TYPE_COMMANDER = 9
var_0_1.PUSH_TYPE_GUILD_MISSION_FORMATION = 10

local var_0_2 = {}
local var_0_3 = false

function var_0_1.Init(arg_1_0)
	var_0_2 = {}

	for iter_1_0, iter_1_1 in ipairs(var_0_0.push_data_template) do
		local var_1_0 = PlayerPrefs.GetInt("push_setting_" .. iter_1_1.id)

		var_0_2[iter_1_1.id] = var_1_0 == 0
	end

	var_0_3 = PlayerPrefs.GetInt("setting_ship_name") == 1
end

function var_0_1.Reset(arg_2_0)
	var_0_2 = {}

	for iter_2_0, iter_2_1 in ipairs(var_0_0.push_data_template) do
		PlayerPrefs.SetInt("push_setting_" .. iter_2_1.id, 0)

		var_0_2[iter_2_1.id] = true
	end

	PlayerPrefs.SetInt("setting_ship_name", 0)

	var_0_3 = false
end

function var_0_1.setSwitch(arg_3_0, arg_3_1, arg_3_2)
	if not var_0_0.push_data_template[arg_3_1] then
		return
	end

	var_0_2[arg_3_1] = arg_3_2

	PlayerPrefs.SetInt("push_setting_" .. arg_3_1, arg_3_2 and 0 or 1)
end

function var_0_1.setSwitchShipName(arg_4_0, arg_4_1)
	var_0_3 = arg_4_1

	PlayerPrefs.SetInt("setting_ship_name", arg_4_1 and 1 or 0)
end

function var_0_1.isEnabled(arg_5_0, arg_5_1)
	return var_0_2[arg_5_1]
end

function var_0_1.isEnableShipName(arg_6_0)
	return var_0_3
end

function var_0_1.Push(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	local var_7_0 = arg_7_3 - var_0_0.TimeMgr.GetInstance():GetServerTime()
	local var_7_1 = os.time() + var_7_0

	NotificationMgr.Inst:ScheduleLocalNotification(arg_7_1, arg_7_2, var_7_1)
	arg_7_0:log(arg_7_1, arg_7_2, var_7_1)
end

function var_0_1.cancelAll(arg_8_0)
	NotificationMgr.Inst:CancelAllLocalNotifications()
end

function var_0_1.PushAll(arg_9_0)
	local var_9_0 = getProxy(PlayerProxy)

	if var_9_0 and var_9_0:getInited() then
		arg_9_0:cancelAll()

		if var_0_2[var_0_1.PUSH_TYPE_EVENT] then
			arg_9_0:PushEvent()
		end

		if var_0_2[var_0_1.PUSH_TYPE_GOLD] then
			arg_9_0:PushGold()
		end

		if var_0_2[var_0_1.PUSH_TYPE_OIL] then
			arg_9_0:PushOil()
		end

		if var_0_2[var_0_1.PUSH_TYPE_BACKYARD] then
			arg_9_0:PushBackyard()
		end

		if var_0_2[var_0_1.PUSH_TYPE_SCHOOL] then
			arg_9_0:PushSchool()
		end

		if var_0_2[var_0_1.PUSH_TYPE_TECHNOLOGY] then
			arg_9_0:PushTechnlogy()
		end

		if var_0_2[var_0_1.PUSH_TYPE_BLUEPRINT] then
			arg_9_0:PushBluePrint()
		end

		if var_0_2[var_0_1.PUSH_TYPE_COMMANDER] then
			arg_9_0:PushCommander()
		end

		if var_0_2[var_0_1.PUSH_TYPE_GUILD_MISSION_FORMATION] then
			arg_9_0:PushGuildMissionFormation()
		end
	end
end

function var_0_1.PushEvent(arg_10_0)
	local var_10_0 = getProxy(EventProxy):getActiveEvents()
	local var_10_1 = var_0_0.push_data_template[arg_10_0.PUSH_TYPE_EVENT]

	for iter_10_0, iter_10_1 in ipairs(var_10_0) do
		local var_10_2 = string.gsub(var_10_1.content, "$1", iter_10_1.template.title)

		arg_10_0:Push(var_10_1.title, var_10_2, iter_10_1.finishTime)
	end
end

function var_0_1.PushGold(arg_11_0)
	local var_11_0 = getProxy(NavalAcademyProxy):GetGoldVO()
	local var_11_1 = var_11_0:bindConfigTable()
	local var_11_2 = var_11_0:GetLevel()
	local var_11_3 = var_11_1[var_11_2].store
	local var_11_4 = var_11_1[var_11_2].production
	local var_11_5 = var_11_1[var_11_2].hour_time
	local var_11_6 = getProxy(PlayerProxy).data
	local var_11_7 = var_11_6.resUpdateTm
	local var_11_8 = var_11_6.goldField

	if var_11_8 < var_11_3 then
		local var_11_9 = var_11_7 + (var_11_3 - var_11_8) / var_11_4 * 60 * 60 / 3

		if var_11_9 > var_0_0.TimeMgr.GetInstance():GetServerTime() then
			local var_11_10 = var_0_0.push_data_template[arg_11_0.PUSH_TYPE_GOLD]

			arg_11_0:Push(var_11_10.title, var_11_10.content, var_11_9)
		end
	end
end

function var_0_1.PushOil(arg_12_0)
	local var_12_0 = getProxy(NavalAcademyProxy):GetOilVO()
	local var_12_1 = var_12_0:bindConfigTable()
	local var_12_2 = var_12_0:GetLevel()
	local var_12_3 = var_12_1[var_12_2].store
	local var_12_4 = var_12_1[var_12_2].production
	local var_12_5 = var_12_1[var_12_2].hour_time
	local var_12_6 = getProxy(PlayerProxy).data
	local var_12_7 = var_12_6.resUpdateTm
	local var_12_8 = var_12_6.oilField

	if var_12_8 < var_12_3 then
		local var_12_9 = var_12_7 + (var_12_3 - var_12_8) / var_12_4 * 60 * 60 / 3

		if var_12_9 > var_0_0.TimeMgr.GetInstance():GetServerTime() then
			local var_12_10 = var_0_0.push_data_template[arg_12_0.PUSH_TYPE_OIL]

			arg_12_0:Push(var_12_10.title, var_12_10.content, var_12_9)
		end
	end
end

function var_0_1.PushBackyard(arg_13_0)
	local var_13_0 = getProxy(DormProxy):getRawData():getFoodLeftTime()

	if var_13_0 > var_0_0.TimeMgr.GetInstance():GetServerTime() then
		local var_13_1 = var_0_0.push_data_template[arg_13_0.PUSH_TYPE_BACKYARD]

		arg_13_0:Push(var_13_1.title, var_13_1.content, var_13_0)
	end
end

function var_0_1.PushSchool(arg_14_0)
	local var_14_0 = getProxy(NavalAcademyProxy):getStudents()
	local var_14_1 = var_0_0.push_data_template[arg_14_0.PUSH_TYPE_SCHOOL]
	local var_14_2 = getProxy(BayProxy):getData()

	for iter_14_0, iter_14_1 in ipairs(var_14_0) do
		if iter_14_1.finishTime > var_0_0.TimeMgr.GetInstance():GetServerTime() then
			local var_14_3 = var_14_2[iter_14_1.shipId]
			local var_14_4 = iter_14_1:getSkillId(var_14_3)
			local var_14_5 = var_14_3.skills[var_14_4]
			local var_14_6 = var_14_3:getName()
			local var_14_7 = getSkillName(iter_14_1:getSkillId(var_14_3))
			local var_14_8 = string.gsub(var_14_1.content, "$1", var_14_6)
			local var_14_9 = string.gsub(var_14_8, "$2", var_14_7)

			arg_14_0:Push(var_14_1.title, var_14_9, iter_14_1.finishTime)
		end
	end
end

function var_0_1.PushTechnlogy(arg_15_0)
	local var_15_0 = var_0_0.push_data_template[var_0_1.PUSH_TYPE_TECHNOLOGY]
	local var_15_1 = getProxy(TechnologyProxy)

	if var_15_0 and var_15_1 then
		local var_15_2 = var_15_1:getPlanningTechnologys()

		if #var_15_2 > 0 and not var_15_2[#var_15_2]:isFinish() then
			arg_15_0:Push(var_15_0.title, var_15_0.content, var_15_2[#var_15_2].time)
		end
	end
end

function var_0_1.PushBluePrint(arg_16_0)
	local var_16_0 = var_0_0.push_data_template[var_0_1.PUSH_TYPE_BLUEPRINT]
	local var_16_1 = getProxy(TechnologyProxy)
	local var_16_2 = getProxy(TaskProxy)

	if var_16_0 and var_16_1 and var_16_2 then
		local var_16_3 = var_16_1:getBuildingBluePrint()

		if var_16_3 then
			local var_16_4 = var_16_3:getTaskIds()

			for iter_16_0, iter_16_1 in ipairs(var_16_4) do
				local var_16_5 = var_16_3:getTaskOpenTimeStamp(iter_16_1)

				if var_16_5 > var_0_0.TimeMgr.GetInstance():GetServerTime() then
					local var_16_6 = var_16_2:getTaskById(iter_16_1) or var_16_2:getFinishTaskById(iter_16_1)
					local var_16_7 = var_16_2:isFinishPrevTasks(iter_16_1)

					if not var_16_6 and var_16_7 then
						local var_16_8 = var_16_3:getShipVO()
						local var_16_9 = string.gsub(var_16_0.content, "$1", var_16_8:getConfig("name"))

						arg_16_0:Push(var_16_0.title, var_16_9, var_16_5)
					end
				end
			end
		end
	end
end

function var_0_1.PushCommander(arg_17_0)
	local var_17_0 = var_0_0.push_data_template[var_0_1.PUSH_TYPE_COMMANDER]
	local var_17_1 = getProxy(CommanderProxy)

	if var_17_0 and var_17_1 then
		local var_17_2 = var_17_1:getBoxes()

		for iter_17_0, iter_17_1 in pairs(var_17_2) do
			if iter_17_1:getState() == CommanderBox.STATE_STARTING then
				local var_17_3 = var_17_0.content

				arg_17_0:Push(var_17_0.title, var_17_3, iter_17_1.finishTime)

				break
			end
		end
	end
end

function var_0_1.PushGuildMissionFormation(arg_18_0)
	local var_18_0 = getProxy(GuildProxy):getRawData()

	if not var_18_0 then
		return
	end

	local var_18_1 = var_18_0:GetActiveEvent()

	if not var_18_1 or var_18_1 and not var_18_1:IsParticipant() then
		return
	end

	local var_18_2 = var_18_1:GetUnlockMission()

	if not var_18_2 then
		return
	end

	local var_18_3 = var_18_2:GetNextFormationTime()

	if var_18_3 <= var_0_0.TimeMgr.GetInstance():GetServerTime() then
		return
	end

	local var_18_4 = var_0_0.push_data_template[var_0_1.PUSH_TYPE_GUILD_MISSION_FORMATION]

	arg_18_0:Push(var_18_4.title, var_18_4.content, var_18_3)
end

function var_0_1.log(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	local var_19_0 = arg_19_3 - os.time()

	originalPrint(arg_19_1, " - ", arg_19_2, " - ", var_19_0, "s后推送")
end

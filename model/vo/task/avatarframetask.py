local var_0_0 = class("AvatarFrameTask", import(".Task"))

var_0_0.type_task_level = "task_level"
var_0_0.type_task_ship = "task_ship"
var_0_0.fillter_task_type = {
	var_0_0.type_task_level,
	var_0_0.type_task_ship
}

local var_0_1 = var_0_0.fillter_task_type
local var_0_2 = "avatar_task_level"
local var_0_3 = {
	"avatar_upgrad_1",
	"avatar_upgrad_2",
	"avatar_upgrad_3"
}
local var_0_4 = "avatar_task_ship_1"
local var_0_5 = "avatar_task_ship_2"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.actId = arg_1_1
	arg_1_0.configId = arg_1_2
	arg_1_0.id = arg_1_3.id
	arg_1_0.progress = arg_1_3.progress or 0
	arg_1_0.acceptTime = arg_1_3.accept_time or 0
	arg_1_0.submitTime = arg_1_3.submit_time or 0

def var_0_0.IsActEnd(arg_2_0):
	local var_2_0 = pg.activity_event_avatarframe[arg_2_0.configId].link_event
	local var_2_1 = getProxy(ActivityProxy).getActivityById(var_2_0)

	return not var_2_1 or var_2_1.isEnd()

def var_0_0.updateProgress(arg_3_0, arg_3_1):
	arg_3_0.progress = arg_3_1 or 0

def var_0_0.isFinish(arg_4_0):
	return arg_4_0.getProgress() >= arg_4_0.getConfig("target_num")

def var_0_0.getProgress(arg_5_0):
	return arg_5_0.progress or 0

def var_0_0.isReceive(arg_6_0):
	return False

def var_0_0.getTaskStatus(arg_7_0):
	if arg_7_0.progress >= arg_7_0.getConfig("target_num"):
		return 1

	return 0

def var_0_0.onAdded(arg_8_0):
	return

def var_0_0.updateProgress(arg_9_0, arg_9_1):
	arg_9_0.progress = arg_9_1

def var_0_0.isSelectable(arg_10_0):
	return False

def var_0_0.judgeOverflow(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	return False, False

def var_0_0.IsUrTask(arg_12_0):
	return False

def var_0_0.GetRealType(arg_13_0):
	return 6

def var_0_0.IsOverflowShipExpItem(arg_14_0):
	return False

def var_0_0.ShowOnTaskScene(arg_15_0):
	return True

def var_0_0.getConfig(arg_16_0, arg_16_1):
	if not arg_16_0.configData:
		local var_16_0 = pg.activity_event_avatarframe[arg_16_0.configId]

		if not var_16_0:
			print("avatart id = " .. arg_16_0.configId .. " is not found")

			return

		local var_16_1 = arg_16_0.getTypeData(var_16_0, arg_16_0.id)

		if not var_16_1:
			return

		local var_16_2 = Clone(var_16_0.award_display)

		var_16_2[1][3] = var_16_1.award_num
		arg_16_0.configData = {
			level = 1,
			sub_type = 0,
			item_id = var_16_0.pt_id,
			desc = var_16_1.desc,
			target_num = var_16_1.target_num,
			award_num = var_16_1.award_num,
			scene = var_16_1.scene,
			award_display = var_16_2
		}

	return arg_16_0.configData[arg_16_1]

def var_0_0.getTypeData(arg_17_0, arg_17_1, arg_17_2):
	for iter_17_0 = 1, #var_0_1:
		local var_17_0 = var_0_1[iter_17_0]
		local var_17_1 = arg_17_1[var_17_0]

		for iter_17_1, iter_17_2 in ipairs(var_17_1):
			if iter_17_2[1] == arg_17_2:
				arg_17_0.avatarType = var_17_0

				return arg_17_0.createData(var_17_0, iter_17_2)

def var_0_0.isAvatarTask(arg_18_0):
	return True

def var_0_0.createData(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0

	if arg_19_1 == var_0_0.type_task_level:
		local var_19_1, var_19_2, var_19_3, var_19_4, var_19_5, var_19_6 = unpack(arg_19_2)
		local var_19_7 = ""

		if var_19_3 > 0 and var_19_3 <= #var_0_3:
			var_19_7 = pg.gametip[var_0_3[var_19_3]].tip

		local var_19_8 = var_19_2 * 10 + 1
		local var_19_9 = pg.ship_data_statistics[var_19_8].name
		local var_19_10
		local var_19_11

		for iter_19_0, iter_19_1 in ipairs(var_19_4):
			assert(pg.chapter_template[iter_19_1] != None, "找不到chapterid = " .. iter_19_1)

			var_19_11 = var_19_11 or {
				"ACTIVITY_MAP",
				{
					pg.chapter_template[iter_19_1].act_id
				}
			}

			if not var_19_10:
				var_19_10 = pg.chapter_template[iter_19_1].chapter_name
			else
				var_19_10 = var_19_10 .. "," .. pg.chapter_template[iter_19_1].chapter_name

		var_19_0 = {
			target_num = var_19_5,
			award_num = var_19_6,
			scene = var_19_11,
			desc = i18n("avatar_task_level", var_19_7, var_19_9, var_19_10, var_19_5)
		}
	elif arg_19_1 == var_0_0.type_task_ship:
		local var_19_12, var_19_13, var_19_14, var_19_15 = unpack(arg_19_2)
		local var_19_16 = var_19_13 * 10 + 1
		local var_19_17 = pg.ship_data_statistics[var_19_16].name

		if var_19_14 == 1:
			var_19_0 = {
				award_num = var_19_15,
				desc = i18n(var_0_4, var_19_17)
			}
		elif var_19_14 == 2:
			var_19_0 = {
				award_num = var_19_15,
				desc = i18n(var_0_5, var_19_17),
				scene = {
					"DOCKYARD",
					{
						mode = "overview"
					}
				}
			}

	return setmetatable(var_19_0, {
		__index = {
			award_num = 1,
			target_num = 1,
			desc = ""
		}
	})

return var_0_0

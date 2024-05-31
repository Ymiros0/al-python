local var_0_0 = class("UpdateStoryCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().storyId

	assert(type(var_1_0) == "string")

	if not pg.ConnectionMgr.GetInstance().getConnection() or not pg.ConnectionMgr.GetInstance().isConnected():
		return

	if not getProxy(PlayerProxy):
		return

	local var_1_1 = pg.NewStoryMgr.GetInstance()
	local var_1_2 = {}

	local function var_1_3(arg_2_0, arg_2_1)
		pg.ConnectionMgr.GetInstance().Send(11017, {
			story_id = arg_2_0
		}, 11018, function(arg_3_0)
			var_1_1.SetPlayedFlag(arg_2_0)

			local var_3_0 = PlayerConst.addTranDrop(arg_3_0.drop_list)

			table.insertto(var_1_2, var_3_0)

			if arg_2_1:
				arg_2_1())

	local function var_1_4(arg_4_0, arg_4_1)
		local var_4_0, var_4_1 = var_1_1.StoryName2StoryId(arg_4_0)
		local var_4_2 = {}

		if var_4_0 and var_4_0 > 0 and not var_1_1.GetPlayedFlag(var_4_0):
			table.insert(var_4_2, function(arg_5_0)
				var_1_3(var_4_0, arg_5_0))

		if var_4_1 and var_4_1 > 0 and not var_1_1.GetPlayedFlag(var_4_1):
			table.insert(var_4_2, function(arg_6_0)
				var_1_3(var_4_1, arg_6_0))

		parallelAsync(var_4_2, arg_4_1)

	local var_1_5 = var_1_1.StoryLinkNames(var_1_0) or {}

	table.insert(var_1_5, var_1_0)

	local var_1_6 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_5):
		table.insert(var_1_6, function(arg_7_0)
			var_1_4(iter_1_1, arg_7_0))

	seriesAsync(var_1_6, function()
		arg_1_0.sendNotification(GAME.STORY_UPDATE_DONE, {
			storyName = var_1_0,
			awards = var_1_2
		}))

return var_0_0

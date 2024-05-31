local var_0_0 = class("SearchFriendCommand", pm.SimpleCommand)

var_0_0.SEARCH_TYPE_LIST = 1
var_0_0.SEARCH_TYPE_RESUME = 2
var_0_0.SEARCH_TYPE_FRIEND = 3

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.keyword

	var_1_2 = var_1_2 and string.gsub(var_1_2, "^%s*(.-)%s*$", "%1")

	local var_1_3
	local var_1_4 = tonumber(var_1_2) and 0 or 1

	if var_1_1 == var_0_0.SEARCH_TYPE_LIST:
		pg.ConnectionMgr.GetInstance().Send(50014, {
			type = 0
		}, 50015, function(arg_2_0)
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.player_list):
				table.insert(var_2_0, Friend.New(iter_2_1))

			arg_1_0.sendNotification(GAME.FRIEND_SEARCH_DONE, {
				type = var_1_1,
				list = var_2_0
			}))
	elif var_1_1 == var_0_0.SEARCH_TYPE_RESUME or var_1_1 == var_0_0.SEARCH_TYPE_FRIEND:
		pg.ConnectionMgr.GetInstance().Send(50001, {
			type = var_1_4,
			keyword = tostring(var_1_2)
		}, 50002, function(arg_3_0)
			local var_3_0 = {}

			if arg_3_0.result == 0:
				table.insert(var_3_0, Friend.New(arg_3_0.player))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("friend_searchFriend_noPlayer"))

			arg_1_0.sendNotification(GAME.FRIEND_SEARCH_DONE, {
				type = var_1_1,
				list = var_3_0
			}))

return var_0_0

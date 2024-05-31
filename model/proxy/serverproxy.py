local var_0_0 = class("ServerProxy", import(".NetProxy"))

var_0_0.SERVERS_UPDATED = "ServerProxy.SERVERS_UPDATED"

def var_0_0.setServers(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.data = {}
	arg_1_0.lastServer = None
	arg_1_0.firstServer = None

	local var_1_0 = {}
	local var_1_1 = arg_1_0.getLoginedServer(arg_1_2)

	for iter_1_0, iter_1_1 in ipairs(arg_1_1):
		assert(isa(iter_1_1, Server), "should be an instance of Server")

		if table.contains(var_1_1, tostring(iter_1_1.id)):
			iter_1_1.isLogined = True

		arg_1_0.data[iter_1_1.id] = iter_1_1

		if iter_1_0 == #arg_1_1:
			arg_1_0.lastServer = iter_1_1

		if iter_1_1.sortIndex == 0:
			table.insert(var_1_0, iter_1_1)

	if #var_1_0 > 0:
		arg_1_0.firstServer = var_1_0[math.random(1, #var_1_0)]

	arg_1_0.facade.sendNotification(var_0_0.SERVERS_UPDATED, arg_1_0.getData())

def var_0_0.setLastServer(arg_2_0, arg_2_1, arg_2_2):
	PlayerPrefs.SetInt("server.id" .. arg_2_2, arg_2_1)

def var_0_0.getLastServer(arg_3_0, arg_3_1):
	local var_3_0 = PlayerPrefs.GetInt("server.id" .. arg_3_1)

	return arg_3_0.data[var_3_0] or arg_3_0.firstServer or arg_3_0.lastServer

def var_0_0.recordLoginedServer(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_0.getLoginedServer(arg_4_1)

	if not table.contains(var_4_0, tostring(arg_4_2)):
		arg_4_0.data[arg_4_2].isLogined = True

		table.insert(var_4_0, tostring(arg_4_2))

		local var_4_1 = table.concat(var_4_0, ".")

		PlayerPrefs.SetString("loginedServer_" .. arg_4_1, var_4_1)
		PlayerPrefs.Save()

def var_0_0.getLoginedServer(arg_5_0, arg_5_1):
	if not arg_5_0.loginedServerIds or arg_5_0.recordUid and arg_5_0.recordUid != arg_5_1:
		arg_5_0.recordUid = arg_5_1

		local var_5_0 = PlayerPrefs.GetString("loginedServer_" .. arg_5_1)

		arg_5_0.loginedServerIds = string.split(var_5_0, ".")

	return arg_5_0.loginedServerIds

return var_0_0

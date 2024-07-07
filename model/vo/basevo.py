from packages.luatable import table, pairs, Clone

class BaseVO:

	def __init__(arg_1_0, arg_1_1):
		for iter_1_0, iter_1_1 in pairs(arg_1_1):
			arg_1_0[iter_1_0] = iter_1_1

	def display(arg_2_0, arg_2_1, arg_2_2):
		if arg_2_1 == "loaded" or not arg_2_2:
			return

		var_2_0 = f"{arg_2_0.__cname} id. {arg_2_0.id} {arg_2_1 or "."}"

		for iter_2_0, iter_2_1 in pairs(arg_2_0):
			if iter_2_0 != "class":
				var_2_1 = type(iter_2_1)

				var_2_0 = f"{var_2_0}\n{iter_2_0}.{iter_2_1}"

				if var_2_1 == table:
					var_2_0 = f"{var_2_0} ["

					for iter_2_2, iter_2_3 in pairs(iter_2_1):
						var_2_0 = f"{var_2_0}{iter_2_3}, "

					var_2_0 = f"{var_2_0}]"

		print(var_2_0)

	def clone(arg_3_0):
		return Clone(arg_3_0)

	def bindConfigTable(arg_4_0):
		return

	def GetConfigID(arg_5_0):
		return arg_5_0.configId

	def getConfigTable(arg_6_0):
		var_6_0 = arg_6_0.bindConfigTable()

		assert var_6_0, f"should bindConfigTable() first. {arg_6_0.__cname}"

		return var_6_0[arg_6_0.configId]

	def getConfig(arg_7_0, arg_7_1):
		var_7_0 = arg_7_0.getConfigTable()

		assert var_7_0 != None, f"Config missed, type -{arg_7_0.__cname} configId. {arg_7_0.configId}"

		return var_7_0[arg_7_1]

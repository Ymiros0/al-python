from luatable import table

var_0_1 = table()
import findtype #????

def typeof(arg_1_0):
	var_1_0 = type(arg_1_0)

	if var_1_0 == table:
		var_1_1 = var_0_1[arg_1_0]

		if var_1_1 == None:
			var_1_1 = typeof(arg_1_0)
			var_0_1[arg_1_0] = var_1_1
	elif var_1_0 == str:
		var_1_1 = var_0_1[arg_1_0]

		if var_1_1 == None:
			var_1_1 = findtype(arg_1_0)
			var_0_1[arg_1_0] = var_1_1
	else:
		raise ValueError(f"attempt to call typeof on type {var_1_0})")

	return var_1_1

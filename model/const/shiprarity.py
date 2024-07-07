from packages.luatable import table

from model.const import ItemRarity

Gray = 2
Blue = 3
Purple = 4
Gold = 5
SSR = 6

def Rarity2Print(arg_1_0):
	return ItemRarity.Rarity2Print(arg_1_0 - 1)

def SSRGradient(arg_2_0):
	return f"<material=outline c=#00000040 x=1 y=1><material=gradient from=#FF0000 to=#00FF00 x=1 y=1>{arg_2_0}</material></material>"

def shipRarity2bgPrint(arg_3_0, arg_3_1, arg_3_2):
	var_3_0 = table()

	table.insert(var_3_0, Rarity2Print(arg_3_0))

	if arg_3_1:
		table.insert(var_3_0, "0")

	if arg_3_2:
		table.insert(var_3_0, "1")

	return table.concat(var_3_0, "_")
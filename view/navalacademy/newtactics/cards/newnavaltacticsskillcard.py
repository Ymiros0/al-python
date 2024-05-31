local var_0_0 = class("NewNavalTacticsSkillCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.icon = findTF(arg_1_0._tf, "icon").GetComponent(typeof(Image))
	arg_1_0.descTxt = findTF(arg_1_0._tf, "descView/desc").GetComponent(typeof(Text))
	arg_1_0.nextTxt = findTF(arg_1_0._tf, "next").GetComponent(typeof(Text))

def var_0_0.Enable(arg_2_0):
	setActive(arg_2_0._tf, True)

def var_0_0.Disable(arg_3_0):
	setActive(arg_3_0._tf, False)

def var_0_0.Update(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.GetName()

	changeToScrollText(arg_4_0._tf.Find("name/Text"), var_4_0)

	arg_4_0.descTxt.text = arg_4_1.GetTacticsDesc()

	local var_4_1 = "Lv." .. arg_4_1.level .. (arg_4_2 and arg_4_2 > 0 and "  <color=#A9F548FF>+" .. arg_4_2 .. "</color>" or "")

	setText(arg_4_0._tf.Find("name/level"), var_4_1)

	if arg_4_1.IsMaxLevel():
		arg_4_0.nextTxt.text = "MAX"
	else
		arg_4_0.nextTxt.text = "<color=#A9F548FF>" .. arg_4_1.exp .. "</color>/" .. arg_4_1.GetNextLevelExp()

	LoadSpriteAsync("skillicon/" .. arg_4_1.GetIcon(), function(arg_5_0)
		arg_4_0.icon.sprite = arg_5_0)

def var_0_0.Dispose(arg_6_0):
	return

return var_0_0

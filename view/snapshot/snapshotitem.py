local var_0_0 = class("SnapshotItem")

var_0_0.NAME_COLOR = {
	"#FFFFFFFF",
	"#5A9BFFFF"
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.go = arg_1_1
	arg_1_0.selected = arg_1_2
	arg_1_0.tr = arg_1_1.transform
	arg_1_0.btn = arg_1_1.GetComponent("Button")
	arg_1_0.nameTF = findTF(arg_1_0.tr, "Text")
	arg_1_0.nameTxt = arg_1_0.nameTF.GetComponent("Text")
	arg_1_0.unselectGo = findTF(arg_1_0.tr, "unselect").gameObject
	arg_1_0.selectedGo = findTF(arg_1_0.tr, "selected").gameObject
	arg_1_0.info = None
	arg_1_0.id = -1

	arg_1_0.selectedGo.SetActive(False)

def var_0_0.Update(arg_2_0, arg_2_1):
	arg_2_0.info = arg_2_1
	arg_2_0.id = arg_2_1.id

	arg_2_0.flush()

def var_0_0.UpdateSelected(arg_3_0, arg_3_1):
	arg_3_0.selected = arg_3_1

	arg_3_0.unselectGo.SetActive(not arg_3_0.selected)
	arg_3_0.selectedGo.SetActive(arg_3_0.selected)

	if arg_3_0.selected:
		arg_3_0.nameTxt.text = setColorStr(arg_3_0.info.name, arg_3_0.NAME_COLOR[2])
	else
		arg_3_0.nameTxt.text = setColorStr(arg_3_0.info.name, arg_3_0.NAME_COLOR[1])

def var_0_0.HasInfo(arg_4_0):
	return arg_4_0.info != None

def var_0_0.GetID(arg_5_0):
	return arg_5_0.id

def var_0_0.flush(arg_6_0):
	arg_6_0.nameTxt.text = arg_6_0.info.name

def var_0_0.SetEulerAngle(arg_7_0, arg_7_1):
	local var_7_0 = rtf(arg_7_0.nameTF).eulerAngles

	rtf(arg_7_0.nameTF).eulerAngles = Vector3(0, 0, arg_7_1)

def var_0_0.RotateUI(arg_8_0, arg_8_1, arg_8_2):
	LeanTween.rotateZ(go(arg_8_0.nameTF), arg_8_1, arg_8_2)

return var_0_0

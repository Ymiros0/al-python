local var_0_0 = class("BackYardFormationCard", import("view.ship.FormationCard"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.propsTr1 = arg_1_0.detailTF.Find("info1")
	arg_1_0.nameTr = arg_1_0.detailTF.Find("name_mask")
	arg_1_0.startTr = arg_1_0.content.Find("front/stars")

def var_0_0.updateProps(arg_2_0, arg_2_1):
	for iter_2_0 = 0, 4:
		local var_2_0 = arg_2_0.propsTr.GetChild(iter_2_0)

		if iter_2_0 < #arg_2_1:
			var_2_0.gameObject.SetActive(True)

			var_2_0.GetChild(0).GetComponent("Text").text = arg_2_1[iter_2_0 + 1][1]
			var_2_0.GetChild(1).GetComponent("Text").text = arg_2_1[iter_2_0 + 1][2]
		else
			var_2_0.gameObject.SetActive(False)

	setAnchoredPosition(arg_2_0.nameTr, {
		y = 270
	})
	setAnchoredPosition(arg_2_0.shipState, {
		y = 32
	})
	setAnchoredPosition(arg_2_0.startTr, {
		y = -14
	})
	setAnchoredPosition(arg_2_0.proposeMark, {
		y = 3.2
	})

def var_0_0.updateProps1(arg_3_0, arg_3_1):
	for iter_3_0 = 0, 2:
		local var_3_0 = arg_3_0.propsTr1.GetChild(iter_3_0)

		if iter_3_0 < #arg_3_1:
			var_3_0.gameObject.SetActive(True)

			var_3_0.GetChild(0).GetComponent("Text").text = arg_3_1[iter_3_0 + 1][1]
			var_3_0.GetChild(1).GetComponent("Text").text = arg_3_1[iter_3_0 + 1][2]
		else
			var_3_0.gameObject.SetActive(False)

	setAnchoredPosition(arg_3_0.nameTr, {
		y = 174
	})
	setAnchoredPosition(arg_3_0.shipState, {
		y = -64
	})
	setAnchoredPosition(arg_3_0.startTr, {
		y = -110
	})
	setAnchoredPosition(arg_3_0.proposeMark, {
		y = -92.8
	})

return var_0_0

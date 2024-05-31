local var_0_0 = class("IdolTrainUI", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "IdolTrainUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()
	setActive(arg_2_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.onTrain = None

	pg.UIMgr.GetInstance().UnblurPanel(arg_3_0._tf, arg_3_0._parentTF)

def var_0_0.InitUI(arg_4_0):
	arg_4_0.trainBtn = arg_4_0.findTF("panel/train_btn")
	arg_4_0.skills = arg_4_0.findTF("panel/skills")
	arg_4_0.info = arg_4_0.findTF("panel/info")
	arg_4_0.skillBtns = {}

	eachChild(arg_4_0.skills, function(arg_5_0)
		table.insert(arg_4_0.skillBtns, arg_5_0))

	arg_4_0.curBuff = arg_4_0.findTF("preview/current", arg_4_0.info)
	arg_4_0.nextBuff = arg_4_0.findTF("preview/next", arg_4_0.info)
	arg_4_0.currentBuffLv = arg_4_0.findTF("title/lv/current", arg_4_0.info)
	arg_4_0.nextBuffLv = arg_4_0.findTF("title/lv/next", arg_4_0.info)

def var_0_0.setCBFunc(arg_6_0, arg_6_1):
	arg_6_0.onTrain = arg_6_1

def var_0_0.set(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.buffInfos = arg_7_1
	arg_7_0.targetIndex = arg_7_2
	arg_7_0.selectIndex = None
	arg_7_0.selectBuffId = None
	arg_7_0.selectBuffLv = None
	arg_7_0.selectNewBuffId = None

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.skillBtns):
		onButton(arg_7_0, iter_7_1, function()
			for iter_8_0, iter_8_1 in ipairs(arg_7_0.buffInfos):
				if iter_7_0 == iter_8_1.group:
					if iter_8_1.next:
						arg_7_0.selectIndex = iter_7_0
						arg_7_0.selectBuffId = iter_8_1.id
						arg_7_0.selectNewBuffId = iter_8_1.next
						arg_7_0.selectBuffLv = iter_8_1.lv
					else
						arg_7_0.selectIndex = None
						arg_7_0.selectBuffId = None
						arg_7_0.selectNewBuffId = None
						arg_7_0.selectBuffLv = None

			arg_7_0.flush(), SFX_PANEL)

	onButton(arg_7_0, arg_7_0.trainBtn, function()
		if arg_7_0.onTrain and arg_7_0.selectBuffId:
			local var_9_0 = pg.benefit_buff_template[arg_7_0.selectBuffId].name

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = "是否要对" .. var_9_0 .. "进行训练" .. arg_7_0.selectBuffId,
				def onYes:()
					arg_7_0.onTrain(arg_7_0.targetIndex, arg_7_0.selectNewBuffId, arg_7_0.selectBuffId)
					arg_7_0.Destroy()
			}), SFX_PANEL)
	arg_7_0.flush()

def var_0_0.flush(arg_11_0):
	if arg_11_0.buffInfos:
		for iter_11_0, iter_11_1 in ipairs(arg_11_0.buffInfos):
			if iter_11_1.next:
				setText(arg_11_0.findTF("lv", arg_11_0.skillBtns[iter_11_1.group]), "Lv." .. iter_11_1.lv)
			else
				setText(arg_11_0.findTF("lv", arg_11_0.skillBtns[iter_11_1.group]), "MAX")

	for iter_11_2, iter_11_3 in ipairs(arg_11_0.skillBtns):
		if iter_11_2 == arg_11_0.selectIndex:
			setActive(arg_11_0.findTF("selected", iter_11_3), True)
		else
			setActive(arg_11_0.findTF("selected", iter_11_3), False)

	if arg_11_0.selectIndex:
		setActive(arg_11_0.info, True)
		setActive(arg_11_0.trainBtn, True)
		setText(arg_11_0.curBuff, pg.benefit_buff_template[arg_11_0.selectBuffId].desc)
		setText(arg_11_0.nextBuff, pg.benefit_buff_template[arg_11_0.selectNewBuffId].desc)
		setText(arg_11_0.nextBuffLv, "Lv." .. arg_11_0.selectBuffLv + 1)
		setText(arg_11_0.currentBuffLv, "Lv." .. arg_11_0.selectBuffLv)
	else
		setActive(arg_11_0.info, False)
		setActive(arg_11_0.trainBtn, False)

return var_0_0

local var_0_0 = class("SVDebugPanel", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "SVDebugPanel"

def var_0_0.OnLoaded(arg_2_0):
	return

def var_0_0.OnInit(arg_3_0):
	local var_3_0 = arg_3_0._tf

	arg_3_0.scrollRect = var_3_0.Find("scrollview").GetComponent(typeof(ScrollRect))
	arg_3_0.rtContent = var_3_0.Find("scrollview/viewport/content")
	arg_3_0.rtText = arg_3_0.rtContent.Find("text")
	arg_3_0.btnX = var_3_0.Find("panel/x")

	onButton(arg_3_0, arg_3_0.btnX, function()
		arg_3_0.Hide())

	local var_3_1 = var_3_0.Find("panel/buttons")
	local var_3_2 = var_3_1.Find("button")

	setActive(arg_3_0.rtText, False)
	setParent(arg_3_0.rtText, var_3_0, False)

	local var_3_3 = nowWorld()
	local var_3_4 = {
		{
			name = "清理打印",
			def func:()
				for iter_5_0 = arg_3_0.rtContent.childCount - 1, 0, -1:
					Destroy(arg_3_0.rtContent.GetChild(iter_5_0))
		},
		{
			name = "entity缓存",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("打印entity缓存信息：")

				local var_6_0 = {}

				for iter_6_0, iter_6_1 in pairs(WPool.pools):
					table.insert(var_6_0, iter_6_0.__cname .. " . " .. #iter_6_1)

				table.sort(var_6_0)

				for iter_6_2, iter_6_3 in ipairs(var_6_0):
					arg_3_0.AppendText(iter_6_3)

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "地图信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("当前大世界进度：")
				arg_3_0.AppendText(tostring(var_3_3.GetProgress()))
				arg_3_0.AppendText("")
				arg_3_0.AppendText("当前所在入口信息：")

				local var_7_0 = var_3_3.GetActiveEntrance()

				if var_7_0:
					arg_3_0.AppendText(var_7_0.DebugPrint())

				arg_3_0.AppendText("")
				arg_3_0.AppendText("当前所在地图信息：")

				local var_7_1 = var_3_3.GetActiveMap()

				if var_7_1:
					arg_3_0.AppendText(var_7_1.DebugPrint())

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "任务信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("任务信息：")

				local var_8_0 = var_3_3.GetTaskProxy().getTasks()

				for iter_8_0, iter_8_1 in pairs(var_8_0):
					arg_3_0.AppendText(iter_8_1.DebugPrint())

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "事件信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("事件信息：")

				local var_9_0 = var_3_3.GetActiveMap()

				if var_9_0:
					local var_9_1 = var_9_0.FindAttachments(WorldMapAttachment.TypeEvent)

					_.each(var_9_1, function(arg_10_0)
						arg_3_0.AppendText(arg_10_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "感染事件",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("感染事件：")

				local var_11_0 = var_3_3.GetActiveMap()

				if var_11_0:
					local var_11_1 = var_11_0.FindAttachments(WorldMapAttachment.TypeEvent)

					_.each(var_11_1, function(arg_12_0)
						if arg_12_0.config.infection_value > 0:
							arg_3_0.AppendText(arg_12_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "路标事件",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("路标事件：")

				local var_13_0 = var_3_3.GetActiveMap()

				if var_13_0:
					local var_13_1 = var_13_0.FindAttachments(WorldMapAttachment.TypeEvent)

					_.each(var_13_1, function(arg_14_0)
						if arg_14_0.IsSign():
							arg_3_0.AppendText(arg_14_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "舰队信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("打印舰队信息：")
				_.each(var_3_3.GetFleets(), function(arg_16_0)
					arg_3_0.AppendText(arg_16_0.DebugPrint()))
				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "敌人信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("打印敌人信息：")

				local var_17_0 = var_3_3.GetActiveMap()

				if var_17_0:
					local var_17_1 = var_17_0.FindEnemys()

					_.each(var_17_1, function(arg_18_0)
						arg_3_0.AppendText(arg_18_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "陷阱信息",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("打印陷阱信息：")

				local var_19_0 = var_3_3.GetActiveMap()

				if var_19_0:
					local var_19_1 = var_19_0.FindAttachments(WorldMapAttachment.TypeTrap)

					_.each(var_19_1, function(arg_20_0)
						arg_3_0.AppendText(arg_20_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "场景物件",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("当前所在地图场景物件信息：")

				local var_21_0 = var_3_3.GetActiveMap()

				if var_21_0:
					local var_21_1 = var_21_0.FindAttachments(WorldMapAttachment.TypeArtifact)

					_.each(var_21_1, function(arg_22_0)
						arg_3_0.AppendText(arg_22_0.DebugPrint()))

				arg_3_0.AppendText("-------------------------------------------------------------------------")
		},
		{
			name = "一键压制",
			def func:()
				arg_3_0.AppendText("-------------------------------------------------------------------------")
				arg_3_0.AppendText("当前地图压制啦")

				local var_23_0 = var_3_3.GetAtlas()

				var_23_0.AddPressingMap(var_23_0.activeMapId)
				arg_3_0.AppendText("-------------------------------------------------------------------------")
		}
	}
	local var_3_5 = UIItemList.New(var_3_1, var_3_2)

	var_3_5.make(function(arg_24_0, arg_24_1, arg_24_2)
		arg_24_1 = arg_24_1 + 1

		if arg_24_0 == UIItemList.EventUpdate:
			setText(arg_24_2.Find("Text"), var_3_4[arg_24_1].name)
			onButton(arg_3_0, arg_24_2, var_3_4[arg_24_1].func))
	var_3_5.align(#var_3_4)

def var_0_0.OnDestroy(arg_25_0):
	setParent(arg_25_0.rtText, arg_25_0.rtContent, False)

def var_0_0.Show(arg_26_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_26_0._tf)
	setActive(arg_26_0._tf, True)

def var_0_0.Hide(arg_27_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_27_0._tf, arg_27_0._parentTf)
	setActive(arg_27_0._tf, False)

def var_0_0.Setup(arg_28_0):
	return

def var_0_0.OnClickRichText(arg_29_0, arg_29_1, arg_29_2):
	if arg_29_1 == "ShipProperty":
		local var_29_0 = tonumber(arg_29_2)
		local var_29_1 = nowWorld().GetShipVO(var_29_0)

		assert(var_29_1, "ship not exist. " .. var_29_0)
		arg_29_0.AppendText("-------------------------------------------------------------------------")
		arg_29_0.AppendText("打印舰娘属性：")
		arg_29_0.AppendText(string.format("[%s] [id. %s] [config_id. %s]", var_29_1.getName(), var_29_1.id, var_29_1.configId))

		local var_29_2 = {
			{
				AttributeType.Durability,
				"耐久"
			},
			{
				AttributeType.Cannon,
				"炮击"
			},
			{
				AttributeType.Torpedo,
				"雷击"
			},
			{
				AttributeType.AntiAircraft,
				"防空"
			},
			{
				AttributeType.AntiSub,
				"反潜"
			},
			{
				AttributeType.Air,
				"航空"
			},
			{
				AttributeType.Reload,
				"装填"
			},
			{
				AttributeType.CD,
				"射速"
			},
			{
				AttributeType.Armor,
				"装甲"
			},
			{
				AttributeType.Hit,
				"命中"
			},
			{
				AttributeType.Speed,
				"航速"
			},
			{
				AttributeType.Luck,
				"幸运"
			},
			{
				AttributeType.Dodge,
				"机动"
			},
			{
				AttributeType.Expend,
				"消耗"
			},
			{
				AttributeType.Damage,
				"伤害"
			},
			{
				AttributeType.Healthy,
				"治疗"
			},
			{
				AttributeType.Speciality,
				"特性"
			},
			{
				AttributeType.Range,
				"射程"
			},
			{
				AttributeType.Angle,
				"射角"
			},
			{
				AttributeType.Scatter,
				"散布"
			},
			{
				AttributeType.Ammo,
				"弹药"
			},
			{
				AttributeType.HuntingRange,
				"狩猎范围"
			},
			{
				AttributeType.OxyMax,
				"氧气最大含量"
			},
			{
				AttributeType.OxyCost,
				"氧气秒消耗"
			},
			{
				AttributeType.OxyRecovery,
				"氧气秒恢复"
			},
			{
				AttributeType.OxyAttackDuration,
				"水面攻击持续时长"
			},
			{
				AttributeType.OxyRaidDistance,
				"水下攻击持续时长"
			},
			{
				AttributeType.SonarRange,
				"声呐范围"
			},
			{
				AttributeType.SonarInterval,
				"声呐间隔"
			},
			{
				AttributeType.SonarDuration,
				"声呐效果持续时间"
			}
		}
		local var_29_3 = var_29_1.getProperties()

		for iter_29_0, iter_29_1 in ipairs(var_29_2):
			local var_29_4

			if iter_29_1[1] == AttributeType.Armor:
				var_29_4 = var_29_1.getShipArmorName()
			else
				var_29_4 = var_29_3[iter_29_1[1]]

			if var_29_4:
				arg_29_0.AppendText(string.format("\t\t%s[%s] . <color=#A9F548>%s</color>", iter_29_1[1], iter_29_1[2], var_29_4))

		arg_29_0.AppendText("-------------------------------------------------------------------------")

def var_0_0.AppendText(arg_30_0, arg_30_1):
	local var_30_0 = cloneTplTo(arg_30_0.rtText, arg_30_0.rtContent, False)

	var_30_0.GetComponent("RichText").AddListener(function(arg_31_0, arg_31_1)
		arg_30_0.OnClickRichText(arg_31_0, arg_31_1))
	setText(var_30_0, arg_30_1)
	print(arg_30_1)

return var_0_0

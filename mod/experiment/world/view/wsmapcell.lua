﻿local var_0_0 = class("WSMapCell", import("...BaseEntity"))

var_0_0.Fields = {
	cell = "table",
	map = "table",
	maskTimer = "table",
	transform = "userdata",
	wsMapResource = "table",
	rtAttachments = "userdata",
	maskUid = "number",
	wsTimer = "table",
	rtFog = "userdata",
	fogTimer = "table",
	fogUid = "number",
	rtMask = "userdata"
}
var_0_0.Listeners = {
	onUpdate = "Update",
	onUpdateFogImage = "UpdateFogImage"
}

function var_0_0.GetResName()
	return "world_cell"
end

function var_0_0.GetName(arg_2_0, arg_2_1)
	return "cell_" .. arg_2_0 .. "_" .. arg_2_1
end

function var_0_0.Setup(arg_3_0, arg_3_1, arg_3_2)
	assert(arg_3_0.cell == nil)

	arg_3_0.map = arg_3_1
	arg_3_0.cell = arg_3_2

	arg_3_0.cell:AddListener(WorldMapCell.EventUpdateInFov, arg_3_0.onUpdate)
	arg_3_0.cell:AddListener(WorldMapCell.EventUpdateDiscovered, arg_3_0.onUpdate)
	arg_3_0.cell:AddListener(WorldMapCell.EventUpdateFog, arg_3_0.onUpdate)
	arg_3_0.cell:AddListener(WorldMapCell.EventUpdateFogImage, arg_3_0.onUpdateFogImage)
	arg_3_0:Init()
end

function var_0_0.Dispose(arg_4_0)
	if arg_4_0.fogTimer then
		arg_4_0.wsTimer:RemoveInMapTimer(arg_4_0.fogTimer)

		arg_4_0.fogTimer = nil
	end

	if arg_4_0.fogUid then
		arg_4_0.wsTimer:RemoveInMapTween(arg_4_0.fogUid)

		arg_4_0.fogUid = nil
	end

	if arg_4_0.maskTimer then
		arg_4_0.wsTimer:RemoveInMapTimer(arg_4_0.maskTimer)

		arg_4_0.maskTimer = nil
	end

	if arg_4_0.maskUid then
		arg_4_0.wsTimer:RemoveInMapTween(arg_4_0.maskUid)

		arg_4_0.maskUid = nil
	end

	clearImageSprite(arg_4_0.rtFog:Find("dark_fog"))
	clearImageSprite(arg_4_0.rtFog:Find("sairen_fog"))
	setCanvasGroupAlpha(arg_4_0.rtFog, 1)
	arg_4_0.cell:RemoveListener(WorldMapCell.EventUpdateInFov, arg_4_0.onUpdate)
	arg_4_0.cell:RemoveListener(WorldMapCell.EventUpdateDiscovered, arg_4_0.onUpdate)
	arg_4_0.cell:RemoveListener(WorldMapCell.EventUpdateFog, arg_4_0.onUpdate)
	arg_4_0.cell:RemoveListener(WorldMapCell.EventUpdateFogImage, arg_4_0.onUpdateFogImage)
	arg_4_0:Clear()
end

local function var_0_1(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	arg_5_0.anchoredPosition = arg_5_1.anchoredPosition + Vector2((arg_5_2.column % 3 - 1) * -arg_5_3.x, (arg_5_2.row % 3 - 1) * arg_5_3.y)
	arg_5_0.localScale = arg_5_1.localScale

	setImageSprite(arg_5_0, getImageSprite(arg_5_1), true)
end

function var_0_0.Init(arg_6_0)
	local var_6_0 = arg_6_0.map.theme
	local var_6_1 = arg_6_0.cell
	local var_6_2 = arg_6_0.transform

	var_6_2.name = var_0_0.GetName(var_6_1.row, var_6_1.column)
	var_6_2.anchoredPosition = var_6_0:GetLinePosition(var_6_1.row, var_6_1.column)
	var_6_2.sizeDelta = var_6_0.cellSize
	arg_6_0.rtAttachments = var_6_2:Find("attachments")
	arg_6_0.rtAttachments.localEulerAngles = Vector3(-var_6_0.angle, 0, 0)
	arg_6_0.rtMask = var_6_2:Find("mask")
	arg_6_0.rtMask.sizeDelta = var_6_0.cellSize + Vector2(WorldConst.LineCross * 2, WorldConst.LineCross * 2)
	arg_6_0.rtFog = var_6_2:Find("fog")

	local var_6_3 = arg_6_0.map.theme
	local var_6_4 = var_6_3.cellSize + var_6_3.cellSpace

	var_0_1(arg_6_0.rtFog:Find("dark_fog"), arg_6_0.wsMapResource.rtDarkFog:Find(WorldConst.Pos2FogRes(var_6_1.row, var_6_1.column)), var_6_1, var_6_4)
	var_0_1(arg_6_0.rtFog:Find("sairen_fog"), arg_6_0.wsMapResource.rtSairenFog:Find(WorldConst.Pos2FogRes(var_6_1.row, var_6_1.column)), var_6_1, var_6_4)
	arg_6_0:Update()
	arg_6_0:UpdateFogImage()
end

function var_0_0.Update(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0.cell
	local var_7_1 = arg_7_0.map.centerCellFOV
	local var_7_2 = 0
	local var_7_3 = 0
	local var_7_4 = 0

	if var_7_1 then
		var_7_3 = math.sqrt((var_7_1.row - var_7_0.row) * (var_7_1.row - var_7_0.row) + (var_7_1.column - var_7_0.column) * (var_7_1.column - var_7_0.column)) * 0.1
		var_7_4 = 0.2
	end

	if arg_7_1 == nil or arg_7_1 == WorldMapCell.EventUpdateInFov or arg_7_1 == WorldMapCell.EventUpdateFog then
		setActive(arg_7_0.rtAttachments, var_7_0:GetInFOV() and not var_7_0:InFog())
	end

	if arg_7_1 == nil or arg_7_1 == WorldMapCell.EventUpdateFog then
		if arg_7_0.fogTimer then
			arg_7_0.wsTimer:RemoveInMapTimer(arg_7_0.fogTimer)

			arg_7_0.fogTimer = nil
		end

		if arg_7_0.fogUid then
			arg_7_0.wsTimer:RemoveInMapTween(arg_7_0.fogUid)

			arg_7_0.fogUid = nil
		end

		if var_7_0:InFog() then
			if arg_7_1 and var_7_3 > 0 then
				setCanvasGroupAlpha(arg_7_0.rtFog, 0)

				arg_7_0.fogTimer = arg_7_0.wsTimer:AddInMapTimer(function()
					arg_7_0.fogUid = LeanTween.alphaCanvas(GetComponent(arg_7_0.rtFog, typeof(CanvasGroup)), 1, var_7_4).uniqueId

					arg_7_0.wsTimer:AddInMapTween(arg_7_0.fogUid)
				end, var_7_3)

				arg_7_0.fogTimer:Start()
			else
				setCanvasGroupAlpha(arg_7_0.rtFog, 1)
			end
		elseif arg_7_1 and var_7_3 > 0 then
			arg_7_0.fogTimer = arg_7_0.wsTimer:AddInMapTimer(function()
				arg_7_0.fogUid = LeanTween.alphaCanvas(GetComponent(arg_7_0.rtFog, typeof(CanvasGroup)), 0, var_7_4).uniqueId

				arg_7_0.wsTimer:AddInMapTween(arg_7_0.fogUid)
			end, var_7_3)

			arg_7_0.fogTimer:Start()
		else
			setCanvasGroupAlpha(arg_7_0.rtFog, 0)
		end
	end

	if arg_7_1 == nil or arg_7_1 == WorldMapCell.EventUpdateInFov or arg_7_1 == WorldMapCell.EventUpdateDiscovered then
		if arg_7_0.maskTimer then
			arg_7_0.wsTimer:RemoveInMapTimer(arg_7_0.maskTimer)

			arg_7_0.maskTimer = nil
		end

		if arg_7_0.maskUid then
			arg_7_0.wsTimer:RemoveInMapTween(arg_7_0.maskUid)

			arg_7_0.maskUid = nil
		end

		if var_7_0:GetInFOV() then
			if arg_7_1 and var_7_3 > 0 then
				arg_7_0.maskTimer = arg_7_0.wsTimer:AddInMapTimer(function()
					arg_7_0.maskUid = LeanTween.alpha(arg_7_0.rtMask, 0, var_7_4).uniqueId

					arg_7_0.wsTimer:AddInMapTween(arg_7_0.maskUid)
				end, var_7_3)

				arg_7_0.maskTimer:Start()
			else
				setImageAlpha(arg_7_0.rtMask, 0)
			end
		else
			local var_7_5 = var_7_0.discovered and 0.3 or 0.8

			if arg_7_1 and var_7_3 > 0 then
				arg_7_0.maskTimer = arg_7_0.wsTimer:AddInMapTimer(function()
					arg_7_0.maskUid = LeanTween.alpha(arg_7_0.rtMask, var_7_5, var_7_4).uniqueId

					arg_7_0.wsTimer:AddInMapTween(arg_7_0.maskUid)
				end, var_7_3)

				arg_7_0.maskTimer:Start()
			else
				setImageAlpha(arg_7_0.rtMask, var_7_5)
			end
		end
	end
end

function var_0_0.UpdateFogImage(arg_12_0)
	local var_12_0 = arg_12_0.cell:LookSairenFog()

	setImageAlpha(arg_12_0.rtFog:Find("dark_fog"), var_12_0 and 0 or 1)
	setImageAlpha(arg_12_0.rtFog:Find("sairen_fog"), var_12_0 and 1 or 0)
end

function var_0_0.GetWorldPos(arg_13_0)
	local var_13_0 = Vector3.New(arg_13_0.transform.localPosition.x, arg_13_0.transform.localPosition.y, 0)

	return arg_13_0.transform.parent:TransformPoint(var_13_0)
end

return var_0_0

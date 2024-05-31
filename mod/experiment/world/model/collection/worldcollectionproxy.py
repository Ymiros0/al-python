local var_0_0 = class("WorldCollectionProxy", import("....BaseEntity"))

var_0_0.Fields = {
	storyGroup = "table",
	data = "table",
	placeGroup = "table"
}
var_0_0.EventPlaceUnlock = "WorldCollectionProxy.EventPlaceUnlock"
var_0_0.WorldCollectionType = {
	FILE = 1,
	RECORD = 2
}
var_0_0.WorldCollectionTemplate = {}
var_0_0.WorldCollectionTemplateExtend = {}

for iter_0_0, iter_0_1 in ipairs(pg.world_collection_file_template.all):
	local var_0_1 = pg.world_collection_file_template[iter_0_1]

	if var_0_0.WorldCollectionTemplate[iter_0_1] != None:
		assert(False, "Repeat Collection UID " .. iter_0_1)

	var_0_0.WorldCollectionTemplate[iter_0_1] = var_0_1
	var_0_0.WorldCollectionTemplateExtend[iter_0_1] = var_0_0.WorldCollectionTemplateExtend[iter_0_1] or {}
	var_0_0.WorldCollectionTemplateExtend[iter_0_1].type = var_0_0.WorldCollectionType.FILE

for iter_0_2, iter_0_3 in ipairs(pg.world_collection_file_group.all):
	local var_0_2 = pg.world_collection_file_group[iter_0_3]

	for iter_0_4, iter_0_5 in ipairs(var_0_2.child):
		if var_0_0.WorldCollectionTemplate[iter_0_5] != None:
			var_0_0.WorldCollectionTemplateExtend[iter_0_5].group = var_0_2.id
		else
			assert(False, "Missing Collection FILE UID " .. iter_0_5)

for iter_0_6, iter_0_7 in ipairs(pg.world_collection_record_template.all):
	local var_0_3 = pg.world_collection_record_template[iter_0_7]

	if var_0_0.WorldCollectionTemplate[iter_0_7] != None:
		assert(False, "Repeat Collection UID " .. iter_0_7)

	var_0_0.WorldCollectionTemplate[iter_0_7] = var_0_3
	var_0_0.WorldCollectionTemplateExtend[iter_0_7] = var_0_0.WorldCollectionTemplateExtend[iter_0_7] or {}
	var_0_0.WorldCollectionTemplateExtend[iter_0_7].type = var_0_0.WorldCollectionType.RECORD

for iter_0_8, iter_0_9 in ipairs(pg.world_collection_record_group.all):
	local var_0_4 = pg.world_collection_record_group[iter_0_9]

	for iter_0_10, iter_0_11 in ipairs(var_0_4.child):
		if var_0_0.WorldCollectionTemplate[iter_0_11] != None:
			var_0_0.WorldCollectionTemplateExtend[iter_0_11].group = var_0_4.id
		else
			assert(False, "Missing Collection RECORD UID " .. iter_0_11)

def var_0_0.GetCollectionTemplate(arg_1_0):
	local var_1_0 = var_0_0.WorldCollectionTemplate[arg_1_0]

	assert(var_1_0, "Missing WorldCollection Config ID. " .. (arg_1_0 or "NIL"))

	return var_1_0

def var_0_0.GetCollectionType(arg_2_0):
	local var_2_0 = var_0_0.WorldCollectionTemplateExtend[arg_2_0]

	assert(var_2_0 and var_2_0.type, "Missing WorldCollection Type ID. " .. (arg_2_0 or "NIL"))

	return var_2_0.type

def var_0_0.GetCollectionGroup(arg_3_0):
	local var_3_0 = var_0_0.WorldCollectionTemplateExtend[arg_3_0]

	assert(var_3_0 and var_3_0.group, "Missing WorldCollection Type ID. " .. (arg_3_0 or "NIL"))

	return var_3_0.group

def var_0_0.GetCollectionFileGroupTemplate(arg_4_0):
	local var_4_0 = pg.world_collection_file_group[arg_4_0]

	assert(var_4_0, "Missing world_collection_file_group Config ID. " .. (arg_4_0 or "NIL"))

	return var_4_0

def var_0_0.GetCollectionFileTemplate(arg_5_0):
	local var_5_0 = pg.world_collection_file_template[arg_5_0]

	assert(var_5_0, "Missing world_collection_file_template Config ID. " .. (arg_5_0 or "NIL"))

	return var_5_0

def var_0_0.GetCollectionRecordGroupTemplate(arg_6_0):
	local var_6_0 = pg.world_collection_record_group[arg_6_0]

	assert(var_6_0, "Missing world_collection_record_group Config ID. " .. (arg_6_0 or "NIL"))

	return var_6_0

def var_0_0.GetCollectionRecordTemplate(arg_7_0):
	local var_7_0 = pg.world_collection_record_template[arg_7_0]

	assert(var_7_0, "Missing world_collection_record_template Config ID. " .. (arg_7_0 or "NIL"))

	return var_7_0

def var_0_0.Setup(arg_8_0, arg_8_1):
	arg_8_0.data = {}

	for iter_8_0, iter_8_1 in ipairs(arg_8_1):
		arg_8_0.data[iter_8_1] = True

def var_0_0.Unlock(arg_9_0, arg_9_1):
	if not arg_9_0.data[arg_9_1]:
		arg_9_0.data[arg_9_1] = True

def var_0_0.IsUnlock(arg_10_0, arg_10_1):
	return tobool(arg_10_0.data[arg_10_1])

return var_0_0

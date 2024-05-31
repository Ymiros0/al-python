local var_0_0 = class("PuzzleActivity", import("model.vo.Activity"))

function var_0_0.GetPicturePuzzleIds(arg_1_0)
	local var_1_0 = arg_1_0.id
	local var_1_1 = pg.activity_event_picturepuzzle[var_1_0]

	assert(var_1_1, "Can't Find activity_event_picturepuzzle 's ID : " .. (var_1_0 or "NIL"))

	local var_1_2 = Clone(var_1_1.pickup_picturepuzzle)

	table.insertto(var_1_2, var_1_1.drop_picturepuzzle)

	return var_1_2
end

return var_0_0

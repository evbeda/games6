
black_12 = [
    '        ',
    ' B B  B ',
    ' B      ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

white_12 = [
    'W     W ',
    '     W  ',
    ' W    W ',
    '   WB   ',
    'W  BW W ',
    '        ',
    '     B  ',
    'WW  W   ',
]
mix_6 = [
    '   B   W',
    ' W      ',
    '       B',
    '   WB   ',
    '   BW   ',
    'W       ',
    '     B  ',
    ' B     W',
]

mix_10 = [
    '   B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

flip_black = [
    'B  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

final_flip_black = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

flip_row_white = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'B B B   ',
    '     B  ',
    ' B     W',
]

final_flip_row_white = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'B B B   ',
    '     B  ',
    ' B     W',
]

diagonal_flip = [
    'B       ',
    ' B B  B ',
    ' BB     ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

final_diagonal_flip = [
    'W       ',
    ' W B  B ',
    ' BW     ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

validate_direction_1 = [
    [None, None, None, None, None, None, "B", "W"],
    [None, "W", None, None, None, None, None, None],
    [None, None, "B", None, None, None, None, 'B'],
    [None, None, None, "W", "B", None, None, None],
    [None, None, None, "B", "W", None, None, "W"],
    ["W", None, 'W', None, 'W', None, "B", None],
    [None, None, None, None, None, 'B', None, None],
    [None, 'B', None, None, None, None, None, "W"]]

validate_direction_2 = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, "W", None],
    ["W", None, None, None, None, None, "W", None],
    [None, "B", None, None, None, None, "W", None],
    ["W", "B", "B", None, None, None, "W", None],
    [None, None, None, "B", None, None, "W", None],
    [None, None, None, None, None, None, "W", None],
    [None, None, None, None, None, None, "B", None]]

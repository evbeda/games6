from .constants import GOLD, ROW, COL

SCENARIO_1 = [[None for j in range(COL)] for i in range(ROW)]
SCENARIO_1[0][0] = "J"

SCENARIO_2 = [[None for j in range(COL)] for i in range(ROW)]
SCENARIO_2[1][3] = "J"

SCENARIO_3 = [[None for j in range(COL)] for i in range(ROW)]
SCENARIO_3[3][5] = "J"

SCENARIO_4 = [[None for j in range(COL)] for i in range(ROW)]

SCENARIO_5 = [[None for j in range(COL)] for i in range(ROW)]
SCENARIO_5[2][4] = "J"


SCENARIO_TEST_GOLD = [[None for j in range(COL)] for i in range(ROW)]
SCENARIO_TEST_GOLD[2][4] = GOLD
SCENARIO_TEST_GOLD[4][5] = GOLD
SCENARIO_TEST_GOLD[7][14] = GOLD
SCENARIO_TEST_GOLD[3][4] = GOLD
SCENARIO_TEST_GOLD[6][4] = GOLD
SCENARIO_TEST_GOLD[5][5] = GOLD

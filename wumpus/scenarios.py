from .constants import GOLD, PLAYER, ROW, COL, WUMPUS

SCENARIO_1 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_1[0][0] = "J"

SCENARIO_2 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_2[1][3] = "J"

SCENARIO_3 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_3[3][5] = "J"

SCENARIO_4 = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_5 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_5[2][4] = "J"

SCENARIO_TEST_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_TEST_GOLD[2][4] = GOLD
SCENARIO_TEST_GOLD[4][5] = GOLD
SCENARIO_TEST_GOLD[7][14] = GOLD
SCENARIO_TEST_GOLD[3][4] = GOLD
SCENARIO_TEST_GOLD[6][4] = GOLD
SCENARIO_TEST_GOLD[5][5] = GOLD


SCENARIO_TEST_DELETE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_TEST_DELETE[5][5] = GOLD
SCENARIO_TEST_DELETE[7][8] = WUMPUS
SCENARIO_TEST_DELETE[7][14] = WUMPUS
SCENARIO_TEST_DELETE[2][10] = GOLD
SCENARIO_TEST_DELETE[3][4] = PLAYER

# include in this scenario the signal of danger when they are already encoded
SCENARIO_DANGER_SIGNAL_HOLES = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_SIGNAL_HOLES[0][0] = "J"
SCENARIO_DANGER_SIGNAL_HOLES[1][1] = "O"

SCENARIO_DANGER_LEFT_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_LEFT_DOWN[0][0] = "J"
SCENARIO_DANGER_LEFT_DOWN[7][0] = "O"

SCENARIO_DANGER_RIGTH_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH_DOWN[0][0] = "J"
SCENARIO_DANGER_RIGTH_DOWN[7][7] = "O"

SCENARIO_DANGER_RIGTH_UP = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH_UP[0][0] = "J"
SCENARIO_DANGER_RIGTH_UP[0][7] = "O"

SCENARIO_DANGER_LEFT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_LEFT[0][0] = "J"
SCENARIO_DANGER_LEFT[4][0] = "O"

SCENARIO_DANGER_RIGTH = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH[0][0] = "J"
SCENARIO_DANGER_RIGTH[4][7] = "O"

SCENARIO_DANGER_UP = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_UP[0][0] = "J"
SCENARIO_DANGER_UP[0][4] = "O"

SCENARIO_DANGER_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_DOWN[0][0] = "J"
SCENARIO_DANGER_DOWN[7][4] = "O"

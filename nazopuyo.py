import puyopuyo as pypy


def solve(field_str, tsumo_str, q_type, q_require):
    t_loop = len(tsumo_str) / 2;

    for i in range(t_loop):
        a_col = tsumo_str[i * 2]
        c_col = tsumo_str[i * 2 + 1]
        for p_key in pypy.CHILD_POSITION.keys():
            if (a_col == c_col) and (p_key == "BOTTOM" or p_key == "LEFT"):
                continue

            for a_x in range(6):
                if (a_x == 0) and (p_key == "LEFT"):
                    continue
                if (a_x == 5) and (p_key == "RIGHT"):
                    continue

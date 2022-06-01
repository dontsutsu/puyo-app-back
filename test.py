import nazopuyo

if __name__ == '__main__':
    field_str = "000000000000000000000000000000000000000000000000000000000000000000000000000000"
    tsumo_str = "12121212"
    q_type = "1"
    q_require = "2"

    answer_list = nazopuyo.solve(field_str, tsumo_str, q_type, q_require)

    print(len(answer_list))
    print(answer_list)
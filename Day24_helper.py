def helper1(gate_connections: list[str], input_size: int) -> None:
    """Для всех возможных inputs сверяет outputs ASIS с TOBE."""
    lst1 = []
    for input_x in range(2**input_size):
        for input_y in range(2 ** input_size):

            output_tobe = input_x + input_y

            wires = get_wires(input_x, input_y)
            output_asis = part1(wires, gate_connections)

            output_tobe = f"{bin(output_tobe)[2:]:0>{input_size}}"
            output_asis = f"{bin(output_asis)[2:]:0>{input_size}}"

            lst2 = []
            for i in range(input_size):
                lst2.append(output_tobe[-(i+1)] == output_asis[-(i+1)])
            lst1.append(lst2)

    for i, smth in enumerate(zip(*lst1)):
        if all(smth):
            print(f"z{i:02} good")
        else:
            print(f"z{i:02} bad")


def helper2(init_wire_values, gate_connections, input_size: int):
    """
    z00 good
    z01 good
    z02 good
    z03 good
    z04 good
    z05 good
    z06 good
    z07 good
    z08 good
    z09 good
    z10 good
    z11 good
    z12 good
    z13 good
    z14 good
    z15 good
    z16 good
    z17 good
    z18 good
    z19 good
    z20 good
    z21 good
    z22 good
    z23 good
    z24 bad
    z25 bad
    z26 bad
    z27 good
    z28 good
    z29 good
    z30 good
    z31 good
    z32 bad
    z33 bad
    z34 bad
    z35 bad
    z36 good
    z37 good
    z38 good
    z39 good
    z40 good
    z41 good
    z42 good
    z43 good
    z44 good
    """
    x = []
    y = []
    for bit_index in range(input_size):
        x_bit = f"x{bit_index:02}"
        y_bit = f"y{bit_index:02}"
        x.append(init_wire_values[x_bit])
        y.append(init_wire_values[y_bit])
    x = int("".join(map(str, reversed(x))), 2)
    y = int("".join(map(str, reversed(y))), 2)

    z_tobe = x + y
    z_asis = part1(init_wire_values, gate_connections)

    z_tobe = f"{bin(z_tobe)[2:]:0>{input_size}}"
    z_asis = f"{bin(z_asis)[2:]:0>{input_size}}"

    for i in range(input_size):
        if z_tobe[-(i+1)] != z_asis[-(i+1)]:
            print(f"z{i:02} bad")
        else:
            print(f"z{i:02} good")

"""
z07 <-> nqk
fgt <-> pcp
z24 <-> fpq
z32 <-> srn
"""
import os


INPUT_DATA_PATH = os.path.join("data", "day24_v4.txt")

INPUT_SIZE = 45


def parse_data(text: str) -> tuple[dict[str, int], list[str]]:

    init_wire_values, gate_connections = text.split("\n\n")
    init_wire_values = {
        init_wire_value[:3]: int(init_wire_value[-1])
        for init_wire_value in init_wire_values.split("\n")
    }
    gate_connections = gate_connections.split("\n")

    return init_wire_values, gate_connections


def part1(wires: dict[str, int], gate_connections: list[str]) -> int:

    wires = wires.copy()

    while gate_connections:
        done = set()
        for gate_connection in gate_connections:
            input_left, gate, input_right, _, output = gate_connection.split()
            if input_left in wires and input_right in wires:
                match gate:
                    case "AND":
                        wires[output] = wires[input_left] & wires[input_right]
                    case "OR":
                        wires[output] = wires[input_left] | wires[input_right]
                    case "XOR":
                        wires[output] = wires[input_left] ^ wires[input_right]
                done.add(gate_connection)
        gate_connections = list(filter(lambda x: x not in done, gate_connections))

    z_wires = sorted([wire for wire in wires if wire.startswith("z")], reverse=True)
    z_values = [str(wires[z_wire]) for z_wire in z_wires]
    output = int("".join(z_values), 2)

    return output


def get_wires(input_x: int, input_y: int) -> dict[str, int]:

    input_x = f"{bin(input_x)[2:]:0>{INPUT_SIZE}}"
    input_y = f"{bin(input_y)[2:]:0>{INPUT_SIZE}}"

    wires = dict()
    for i, bit in enumerate(reversed(input_x)):
        wires[f"x{i:02}"] = int(bit)
    for i, bit in enumerate(reversed(input_y)):
        wires[f"y{i:02}"] = int(bit)

    return wires


def part2(gate_connections: list[str]):
    """
    https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
    """
    forward = dict()
    backward = dict()
    for gate_connection in gate_connections:
        input_left, gate, input_right, _, output = gate_connection.split()
        forward[(frozenset((input_left, input_right)), gate)] = output
        backward[output] = (frozenset((input_left, input_right)), gate)

    swapped = []
    c_out_bits = dict()
    for bit_index in range(45):

        print(f"bit {bit_index:02}")

        # 1-bit half adder
        if bit_index == 0:
            x_bit = "x00"
            y_bit = "y00"
            z_bit = "z00"

            xor1 = forward[(frozenset((x_bit, y_bit)), "XOR")]
            if xor1 != z_bit:
                swapped.extend([z_bit, xor1])
                forward[backward[xor1]], forward[backward[z_bit]] = forward[backward[z_bit]], forward[backward[xor1]]
                backward[z_bit], backward[xor1] = backward[xor1], backward[z_bit]

            and1 = forward[(frozenset((x_bit, y_bit)), "AND")]
            c_out_bits[bit_index] = and1

        # 1-bit full adder
        else:
            x_bit = f"x{bit_index:02}"
            y_bit = f"y{bit_index:02}"
            z_bit = f"z{bit_index:02}"
            c_in_bit = c_out_bits[bit_index-1]

            xor1 = forward[(frozenset((x_bit, y_bit)), "XOR")]
            and1 = forward[(frozenset((x_bit, y_bit)), "AND")]

            # проверка XOR_1
            inputs, gate = backward[z_bit]
            if gate != "XOR":
                anti_z_bit = forward[(frozenset((xor1, c_in_bit)), "XOR")]
                swapped.extend([z_bit, anti_z_bit])
                print(f"{swapped=}")
                # swap
                forward[backward[z_bit]], forward[backward[anti_z_bit]] = forward[backward[anti_z_bit]], forward[backward[z_bit]]
                backward[z_bit], backward[anti_z_bit] = backward[anti_z_bit], backward[z_bit]
            elif xor1 not in inputs:
                if c_in_bit not in inputs:
                    print("пока хз, что делать")
                else:
                    anti_xor1, = inputs - {c_in_bit}
                    swapped.extend([xor1, anti_xor1])
                    print(f"{swapped=}")
                    # swap
                    forward[backward[xor1]], forward[backward[anti_xor1]] = forward[backward[anti_xor1]], forward[backward[xor1]]
                    backward[xor1], backward[anti_xor1] = backward[anti_xor1], backward[xor1]
                    xor1 = anti_xor1

            and2 = forward[(frozenset((xor1, c_in_bit)), "AND")]
            or3 = forward[(frozenset((and1, and2)), "OR")]

            c_out_bits[bit_index] = or3

    return


def helper2(init_wire_values, gate_connections, input_size: int):

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


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    init_wire_values, gate_connections = parse_data(text)

    # part1_result = part1(init_wire_values, gate_connections)
    # part2_result = part2(gate_connections)
    # helper2(init_wire_values, gate_connections, INPUT_SIZE)

    # print(part1_result)
    # print(part2_result)

    print(",".join(sorted(["z07", "nqk", "fgt", "pcp", "z24", "fpq", "z32", "srn"])))

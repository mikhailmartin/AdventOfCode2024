import os


INPUT_DATA_PATH = os.path.join("data", "day24.txt")


def parse_data(text: str) -> tuple[list[str], list[str]]:

    init_wire_values, gate_connections = text.split("\n\n")
    init_wire_values = init_wire_values.split("\n")
    gate_connections = gate_connections.split("\n")

    return init_wire_values, gate_connections


def part1(text: str) -> int:

    init_wire_values, gate_connections = parse_data(text)

    wires = dict()
    for init_wire_value in init_wire_values:
        wire, value = init_wire_value.split(": ")
        wires[wire] = int(value)

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


def part2(text: str):
    """
    https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
    """
    _, gate_connections = parse_data(text)

    forward = dict()
    backward = dict()
    for gate_connection in gate_connections:
        input_left, gate, input_right, _, output = gate_connection.split()
        forward[(frozenset((input_left, input_right)), gate)] = output
        backward[output] = (frozenset((input_left, input_right)), gate)

    swapped = []
    c_out_bits = dict()
    for bit_index in range(45):

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
            c_out_bits[0] = and1

        # 1-bit full adder
        else:
            x_bit = f"x{bit_index:02}"
            y_bit = f"y{bit_index:02}"
            z_bit = f"z{bit_index:02}"
            c_in_bit = c_out_bits[bit_index-1]

            xor1 = forward[(frozenset((x_bit, y_bit)), "XOR")]
            ...

            and1 = forward[(frozenset((x_bit, y_bit)), "AND")]

            xor2 = forward[(frozenset((xor1, c_in_bit)), "XOR")]
            if xor2 != z_bit:
                swapped.extend([z_bit, xor2])

            and2 = forward.get((frozenset((xor1, c_in_bit)), "AND"), "not found")
            if and2 == "not found":
                ...  # TODO

            or3 = forward.get((frozenset((and1, and2)), "OR"), "not found")
            if or3 == "not found":
                ...  # TODO

    return


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    # part1_result = part1(text)
    part2_result = part2(text)

    # print(part1_result)
    print(part2_result)

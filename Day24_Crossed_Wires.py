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


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)

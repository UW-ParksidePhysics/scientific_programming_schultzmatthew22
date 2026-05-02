def parse_constants_file(filename):
    constants = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    for i, part in enumerate(parts):
                        try:
                            value = float(part)
                            name = ' '.join(parts[:i])
                            constants[name] = value
                            break
                        except ValueError:
                            continue
                except (ValueError, IndexError):
                    continue
    return constants


if __name__ == '__main__':
    filename = 'constants.txt'
    constants_dict = parse_constants_file(filename)

    print(f"Total constants parsed: {len(constants_dict)}")
    for name, val in constants_dict.items():
        print(f"{name}: {val}")
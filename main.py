coordinates = [
    (1, 1),
    (2, 7),
    (12, 2),
    (4, 4),
    (6, 5),
    (2, 5),
    (2, 2),
    (7, 3)
]


def check_coord(data):
    clear_coord = []
    for i in range(len(data)):
        if data.count(data[i]) == 1:
            clear_coord.append(data[i])

    return clear_coord


def main(coord):
    raw_cell_coord = []
    ln = len(coord)

    for i in range(ln - 1):
        for j in range(i + 1, ln):
            x_1 = coord[i][0]
            y_1 = coord[i][1]
            x_2 = coord[j][0]
            y_2 = coord[j][1]

            a = y_2 - y_1
            b = x_1 - x_2
            c = x_1 * y_2 - y_1 * x_2

            sign_dict = {
                "+": 0,
                "-": 0
            }

            for k in range(ln):
                if k != i and k != j:
                    x = coord[k][0]
                    y = coord[k][1]

                    sign = a * x + b * y - c

                    if sign > 0:
                        sign_dict["+"] += 1
                    if sign < 0:
                        sign_dict["-"] += 1

            if abs(sign_dict["+"] - sign_dict["-"]) == max(sign_dict["+"], sign_dict["-"], 1):
                point_1 = coord[i]
                point_2 = coord[j]

                if point_1 in raw_cell_coord:
                    raw_cell_coord.append(point_2)
                else:
                    raw_cell_coord.append(point_1)

    return check_coord(raw_cell_coord)


cell_coord = main(coordinates)
print(cell_coord)

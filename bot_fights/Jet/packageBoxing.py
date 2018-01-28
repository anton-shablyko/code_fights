def packageBoxing(pkg, boxes):
    pkg = sorted(pkg)
    boxes = [sorted(i) for i in boxes]

    if pkg in boxes:  # check if complete match
        return boxes.index(pkg)

    available_boxes = valid_boxes(pkg, boxes)  # check what boxes are available

    if not available_boxes:
        return -1

    elif len(available_boxes) == 1:
        return boxes.index(available_boxes[0][0])

    else:
        sort_vol = sorted(available_boxes, key=lambda x: x[1])
        final_box = sort_vol[0][0]
        return boxes.index(final_box)


def valid_boxes(pkg, boxes):
    temp_boxes = []
    for box in boxes:
        box_vol = box[0] * box[1] * box[2]
        sub = [b - p for b, p in zip(box, pkg) if (b - p) >= 0]
        if len(sub) == 3:
            temp_boxes.append([box, box_vol])
    return temp_boxes



pkg = [4, 2, 5]
boxes = [[5, 3, 5], [5, 2, 5], [7,8,9]]

print(packageBoxing(pkg, boxes))

"""
Before delivery, all orders at Jet are packed into boxes to protect them from damage.

Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. The package should fit inside the box, keeping in mind that the size of the package should not exceed the size of the box in any dimension (note that the package can be rotated to fit and it can be positioned upside down). For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.

Given a package pkg and available boxes, find the 0-based index of the smallest-by-volume box such that the package fits inside it, or return -1 if there is no such box.

Example

For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be
packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60) is greater than the volume of the second (5 * 5 * 2 = 50).

For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be
packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, but the first box is chosen because it has less volume overall.

For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be
packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer pkg

Array of three positive integers denoting the size of the package as its width, height and length.

Guaranteed constraints:
1 ≤ pkg[i] ≤ 500.

[input] array.array.integer boxes

Every box is given as an array of three positive integers denoting its width, height and length.
It is guaranteed that each box has a unique volume.

Guaranteed constraints:
0 ≤ boxes.length ≤ 15,
1 ≤ boxes[i][j] ≤ 500.

[output] integer

The 0-based index of the smallest-by-volume box such that the package fits inside it, or -1 if there is no such box.
"""
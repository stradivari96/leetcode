"""
Given a list of order requirements and a list of flasks with their measurements,
write an algorithm to determine the single type of flask that will result
in minimal waste.

Waste is the sum of marking - requirement for each order.
Output the zero-based index of the flask type chosen.
If there are multiple answers, output the minimum index.
If no flask will satisfy the constraints, output -1.

requirements, a list of integers representing the requirements for the orders;
flaskTypes, an integer representing the number of flask types;
totalMarks, an integer representing the total number of markings;
markings, a list of pairs of integers where the first integer represents the index of the flask and second represents the one mark.

Return an integer representing the index of the flask to choose or return -1 if none will work.
"""


def choose_flask(requirements, markings):
    flasks = {}

    def calculate_loss(f):
        loss = 0
        for req in requirements:
            if req > flasks[f][-1]:
                return float("inf")
            else:
                loss += min([m for m in flasks[f] if m >= req]) - req
        return loss

    for f, mark in markings:
        if f not in flasks:
            flasks[f] = [mark]
        else:
            flasks[f].append(mark)
    best_flask = 0
    best_loss = float("inf")
    for f, marks in flasks.items():
        loss = calculate_loss(f)
        if loss < best_loss:
            best_flask = f
            best_loss = loss
    return best_flask


if __name__ == "__main__":
    assert (
        choose_flask(
            [4, 6, 6, 7],
            [[0, 3], [0, 5], [0, 7], [1, 6], [1, 8], [1, 9], [2, 3], [2, 5], [2, 6]],
        )
        == 0
    )

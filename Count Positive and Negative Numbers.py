def count_pos_neg(count):

    positive = 0
    negative = 0

    for i in count:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
    return positive,negative

count_pos_neg([1,-2,3,-4,5,0])

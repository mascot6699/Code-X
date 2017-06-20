def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:  # Leaf.
        return partial_path_sum
    # Non-leaf.
    return (sum_root_to_leaf(tree.left, partial_path_sum) +
            sum_root_to_leaf(tree.right, partial_path_sum))


def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    return (has_path_sum(tree.left, remaining_weight - tree.data) or
            has_path_sum(tree.right, remaining_weight - tree.data))



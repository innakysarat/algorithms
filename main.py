import queue


class TreeNode:

    def __init__(self, key: int, level=0):
        self.key = key
        self.left = None
        self.right = None
        #self.parent = parent
        self.level = level


def get_pre_ind():
    return build_tree.pre_index


def inc_pre_ind():
    build_tree.pre_index += 1


def build_tree(pre: list, index: int, low: int, high: int):

    if low > high:
        return None

    root = TreeNode(key=pre[get_pre_ind()], level=index)
    inc_pre_ind()

    if low == high:
        return root

    r_child_ind = -1
    for i in range(low, high+1):
        if pre[i] > root.key:
            r_child_ind = i
            break

    if r_child_ind == -1:
        r_child_ind = get_pre_ind() + (high - low)

    root.left = build_tree(pre, index+1, get_pre_ind(), r_child_ind-1)
    root.right = build_tree(pre, index+1, r_child_ind, high)

    return root


def get_level_order_keys_and_levels(preorder_keys: list):
    build_tree.pre_index = 0
    root = build_tree(preorder_keys, 0, 0, len(preorder_keys) - 1)

    keys = list()
    levels = list()
    q = queue.Queue()

    q.put(root)
    while not q.empty():
        current = q.get()
        keys.append(current.key)
        levels.append(current.level)
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)

    return keys, levels


def solution():
    preorder_keys = [5, 3, 1, 4, 7, 9]
    level_order_keys, levels = get_level_order_keys_and_levels(preorder_keys)
    print(' '.join(map(str, level_order_keys)))
    print(' '.join(map(str, levels)))


if __name__ == '__main__':
    solution()


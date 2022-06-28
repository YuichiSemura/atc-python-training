from collections import defaultdict, deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self, debug=False):
        self.root = None
        self.nodes = defaultdict(list)
        self.debug = debug

    def insert(self, key):
        if self.debug:
            print(f"---insert : {key}---")
        if self.root is None:
            self.root = Node(key)
            return
        nd, st = self.searchNode(key)
        if key < nd.key:
            nd.left = Node(key)
        else:
            nd.right = Node(key)
        # 調整
        nn = st.pop()
        while(nn):
            ld = self.get_depth(nn.left)
            rd = self.get_depth(nn.right)
            mlr = abs(ld-rd)
            if mlr == 0:
                return
            elif mlr == 1:
                nd, nn = nn, st.pop()
            else:
                # 回転
                one = ld > rd
                checknd = nn.left if one else nn.right
                two = self.get_depth(
                    checknd.left) > self.get_depth(checknd.right)
                self.rotate(one, two, nn)

    def rotate(self, one, two, nn):
        nd = nn.left if one else nn.right
        if one and two:
            if self.debug:
                print("---rotate : LL---")
            nn.key, nd.key = nd.key, nn.key
            nn.left, nd.left, nd.right, nn.right = nd.left, nd.right, nn.right, nn.left
        elif one and not two:
            if self.debug:
                print("---rotate : LR---")
            ne = nd.right
            nn.key, ne.key = ne.key, nn.key
            nd.right, nn.right, ne.left, ne.right = ne.left, nd.right, ne.right, nn.right
        elif not one and two:
            if self.debug:
                print("---rotate : RL---")
            ne = nd.left
            nn.key, ne.key = ne.key, nn.key
            nd.left, nn.left, ne.left, ne.right = ne.right, nd.left, nn.left, ne.left
        elif not one and not two:
            if self.debug:
                print("---rotate : RR---")
            nn.key, nd.key = nd.key, nn.key
            nn.left, nd.left, nd.right, nn.right = nn.right, nn.left, nd.left, nd.right

    def get_depth(self, node):
        if not node:
            return 0
        return max(self.get_depth(node.left) + 1, self.get_depth(node.right) + 1)

    def searchNode(self, key):
        nd = self.root
        st = deque()
        st.append(None)
        while(True):
            nn = nd.left if nd.key >= key else nd.right
            if nn is None:
                break
            st.append(nd)
            nd = nn
        return nd, st

    def search(self, key):
        nd, _ = self.searchNode(key)
        return nd.key

    def delete(self, key):
        if self.debug:
            print(f"---delete : {key}---")
        nd = self.root
        st = deque()
        st.append(None)
        while(True):
            if nd.key == key:
                break
            ne = nd.left if nd.key >= key else nd.right
            if ne is None:
                # 見つからない場合
                return
            nn = nd
            nd = ne
            st.append(nn)
        if nd.left is None and nd.right is None:
            if nd == self.root:
                self.root = None
            elif nn.left == nd:
                nn.left = None
            else:
                nn.right = None
        elif nd.left is not None and nd.right is None:
            if nd == self.root:
                self.root = nd.left
            elif nn.left == nd:
                nn.left = nd.left
            else:
                nn.right = nd.left
        elif nd.right is not None and nd.left is None :
            if nd == self.root:
                self.root = nd.right
            elif nn.left == nd:
                nn.left = nd.right
            else:
                nn.right = nd.right
        else:
            dl = nd.left
            while True:
                if not dl.right:
                    break
                st.append(dl)
                dl = dl.right
            if dl == nd.left:
                nd.key, nd.left = dl.key, dl.left
            else:
                ne = st.pop()
                nd.key, ne.right = dl.key, dl.left
                st.append(ne)
        # 回転
        nn = st.pop()
        while(nn):
            ld = self.get_depth(nn.left)
            rd = self.get_depth(nn.right)
            mlr = abs(ld-rd)
            if mlr == 0:
                return
            elif mlr == 1:
                nd, nn = nn, st.pop()
            else:
                # 回転
                one = ld > rd
                checknd = nn.left if one else nn.right
                two = self.get_depth(checknd.left) > self.get_depth(checknd.right)
                self.rotate(one, two, nn)

    def get_tree_structure(self, tree, depth, width):
        if len(self.nodes) < depth + 1:
            self.nodes.append([None]*(2 ** depth))
        if tree is None:
            return
        self.nodes[depth][width] = tree.key
        self.get_tree_structure(tree.left, depth + 1, width * 2)
        self.get_tree_structure(tree.right, depth + 1, width * 2 + 1)

    def display_tree(self):
        self.nodes = list()
        self.get_tree_structure(self.root, 0, 0)
        depth = len(self.nodes)
        print("".join(["-"]*(2 ** (depth+1)+8)))
        for d in range(depth):
            if d == 0:
                print("root   :", end="")
            else:
                print("depth {}:".format(d), end="")
            for node in self.nodes[d]:
                print("".join([" "]*(2 ** (depth-d)-1)), end="")
                if not node:
                    print(" x".format(node), end=" ")
                else:
                    print("{0:2d}".format(node), end=" ")
                print("".join([" "]*(2 ** (depth-d)-2)), end="")
            print()

    def get_sorted_list(self):
        l = []

        def print_recursive(nd, l):
            if not nd:
                return
            print_recursive(nd.left, l)
            l.append(str(nd.key))
            print_recursive(nd.right, l)
        print_recursive(self.root, l)
        return l


def main():

    tree = AVLTree()
    tree.insert(25)
    # tree.display_tree()
    tree.insert(15)
    # tree.display_tree()
    tree.insert(20)
    # tree.display_tree()
    tree.insert(30)
    # tree.display_tree()
    tree.insert(13)
    # tree.display_tree()
    tree.insert(12)
    # tree.display_tree()
    tree.insert(11)
    # tree.display_tree()
    tree.insert(8)
    # tree.display_tree()
    tree.insert(27)
    # tree.display_tree()
    tree.insert(50)
    # tree.display_tree()
    tree.insert(60)
    # tree.display_tree()
    tree.insert(29)
    # tree.display_tree()
    tree.insert(28)
    # tree.display_tree()
    tree.insert(10)
    # tree.display_tree()
    tree.insert(7)
    # tree.display_tree()
    tree.insert(70)
    tree.display_tree()
    print(" ".join(tree.get_sorted_list()))
    # delete
    tree.delete(25)
    # tree.display_tree()
    tree.delete(60)
    # tree.display_tree()
    tree.delete(30)
    # tree.display_tree()
    tree.delete(20)
    # tree.display_tree()
    tree.delete(8)
    # tree.display_tree()
    tree.delete(11)
    # tree.display_tree()
    tree.delete(13)
    # tree.display_tree()
    tree.delete(10)
    # tree.display_tree()
    tree.delete(7)
    # tree.display_tree()
    tree.delete(29)
    # tree.display_tree()
    tree.delete(50)
    # tree.display_tree()
    tree.delete(70)
    # tree.display_tree()
    tree.delete(27)
    # tree.display_tree()
    tree.delete(29)
    tree.delete(30)
    tree.display_tree()
    print(" ".join(tree.get_sorted_list()))


if __name__ == '__main__':
    main()

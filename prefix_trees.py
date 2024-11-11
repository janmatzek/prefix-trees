from mock_data import MOCK_DATA


class PrefixTreeNode:
    """Defines the structure of a node"""

    def __init__(self):
        self.children: dict = {}
        self.phone_number: str | None = None


class PrefixTree:
    """Prefix tree for storing and accessing the data"""

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, name: str, phone_number: str) -> bool:
        # start at the root of the trie/prefix tree
        node: PrefixTreeNode = self.root

        # avoid case sensitivity of names
        name = name.lower()

        for char in name:
            # if char is not a child of the node, add it
            if char not in node.children:
                node.children[char] = PrefixTreeNode()

            # move to the next node (deeper into the trie)
            node = node.children[char]

        # check if final node already has a phone number
        if node.phone_number:
            return False

        # add the phone number to the final node
        node.phone_number = phone_number
        return True

    def find_node(self, input) -> PrefixTreeNode:
        """Finds the last node corresponding to the input"""

        # avoid case sensitivity of names
        input = input.lower()

        # start at the root
        node: PrefixTreeNode = self.root

        for char in input:
            if char not in node.children:
                raise ValueError("Name not in the database")

            node = node.children[char]

        return node

    def find_all_numbers(self, node: PrefixTreeNode) -> list[str]:
        """Finds all phone numbers in the subtree of the given node"""

        numbers: list[str] = []

        if node.phone_number:
            numbers.append(node.phone_number)

        for child_node in node.children.values():  # .values gets all the child nodes
            numbers.extend(self.find_all_numbers(child_node))

        return numbers


# innitialize the "database" and fill it with mock data
db = PrefixTree()
for entry in MOCK_DATA:
    db.insert(entry["name"], entry["phone_number"])


def search_contact(name: str) -> list[str]:
    """Search the databse for names starting with name and returns a list of phone numbers"""
    try:
        node: PrefixTreeNode = db.find_node(name)
        return db.find_all_numbers(node)
    except ValueError as e:
        print(e)  # imagine a logger here
        return []


def add_contact(name: str, number: str) -> bool:
    """Add a new contact to the database
    Returns True if the contact was added successfully, False otherwise
    """
    return db.insert(name, number)

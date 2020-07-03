from collections import defaultdict
 # A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.insert("/", handler)

    def insert(self, path, handler):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
        road_listing = self.split_path(path)
        active_node = self.root
        for path in road_listing:
            active_node = active_node.children[path]
        active_node.handler = handler


    def find(self, path):
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
        road_listing = self.split_path(path)
        active_node = self.root
        for path in road_listing:
            if path not in active_node.children:
                return
            active_node = active_node.children[path]
        return active_node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
            road_listing = path.split("/")
            road_listing[0] = "/"
            if road_listing[-1] == "":
                return road_listing[:-1]
            return road_listing

    # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
        def __init__(self):
            # Initialize the node with children as before, plus a handler
            self.children = defaultdict(RouteTrieNode)
            self.handler = None

    # The Router class will wrap the Trie and handle
class Router:
        def __init__(self, handler, nohandler=None):
            # Create a new RouteTrie for holding our routes
            # You could also add a handler for 404 page not found responses as well!
            self.route = RouteTrie(handler)
            self.not_fount = nohandler

        def add_handler(self, path, handler):
            # Add a handler for a path
            # You will need to split the path and pass the pass parts
            # as a list to the RouteTrie
            if path == "" or not isinstance(path, str):
                return "Please input an valid path!"
            self.route.insert(path, handler)

        def lookup(self, path):
            # lookup path (by parts) and return the associated handler
            # you can return None if it's not found or
            # return the "not found" handler if you added one
            # bonus points if a path works with and without a trailing slash
            # e.g. /about and /about/ both return the /about handler
            if path == "" or not isinstance(path, str):
                return "Please input an valid path!"
            handler = self.route.find(path)
            return handler if handler is not None else self.not_fount

# Here are some test cases and expected outputs you can use to test your implementation
router = Router(None)
print(router.lookup('/')) #None
print(router.lookup('/b/b/c')) #None (Empty router none root handler)


# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/help", "help handler")

# some lookups with the expected output
print(router.lookup(""))  # should print "Please input an valid path!" message.
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/help"))  # should print 'help handler' or None if you did not implement one

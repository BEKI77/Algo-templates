class SegmentTree:
    # Initialize the segment tree with an array of values
    def __init__(self, values):

        # Neutral element for sum operations
        self.neutral_element = 0 #Update this 

        n = len(values)
        # Calculate the smallest power of 2 >= n for the tree size
        min_power_of_2 = (n-1).bit_length()
        self.tree_size = pow(2, min_power_of_2)
        # Initialize the tree array with neutral Node elements
        self.tree = [self.neutral_element] * (self.tree_size * 2)
        
        # Build the segment tree with the given values
        self.build_tree(values)

    # Build the segment tree by placing values and constructing parent nodes
    def build_tree(self, values):
        # Insert values into the second half of the tree as Node instances
        for i in range(len(values)):
            self.tree[i + self.tree_size] = values[i]
        
        # Construct internal nodes by merging child nodes
        for i in range(self.tree_size - 1, 0, -1):
            self.tree[i] = self.merge_nodes(self.tree[i * 2], self.tree[i * 2 + 1])

    # Define the merge operation for two Node instances
    def merge_nodes(self, left_node, right_node):
        #Update this
        return left_node + right_node

    # Update a value at a specific index and propagate changes upward
    def update_value(self, index, new_value):
        # Convert index to position in the segment tree array
        index += self.tree_size
        # Update the node's value
        self.tree[index] = new_value
        # Update parent nodes by merging their children
        while index > 1:
            index //= 2
            self.tree[index] = self.merge_nodes(self.tree[index * 2], self.tree[index * 2 + 1])

    # Query the sum in the range [left, right]
    def range_query(self, left, right):
        # Convert range indices to segment tree positions
        left += self.tree_size
        # Add 1 to right to make the query [left, right)
        right += self.tree_size + 1
        result = self.neutral_element

        while left < right:
            # If left is odd, add left node's value to result and move right
            if left % 2:
                result = self.merge_nodes(result, self.tree[left])
                left += 1
            # If right is odd, decrement and add right node's value to result
            if right % 2:
                right -= 1
                result = self.merge_nodes(result, self.tree[right])
            # Move up to the next level
            left //= 2
            right //= 2

        return result

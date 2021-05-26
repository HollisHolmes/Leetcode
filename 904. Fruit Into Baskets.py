class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        Sliding window where the length of the window is the number of items in the basket.
        Iterate ending points for the window and adjust the starting point so len(basket) <= 2.
        Check the window size against the previous max, and return max window size at the end.
        '''
        basket = {}
        start = 0
        max_items = 0
        # Iterate throuh ending points for the window
        for end in range(len(tree)):
            right_fruit = tree[end]
            # If this fruit already in teh basket, add 1 to its count
            if right_fruit in basket:
                basket[right_fruit] += 1
            # If it isn't, set its count to one, and make sure we aren't over the basket limit
            else:
                basket[right_fruit] = 1
                # Move window start untill there are only 2 fruits
                while len(basket) > 2:
                    left_fruit = tree[start]
                    if basket[left_fruit] > 1:
                        basket[left_fruit] -= 1
                    else:
                        del basket[left_fruit]
                    start += 1
            # Compare max window size
            win_len = end - start + 1
            max_items = max(max_items, win_len)
        return max_items
            

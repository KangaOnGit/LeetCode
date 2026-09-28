class Solution:
    def numTrees(self, n: int) -> int:
        """
        When asked how many Unique... (Paths, Trees, Sums, Nums)
            You can use Tabulation
            How many unique set of numbers in nums {1, 2, 3} to make total = 6
                -> If last number picked was 3 then there's exactly 1 + C(3)
                        -> We just need to calculate the unique set of numbers needed to make 3
                            -> If last picked was 2 then C(3) = 1 + C(1)
                                ...
        Unique Tree with 1 Increasing Values -> There's exactly 1 Tree
        Unique Tree with 2 Increasing Values -> There's exactly 2 Trees
        Unique Tree with 3 Increasing Values -> There's exactly 5 Trees
        """

        # Store base case in Cache
        cache_LR = {}
        def numTrees_memoLR(left, right):
            """
            If we take 2 as the Root, how many trees can we make?
                If we take 2 as the Root and root.right = 3 then how many trees to the right can we make?
                If we take 2 as the Root and root.right = 1 then how many trees to the left can we make?
            Unique Tree of Root(n) = UniqueLeftTree*UniqueRightTree
            For 1 as starting Node
            Then:
                We have 1 option for Left Node that is None
                We have 2 options for Right Node 3.left = 2 or 2.right = 3
            -> We have: Left*Right = 2 Unique Trees
            """
            if (left, right) in cache_LR:
                return cache_LR[(left, right)]
            if left > right:
                return 1 # [None]

            count = 0
            for num in range(left, right + 1):
                count_leftTrees = numTrees_memoLR(left, num - 1)
                count_rightTrees = numTrees_memoLR(num+1, right)
                count += count_leftTrees*count_rightTrees
            cache_LR[(left, right)] = count
            return cache_LR[(left, right)]
        #return numTrees_memoLR(1, n)

        cache = {}
        def numTrees_memo(remaining_nodes):
            """
            Rather than Caching Left to Right
                We count how many Nodes are left
            If there are 1/2 Left Nodes, then there will be 1/2 Trees on the Left
            If there are 1/2 Right Nodes, then there will be 1/2 Trees on the Right
            If there are N nodes, then there will always be C(N) Trees
            """

            if remaining_nodes in cache:
                return cache[remaining_nodes]
            if remaining_nodes <= 1:
                return 1 # [None] Node or itself

            count = 0
            for num in range(1, remaining_nodes + 1):
                # Remaining Left is every number lesser than num
                left = numTrees_memo(num - 1)
                # Remaining Right is every number greater than num
                right = numTrees_memo(remaining_nodes - num)
                count += left*right

            cache[remaining_nodes] = count
            return cache[remaining_nodes]
        #return numTrees_memo(n)
    
        def numTrees_catalan(n):
            """     
                Catalan Numbers/Sequence
            """
            c = 1
            for k in range(n):
                c = c * 2 * (2 * k + 1) // (k + 2)
            return c
        #return numTrees_catalan(n)

        def numTrees_tabulation(n):
            """
                Bottom-Up DP (Tabulation) is usually 1 to 2 for-loops
                    And they use a List with no Recursion
            """
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 1
            for nodes in range(2, n+1):
                for root in range(1, nodes + 1):
                    left = root - 1
                    right = nodes - root
                    dp[nodes] += dp[left] * dp[right]

            return dp[n]

        return numTrees_tabulation(n)
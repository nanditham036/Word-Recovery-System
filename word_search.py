
from trie import Trie


def find_words(grid, dictionary):

    # Check grid
    if not grid:
        return {}

    rows = len(grid)
    cols = len(grid[0])

    if cols == 0:
        return {}

    if rows > 10 or cols > 10:
        raise ValueError("Grid size cannot exceed 10 x 10")

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular")

    if any(
        not isinstance(ch, str) or len(ch) != 1
        or not ('a' <= ch <= 'z')
        for row in grid for ch in row
    ):
        raise ValueError("Grid must contain lowercase letters")

    # Create Trie
    trie = Trie()

    # Insert dictionary words
    for word in dictionary:

        if not isinstance(word, str):
            raise ValueError("Dictionary words must be strings")

        if not word or len(word) > 10:
            raise ValueError("Words must contain 1 to 10 letters")

        if not all('a' <= ch <= 'z' for ch in word):
            raise ValueError("Use lowercase English letters only")

        trie.insert(word)

    # Store found words and their paths
    results = {}

    # Track visited cells
    visited = [[False] * cols for _ in range(rows)]

    # Store current path
    path = []

    # Four directions
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    def dfs(row, col, parent):

        char = grid[row][col]

        # Prefix pruning
        if char not in parent.children:
            return

        node = parent.children[char]

        # Mark current cell
        visited[row][col] = True

        # Save coordinate (1-based)
        path.append((row + 1, col + 1))

        # Check for complete word
        if node.word is not None:

            results[node.word] = path.copy()

            # Avoid duplicate results
            node.word = None

        # Search neighboring cells
        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                not visited[nr][nc]
            ):

                dfs(nr, nc, node)

        # Backtracking
        path.pop()
        visited[row][col] = False

    # Start DFS from every cell
    for row in range(rows):
        for col in range(cols):

            dfs(row, col, trie.root)

    return results

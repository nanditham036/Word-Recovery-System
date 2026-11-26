
from word_search import find_words


def display_grid(grid):
    print("\nLETTER GRID:")

    for row in grid:
        print("  ".join(row))


def display_path(grid, path):

    print(
        "Path:",
        " -> ".join(f"({r},{c})" for r, c in path)
    )

    highlighted = set(path)

    print("Highlighted grid:")

    for r in range(len(grid)):

        for c in range(len(grid[0])):

            if (r + 1, c + 1) in highlighted:
                print(f"[{grid[r][c]}]", end=" ")
            else:
                print(f" {grid[r][c]} ", end=" ")

        print()


def main():

    print("=" * 45)
    print("       EXPEDITION'S LOST WORDS")
    print("          WORD RECOVERY SYSTEM")
    print("=" * 45)

    try:

        # Read grid dimensions
        rows = int(input("\nEnter number of rows (1-10): "))
        cols = int(input("Enter number of columns (1-10): "))

        if not (1 <= rows <= 10 and 1 <= cols <= 10):
            print("Invalid grid dimensions.")
            return

        # Read grid
        grid = []

        print("\nEnter grid rows (lowercase letters):")

        for i in range(rows):

            row = input(f"Row {i + 1}: ").strip()

            if (
                len(row) != cols or
                not all('a' <= ch <= 'z' for ch in row)
            ):
                print(
                    f"Invalid row. Enter exactly {cols} "
                    "lowercase letters."
                )
                return

            grid.append(list(row))

        # Read dictionary
        n = int(input("\nEnter number of dictionary words: "))

        if not 0 <= n <= 10000:
            print("Dictionary size must be between 0 and 10000.")
            return

        dictionary = []

        print("\nEnter dictionary words:")

        for i in range(n):

            word = input(f"Word {i + 1}: ").strip()

            if (
                not word or len(word) > 10 or
                not all('a' <= ch <= 'z' for ch in word)
            ):
                print("Invalid word. Use lowercase words of 1-10 letters.")
                return

            dictionary.append(word)

        # Display input
        display_grid(grid)

        # Search words
        results = find_words(grid, dictionary)

        # Display output
        print("\n" + "=" * 45)
        print("             SEARCH RESULTS")
        print("=" * 45)

        if not results:

            print("No words found in the grid.")

        else:

            print("Total words found:", len(results))

            for word, path in sorted(results.items()):

                print("\nFound word:", word)

                display_path(grid, path)

        print("\nSearch completed!")

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()

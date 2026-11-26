
import streamlit as st
import html

from word_search import find_words

st.set_page_config(
    page_title="Word Recovery System",
    page_icon="🔎",
    layout="wide"
)

# Application styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    color: #17365d;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# Application heading
st.title("🔎 WORD RECOVERY SYSTEM")
st.subheader("The Expedition's Lost Words")

st.write(
    "Discover hidden words in a letter grid "
    "using Recursion, Backtracking and Trie."
)

st.divider()


# Grid configuration
st.header("1. Grid Configuration")

col1, col2 = st.columns(2)

with col1:
    rows = st.number_input(
        "Number of Rows",
        min_value=1,
        max_value=10,
        value=5
    )

with col2:
    cols = st.number_input(
        "Number of Columns",
        min_value=1,
        max_value=10,
        value=5
    )


# Grid input
st.header("2. Enter Letter Grid")

default_grid = """mango
grape
apple
lemon
peach"""

grid_text = st.text_area(
    "Enter one row per line",
    value=default_grid,
    height=150
)


# Dictionary input
st.header("3. Enter Dictionary")

dictionary_text = st.text_area(
    "Enter words separated by commas or new lines",
    value="mango, grape, apple, lemon, peach, man, ape",
    height=120
)


# Search button
if st.button("SEARCH WORDS", type="primary"):

    grid_rows = [
        line.strip()
        for line in grid_text.splitlines()
        if line.strip()
    ]

    # Validate grid
    if len(grid_rows) != rows:

        st.error(f"Please enter exactly {rows} rows.")

    elif any(
        len(line) != cols or
        not all('a' <= ch <= 'z' for ch in line)
        for line in grid_rows
    ):

        st.error(
            f"Each row must contain exactly {cols} "
            "lowercase letters."
        )

    else:

        grid = [list(line) for line in grid_rows]

        # Read dictionary
        dictionary = [
            word.strip()
            for word in dictionary_text.replace(
                ",", "\n"
            ).splitlines()
            if word.strip()
        ]

        # Validate dictionary
        if len(dictionary) > 10000:

            st.error("Maximum dictionary size is 10,000.")

        elif any(
            len(word) > 10 or
            not all('a' <= ch <= 'z' for ch in word)
            for word in dictionary
        ):

            st.error(
                "Dictionary words must contain "
                "1 to 10 lowercase letters."
            )

        else:

            # Search words
            try:
                results = find_words(grid, dictionary)

                st.divider()
                st.header("4. Recovered Words")

                if not results:

                    st.warning("No matching words found.")

                else:

                    st.success(
                        f"Successfully found {len(results)} words!"
                    )

                    # Display results
                    for word, path in sorted(results.items()):

                        with st.container(border=True):

                            st.subheader(f"🟢 {word.upper()}")

                            coordinates = " → ".join(
                                f"({r},{c})"
                                for r, c in path
                            )

                            st.write("**Path:**", coordinates)

                            st.write("**Highlighted Grid:**")

                            selected = set(path)

                            grid_html = (
                                '<div style="display:grid;'
                                f'grid-template-columns:repeat({cols},48px);'
                                'gap:5px;">'
                            )

                            for r in range(rows):

                                for c in range(cols):

                                    letter = html.escape(grid[r][c])

                                    if (r + 1, c + 1) in selected:
                                        bg = "#bbf7d0"
                                        border = "#16a34a"
                                    else:
                                        bg = "#e2e8f0"
                                        border = "#cbd5e1"

                                    grid_html += f"""
                                    <div style="
                                        background:{bg};
                                        border:2px solid {border};
                                        border-radius:8px;
                                        padding:12px;
                                        text-align:center;
                                        font-size:20px;
                                        font-weight:bold;
                                        color:#172554;">
                                        {letter}
                                    </div>
                                    """

                            grid_html += "</div>"

                            st.markdown(
                                grid_html,
                                unsafe_allow_html=True
                            )

                st.info(
                    "Search completed using Trie, DFS and Backtracking."
                )

            except (ValueError, TypeError) as error:
                st.error(f"Search error: {error}")


# Footer
st.divider()

st.caption(
    "Word Recovery System | Recursion | "
    "Backtracking | Prefix Search"
)


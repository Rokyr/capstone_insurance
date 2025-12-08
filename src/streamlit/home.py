import streamlit as st


def main():

    # Define pages
    home_page = st.Page("pages/home_page.py", title="Home")
    app1_page = st.Page("pages/app1.py", title="App 1")
    app2_page = st.Page("pages/app2.py", title="App 2")

    # Navigation setup
    pages = st.navigation([home_page, app1_page, app2_page])

    # Run navigation
    pages.run()


if __name__ == "__main__":
    main()

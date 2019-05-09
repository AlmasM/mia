from app import app
from modules.index_page.index_layout import index_layout

def main():
    index_layout()
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
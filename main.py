from managers.data_manager import DataManager
from ui.login_window import LoginWindow
from ui.bookstore_app import OnlineBookstoreApp


def main():
    dm = DataManager()

    def on_login_success(username):
        app = OnlineBookstoreApp(username, dm)
        app.run()

    login = LoginWindow(dm, on_login_success)
    login.run()


if __name__ == "__main__":
    main()

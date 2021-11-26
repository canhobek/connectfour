from app_fact.app_factory import AppFactory, AppType


class Application:
    @staticmethod
    def main():
        AppFactory.startApp(AppType.WEB)


if __name__ == '__main__':
    Application.main()

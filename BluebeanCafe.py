from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 640)
Window.minimum_width = 320
Window.minimum_height = 560


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class DetailScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class CartScreen(Screen):
    pass


class CheckoutScreen(Screen):
    pass


class BluebeanCafeApp(App):
    def build(self):
        return Builder.load_file("bluebean.kv")


if __name__ == "__main__":
    BluebeanCafeApp().run()
# Aplikasi Bluebean Cafe - Navigasi Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    LoginScreen:
    HomeScreen:
    DetailScreen:
    ProfileScreen:
    CartScreen:
    CheckoutScreen:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 15
        
        Label:
            text: 'Bluebean CAFE'
            font_size: '28sp'
            bold: True
            size_hint_y: None
            height: 50
            
        Label:
            text: 'Selamat Datang!\\nSilahkan masuk untuk melanjutkan'
            halign: 'center'
            size_hint_y: None
            height: 40

        TextInput:
            hint_text: 'Email'
            multiline: False
            size_hint_y: None
            height: 45

        TextInput:
            hint_text: 'Kata Sandi'
            password: True
            multiline: False
            size_hint_y: None
            height: 45

        Button:
            text: 'Masuk'
            size_hint_y: None
            height: 50
            on_release:
                app.root.current = 'home'

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10

        Label:
            text: 'Good Coffee, Good Vibes'
            font_size: '20sp'
            bold: True
            size_hint_y: None
            height: 40

        Label:
            text: 'Menu Favorit: Bluebean Latte'
            size_hint_y: None
            height: 30

        Button:
            text: 'Lihat Detail Produk'
            size_hint_y: None
            height: 45
            on_release:
                app.root.current = 'detail'

        GridLayout:
            cols: 3
            size_hint_y: None
            height: 50
            spacing: 5

            Button:
                text: 'Home'
                on_release: app.root.current = 'home'
            Button:
                text: 'Keranjang'
                on_release: app.root.current = 'cart'
            Button:
                text: 'Profile'
                on_release: app.root.current = 'profile'

<DetailScreen>:
    name: 'detail'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: 'Detail Produk'
            font_size: '22sp'
            bold: True
            size_hint_y: None
            height: 40

        Label:
            text: 'Bluebean Latte\\nRp. 28.000\\n\\nPerpaduan espresso dan susu segar'
            halign: 'center'

        Button:
            text: 'Tambah ke Keranjang'
            size_hint_y: None
            height: 50
            on_release:
                app.root.current = 'cart'

        Button:
            text: '< Kembali ke Home'
            size_hint_y: None
            height: 40
            on_release:
                app.root.current = 'home'

<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: 'Profil User'
            font_size: '22sp'
            bold: True
            size_hint_y: None
            height: 40

        Label:
            text: 'User\\nuser@gmail.com'
            halign: 'center'

        Button:
            text: 'Keluar (Logout)'
            size_hint_y: None
            height: 45
            on_release:
                app.root.current = 'login'

        Button:
            text: 'Kembali ke Home'
            size_hint_y: None
            height: 45
            on_release:
                app.root.current = 'home'

<CartScreen>:
    name: 'cart'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: 'Keranjang Belanja'
            font_size: '22sp'
            bold: True
            size_hint_y: None
            height: 40

        Label:
            text: '1x Bluebean Latte - Rp. 28.000\\n2x Matcha Latte - Rp. 54.000\\nTotal: Rp. 114.000'

        Button:
            text: 'Bayar Sekarang'
            size_hint_y: None
            height: 50
            on_release:
                app.root.current = 'checkout'

        Button:
            text: '< Kembali'
            size_hint_y: None
            height: 40
            on_release:
                app.root.current = 'home'

<CheckoutScreen>:
    name: 'checkout'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: 'Pesanan Berhasil!'
            font_size: '24sp'
            bold: True
            size_hint_y: None
            height: 50

        Label:
            text: 'No. Pesanan: #BBB243512\\nTotal: Rp. 114.000\\nEstimasi Pengiriman: 15-20 Menit'
            halign: 'center'

        Button:
            text: 'Kembali ke Home'
            size_hint_y: None
            height: 50
            on_release:
                app.root.current = 'home'
'''

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
        return Builder.load_string(KV)

if __name__ == '__main__':
    BluebeanCafeApp().run()
    

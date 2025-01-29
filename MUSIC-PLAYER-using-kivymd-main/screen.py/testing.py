import subprocess
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Install Python Module"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10

    MDLabel:
        text: "Click the button to install a module."
        halign: "center"

    MDRaisedButton:
        text: "Install Requests"
        pos_hint: {"center_x": 0.5}
        on_release: app.install_module()
'''

class MainApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def install_module(self):
        try:
            # Use subprocess to run pip install
            result = subprocess.run(
                ["python", "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            # Show output in a dialog
            self.show_dialog(f"Output:\n{result.stdout}\nError:\n{result.stderr}")
        except Exception as e:
            self.show_dialog(f"Failed to install. Error: {e}")

    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDRaisedButton(
                        text="CLOSE", on_release=lambda x: self.dialog.dismiss()
                    )
                ],
            )
        else:
            self.dialog.text = message

        self.dialog.open()


MainApp().run()

def main():
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.floatlayout import FloatLayout
    from kivy.uix.label import Label
    from kivy.uix.image import Image
    from kivy.uix.boxlayout import BoxLayout
    from kivy.garden.mapview import MapView, MapMarkerPopup
    from kivy.clock import Clock
    from kivy.animation import Animation
    from kivy.graphics import Color, Rectangle
    from math import radians, cos, sin, asin, sqrt
    from kivy.uix.textinput import TextInput
    from kivy.uix.behaviors import ButtonBehavior
    from kivy.graphics import Color, Rectangle
    from kivy.uix.widget import Widget

    class ImageButton(ButtonBehavior, Image):
        pass

    class CanvasWidget(FloatLayout):
        def __init__(self, **kwargs):
            super(CanvasWidget, self).__init__(**kwargs)

            #with self.canvas:
                #Color(1, 1, 1, 1)  # set the colour
                #self.rect = Rectangle(source='C:\\Users\\fabia\\OneDrive\\Desktop\\clouds.webp', pos=self.pos, size=self.size)
                #self.bind(pos=self.update_rect, size=self.update_rect)


    class Page1(FloatLayout):
        def __init__(self, **kwargs):
            super(Page1, self).__init__(**kwargs)

            with self.canvas.before:
                Color(1, 1, 1, 1)  # White color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

            self.cols = 5


            layout = BoxLayout()

            self.bind(size=self.update_button_sizes)  # Bind the size to update_button_sizes

            self.CUM = ImageButton(source='CAM.png', size_hint=(0.1, 0.1),
                                     pos_hint={'center_x': 0.05, 'y': 0.9})
            self.GO = ImageButton(source='GO.png', size_hint=(0.6, 0.6),
                                     pos_hint={'center_x': 0.5, 'y': 0.35})
            self.press_home = ImageButton(source='HOME.png', size_hint=(None, 0.17),
                                          pos_hint={'x': 0, 'y': 0})
            self.press_home.bind(on_press=self.click_me)
            self.press_map = ImageButton(source='MAP.png', size_hint=(None, 0.17),
                                         pos_hint={'x': 0.25, 'y': 0})
            self.press_map.bind(on_press=self.click_me1)
            self.press_video = ImageButton(source='CHAT.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.5, 'y': 0})
            self.press_video.bind(on_press=self.click_me2)

            self.press_store = ImageButton(source='STORE.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.75, 'y': 0})
            self.press_store.bind(on_press=self.click_me3)

            self.press_settings = ImageButton(source='SETTINGS.png', size_hint=(0.1, 0.1),
                                              pos_hint={'x': 0.9, 'y': 0.9})
            self.press_settings.bind(on_press=self.click_me_settings)

            self.add_widget(self.CUM)
            self.add_widget(self.GO)
            self.add_widget(self.press_home)
            self.add_widget(self.press_map)
            self.add_widget(self.press_video)
            self.add_widget(self.press_store)
            self.add_widget(self.press_settings)

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

        def update_button_sizes(self, instance, value):
            self.press_home.size = (self.width / 4, self.press_home.height)
            self.press_map.size = (self.width / 4, self.press_map.height)
            self.press_video.size = (self.width / 4, self.press_video.height)
            self.press_store.size = (self.width / 4, self.press_store.height)
            self.press_settings.size = (75, 50)

        def click_me(self, instance):
            global current_page
            page1 = Page1()
            self.parent.add_widget(page1)
            current_page = page1
            self.parent.remove_widget(self)

        def click_me1(self, insatnce):
            global current_page
            page2 = Page2()
            self.parent.add_widget(page2)
            current_page = page2
            self.parent.remove_widget(self)

        def click_me2(self, instance):
            global current_page
            page3 = Page3()
            self.parent.add_widget(page3)
            current_page = page3
            self.parent.remove_widget(self)

        def click_me3(self, instance):
            global current_page
            page4 = Page4()
            self.parent.add_widget(page4)
            current_page = page4
            self.parent.remove_widget(self)

        def click_me_settings(self, instnace):
            global current_page
            page5 = Page5()
            self.parent.add_widget(page5)
            current_page = page5
            self.parent.remove_widget(self)

    class Page2(FloatLayout):
        def __init__(self, **kwargs):
            super(Page2, self).__init__(**kwargs)


            # Add the rest of the UI elements
            self.cols = 2

            self.bind(size=self.update_button_sizes)

            # Create a MapView widget
            self.map_view = MapView(
                lat=51.5074,  # Initial latitude
                lon=0.1278,  # Initial longitude
                zoom=10,  # Initial zoom level
                size_hint=(1, 1),  # Adjust size as needed
                pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Adjust position as needed
            )
            self.add_widget(self.map_view)

            self.press_home = ImageButton(source='HOME.png', size_hint=(None, 0.17),
                                          pos_hint={'x': 0, 'y': 0})
            self.press_home.bind(on_press=self.click_me)
            self.press_map = ImageButton(source='MAP.png', size_hint=(None, 0.17),
                                         pos_hint={'x': 0.25, 'y': 0})
            self.press_map.bind(on_press=self.click_me1)
            self.press_video = ImageButton(source='CHAT.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.5, 'y': 0})
            self.press_video.bind(on_press=self.click_me2)

            self.press_store = ImageButton(source='STORE.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.75, 'y': 0})
            self.press_store.bind(on_press=self.click_me3)

            self.press_settings = ImageButton(source='SETTINGS.png', size_hint=(0.1, 0.1),
                                              pos_hint={'x': 0.9, 'y': 0.9})
            self.press_settings.bind(on_press=self.click_me_settings)

            self.add_widget(self.press_home)
            self.add_widget(self.press_map)
            self.add_widget(self.press_video)
            self.add_widget(self.press_store)
            self.add_widget(self.press_settings)

        def update_button_sizes(self, instance, value):
            self.press_home.size = (self.width / 4, self.press_home.height)
            self.press_map.size = (self.width / 4, self.press_map.height)
            self.press_video.size = (self.width / 4, self.press_video.height)
            self.press_store.size = (self.width / 4, self.press_store.height)
            self.press_settings.size = (75, 50)

        def click_me(self, instance):
            global current_page
            page1 = Page1()
            self.parent.add_widget(page1)
            current_page = page1
            self.parent.remove_widget(self)

        def click_me1(self, instance):
            global current_page
            page2 = Page2()
            self.parent.add_widget(page2)
            current_page = page2
            self.parent.remove_widget(self)

        def click_me2(self, instance):
            global current_page
            page3 = Page3()
            self.parent.add_widget(page3)
            current_page = page3
            self.parent.remove_widget(self)

        def click_me3(self, instance):
            global current_page
            page4 = Page4()
            self.parent.add_widget(page4)
            current_page = page4
            self.parent.remove_widget(self)

        def click_me_settings(self, instance):
            global current_page
            page5 = Page5()
            self.parent.add_widget(page5)
            current_page = page5
            self.parent.remove_widget(self)

        def on_stop(self):
            self.gps_handler.stop()

    class TransparentOverlay(Widget):
        def __init__(self, close_callback, **kwargs):
            super(TransparentOverlay, self).__init__(**kwargs)
            self.close_callback = close_callback
            with self.canvas:
                Color(0, 0, 0, 0)  # Transparent color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

        def on_touch_down(self, touch):
            if not self.collide_point(*touch.pos):
                self.close_callback()
            return super(TransparentOverlay, self).on_touch_down(touch)

    class LeftPanel(FloatLayout):
        def __init__(self, **kwargs):
            super(LeftPanel, self).__init__(**kwargs)
            with self.canvas.before:
                Color(0.5, 0.5, 0.5, 1)  # Grey color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

            self.size_hint = (0.75, 1)
            self.pos_hint = {'x': 0, 'y': 0}  # Positioned on the left side
            self.add_widget(Label(text="Left Panel Content", color=(0, 0, 0, 1), size_hint=(None, None),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5}))#LLLLLLLSFLSLDFGLDFGLDFGLDFGLDFGLDGLDLGDLDLDFLGDFGLDFGLDGLDFGL

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

    class InvisibleButton(ButtonBehavior, Widget):
        def __init__(self, **kwargs):
            super(InvisibleButton, self).__init__(**kwargs)
            with self.canvas:
                Color(0, 0, 0, 0)  # Transparent color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

    class Page3(FloatLayout):
        def __init__(self, **kwargs):
            super(Page3, self).__init__(**kwargs)
            self.cols = 2
            self.left_panel = None
            self.overlay = None
            self.invisible_button = None  # Initialize invisible button attribute

            with self.canvas.before:
                Color(1, 1, 1, 1)  # White color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

            # Initialize list to store message labels
            self.message_labels = []
            # Initialize list to store chat messages
            self.chat_messages = []

            # Add a label to display messages
            self.message_label = Label(
                size_hint=(None, None),
                pos_hint={'center_x': 0.5, 'top': 0.7},
                font_size='16sp', color=(0, 0, 0, 1))
            self.add_widget(self.message_label)

            # Add a TextInput for typing messages
            self.chat_input = TextInput(multiline=False,
                                        size_hint=(0.8, None),
                                        height=60,
                                        pos_hint={'center_x': 0.5, 'top': 0.25},
                                        hint_text="Type here...",
                                        text=self.get_last_message())  # Set initial text
            self.chat_input.bind(on_text_validate=self.send_message)
            self.add_widget(self.chat_input)

            self.bind(size=self.update_button_sizes)  # Bind the size to update_button_sizes

            self.press_home = ImageButton(source='HOME.png', size_hint=(None, 0.17),
                                          pos_hint={'x': 0, 'y': 0})
            self.press_home.bind(on_press=self.click_me)
            self.press_map = ImageButton(source='MAP.png', size_hint=(None, 0.17),
                                         pos_hint={'x': 0.25, 'y': 0})
            self.press_map.bind(on_press=self.click_me1)
            self.press_video = ImageButton(source='CHAT.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.5, 'y': 0})
            self.press_video.bind(on_press=self.click_me2)

            self.press_store = ImageButton(source='STORE.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.75, 'y': 0})
            self.press_store.bind(on_press=self.click_me3)

            self.press_settings = ImageButton(source='SETTINGS.png', size_hint=(0.1, 0.1),
                                              pos_hint={'x': 0.9, 'y': 0.9})
            self.press_settings.bind(on_press=self.click_me_settings)

            self.press_friends = ImageButton(source='FRIENDS.png', size_hint=(0.1, 0.1),
                                             pos_hint={'x': 0, 'y': 0.9})
            self.press_friends.bind(on_press=self.click_me_friends)

            self.add_widget(self.press_home)
            self.add_widget(self.press_map)
            self.add_widget(self.press_video)
            self.add_widget(self.press_store)
            self.add_widget(self.press_settings)
            self.add_widget(self.press_friends)

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

        def update_button_sizes(self, instance, value):
            self.press_home.size = (self.width / 4, self.press_home.height)
            self.press_map.size = (self.width / 4, self.press_map.height)
            self.press_video.size = (self.width / 4, self.press_video.height)
            self.press_store.size = (self.width / 4, self.press_store.height)
            self.press_settings.size = (75, 50)

            # Update the size and position of the invisible button if it exists
            if self.invisible_button:
                self.invisible_button.size_hint = (0.25, 1)
                self.invisible_button.pos_hint = {'right': 1, 'y': 0}

        def click_me(self, instance):
            if self.left_panel is None:
                global current_page
                page1 = Page1()
                self.parent.add_widget(page1)
                current_page = page1
                self.parent.remove_widget(self)

        def click_me1(self, instance):
            if self.left_panel is None:
                global current_page
                page2 = Page2()
                self.parent.add_widget(page2)
                current_page = page2
                self.parent.remove_widget(self)

        def click_me2(self, instance):
            if self.left_panel is None:
                global current_page
                page3 = Page3()
                self.parent.add_widget(page3)
                current_page = page3
                self.parent.remove_widget(self)

        def click_me3(self, instance):
            if self.left_panel is None:
                global current_page
                page4 = Page4()
                self.parent.add_widget(page4)
                current_page = page4
                self.parent.remove_widget(self)

        def click_me_settings(self, instance):
            if self.left_panel is None:
                global current_page
                page5 = Page5()
                self.parent.add_widget(page5)
                current_page = page5
                self.parent.remove_widget(self)

        def click_me_friends(self, instance):
            if self.left_panel is None:
                self.left_panel = LeftPanel()
                self.overlay = TransparentOverlay(self.close_left_panel)
                self.add_widget(self.overlay)
                self.add_widget(self.left_panel)

                # Create or show the invisible button
                if not self.invisible_button:
                    self.invisible_button = InvisibleButton(size_hint=(0.25, 1), pos_hint={'right': 1, 'y': 0})
                    self.invisible_button.bind(on_press=self.invisible_button_pressed)
                    self.add_widget(self.invisible_button)

        def close_left_panel(self):
            if self.left_panel:
                self.remove_widget(self.left_panel)
                self.left_panel = None
            if self.overlay:
                self.remove_widget(self.overlay)
                self.overlay = None

            # Remove the invisible button when closing the left panel
            if self.invisible_button:
                self.remove_widget(self.invisible_button)
                self.invisible_button = None

        def send_message(self, instance):
            message = self.chat_input.text.strip()
            if message:
                new_label = Label(text=f"You: {message}",
                                  size_hint=(None, None),
                                  pos_hint={'center_x': 0.5},
                                  font_size='16sp', color=(0, 0, 0, 1))
                self.add_widget(new_label)
                self.message_labels.append(new_label)

                # Append the message to chat_messages list
                self.chat_messages.append(message)

                # Adjust positions of existing labels
                for i, label in enumerate(reversed(self.message_labels)):
                    label.pos_hint = {'center_x': 0.8, 'top': 0.35 + (i + 1) * 0.05}

                # Remove the oldest message label if there are more than 10
                if len(self.message_labels) > 10:
                    old_label = self.message_labels.pop(0)
                    self.remove_widget(old_label)

                # Clear the chat input field
                self.chat_input.text = ""

        def invisible_button_pressed(self, instance):
            global current_page
            page3 = Page3()
            self.parent.add_widget(page3)
            current_page = page3
            self.parent.remove_widget(self)

        def get_last_message(self):
            if self.chat_messages:
                return self.chat_messages[-1]
            return ""

    class Page4(FloatLayout):
        def __init__(self, **kwargs):
            super(Page4, self).__init__(**kwargs)
            self.cols = 2
            self.add_widget(Label(text="Store"))

            with self.canvas.before:
                Color(1, 1, 1, 1)  # White color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

            self.bind(size=self.update_button_sizes)  # Bind the size to update_button_sizes

            self.press_home = ImageButton(source='HOME.png', size_hint=(None, 0.17),
                                          pos_hint={'x': 0, 'y': 0})
            self.press_home.bind(on_press=self.click_me)
            self.press_map = ImageButton(source='MAP.png', size_hint=(None, 0.17),
                                         pos_hint={'x': 0.25, 'y': 0})
            self.press_map.bind(on_press=self.click_me1)
            self.press_video = ImageButton(source='CHAT.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.5, 'y': 0})
            self.press_video.bind(on_press=self.click_me2)

            self.press_store = ImageButton(source='STORE.png', size_hint=(None, 0.17),
                                           pos_hint={'x': 0.75, 'y': 0})
            self.press_store.bind(on_press=self.click_me3)

            self.press_settings = ImageButton(source='SETTINGS.png', size_hint=(0.1, 0.1),
                                              pos_hint={'x': 0.9, 'y': 0.9})
            self.press_settings.bind(on_press=self.click_me_settings)

            self.add_widget(self.press_home)
            self.add_widget(self.press_map)
            self.add_widget(self.press_video)
            self.add_widget(self.press_store)
            self.add_widget(self.press_settings)

            self.add_widget(Label(text="Egeszseges elelmiszer", size_hint=(None, None), pos_hint={'x': 0.5, 'y': 0.75},color=(0, 0, 0, 1)))
            self.add_widget(Label(text="Sport uzletek", size_hint=(None, None), pos_hint={'x': 0.5, 'y': 0.65}, color=(0, 0, 0, 1)))
            self.add_widget(Label(text="Gym", size_hint=(None, None), pos_hint={'x': 0.5, 'y': 0.55}, color=(0, 0, 0, 1)))
            self.add_widget(Label(text="Sport ruhazat", size_hint=(None, None), pos_hint={'x': 0.5, 'y': 0.45}, color=(0, 0, 0, 1)))
            self.add_widget(Label(text="Mittomen", size_hint=(None, None), pos_hint={'x':0.5, 'y':0.35}, color=(0, 0, 0, 1)))

        def update_rect(self, *args):
            self.rect.size = self   .size
            self.rect.pos = self.pos

        def update_button_sizes(self, instance, value):
            self.press_home.size = (self.width / 4, self.press_home.height)
            self.press_map.size = (self.width / 4, self.press_map.height)
            self.press_video.size = (self.width / 4, self.press_video.height)
            self.press_store.size = (self.width / 4, self.press_store.height)
            self.press_settings.size = (75, 50)

        def click_me(self, instance):
            global current_page
            page1 = Page1()
            self.parent.add_widget(page1)
            current_page = page1
            self.parent.remove_widget(self)

        def click_me1(self, insatnce):
            global current_page
            page2 = Page2()
            self.parent.add_widget(page2)
            current_page = page2
            self.parent.remove_widget(self)

        def click_me2(self, instance):
            global current_page
            page3 = Page3()
            self.parent.add_widget(page3)
            current_page = page3
            self.parent.remove_widget(self)

        def click_me3(self, instance):
            global current_page
            page4 = Page4()
            self.parent.add_widget(page4)
            current_page = page4
            self.parent.remove_widget(self)

        def click_me_settings(self, instnace):
            global current_page
            page5 = Page5()
            self.parent.add_widget(page5)
            current_page = page5
            self.parent.remove_widget(self)


    class Page5(FloatLayout):
        def __init__(self, **kwargs):
            super(Page5, self).__init__(**kwargs)
            self.cols =2
            self.add_widget(Label(text="Settings..."))

            with self.canvas.before:
                Color(1, 1, 1, 1)  # White color
                self.rect = Rectangle(size=self.size, pos=self.pos)
                self.bind(size=self.update_rect, pos=self.update_rect)

            self.press_back = ImageButton(source="BACK.png", size_hint=(None, None),
                                          pos_hint={'x': 0, 'y': 0.9})
            self.press_back.bind(on_press=self.back)

        def update_rect(self, *args):
            self.rect.size = self.size
            self.rect.pos = self.pos

            self.add_widget(self.press_back)

        def back(self, instance):
            global current_page
            current_page = Page1()
            self.parent.add_widget(current_page)
            self.parent.remove_widget(self)
    current_page = Page1()


    class Applikacio(App):
        def build(self):
            #self.gps_handler = GPSHandler()
            #self.gps_handler.start()
            return current_page

        #def on_stop(self):
            #self.gps_handler.stop()



    #if __name__ == "__main__":
    Applikacio().run()

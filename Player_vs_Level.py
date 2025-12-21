#LevelApp.py
#Imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, InstructionGroup, Ellipse, Triangle, Line
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from plyer import orientation
import random
import os

try:
    import android
    android.permissions.request_permission([android.permissions.READ_INTERNAL_STORAGE])
except (ImportError, AttributeError):
    print("File not Found")

levels = [
# Levels 1-50
{"platforms": [(30, 150, 400, 20), (500, 250, 300, 20)], "yellow": (750, 270), "start": (50, 200)},
{"platforms": [(50, 150, 200, 20), (300, 300, 250, 20), (700, 400, 300, 20)], "yellow": (950, 420), "start": (60, 200)},
{"platforms": [(20, 200, 300, 20), (400, 350, 350, 20)], "yellow": (800, 370), "start": (40, 220)},
{"platforms": [(60, 180, 250, 20), (350, 330, 300, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (50, 200)},
{"platforms": [(30, 160, 300, 20), (400, 280, 350, 20)], "yellow": (850, 300), "start": (50, 210)},
{"platforms": [(50, 150, 200, 20), (250, 300, 200, 20), (600, 400, 250, 20)], "yellow": (850, 420), "start": (60, 200)},
{"platforms": [(30, 180, 250, 20), (300, 330, 300, 20)], "yellow": (750, 370), "start": (50, 220)},
{"platforms": [(40, 150, 300, 20), (350, 300, 250, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (50, 200)},
{"platforms": [(50, 170, 200, 20), (250, 320, 250, 20)], "yellow": (800, 350), "start": (60, 210)},
{"platforms": [(30, 150, 300, 20), (400, 300, 300, 20)], "yellow": (850, 400), "start": (50, 200)},
{"platforms": [(50, 160, 200, 20), (300, 310, 250, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (60, 200)},
{"platforms": [(30, 180, 250, 20), (300, 350, 300, 20)], "yellow": (750, 370), "start": (50, 220)},
{"platforms": [(40, 150, 300, 20), (350, 300, 250, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (50, 200)},
{"platforms": [(50, 170, 200, 20), (250, 320, 250, 20)], "yellow": (800, 350), "start": (60, 210)},
{"platforms": [(30, 150, 300, 20), (400, 300, 300, 20)], "yellow": (850, 400), "start": (50, 200)},
{"platforms": [(50, 160, 200, 20), (300, 310, 250, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (60, 200)},
{"platforms": [(30, 180, 250, 20), (300, 350, 300, 20)], "yellow": (750, 370), "start": (50, 220)},
{"platforms": [(40, 150, 300, 20), (350, 300, 250, 20), (700, 400, 200, 20)], "yellow": (900, 420), "start": (50, 200)},
{"platforms": [(50, 170, 200, 20), (250, 320, 250, 20)], "yellow": (800, 350), "start": (60, 210)},
{"platforms": [(30, 150, 300, 20), (400, 300, 300, 20)], "yellow": (850, 400), "start": (50, 200)},
{"platforms": [(40, 160, 300, 20), (350, 320, 250, 20)], "yellow": (900, 420), "start": (50, 200)},  # 21
{"platforms": [(30, 180, 250, 20), (300, 350, 300, 20)], "yellow": (850, 400), "start": (60, 220)},  # 22
{"platforms": [(50, 170, 200, 20), (400, 330, 250, 20)], "yellow": (900, 430), "start": (50, 210)},  # 23
{"platforms": [(30, 190, 250, 20), (320, 360, 300, 20)], "yellow": (850, 440), "start": (60, 220)},  # 24
{"platforms": [(40, 160, 200, 20), (350, 300, 250, 20), (700, 420, 200, 20)], "yellow": (950, 450), "start": (50, 200)},  # 25
{"platforms": [(30, 180, 250, 20), (300, 330, 300, 20), (650, 400, 250, 20)], "yellow": (900, 460), "start": (50, 220)},  # 26
{"platforms": [(50, 170, 200, 20), (400, 310, 250, 20), (700, 420, 200, 20)], "yellow": (950, 470), "start": (60, 210)},  # 27
{"platforms": [(30, 200, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 480), "start": (50, 220)},  # 28
{"platforms": [(40, 170, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 490), "start": (60, 200)},  # 29
{"platforms": [(50, 180, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 500), "start": (50, 210)},  # 30
{"platforms": [(30, 200, 200, 20), (400, 330, 250, 20), (700, 420, 200, 20)], "yellow": (950, 510), "start": (60, 220)},  # 31
{"platforms": [(50, 190, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 520), "start": (50, 210)},  # 32
{"platforms": [(30, 180, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 530), "start": (60, 200)},  # 33
{"platforms": [(50, 200, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 540), "start": (50, 220)},  # 34
{"platforms": [(30, 190, 200, 20), (400, 330, 250, 20), (700, 420, 200, 20)], "yellow": (950, 550), "start": (60, 210)},  # 35
{"platforms": [(50, 180, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 560), "start": (50, 220)},  # 36
{"platforms": [(30, 200, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 570), "start": (60, 200)},  # 37
{"platforms": [(50, 190, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 580), "start": (50, 210)},  # 38
{"platforms": [(30, 200, 200, 20), (400, 330, 250, 20), (700, 420, 200, 20)], "yellow": (950, 590), "start": (60, 220)},  # 39
{"platforms": [(50, 180, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 600), "start": (50, 200)},  # 40
{"platforms": [(30, 200, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 610), "start": (60, 210)},  # 41
{"platforms": [(50, 190, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 620), "start": (50, 220)},  # 42
{"platforms": [(30, 200, 200, 20), (400, 330, 250, 20), (700, 420, 200, 20)], "yellow": (950, 630), "start": (60, 200)},  # 43
{"platforms": [(50, 180, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 640), "start": (50, 210)},  # 44
{"platforms": [(30, 200, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 650), "start": (60, 220)},  # 45
{"platforms": [(50, 190, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 660), "start": (50, 200)},  # 46
{"platforms": [(30, 200, 200, 20), (400, 330, 250, 20), (700, 420, 200, 20)], "yellow": (950, 670), "start": (60, 210)},  # 47
{"platforms": [(50, 180, 250, 20), (300, 360, 300, 20), (650, 400, 250, 20)], "yellow": (900, 680), "start": (50, 220)},  # 48
{"platforms": [(30, 200, 200, 20), (350, 320, 250, 20), (700, 420, 200, 20)], "yellow": (950, 690), "start": (60, 200)},  # 49
{"platforms": [(50, 190, 250, 20), (300, 350, 300, 20), (650, 400, 250, 20)], "yellow": (900, 700), "start": (50, 210)},  # 50
]

#------------------------------------------
#Menu Class
#------------------------------------------
class GameMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Window Color
        Window.clearcolor = (1, 1, 1, 1)
        
        #Layout
        layout = BoxLayout(orientation="vertical", spacing=20, padding=50)
        
        #Main Label
        Main_Label = Label(text="PLAYER V.S LEVEL", font_size=100, pos=(400, 400), color=(0, 0, 0, 1))
        layout.add_widget(Main_Label)
        
        grow = Animation(font_size=120, duration=0.6)
        shrink = Animation(font_size=100, duration=0.6)
        pulse = grow + shrink
        pulse.repeat = True
        pulse.start(Main_Label)
        
        start_btn = Button(text="Start", font_size=40, size=(600, 700), border=(0, 0, 0, 0))
        start_btn.bind(on_release=self.start_game)
        layout.add_widget(start_btn)
        
        self.settings_btn = Button(text="Settings", font_size=40, size=(600, 700), border=(0, 0, 0, 0))
        self.settings_btn.bind(on_release=self.settings)
        layout.add_widget(self.settings_btn)
        
        quit_btn = Button(text="Quit", font_size=40, size=(100, 100), border=(0, 0, 0, 0))
        quit_btn.bind(on_release=self.quit_game)
        layout.add_widget(quit_btn)
        
        self.add_widget(layout)
        
    def start_game(self, instance):
        game_screen = self.manager.get_screen("game")
        
        mechanics = game_screen.children[0]
        mechanics.restart()
        mechanics.player_speed = 5
        mechanics.enemy_speed = 2
        
        self.manager.current = "game"
        
    def settings(self, instance):
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        
        difficulty_label = Label(text="Select Difficulty:", size_hint_y=None, height=40)
        content.add_widget(difficulty_label)
        
        difficulty_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        for level in ["Easy", "Normal", "Hard", "Extreme"]:
            btn = Button(text=level)
            btn.bind(on_release=lambda b, l=level: self.set_difficulty(l))
            difficulty_layout.add_widget(btn)
        content.add_widget(difficulty_layout)
        
        reset_btn = Button(text="Reset Progress", size_hint_y=None, height=50)
        reset_btn.bind(on_release=self.reset_progress)
        content.add_widget(reset_btn)
        
        close_btn = Button(text="Close", size_hint_y=None, height=50)
        popup = Popup(title='Settings', content=content, size_hint=(0.8, 0.6), auto_dismiss=False)
        close_btn.bind(on_release=lambda x: popup.dismiss())
        content.add_widget(close_btn)
        
        popup.open()
        
    def set_difficulty(self, level):
        game_screen = self.manager.get_screen("game")
        mechanics = game_screen.children[0]
        
        print(f"Difficulty Set To: {level}")
        if level == "Noob":
            mechanics.current_enemy_speed = 0
        elif level == "Easy":
            mechanics.current_enemy_speed = 3
        elif level == "Normal":
            mechanics.current_enemy_speed = 4
        elif level == "Hard":
            mechanics.current_enemy_speed = 6
        elif level == "Extreme":
            mechanics.current_enemy_speed = 67
        
        for enemy in mechanics.enemies:
            enemy.enemy_speed = mechanics.current_enemy_speed
        
    def reset_progress(self, instance):
        print("Progress Reset")
        game_screen = self.manager.get_screen("game")
        mechanics = game_screen.children[0]
        mechanics.restart()
        for enemy in mechanics.enemies:
            mechanics.current_enemy_speed = 3
        
    def quit_game(self, instance):
        App.get_running_app().stop()
        
class GameScreen(Screen):
    pass

# -----------------------------------------
# Mechanics class
# -----------------------------------------
class Mechanics(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Window Color
        Window.clearcolor = (1, 1, 1, 1)

        # Player and Enemy variables
        self.size_square = 100
        self.pos_x = Window.width / 10
        self.pos_y = Window.height / 4
        self.gravity = -1
        self.vy = 0
        self.is_jumping = False
        self.walking_forward = False
        self.walking_back = False
        self.player_speed = 5
        self.current_enemy_speed = 3
        self.boost_active = False
        self.max_health = 1000
        self.health = self.max_health

        # Game variables
        self.platforms = []
        self.enemies = []
        self.hitbox_group = None
        self.boost = None
        self.level_index = 0
        self.level_counter = 1
        self.yellow_collected = 0
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        self.keys = set()
        self.yellow = None
        self.paused = False
        self.dev_mode = False
        self.god_mode = False
        self.green_triangle = None
        self.show_hitboxes = False
        self.paused_for_player_only = False
        self.dev_count = 0
        self.game_over_count = 0
        self.dev_abuse_count = 0
        self.game_over_flag = False
        self.jumpscare_triggered = False
        self.free_jump = False
        self.bg = None

        #Plyer things
        orientation.set_landscape()
        
        #os things
        BASE_DIR = "/storage/emulated/0/Player_VS_Level"
        
        #Sound and Image Path
        BACKGROUND_IMG_PATH = os.path.join(BASE_DIR, "cloud.png")
        JUMPSCARE_SOUND_PATH = os.path.join(BASE_DIR, "fnaf_jumpscare.mp3")
        JUMPING_SOUND_PATH = os.path.join(BASE_DIR, "jumping.wav")
        
        #Sound😈
        self.jumpscare_sound = SoundLoader.load(JUMPSCARE_SOUND_PATH)
        self.jump_sound = SoundLoader.load(JUMPING_SOUND_PATH)
        
        #Image
        if os.path.exists(BACKGROUND_IMG_PATH):
            self.bg = Image(source=BACKGROUND_IMG_PATH, size_hint=(None, None), size=(3000, 2000))
            self.add_widget(self.bg)

        # UI buttons
        self.btn = Button(text="Forward", font_size=40, pos=(300, 40), size=(200, 100), size_hint=(None, None))
        self.btn.bind(on_press=self.set_walking)
        self.btn.bind(on_release=self.stop_walking)
        self.add_widget(self.btn)

        self.btn2 = Button(text="Back", font_size=40, pos=(10, 40), size=(200, 100), size_hint=(None, None))
        self.btn2.bind(on_press=self.set_back)
        self.btn2.bind(on_release=self.stop_back)
        self.add_widget(self.btn2)

        self.jump = Button(text="Jump", font_size=40, pos=(1200, 40), size=(200, 100), size_hint=(None, None))
        self.jump.bind(on_press=self.jumping)
        self.add_widget(self.jump)

        self.pause = Button(text="l l", font_size=40, pos=(1300, 556), size=(100, 100), size_hint=(None, None))
        self.pause.bind(on_press=self.show_popup)
        self.add_widget(self.pause)

        self.progressbar_label = Label(text="Health Bar:", pos=(380, 520), color=(0, 0, 0, 1))
        self.add_widget(self.progressbar_label)

        self.healthbar = ProgressBar(max=self.max_health, value=self.health, size_hint=(None, None), size=(500, 50), pos=(500, 540))
        self.add_widget(self.healthbar)
        
        self.slider = Slider(min=0, max=100, value=50, step=1, orientation="horizontal", size_hint=(None, None), size=(500, 50), pos=(400, 600))
        self.slider.bind(value=self.enemy_speed_change)
        
        self.checkbox = CheckBox(pos=(600, 600))
        self.checkbox.bind(active=self.update_checkbox)
        
        self.pause_all_switch = Switch(pos=(800, 600), size_hint=(None, None), size=(100, 50))
        self.pause_all_switch.bind(active=self.toggle_pause_all)

        # Dev mode buttons
        self.dev_button = Button(text="Dev Mode", size_hint=(None, None), size=(200, 100), pos=(50, 600))
        self.dev_button.bind(on_press=self.toggle_dev_mode)

        self.speed_inc_btn = Button(text="+Speed", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 150))
        self.speed_inc_btn.bind(on_press=lambda x: self.change_speed(1))
        self.speed_dec_btn = Button(text="-Speed", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 50))
        self.speed_dec_btn.bind(on_press=lambda x: self.change_speed(-1))
        self.speed_reset_btn = Button(text="Reset Speed", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 250))
        self.speed_reset_btn.bind(on_press=lambda x: self.change_speed(0))
        self.god_mode_btn = Button(text="God Mode: OFF", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 450))
        self.god_mode_btn.bind(on_press=self.toggle_god_mode)
        self.hitbox_btn = Button(text="Hitboxes: OFF", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 550))
        self.hitbox_btn.bind(on_press=self.toggle_hitboxes)
        self.skip_level = Button(text="Next Level", size_hint=(None, None), size=(250, 80), pos=(Window.width-380, 350))
        self.skip_level.bind(on_press=self.next_level)

        # Load first level
        self.load_level(self.level_index)

        # Spawn initial enemies
        self.spawn_enemy((600, 200), personality="aggressive")
        self.spawn_enemy((900, 300), personality="cautious")
        self.spawn_enemy((300, 100), personality="zigzag")
        self.spawn_enemy((1000, 400), personality="ambusher")
        self.spawn_enemy((1200, 400), personality="lazy")

        Clock.schedule_interval(self.update, 1/60)

    # -----------------------------------------
    # Load level
    # -----------------------------------------
    def load_level(self, level_index):
        # Remove existing platforms & yellow
        for plat in self.platforms:
            self.canvas.remove(plat)
        if self.yellow:
            self.canvas.remove(self.yellow)
        self.platforms.clear()

        level_data = levels[level_index]

        with self.canvas:
            Color(0.5, 0.5, 0.5, 1)
            for plat_data in level_data["platforms"]:
                rect = Rectangle(pos=(plat_data[0], plat_data[1]), size=(plat_data[2], plat_data[3]))
                self.platforms.append(rect)

            Color(1, 1, 0, 1)
            self.yellow = Ellipse(pos=level_data["yellow"], size=(50, 50))

        # Reset player
        self.pos_x, self.pos_y = level_data.get("start", (50, 200))
        self.vy = 0
        self.is_jumping = False

        if hasattr(self, "square"):
            self.square.pos = (self.pos_x, self.pos_y)
        else:
            with self.canvas:
                Color(0, 1, 0, 1)
                self.square = Rectangle(pos=(self.pos_x, self.pos_y), size=(self.size_square, self.size_square))

        self.spawn_boost()
        
        if self.level_index == 49:
            self.spawn_boss(Window.width/2, 200)
            
        if random.randint(1, 1000) == 1:
            if self.platforms:
                plat = random.choice(self.platforms)
                plat_x, plat_y = plat.pos
                plat_w, plat_h = plat.size
                if plat_y + plat_h + 50 < Window.height - 50:
                    tri_size = 50
                    tri_x = plat_x + plat_w/2 - tri_size/2
                    tri_y = plat_y + plat_h
                with self.canvas:
                    Color(0, 1, 0, 1)
                    self.green_triangle = Triangle(points=[tri_x, tri_y, tri_x + tri_size, tri_y, tri_x + tri_size/2, tri_y + tri_size])
        else:
            self.green_triangle = None
            
        if random.randint(1, 1000) == 1:
            self.add_widget(InvisibleSquare(pos=(random.randint(0, Window.width-100), random.randint(0, Window.height-100))))
            
        if random.randint(1, 10000) == 1:
            self.add_widget(RainbowSquare(pos=(random.randint(0, Window.width-100), random.randint(0, Window.height-100))))
            
        if random.randint(1, 1000) == 1:
            self.add_widget(AngrySquare(pos=(random.randint(0, Window.width-100), random.randint(0, Window.height-100))))

    # -----------------------------------------
    # Check yellow collection
    # -----------------------------------------
    def check_yellow(self):
        if not self.yellow:
            return
        px1, py1 = self.pos_x, self.pos_y
        px2, py2 = self.pos_x + self.size_square, self.pos_y + self.size_square

        yellow_x1, yellow_y1 = self.yellow.pos
        yellow_x2, yellow_y2 = yellow_x1 + self.yellow.size[0], yellow_y1 + self.yellow.size[1]

        if px1 < yellow_x2 and px2 > yellow_x1 and py1 < yellow_y2 and py2 > yellow_y1:
            self.level_index += 1
            self.level_counter += 1
            self.yellow_collected += 1
            if self.level_index < len(levels):
                self.load_level(self.level_index)
            else:
                self.win_game()

    # -----------------------------------------
    # Update loop
    # -----------------------------------------
    def update(self, *args):
        dt = args[-1] if isinstance(args[-1], (int, float)) else 0

        if self.walking_forward:
            self.pos_x += self.player_speed
        if self.walking_back:
            self.pos_x -= self.player_speed
        
        if 275 in self.keys or 100 in self.keys:
            self.pos_x += self.player_speed
        if 276 in self.keys or 97 in self.keys:
            self.pos_x -= self.player_speed
        if 32 in self.keys and (self.free_jump or not self.is_jumping):
            self.vy = 20
            self.is_jumping = True
            self.animate_jump()
            
            if self.jump_sound:
                self.jump_sound.play()
        if 27 in self.keys:
            self.show_popup(None)

        # Apply gravity
        self.vy += self.gravity
        self.pos_y += self.vy

        # Platform collisions
        for plat in self.platforms:
            px1, py1 = self.pos_x, self.pos_y
            px2, py2 = self.pos_x + self.size_square, self.pos_y + self.size_square

            plat_x1, plat_y1 = plat.pos
            plat_x2, plat_y2 = plat.pos[0] + plat.size[0], plat.pos[1] + plat.size[1]

            if self.vy <= 0 and px2 > plat_x1 and px1 < plat_x2 and py1 <= plat_y2 and py2 >= plat_y1 - 10:
                self.pos_y = plat_y2
                self.vy = 0
                self.is_jumping = False
                Animation(size=(120, 80), duration=0.08).start(self.square)
                Animation(size=(100, 100), duration=0.08).start(self.square)

        self.square.pos = (self.pos_x, self.pos_y)
        self.healthbar.value = self.health

        self.check_yellow()

        # Boost collision
        if self.boost:
            bx, by = self.boost.pos
            bw, bh = 40, 40
            if (self.pos_x < bx + bw and self.pos_x + self.size_square > bx and
                self.pos_y < by + bh and self.pos_y + self.size_square > by):
                self.player_speed += 4
                self.boost_active = True
                self.remove_widget(self.boost)
                self.boost = None
                Clock.schedule_once(self.end_boost, 5)

        # Enemy behavior
        for enemy in self.enemies:
            enemy_center_x = enemy.x + enemy.enemy_size[0] / 2
            player_center_x = self.pos_x + self.size_square / 2
            distance = player_center_x - enemy_center_x
            if abs(distance) < 150:
                enemy.x += enemy.enemy_speed if distance > 0 else -enemy.enemy_speed
            else:
                enemy.patrol()
                
            for enemy in self.enemies:
                ex1, ey1 = enemy.x, enemy.y
                ex2, ey2 = enemy.x + enemy.enemy_size[0], enemy.y + enemy.enemy_size[1]
                px1, py1 = self.pos_x, self.pos_y
                px2, py2 = self.pos_x + self.size_square, self.pos_y + self.size_square
                if not self.god_mode:
                    if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
                        self.take_damage(1)
                

            # Collision with player
            if hasattr(self, "boss") and self.boss is not None:
                boss_x1, boss_y1 = self.boss.x, self.boss.y
                boss_x2, boss_y2 = boss_x1 + self.boss.boss_size[0], boss_y1 + self.boss.boss_size[1]
                if not self.god_mode:
                    if px1 < boss_x2 and px2 > boss_x1 and py1 < boss_y2 and py2 > boss_y1:
                        self.take_damage(2)

        self.check_fall()
        
        if self.show_hitboxes and self.hitbox_group:
            self.player_hitbox.pos(self.pos_x, self.pos_y)
            
        if hasattr(self, "boss"):
            self.boss.move()
            
        if hasattr(self, "boss") and self.boss is not None:
            self.boss.chase_player(self.pos_x, self.pos_y)
            
        if self.green_triangle:
            px1, py1 = self.pos_x, self.pos_y
            px2, py2 = self.pos_x + self.size_square, self.pos_y + self.size_square
            
            tri_x = min(self.green_triangle.points[::2])
            tri_y = min(self.green_triangle.points[1::2])
            tri_w = max(self.green_triangle.points[::2]) - tri_x
            tri_h = max(self.green_triangle.points[1::2]) - tri_y
            
            if px1 < tri_x + tri_w and px2 > tri_x and py1 < tri_y + tri_h and py2 > tri_y:
                if self.dev_button.parent is None:
                    self.add_widget(self.dev_button)
                self.canvas.remove(self.green_triangle)
                self.green_triangle = None
                
        if getattr(self, "paused_for_player_only", False):
            if self.walking_forward:
                self.pos_x += self.player_speed
            if self.walking_back:
                self.pos_x -= self.player_speed
            return
            
        if self.dev_mode:
            dev_buttons_pressed = sum([self.speed_inc_btn.parent is not None, self.speed_dec_btn.parent is not None, self.speed_reset_btn.parent is not None, self.god_mode_btn.parent is not None, self.hitbox_btn.parent is not None, self.skip_level.parent is not None])
            if dev_buttons_pressed >= 100:
                self.dev_abuse_count += 1
                if self.dev_abuse_count > 120:
                    self.trigger_bad_ending()

    # -----------------------------------------
    # Game over
    # -----------------------------------------
    def game_over(self):
        if self.game_over_flag:
            return
        self.game_over_flag = True
        self.walking_forward = False
        self.walking_back = False
        
        self.health = 0
        self.healthbar.max = self.health
        self.healthbar.value = self.health
        if hasattr(self, "square"):
            self.remove_widget(self.square)
            
        #Good Ending
        if not self.jumpscare_triggered:
            self.game_over_count += 1
            if self.game_over_count >= 10 and not self.jumpscare_triggered:
                self.trigger_jumpscare()
                return
        
        self.game_over_label = Label(text="Game Over!", font_size=80, pos=(Window.width/2, Window.height/2), color=(0, 0, 0, 1))
        self.add_widget(self.game_over_label)
        
        for b in [self.btn, self.btn2, self.jump]:
            b.disabled = True
        Clock.unschedule(self.update)

    # -----------------------------------------
    # Win game
    # -----------------------------------------
    #True Ending
    def win_game(self):
        self.walking_forward = False
        self.walking_back = False
        self.win_label = Label(text="YOU ESCAPED!!!", font_size=80, pos=(Window.width/2, Window.height/2), color=(0, 0, 0, 1))
        for b in [self.btn, self.btn2, self.jump]:
            b.disabled = True
        Clock.unschedule(self.update)
        self.add_widget(self.win_label)

    # -----------------------------------------
    # Restart
    # -----------------------------------------
    def restart(self):
        # Remove labels
        if hasattr(self, 'game_over_label'):
            if self.game_over_label in self.children:
                self.remove_widget(self.game_over_label)
            self.game_over_label = None
        if hasattr(self, 'win_label'):
            if self.win_label in self.children:
                self.remove_widget(self.win_label)
            self.win_label = None

        # Reset player
        self.pos_x = Window.width / 10
        self.pos_y = Window.height / 4
        self.player_speed = 5
        self.health = self.max_health
        self.healthbar.max = self.health
        self.healthbar.value = self.health
        self.vy = 0
        self.is_jumping = False
        self.walking_forward = False
        self.game_over_flag = False
        self.jumpscare_triggered = False
        self.walking_back = False
        self.boost_active = False

        # Reset level
        self.level_index = 0
        self.level_counter = 1
        self.yellow_collected = 0
        self.load_level(self.level_index)

        # Remove enemies
        for e in self.enemies:
            self.remove_widget(e)
        self.enemies.clear()
        self.spawn_enemy((600, 200), personality="aggressive")
        self.spawn_enemy((900, 300), personality="cautious")
        self.spawn_enemy((300, 100), personality="zigzag")
        self.spawn_enemy((1000, 400), personality="ambusher")
        self.spawn_enemy((1200, 400), personality="lazy")
        
        #Remove boss
        if hasattr(self, "boss"):
            self.remove_widget(self.boss)
            del self.boss

        # Remove boost
        if self.boost:
            self.remove_widget(self.boost)
            self.boost = None
        self.spawn_boost()

        # Re-enable buttons
        for b in [self.btn, self.btn2, self.jump]:
            b.disabled = False

        Clock.unschedule(self.update)
        Clock.schedule_interval(self.update, 1/60)

    # -----------------------------------------
    # Spawn boost
    # -----------------------------------------
    def spawn_boost(self):
        if self.boost:
            self.remove_widget(self.boost)
        self.boost = SpeedBoost()
        self.boost.pos = (random.randint(0, int(Window.width-50)), random.randint(0, int(Window.height-50)))
        self.add_widget(self.boost)

    def end_boost(self, dt):
        if self.boost_active:
            self.player_speed -= 4
            self.boost_active = False

    # -----------------------------------------
    # Take damage
    # -----------------------------------------
    def take_damage(self, amount):
        if self.god_mode:
            self.health = self.max_health
            return
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.game_over()

    def activate_god_mode(self):
        if self.god_mode:
            print("God Mode Activated")
            self.god_mode = True
            self.player_speed = 10
            self.check_fall()
        else:
            print("God Mode Disabled")
            self.god_mode = False
            self.player_speed = 5
            
    def activate_hitbox(self):
        self.show_hitboxes = not self.show_hitboxes
        if self.show_hitboxes:
            if self.hitbox_group:
                print("Hitbox not showed")
                self.canvas.remove(self.hitbox_group)
                self.hitbox_group = False
                self.show_hitboxes = False
        else:
            self.hitbox_group = InstructionGroup()
            print("Hitbox showed")
            self.hitbox_group.add(Color(1, 0, 0, 0.5))
            self.player_hitbox = Rectangle(pos=(self.pos_x, self.pos_y), size=(self.size_square, self.size_square))
            self.hitbox_group.add(self.player_hitbox)
            self.enemy_hitboxes = []
            for enemy in self.enemies:
                enemy_hitbox = Rectangle(pos=(enemy.x, enemy.y), size=(100, 100))
                self.hitbox_group.add(enemy_hitbox)
            self.canvas.add(self.hitbox_group)
            self.show_hitbox = True

    # -----------------------------------------
    # Player controls
    # -----------------------------------------
    def set_walking(self, instance):
        self.walking_forward = True
    def stop_walking(self, instance):
        self.walking_forward = False
    def set_back(self, instance):
        self.walking_back = True
    def stop_back(self, instance):
        self.walking_back = False
    def jumping(self, instance):
        if self.free_jump or not self.is_jumping:
            self.vy = 20
            self.is_jumping = True
            self.animate_jump()
            
            if self.jump_sound:
                self.jump_sound.play()

    # -----------------------------------------
    # Toggle dev/god mode & speed
    # -----------------------------------------
    def toggle_dev_mode(self, instance):
        self.dev_mode = not self.dev_mode
        if self.dev_mode:
            for dev_buttons in [self.speed_inc_btn, self.speed_dec_btn, self.speed_reset_btn, self.god_mode_btn, self.hitbox_btn, self.skip_level, self.slider, self.checkbox, self.pause_all_switch]:
                if dev_buttons.parent is None:
                    self.add_widget(dev_buttons)
        else:
            for dev_buttons in [self.speed_inc_btn, self.speed_dec_btn, self.speed_reset_btn, self.god_mode_btn, self.hitbox_btn, self.skip_level, self.slider, self.checkbox, self.pause_all_switch]:
                if dev_buttons.parent:
                    self.remove_widget(dev_buttons)
                
    def change_speed(self, value):
        if value == 0:
            self.player_speed = 5
        else:
            self.player_speed += value
            
    def toggle_god_mode(self, instance):
        self.god_mode = not self.god_mode
        instance.text = "God Mode: ON" if self.god_mode else "God Mode: OFF"
        self.activate_god_mode()
        
    def toggle_hitboxes(self, instance):
        instance.text = "Hitboxes: ON" if self.show_hitboxes else "Hitboxes: OFF"
        self.activate_hitbox()

    # -----------------------------------------
    # Check fall
    # -----------------------------------------
    def check_fall(self):
        if self.pos_y < 0:
            if self.god_mode:
                self.respawn()
            else:
                self.game_over()

    def respawn(self):
        level_data = levels[self.level_index]
        self.pos_x, self.pos_y = level_data.get("start", (50, 200))
        self.vy = 0
        self.is_jumping = False

    # -----------------------------------------
    # Spawn enemy
    # -----------------------------------------
    def spawn_enemy(self, pos, personality="normal"):
        enemy = Enemy(pos=pos, personality=personality, speed=self.current_enemy_speed)
        self.enemies.append(enemy)
        self.add_widget(enemy)

    # -----------------------------------------
    # Popup
    # -----------------------------------------
    def show_popup(self, instance):
        self.paused = True
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        btns = BoxLayout(size_hint_y=None, height=40, spacing=10)
        content.add_widget(Label(text=f"Yellow Collected: {self.yellow_collected}\nLevel: {self.level_counter}\n Game Overs: {self.game_over_count}", halign='center'))
        resume_btn = Button(text='Resume')
        restart_btn = Button(text='Restart')
        menu_btn = Button(text='Go Back to Menu')
        quit_btn = Button(text='Quit')

        popup = Popup(title="Game Paused", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
        
        def do_resume(btn_instance):
            popup.dismiss()
            Clock.schedule_interval(self.update, 1/60)
        def do_restart(btn_instance):
            popup.dismiss()
            self.restart()
        def do_menu(btn_instance):
            popup.dismiss()
            
            Clock.unschedule(self.update)
            self.paused = False
            
            app = App.get_running_app()
            app.root.current = "menu"
        def do_quit(btn_instance):
            popup.dismiss()
            App.get_running_app().stop()

        resume_btn.bind(on_release=do_resume)
        restart_btn.bind(on_release=do_restart)
        menu_btn.bind(on_release=do_menu)
        quit_btn.bind(on_release=do_quit)

        btns.add_widget(resume_btn)
        btns.add_widget(restart_btn)
        btns.add_widget(menu_btn)
        btns.add_widget(quit_btn)
        content.add_widget(btns)

        Clock.unschedule(self.update)
        popup.open()
        
    def next_level(self, instance=None):
        if self.level_index < len(levels) - 1:
            self.level_index += 1
            self.level_counter += 1
            self.yellow_collected += 1
            self.load_level(self.level_index)
        else:
            self.win_game()
        
    def spawn_boss(self, x, y):
        self.boss = Boss(pos=(x, y))
        self.boss.mechanics = self
        self.add_widget(self.boss)
        
    def enemy_speed_change(self, instance,value):
        self.current_enemy_speed = value
        for enemy in self.enemies:
            enemy.enemy_speed = value
            
    def trigger_jumpscare(self):
        self.jumpscare_triggered = True
        
        Window.clearcolor = (0, 0, 0, 1)
        
        if self.bg and self.bg.parent:
            self.remove_widget(self.bg)
            self.bg = None
        
        Clock.unschedule(self.update)
        
        if hasattr(self, "game_over_label"):
            self.remove_widget(self.game_over_label)
            del self.game_over_label
        
        for widget in self.children:
            if isinstance(widget, Button):
                widget.disabled = True
                for buttons in [self.btn, self.btn2, self.jump, self.dev_button, self.pause]:
                    buttons.disabled = True
                
        if self.jumpscare_sound:
            self.jumpscare_sound.volume = 1.0
            self.jumpscare_sound.play()
            
        self.scare = Label(text="You Died", font_size=100, center=(Window.width / 2, Window.height / 2), color=(1, 0, 0, 1))
        self.add_widget(self.scare)
        
    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        self.keys.add(key)
        
        if key == ord('s') and self.paused:
            self.resume_game()
        if key == ord('r') and (self.paused or self.game_over):
            self.restart()
        if key == ord('q') and (self.paused or self.game_over):
            self.quit_game()
        
    def on_key_up(self, window, key, scancode):
        if key in self.keys:
            self.keys.remove(key)
            
    def resume_game(self):
        self.paused = False
        Clock.schedule_interval(self.update, 1/60)
    
    def quit_game(self):
        App.get_running_app().stop()
        
    def update_checkbox(self, instance, value):
        self.free_jump = value
        self.vy = 20
        self.is_jumping = True
        
    def toggle_pause_all(self, instance, value):
        if value:
            Clock.unschedule(self.update)
            self.paused_for_player_only = True
        else:
            Clock.schedule_interval(self.update, 1/60)
            self.paused_for_player_only = False
            
    def animate_jump(self):
        squash = Animation(size=(120, 80), duration=0.08)
        stretch = Animation(size=(80, 120), duration=0.08)
        normal = Animation(size=(100, 100), duration=0.1)
        
        squash.bind(on_complete=lambda *a: stretch.start(self.square))
        stretch.bind(on_complete=lambda *a: normal.start(self.square))
        
        squash.start(self.square)
        
    def trigger_bad_ending(self):
        if getattr(self, 'bad_ending_flag', False):
            return
        self.bad_ending_flag = True
        
        Clock.unschedule(self.update)
        self.walking_forward = False
        self.walking_back = False
        
        for b in [self.btn, self.btn2, self.jump, self.pause, self.dev_button]:
            b.disabled = True
            
        Window.clearcolor = (1, 0, 0, 1)
        
        if self.bg and self.bg.parent:
            self.remove_widget(self.bg)
            self.bg = None
        
        self.bad_label = Label(text="THE LEVEL HAS TAKEN YOU", font_size=90, center=(Window.width/2, Window.height/2), color=(0, 0, 0, 1))
        self.add_widget(self.bad_label)
        
        anim = Animation(font_size=100, duration=0.7) + Animation(font_size=90, duration=0.7)
        anim.repeat = True
        anim.start(self.bad_label)
        
        for enemy in self.enemies:
            enemy.enemy_speed *= 2
            
        if self.jumpscare_sound:
            self.jumpscare_sound.volume = 1.0
            self.jumpscare_sound.play()

# -----------------------------------------
# SpeedBoost
# -----------------------------------------
class SpeedBoost(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (40, 40)
        with self.canvas:
            Color(0, 0, 1, 1)
            self.elli = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_elli)

    def update_elli(self, *args):
        self.elli.pos = self.pos

# -----------------------------------------
# Enemy
# -----------------------------------------
class Enemy(Widget):
    personality = StringProperty("normal")
    enemy_speed = NumericProperty(2)
    def __init__(self, pos=(0, 0), personality="normal", speed=2 ,**kwargs):
        super().__init__(**kwargs)
        self.enemy_size = (100, 100)
        self.enemy_speed = speed
        self.vel_x = 2
        self.vel_y = 0
        self.direction = 1
        self.patrol_range = 200
        self.start_x = pos[0]
        self.pos  = pos
        self.personality = personality
        
        if self.personality == "aggressive":
            enemy_color = (1, 0, 0, 1) #Red
        elif self.personality == "cautious":
            enemy_color = (0, 0, 1, 0.7) #Blue
        elif self.personality == "zigzag":
            enemy_color = (1, 0.5, 0, 1) #Orange
        elif self.personality == "ambusher":
            enemy_color = (0.5, 0, 0.5, 1) #Purple
        elif self.personality == "lazy":
            enemy_color = (1, 1, 0, 1) #Yellow
        
        with self.canvas:
            Color(*enemy_color)
            self.enemy_rect = Rectangle(pos=self.pos, size=self.enemy_size)

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.enemy_rect.pos = self.pos
        self.enemy_rect.size = self.enemy_size

    def patrol(self):
        if self.personality == "aggressive":
            self.x += self.enemy_speed * self.direction * 1.5
        elif self.personality == "cautious":
            self.x += self.enemy_speed * self.direction * 0.5
        elif self.personality == "zigzag":
            self.x += self.enemy_speed * self.direction
            self.y += (self.enemy_speed / 2) * self.direction
        elif self.personality == "ambusher":
            player = self.parent
            
            if player:
                px_center = player.pos_x + player.size_square / 2
                ex_center = self.x + self.enemy_size[0] / 2
                distance = px_center - ex_center
                
                detection_range = 250
                
                if abs(distance) < detection_range:
                    self.x += self.enemy_speed * 2 if distance > 0 else -self.enemy_speed * 2
                else:
                    self.x += self.enemy_speed * 0.5 * self.direction
        elif self.personality == "lazy":
            self.x += self.enemy_speed * self.direction
        
        if abs(self.x - self.start_x) > self.patrol_range:
            self.direction *= -1
            self.x += self.enemy_speed * self.direction
            
        self.x = max(0, min(self.x, Window.width - self.enemy_size[0]))
        self.y = max(0, min(self.y, Window.height -self.enemy_size[1]))
            
#-----------------------------------------
#Boss
#-----------------------------------------
class Boss(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.mechanics = None
        self.boss_size = (150, 150)
        self.boss_health = 120
        self.boss_speed = 11
        self.boss_vx = random.choice([-1, 1]) * self.boss_speed
        self.boss_vy = random.choice([-1, 1]) * (self.boss_speed//2)
        self.direction = 1
        self.patrol_range = 200
        self.start_x = kwargs.get("pos", (0, 0))[0]
        
        with self.canvas:
            Color(1, 0, 0, 1.2)
            self.boss_rect = Rectangle(pos=self.pos, size=self.boss_size)
            
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        
    def update_graphics(self, *args):
        self.boss_rect.pos = self.pos
        self.boss_rect.size = self.boss_size
        
    def patrol(self):
        self.x += self.boss_speed * self.direction
        if abs(self.x - self.start_x) > self.patrol_range:
            self.direction *= -1
            self.x += self.boss_speed * self.direction
            
    def move(self):
        self.x += self.boss_vx
        self.y += self.boss_vy
        
        if self.x <= 0 or self.x + self.boss_size[0] >= Window.width:
            self.boss_vx *= -1
        if self.y <= 0 or self.y + self.boss_size[1] >= Window.height:
            self.boss_vy *= -1
            
    def chase_player(self, player_x, player_y):
        if random.random() < 0.02:
            self.boss_vx = self.boss_speed if player_x > self.x else -self.boss_speed
            self.boss_vy = self.boss_speed if player_y > self.y else -self.boss_speed
    
    def take_damage(self, amount):
        if self.god_mode:
            self.activate_god_mode()
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.defeat()
            
    def defeat(self):
        self.defeat_label = Label(text="Defeated", font_size=80, pos=(Window.width/2, Window.height/2), color=(0, 0, 0, 1))
        self.add_widget(self.defeat_label)
        for b in [self.btn, self.btn2, self.jump]:
            b.disabled = True
        Clock.unschedule(self.update)
        
class InvisibleSquare(Widget):
    def __init__(self, pos=(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.size = (100, 100)
        self.pos = pos
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
class RainbowSquare(Widget):
    def __init__(self, pos=(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.size = (100, 100)
        self.pos = pos
        with self.canvas:
            self.color = Color(random.random(), random.random(), random.random(),1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        Clock.schedule_interval(self.change_color, 0.2)
        
    def change_color(self, dt):
        self.color.r = random.random()
        self.color.g = random.random()
        self.color.b = random.random()
        
class AngrySquare(Widget):
    def __init__(self, pos=(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.size = (100, 100)
        self.pos = pos
        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        Clock.schedule_interval(self.chase_player, 1/30)
        
    def chase_player(self, dt):
        if hasattr(mechanics, "pos_x") and hasattr(mechanics, "pos_y"):
            mechanics = self.parent
            if not mechanics:
                return
            player_x = mechanics.pos_x + mechanics.size_square / 2
            player_y = mechanics.pos_y + mechanics.size_square / 2
            ex = self.x + self.size[0] / 2
            ey = self.y + self.size[1] / 2
            dx = player_x - self.pos[0]
            dy = player_y - self.pos[1]
            dist = (dx**2 + dy**2)**0.5
            if dist != 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist
                
            self.x = max(0, min(self.x, Window.width - self.size[0]))
            self.y = max(0, min(self.y, Window.height - self.size[1]))
            
            self.rect.pos = self.pos

#Square: Living Things
#Ellipse: Power items or Helper
#Triangle: DEV MODE!!!!
#Line: Do i exist?

# -----------------------------------------
# Kivy App
# -----------------------------------------
class LevelApp(App):
    def build(self):
        #Screen Manager
        sm = ScreenManager()
        #adding menu
        sm.add_widget(GameMenu(name="menu"))
        #Game
        game_screen = GameScreen(name="game")
        game_screen.add_widget(Mechanics())
        sm.add_widget(game_screen)
        
        return sm

# -----------------------------------------
# Run App
# -----------------------------------------
if __name__ == '__main__':
    LevelApp().run()
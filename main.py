import sqlite3

from datetime import datetime
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.videoplayer import VideoPlayer

# Класс главного экрана
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fonn.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Добавляем надпись на экран приветствия
        self.welcome_label = Label(text="Добро пожаловать в приложение \n        для ментального здоровья \n                   TranquilMind!",
                                   color=(0, 0, 0, 1), size_hint=(None, None), size=(Window.width, Window.height),
                                   font_name="fonts/ofont.ru_Chekharda.ttf", font_size=50)
        self.add_widget(self.welcome_label)

        # Запускаем таймер для исчезновения надписи через 3 секунды
        Clock.schedule_once(self.fade_out_label, 3)

    def fade_out_label(self, dt):
        # Анимация исчезновения надписи
        welcome_animation = Animation(opacity=0, duration=1)
        welcome_animation.bind(on_complete=self.show_buttons)
        welcome_animation.start(self.welcome_label)
        welcome_animation.start(self.background)

    def show_buttons(self, widget, value):
        # Создаем макет для основного экрана с кнопками
        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fonbut.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        main_layout = RelativeLayout(size_hint=(1, 1))
        meditation_button = Button(text="Начать медитацию", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                   size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.7}, opacity=0,
                                   font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        breathing_button = Button(text="Упражнения на дыхание", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                  size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.5}, opacity=0,
                                  font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        mood_tracking_button = Button(text="Отслеживание настроения", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                      size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.3}, opacity=0,
                                      font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)

        # Добавляем кнопки на экран и анимируем их появление
        main_layout.add_widget(meditation_button)
        main_layout.add_widget(breathing_button)
        main_layout.add_widget(mood_tracking_button)

        # Связываем кнопку "Начать медитацию" с методом для отображения экрана выбора медитации
        meditation_button.bind(on_press=self.switch_to_meditation_selection_screen)

        # Связываем кнопку "Упражнения на дыхание" с методом для отображения экрана упражнений на дыхание
        breathing_button.bind(on_press=self.switch_to_breathing_exercises_screen)

        # Связываем кнопку "Отслеживание настроения" с методом для отображения экрана отслеживания настроения
        mood_tracking_button.bind(on_press=self.switch_to_mood_tracking_screen)

        # Запускаем анимацию появления кнопок
        Animation(opacity=1, duration=1).start(meditation_button)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=1).start(breathing_button), 0.2)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=1).start(mood_tracking_button), 0.4)

        self.add_widget(main_layout)

    def switch_to_meditation_selection_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "meditation_selection_screen"

    def switch_to_breathing_exercises_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "breathing_exercises_screen"


    def switch_to_mood_tracking_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "mood_tracking_screen"

# Класс экрана выбора медитации
class MeditationSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(MeditationSelectionScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fonbut.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Создаем макет для кнопок выбора типа медитации
        self.selection_layout = RelativeLayout(size_hint=(1, 1))
        self.add_widget(self.selection_layout)

        # Добавляем кнопки для выбора типа медитации
        meditation_button_1 = Button(text="Майндфулнесс", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                    size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.7}, opacity=0,
                                    font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        meditation_button_2 = Button(text="Трансцендентальная \n      медитация", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                    size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.5}, opacity=0,
                                    font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        meditation_button_3 = Button(text="Випассана", background_color=(0, 1, 0, 1), size_hint=(None, None),
                                    size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.3}, opacity=0,
                                    font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)

        # Добавляем кнопку "Назад"
        back_button = Button(text="Назад", background_color=(1, 0, 0, 1), size_hint=(None, None),
                             size=(150, 50), pos_hint={'x': 0.02, 'top': 0.98}, opacity=0,
                             font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)

        # Привязываем обработчики событий для кнопок
        meditation_button_1.bind(on_press=self.switch_to_mindfulness_screen)
        back_button.bind(on_press=self.go_back)

        meditation_button_2.bind(on_press=self.switch_to_transcendental_meditation_screen)
        back_button.bind(on_press=self.go_back)

        meditation_button_3.bind(on_press=self.switch_to_vipassana_screen)
        back_button.bind(on_press=self.go_back)

        # Добавляем кнопки на экран и анимируем их появление
        self.selection_layout.add_widget(meditation_button_1)
        self.selection_layout.add_widget(meditation_button_2)
        self.selection_layout.add_widget(meditation_button_3)
        self.selection_layout.add_widget(back_button)

        # Запускаем анимацию появления кнопок
        Animation(opacity=1, duration=1).start(meditation_button_1)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=1).start(meditation_button_2), 0.2)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=1).start(meditation_button_3), 0.4)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=1).start(back_button), 0.6)

        # Привязываем обработчик события для кнопки "Назад"
        back_button.bind(on_press=self.go_back)

    # Метод для перехода на главный экран
    def go_back(self, instance):
        self.manager.transition.direction = 'right'  # Устанавливаем направление анимации
        self.manager.current = 'main_screen'  # Переходим на главный экран

    # Метод для перехода на экран с медитацией "Майндфулнесс"
    def switch_to_mindfulness_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "mindfulness_screen"

    # Метод для перехода на экран с медитацией TM
    def switch_to_transcendental_meditation_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "transcendental_meditation_screen"

    # Метод для перехода на экран с випассана
    def switch_to_vipassana_screen(self, instance):
        self.manager.transition.direction = 'left'  # Устанавливаем направление анимации
        self.manager.current = "vipassana_screen"

# Класс для 1 вида медитации
class MindfulnessScreen(Screen):
    def __init__(self, **kwargs):
        super(MindfulnessScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fontxt.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Создаем макет для экрана с вертикальной прокруткой
        layout = BoxLayout(orientation='vertical')

        # Создаем GridLayout для размещения контента на экране
        layout = GridLayout(cols=1, spacing=20, size_hint_y=None, padding=(30, 30))
        layout.bind(minimum_height=layout.setter('height'))

        # Добавляем текст о майндфулнесс-медитации
        mindfulness_text = (
            "Майндфулнесс-медитация — это практика, которая призвана улучшить осознанность и внимание к настоящему моменту. Она базируется на принципе активного внимания к тому, что происходит внутри и вокруг нас без суда или оценки. Основная идея — просто наблюдать свои мысли, эмоции, физические ощущения и внешние впечатления, не погружаясь в них и не привязываясь к ним.\n\n"
            "Как выполнять майндфулнесс-медитацию:\n\n"
            "1. Настройтесь на медитацию. Найдите спокойное место, где вас ничто не будет отвлекать. Сядьте в удобной позе, прямо или на стуле, закройте глаза или сфокусируйтесь на точке перед собой.\n\n"
            "2. Сосредоточьтесь на дыхании. Начните с того, чтобы просто обратить внимание на свое дыхание. Чувствуйте, как воздух входит и выходит из носа или рта. Не пытайтесь контролировать дыхание, просто наблюдайте за ним.\n\n"
            "3. Обратите внимание на свои мысли и ощущения. Когда вы медитируете, вы заметите, что ваш разум начнет блуждать. Это нормально. Просто заметьте, что вы думаете, какие чувства у вас возникают, а затем вернитесь к своему дыханию.\n\n"
            "4. Примите все, что возникает. Не старайтесь подавлять мысли или чувства. Просто примите их такими, какие они есть, и позвольте им уйти, вернувшись снова к своему дыханию.\n\n"
            "5. Продолжайте практиковать. Начинайте с небольших сессий — от 5 до 10 минут в день, постепенно увеличивая время. Регулярная практика поможет вам улучшить вашу осознанность и умение оставаться в настоящем моменте.\n\n"
            "Майндфулнесс-медитация может быть простой, но это не означает, что она легкая. Она требует практики и терпения, но может принести множество пользы для вашего физического и эмоционального благополучия."
        )

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))
        label = Label(text=mindfulness_text, font_size=24, size_hint_y=None,
                      color=(0, 0, 0, 1), padding=(30, 0), font_name="fonts/ofont.ru_Dudka.ttf")
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)))
        label.bind(texture_size=label.setter('size'))
        scroll_view.add_widget(label)
        layout.add_widget(scroll_view)

        # Создаем кнопку "Назад"
        back_button = Button(text="Назад", size_hint_y=None, height=50,
                             background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Добавляем GridLayout на экран
        self.add_widget(layout)

        # Метод для перехода на экран выбора медитации
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'meditation_selection_screen'

# Класс для 2 вида медитации
class TranscendentalMeditationScreen(Screen):
    def __init__(self, **kwargs):
        super(TranscendentalMeditationScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fontxt.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Создаем макет для экрана с вертикальной прокруткой
        layout = BoxLayout(orientation='vertical')

        # Создаем GridLayout для размещения контента на экране
        layout = GridLayout(cols=1, spacing=20, size_hint_y=None, padding=(30, 30))
        layout.bind(minimum_height=layout.setter('height'))

        # Добавляем текст о трансцендентальной медитации
        transcendental_meditation_text = (
            "Трансцендентальная медитация (ТМ) — это метод медитации, который был разработан в Индии в 1950-х годах Махариши Махеш Йоги. Он стал широко популярным благодаря своей простоте и эффективности. Основная идея ТМ — достижение состояния глубокого покоя и спокойствия путем повторения мантры.\n\n"
            "Как выполнять трансцендентальную медитацию:\n\n"
            "1. Подготовка к медитации. Найдите тихое место, где вас никто не будет беспокоить. Сядьте в удобной позе, закройте глаза и расслабьтесь.\n\n"
            "2. Выбор мантры. Мантра — это слово или фраза на санскрите, которую вы будете повторять во время медитации. Мантра в ТМ обычно индивидуализируется и предоставляется учителем медитации.\n\n"
            "3. Повторение мантры. Когда вы сидите в медитации, мягко и тихо повторяйте мантру в своем уме. Не старайтесь анализировать мантру или придумывать какие-то специальные мысли — просто позвольте ей быть.\n\n"
            "4. Допускание мыслей. Как и в любой медитации, в ТМ могут возникать мысли или ощущения. Когда это происходит, просто вернитесь к повторению мантры.\n\n"
            "5. Продолжайте медитацию. Практикуйте трансцендентальную медитацию в течение 15-20 минут два раза в день — утром и вечером.\n\n"
            "Основная идея трансцендентальной медитации заключается в том, что практика мантры помогает умиротворить разум и достичь состояния глубокой релаксации и покоя. Это состояние, по словам практикующих, может помочь улучшить концентрацию, снизить уровень стресса и повысить общее чувство благополучия.\n\n"
            "Важно отметить, что для обучения ТМ рекомендуется обратиться к квалифицированному учителю, который сможет предоставить вам индивидуализированную мантру и научить правильной технике медитации."
        )

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))
        label = Label(text=transcendental_meditation_text, font_size=24, size_hint_y=None,
                      color=(0, 0, 0, 1), padding=(30, 0), font_name="fonts/ofont.ru_Dudka.ttf")
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)))
        label.bind(texture_size=label.setter('size'))
        scroll_view.add_widget(label)
        layout.add_widget(scroll_view)

        # Создаем кнопку "Назад"
        back_button = Button(text="Назад", size_hint_y=None, height=50,
                             background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Добавляем GridLayout на экран
        self.add_widget(layout)

        # Метод для перехода на экран выбора медитации
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'meditation_selection_screen'

# Класс для 3 вида медитации
class VipassanaScreen(Screen):
    def __init__(self, **kwargs):
        super(VipassanaScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Добавляем фоновое изображение
        self.background = Image(source='C:/C_imlesii/Учёба/Диплом/pythonProject1/HealthApp/fontxt.jpg',
                                allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Создаем макет для экрана с вертикальной прокруткой
        layout = BoxLayout(orientation='vertical')

        # Создаем GridLayout для размещения контента на экране
        layout = GridLayout(cols=1, spacing=20, size_hint_y=None, padding=(30, 30))
        layout.bind(minimum_height=layout.setter('height'))

        # Добавляем текст о Випассана
        vipassana_text = (
            "Випассана — это древняя техника медитации, которая возникла в буддийской традиции. Термин 'Випассана' на санскрите означает 'осмотрение' или 'различение'. Этот метод медитации призван развить глубокое понимание реальности путем наблюдения за тем, что происходит внутри нас и вокруг нас.\n\n"
            "Как выполнять випассану:\n\n"
            "1. Подготовка к медитации. Найдите тихое место для сидения, где вас не будут беспокоить. Сядьте в удобной позе, закройте глаза или оставьте их приоткрытыми, и сфокусируйтесь на своем дыхании.\n\n"
            "2. Наблюдение за дыханием. Начните медитацию, обращая внимание на свое дыхание. Просто наблюдайте, как воздух входит и выходит из носа или рта. Не старайтесь изменить дыхание, просто наблюдайте за ним.\n\n"
            "3. Обращение внимания на телесные ощущения. По мере того как вы сидите и наблюдаете за дыханием, вы можете начать замечать различные телесные ощущения, такие как дискомфорт, боль, тепло или холод. Просто наблюдайте эти ощущения без суда или стремления изменить их.\n\n"
            "4. Примечание мыслей и чувств. В процессе медитации могут возникать различные мысли, эмоции и чувства. Просто замечайте их, но не привязывайтесь к ним. Позвольте им прийти и уйти, возвращаясь снова к своему дыханию или телесным ощущениям.\n\n"
            "5. Продолжайте медитацию. Продолжайте практиковать Випассану в течение определенного периода времени, обычно от 20 минут до нескольких часов в день. Постепенно увеличивайте время медитации по мере того, как ваша практика становится более глубокой.\n\n"
            "Целью випассана-медитации является развитие глубокого понимания реальности путем наблюдения за нашими телесными ощущениями, мыслями и эмоциями без привязки к ним. Это практика, которая может помочь нам освободиться от страданий и достичь внутреннего спокойствия и мудрости."
        )

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))
        label = Label(text=vipassana_text, font_size=24, size_hint_y=None,
                      color=(0, 0, 0, 1), padding=(30, 0), font_name="fonts/ofont.ru_Dudka.ttf")
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)))
        label.bind(texture_size=label.setter('size'))
        scroll_view.add_widget(label)
        layout.add_widget(scroll_view)

        # Создаем кнопку "Назад"
        back_button = Button(text="Назад", size_hint_y=None, height=50,
                             background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Добавляем GridLayout на экран
        self.add_widget(layout)

    # Метод для перехода на экран выбора медитации
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'meditation_selection_screen'

# Класс для экрана с видео упражнениями на дыхание
class BreathingExercisesScreen(Screen):
    def __init__(self, **kwargs):
        super(BreathingExercisesScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        # Пути к видео
        self.video_paths = [
            "video/video1.mp4",
            "video/video2.mp4",
            "video/video3.mp4",
            "video/video4.mp4"
        ]

        # Создаем кнопки для каждого видео
        for i, path in enumerate(self.video_paths, start=1):
            button = Button(text=f"Видео {i}", size_hint=(1, None), height=50,
                            background_color=(0, 1, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
            button.bind(on_press=lambda instance, p=path: self.play_video(p))
            self.layout.add_widget(button)

        # Создаем видеоплеер
        self.video_player = VideoPlayer(size_hint=(1, 0.8))  # Занимает 80% высоты экрана
        self.layout.add_widget(self.video_player)

        # Создаем кнопку "Назад"
        back_button = Button(text="Назад", size_hint=(1, None), height=50,
                             background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf", font_size=20)
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    # Метод для воспроизведения видео
    def play_video(self, path):
        self.video_player.source = path
        self.video_player.state = 'play'

    # Метод для перехода на экран выбора медитации
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

    # Метод вызывается при выходе из экрана
    def on_leave(self, *args):
        # При выходе из экрана останавливаем видеоплеер
        if self.video_player:
            self.video_player.state = 'stop'

# Класс для кнопки "Отслеживание настроения"
class MoodTrackingScreen(Screen):
    def __init__(self, **kwargs):
        super(MoodTrackingScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Создаем вертикальный макет для элементов на экране
        layout = BoxLayout(orientation='vertical', spacing=10, padding=30)

        # Добавляем метку для заголовка
        title_label = Label(
            text="Отслеживание настроения — это важная часть заботы о своем эмоциональном благополучии. "
                 "Записывайте свое настроение каждый день, "
                 "чтобы вы могли увидеть, как оно меняется со временем.",
            font_size=26,
            font_name="fonts/ofont.ru_Dudka.ttf",
            color=(0, 0, 0, 1),
            text_size=(Window.width - 60, None),
            halign='center',
            valign='middle',
        )
        layout.add_widget(title_label)

        # Добавляем метку для выбора даты
        date_label = Label(text="Выберите дату:", font_size=22, font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 1, 0, 1))
        layout.add_widget(date_label)

        # Добавляем поле для выбора даты
        self.date_input = TextInput(hint_text="ДД-ММ-ГГГГ", font_size=20)
        layout.add_widget(self.date_input)

        # Добавляем метку для выбора настроения
        mood_label = Label(text="Выберите настроение:", font_size=22, font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 1, 0, 1))
        layout.add_widget(mood_label)

        # Создаем кнопки для выбора настроения
        mood_buttons_layout = BoxLayout(spacing=10)
        moods = ["Отлично", "Хорошо", "Нейтрально", "Плохо", "Ужасно"]
        self.mood_buttons = []
        for mood in moods:
            button = Button(text=mood, font_size=20, font_name="fonts/ofont.ru_Dudka.ttf")
            button.bind(on_press=self.set_mood)
            mood_buttons_layout.add_widget(button)
            self.mood_buttons.append(button)
        layout.add_widget(mood_buttons_layout)

        # Добавляем поле для записи заметок
        note_label = Label(text="Добавьте заметку (опционально):", font_size=22, font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 1, 0, 1))
        layout.add_widget(note_label)
        self.note_input = TextInput(hint_text="Ваш комментарий", font_size=20)
        layout.add_widget(self.note_input)

        # Добавляем кнопку для сохранения данных
        save_button = Button(text="Сохранить", font_size=20, background_color=(0, 1, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf")
        save_button.bind(on_press=self.save_mood_data)
        layout.add_widget(save_button)

        # Добавляем кнопку для просмотра сохраненных данных
        view_data_button = Button(text="Просмотр данных", font_size=20, background_color=(0, 1, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf")
        view_data_button.bind(on_press=self.view_saved_data)
        layout.add_widget(view_data_button)

        # Добавляем кнопку "Назад"
        back_button = Button(text="Назад", font_size=20, background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf")
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    # Метод для установки выбранного настроения
    def set_mood(self, instance):
        for button in self.mood_buttons:
            button.background_color = (0.6, 0.6, 0.6, 1)
        instance.background_color = (0, 1, 0, 1)
        self.selected_mood = instance.text

    # Метод для сохранения данных о настроении
    def save_mood_data(self, instance):
        date = self.date_input.text
        mood = self.selected_mood if hasattr(self, 'selected_mood') else None
        note = self.note_input.text if self.note_input.text.strip() != "" else None

        # Конвертируем дату в формат ДД-ММ-ГГГГ
        try:
            formatted_date = datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            # Если формат даты неверный, можно обработать ошибку или вернуть ошибку пользователю
            self.date_input.hint_text = "Неверный формат даты. Используйте ДД-ММ-ГГГГ."
            self.date_input.text = ""
            return

        conn = sqlite3.connect("mood_data.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS mood_data (date TEXT, mood TEXT, note TEXT)")
        c.execute("INSERT INTO mood_data (date, mood, note) VALUES (?, ?, ?)", (formatted_date, mood, note))
        conn.commit()
        conn.close()

        # После сохранения данных можно очистить поля ввода
        self.date_input.text = ""
        self.note_input.text = ""
        for button in self.mood_buttons:
            button.background_color = (0.6, 0.6, 0.6, 1)

    # Метод для перехода к экрану просмотра сохраненных данных
    def view_saved_data(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'view_mood_data_screen'

    # Метод для перехода на предыдущий экран
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

# Класс для просмотра сохраненных данных
class ViewMoodDataScreen(Screen):
    def __init__(self, **kwargs):
        super(ViewMoodDataScreen, self).__init__(**kwargs)

        # Задаем цвет фона экрана
        Window.clearcolor = (1, 1, 1, 1)  # Белый цвет фона

        # Создаем вертикальный макет для элементов на экране
        layout = BoxLayout(orientation='vertical', spacing=10, padding=30)

        # Создаем ScrollView для отображения данных
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))

        # Создаем макет для отображения данных
        self.data_layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))
        scroll_view.add_widget(self.data_layout)
        layout.add_widget(scroll_view)

        # Добавляем кнопку "Назад"
        back_button = Button(text="Назад", font_size=20, background_color=(1, 0, 0, 1), font_name="fonts/ofont.ru_Newland Black.ttf")
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    # Метод для отображения сохраненных данных
    def on_pre_enter(self, *args):
        self.data_layout.clear_widgets()
        conn = sqlite3.connect("mood_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM mood_data ORDER BY date ASC")
        data = c.fetchall()
        conn.close()

        if data:
            for row in data:
                if row[0]:  # Проверка, что дата не пуста
                    # Конвертируем дату обратно в формат ДД-ММ-ГГГГ
                    formatted_date = datetime.strptime(row[0], "%Y-%m-%d").strftime("%d-%m-%Y")
                else:
                    formatted_date = "Нет данных"

                # Label для даты
                date_label = Label(text=formatted_date, font_size=20, size_hint=(0.2, None), height=40,
                                   font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 0, 0, 1))

                # Label для настроения
                mood_label = Label(text=row[1], font_size=20, size_hint=(0.2, None), height=40,
                                   font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 0, 0, 1))

                # Label для заметок
                note_label = Label(text=row[2], font_size=20, size_hint=(0.6, None), height=40,
                                   font_name="fonts/ofont.ru_Dudka.ttf", color=(0, 0, 0, 1))

                self.data_layout.add_widget(date_label)
                self.data_layout.add_widget(mood_label)
                self.data_layout.add_widget(note_label)

        else:
            no_data_label = Label(text="Нет сохраненных данных", font_size=20, font_name="fonts/ofont.ru_Dudka.ttf",
                                  color=(0, 0, 0, 1))
            self.data_layout.add_widget(no_data_label)

    # Метод для перехода на предыдущий экран
    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'mood_tracking_screen'


class HealthApp(App):
    def build(self):
        # Создаем менеджер экранов
        sm = ScreenManager()

        # Добавляем главный экран
        main_screen = MainScreen(name="main_screen")
        sm.add_widget(main_screen)

        # Добавляем экран выбора медитации
        meditation_selection_screen = MeditationSelectionScreen(name="meditation_selection_screen")
        sm.add_widget(meditation_selection_screen)

        # Добавляем экран медитации "Майндфулнесс"
        mindfulness_screen = MindfulnessScreen(name="mindfulness_screen")
        sm.add_widget(mindfulness_screen)

        # Добавляем экран медитации "Трансцендентальная медитация"
        transcendental_meditation_screen = TranscendentalMeditationScreen(name="transcendental_meditation_screen")
        sm.add_widget(transcendental_meditation_screen)

        # Добавляем экран медитации "Випассана"
        vipassana_screen = VipassanaScreen(name="vipassana_screen")
        sm.add_widget(vipassana_screen)

        # Добавляем экран просмотра видео
        breathing_exercises_screen = BreathingExercisesScreen(name="breathing_exercises_screen")
        sm.add_widget(breathing_exercises_screen)

        # Добавляем экран отслеживания настроения
        mood_tracking_screen = MoodTrackingScreen(name="mood_tracking_screen")
        sm.add_widget(mood_tracking_screen)

        # Добавляем экран просмотра сохраненных данных о настроении
        view_mood_data_screen = ViewMoodDataScreen(name="view_mood_data_screen")
        sm.add_widget(view_mood_data_screen)

        return sm


# Запуск приложения
if __name__ == '__main__':
    HealthApp().run()
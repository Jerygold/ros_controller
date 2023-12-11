import ctypes

import pygame

import pygame_menu

from track import Track_dataset

ctypes.windll.user32.SetProcessDPIAware()


class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self._screen_size = pygame.Vector2(1920, 1080)
        self._rendering_surface = pygame.Surface(self._screen_size)
        self._screen = pygame.display.set_mode(self._screen_size, pygame.FULLSCREEN)

        self._fps = 60
        self._dt = 0
        self._frame_count = 0
        self._clock = pygame.time.Clock()
        self._is_running = False
        self._is_paused = False

        self._simulation_menu = pygame_menu.Menu('Simulation', 300, self._screen_size.y)
        self._simulation_menu.set_absolute_position(0, 0)
        self._simulation_menu.add.button('Quit', lambda: setattr(self, '_is_running', False))
        self._simulation_menu.add.button('Pause', lambda: setattr(self, '_is_paused', not self._is_paused))
        self._simulation_menu.add.range_slider('FPS', default=self._fps, onchange=lambda x: setattr(self, '_fps', int(x)),
                                               range_values=(0, 60), increment=1)
        self._fps_label = self._simulation_menu.add.label(f'fps: {self._fps}', label_id='fps_label')
        self._dt_label = self._simulation_menu.add.label(f'dt: {self._dt}', label_id='dt_label')
        self._frame_label = self._simulation_menu.add.label('frame: 0', label_id='frame_label')

        self._track_dataset = Track_dataset(pygame.Rect(300, 0, self._screen_size.x - 600, self._screen_size.y))
        self._track_dataset_menu = pygame_menu.Menu('Select Track', 300, self._screen_size.y)
        self._track_dataset_menu.set_absolute_position(self._screen_size.x - 300, 0)
        for index, track in enumerate(self._track_dataset.get_tracks()):
            self._track_dataset_menu.add.button(track.get_name(), self._track_dataset.set_current_track, index)

    def run(self):
        self._is_running = True
        while self._is_running:
            self._dt = self._clock.tick(self._fps)
            self._handle_events()
            if not self._is_paused:
                self._update(self._dt)
            self._draw()
        self._quit()

    def _quit(self):
        pygame.quit()

    def _handle_events(self):
        events = pygame.event.get()

        self._simulation_menu.update(events)
        self._track_dataset_menu.update(events)

        for event in events:
            if event.type == pygame.QUIT:
                self._is_running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._is_running = False

    def _update(self, dt: float):
        current_fps = self._clock.get_fps()
        self._fps_label.set_title(f'fps: {current_fps:.2f}')
        self._dt_label.set_title(f'dt: {dt}')
        self._frame_label.set_title(f'frame: {self._frame_count}')
        self._frame_count += 1

    def _draw(self):
        self._rendering_surface.fill((0, 0, 0))
        self._screen.fill((0, 0, 0))

        self._simulation_menu.draw(self._rendering_surface)
        self._track_dataset_menu.draw(self._rendering_surface)

        self._track_dataset.draw_current_track(self._rendering_surface)

        # self._car.draw(self._rendering_surface)

        self._screen.blit(self._rendering_surface, (0, 0))

        pygame.display.flip()

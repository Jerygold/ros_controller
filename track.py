import os

import pygame

from scipy.spatial import KDTree


def map(value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def get_min_max_values(arrays: list[list[pygame.Vector2]]):
    min_x = min(min(array, key=lambda v: v.x).x for array in arrays if array)
    max_x = max(max(array, key=lambda v: v.x).x for array in arrays if array)
    min_y = min(min(array, key=lambda v: v.y).y for array in arrays if array)
    max_y = max(max(array, key=lambda v: v.y).y for array in arrays if array)

    return min_x, max_x, min_y, max_y


def convert_to_screen_space(screen_size: tuple[int, int], arrays: list[list[pygame.Vector2]], padding: int = 50):
    min_x, max_x, min_y, max_y = get_min_max_values(arrays)

    for array in arrays:
        for point in array:
            point.x = map(point.x, min_x, max_x, padding, screen_size[0] - padding)
            point.y = map(point.y, min_y, max_y, padding, screen_size[1] - padding)


class Track:
    def __init__(self, file_path: str, file_name: str, screen_rect: pygame.Rect):
        self._file_path = file_path
        self._name = file_name
        self._screen_rect = screen_rect
        self._rendered_surface = pygame.Surface(screen_rect.size)
        self.is_loaded = False

        self._center_line: list[pygame.Vector2] = []
        self._left_edge: list[pygame.Vector2] = []
        self._right_edge: list[pygame.Vector2] = []
        self.edges_array: list[pygame.Vector2] = []
        self.kdtree = None

    def init(self):
        if self.is_loaded:
            return
        else:
            self._load_from_file(self._file_path + self._name)
            convert_to_screen_space(self._screen_rect.size, [self._center_line, self._left_edge, self._right_edge], 100)
            self.is_loaded = True

    def _load_from_file(self, file_path: str):
        with open(file_path) as file:
            previous_point = None
            min_edge_distance = 0
            for row in file:
                if row.startswith("#"):
                    continue
                values = row.split(",")
                center_point = pygame.Vector2(float(values[0]), float(values[1]))
                self._center_line.append(center_point)

                if previous_point:
                    tangent = (center_point - previous_point).normalize()
                    perp_vec = pygame.Vector2(-tangent.y, tangent.x)

                    left_distance = float(values[2])
                    right_distance = float(values[3])
                    left_edge_point = center_point + perp_vec * (left_distance + min_edge_distance)
                    right_edge_point = center_point - perp_vec * (right_distance + min_edge_distance)

                    self._left_edge.append(left_edge_point)
                    self._right_edge.append(right_edge_point)

                previous_point = center_point

            self.edges_array = self._left_edge + self._right_edge
            self.kdtree = KDTree(self.edges_array)

        # self.print_lines()

    def render(self):
        self._rendered_surface.fill((50, 50, 70))
        for point in self._center_line:
            pygame.draw.circle(self._rendered_surface, (255, 255, 255), point, 1)
        for point in self._left_edge:
            pygame.draw.circle(self._rendered_surface, (255, 255, 0), point, 1)
        for point in self._right_edge:
            pygame.draw.circle(self._rendered_surface, (0, 0, 255), point, 1)

    def draw(self, surface: pygame.Surface):
        surface.blit(self._rendered_surface, (self._screen_rect.x, self._screen_rect.y))

    def get_name(self) -> str:
        return self._name

    def print_lines(self):
        string = ""
        for point in self._center_line:
            str = point.__str__()
            string += str + ","
        print(string)
        string = ""
        for point in self._left_edge:
            str = point.__str__()
            string += str + ","
        print(string)
        string = ""
        for point in self._right_edge:
            str = point.__str__()
            string += str + ","
        print(string)


class Track_dataset:
    def __init__(self, screen_rect: pygame.Rect):
        self._screen_rect = screen_rect
        self._tracks: list[Track] = []
        self._load_dataset(self._screen_rect)
        self._current_track_id = 0
        
    def _load_dataset(self, screen_rect: pygame.Rect):
        path = "datasets/tracks/"
        files = os.listdir(path)
        for file in files:
            track = Track(path, file, screen_rect)
            self._tracks.append(track)
        self.set_current_track(0)

    def set_current_track(self, id: int):
        if id < 0 or id >= len(self._tracks):
            print("Invalid track id")
            return

        self._current_track_id = id
        self._tracks[self._current_track_id].init()
        self.update_track_render()

    def get_tracks(self) -> list[Track]:
        return self._tracks

    def get_current_track(self) -> Track:
        return self._tracks[self._current_track_id]

    def get_raycast_args(self):
        return self._tracks[self._current_track_id].kdtree, self._tracks[self._current_track_id].edges_array

    def update_track_render(self):
        self._tracks[self._current_track_id].render()

    def draw_current_track(self, surface: pygame.Surface):
        self._tracks[self._current_track_id].draw(surface)

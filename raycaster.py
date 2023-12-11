import pygame

import random

import math

from scipy.spatial import KDTree


class RayCaster:
    def __init__(self):
        self._num_rays = 50
        self._max_distance = 200
        self._start_angle = -180
        self._end_angle = 0
        self.ray_lengths = []

    def cast_rays(self, origin, kdtree, points):
        self.ray_lengths = []
        near_points_indices = kdtree.query_ball_point(origin, self._max_distance)
        step = max(1, (self._end_angle - self._start_angle) // self._num_rays)
        for angle in range(self._start_angle, self._end_angle, step):
            rad = math.radians(angle)
            closest_distance = self._max_distance

            for i in near_points_indices:
                point = points[i]
                bx, by = point
                dx, dy = math.cos(rad), math.sin(rad)
                fx, fy = bx - origin[0], by - origin[1]
                t = fx * dx + fy * dy

                # Check if the ray is pointing towards the ball
                if t > 0:
                    closest_x = origin[0] + dx * t
                    closest_y = origin[1] + dy * t

                    # Check if this point is within the ball's radius
                    distance_to_ball = math.hypot(bx - closest_x, by - closest_y)

                    if distance_to_ball < 3:
                        # Find distance from origin to the closest collision point
                        collision_distance = math.hypot(origin[0] - closest_x, origin[1] - closest_y)

                        if collision_distance < closest_distance:
                            closest_distance = collision_distance

            self.ray_lengths.append(closest_distance)
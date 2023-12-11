import pygame
import random
import math
from scipy.spatial import KDTree

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycasting with Pygame")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball settings
BALL_COUNT = 20
BALL_RADIUS = 10
balls = []

# Ray settings
start_angle = -180
end_angle = 0
num_rays = 50
max_distance = 200  # Set this according to your needs, perhaps the diagonal of the screen

# Create random balls
for _ in range(BALL_COUNT):
    balls.append((random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
                  random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)))

# Create a KDTree for fast nearest neighbor lookup
ball_tree = KDTree(balls)


def cast_rays(origin):
    ray_lengths = []
    near_balls_indices = ball_tree.query_ball_point(origin, max_distance)
    step = max(1, (end_angle - start_angle) // num_rays)
    for angle in range(start_angle, end_angle, step):
        rad = math.radians(angle)
        closest_distance = max_distance

        for i in near_balls_indices:
            ball = balls[i]
            bx, by = ball
            dx, dy = math.cos(rad), math.sin(rad)
            fx, fy = bx - origin[0], by - origin[1]
            t = fx * dx + fy * dy

            # Check if the ray is pointing towards the ball
            if t > 0:
                closest_x = origin[0] + dx * t
                closest_y = origin[1] + dy * t

                # Check if this point is within the ball's radius
                distance_to_ball = math.hypot(bx - closest_x, by - closest_y)

                if distance_to_ball < BALL_RADIUS:
                    # Find distance from origin to the closest collision point
                    collision_distance = math.hypot(origin[0] - closest_x, origin[1] - closest_y)

                    if collision_distance < closest_distance:
                        closest_distance = collision_distance

        # Store the ray length
        ray_lengths.append(closest_distance)

        # Draw the ray up to the closest collision point for each angle
        end_x = int(origin[0] + closest_distance * math.cos(rad))
        end_y = int(origin[1] + closest_distance * math.sin(rad))
        pygame.draw.line(screen, WHITE, origin, (end_x, end_y), 1)

    return ray_lengths


def display_ray_lengths(ray_lengths):
    square_size = WIDTH // len(ray_lengths)
    for i, length in enumerate(ray_lengths):
        normalized_length = length / max_distance
        color_intensity = int(255 * (1 - normalized_length))
        color = (color_intensity, color_intensity, color_intensity)
        pygame.draw.rect(screen, color, (i * square_size, HEIGHT - square_size, square_size, square_size))


# Main loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.set_caption("Raycasting with Pygame | FPS: " + str(int(clock.get_fps())))

    screen.fill((50, 50, 50))  # Clear screen

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Cast rays from mouse position
    ray_lengths = cast_rays(mouse_pos)

    # Display ray lengths as squares
    display_ray_lengths(ray_lengths)

    # Draw the balls
    for ball in balls:
        pygame.draw.circle(screen, RED, ball, BALL_RADIUS)

    pygame.display.flip()

pygame.quit()

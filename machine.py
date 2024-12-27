# Define a simple road map using a 2D grid
# 0 = empty road, 1 = obstacle, 2 = car
road_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]


def print_road_map(road_map):
    """Function to print the road map."""
    for row in road_map:
        print(" ".join(str(cell) for cell in row))
    print()


def find_car_position(road_map):
    """Find the position of the car in the road map."""
    for i, row in enumerate(road_map):
        for j, cell in enumerate(row):
            if cell == 2:  # Car position
                return i, j
    return None


def move_car(road_map, direction):
    """Move the car in the given direction."""
    i, j = find_car_position(road_map)
    if direction == "up" and i > 0 and road_map[i - 1][j] == 0:
        road_map[i][j], road_map[i - 1][j] = 0, 2
    elif direction == "down" and i < len(road_map) - 1 and road_map[i + 1][j] == 0:
        road_map[i][j], road_map[i + 1][j] = 0, 2
    elif direction == "left" and j > 0 and road_map[i][j - 1] == 0:
        road_map[i][j], road_map[i][j - 1] = 0, 2
    elif direction == "right" and j < len(road_map[0]) - 1 and road_map[i][j + 1] == 0:
        road_map[i][j], road_map[i][j + 1] = 0, 2


def detect_obstacles(road_map, car_position):
    """Detect obstacles around the car."""
    i, j = car_position
    obstacles = []
    if i > 0 and road_map[i - 1][j] == 1:
        obstacles.append("up")
    if i < len(road_map) - 1 and road_map[i + 1][j] == 1:
        obstacles.append("down")
    if j > 0 and road_map[i][j - 1] == 1:
        obstacles.append("left")
    if j < len(road_map[0]) - 1 and road_map[i][j + 1] == 1:
        obstacles.append("right")
    return obstacles


# Main loop
print("Initial Road Map:")
print_road_map(road_map)

for _ in range(5):  # Simulate 5 steps
    car_position = find_car_position(road_map)
    obstacles = detect_obstacles(road_map, car_position)
    print(f"Car Position: {car_position}")
    print(f"Detected Obstacles: {obstacles}")

    # Move the car randomly avoiding obstacles
    possible_moves = ["up", "down", "left", "right"]
    for move in possible_moves:
        if move not in obstacles:
            move_car(road_map, move)
            break

    print("Updated Road Map:")
    print_road_map(road_map)

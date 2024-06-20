import random

def generate_path(N, M, filename):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly. Exceptions for TypeError
    # and KeyError are handled.

    # your code here
    try:        #uses try except loop to iterate all lines of the file
        maze_file = open(filename, 'r')
        maze = {}
        for i in range(N):
            line = maze_file.readline().strip() #splits the lines and changes the value of the background board (numbers) according to the on screen board
            for j in range(M):
                cell = line[4 * j + 1]
                if cell == ' ':
                    maze[(i, j)] = 0
                elif cell == 'X':
                    maze[(i, j)] = 1
                elif cell == 'O':
                    maze[(i, j)] = 2
        maze_file.close()
        return maze
    except FileNotFoundError:
        print("Error: File not found!")
        return None

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    numbers_obstacles = 0       #start value of the obstacles
    try:
        while numbers_obstacles < min_obstacles:
            row = random.randint(0, N - 1)
            col = random.randint(0, M - 1)
            if maze[(row, col)] == 0:  # Check whether the cell is empty
                maze[(row, col)] = 1
                numbers_obstacles += 1
    except KeyError:
        print('There is a Key Error!')

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        row, col = map(int, input('Enter the coordinates to set an obstacle (row col): ').split())
        if row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError
        if maze[(row, col)] == 2:
            print("Cannot place an obstacle on the path!")
        elif maze[(row, col)] == 1:
            print("Obstacle already exists at this location.")
        else:
            maze[(row, col)] = 1
            print("Obstacle set at coordinates:", (row, col))
    except ValueError:
        print("Value Error in set obstacle function. Need to be coordinates")

def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        row, col = map(int, input('Enter the coordinates to remove an obstacle (row col): ').split())
        if row < 0 or row >= N or col < 0 or col >= M:
            print("Obstacle cannot be removed on the path")
        elif maze[(row, col)] == 2:
            print("There are no obstacles to remove")
        else:
            maze[(row-1, col-1)] = 0
            print("Obstacle removed from coordinates:", (row, col))
    except ValueError:
        print("Error: Invalid coordinates. Please enter integers.")

def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string:
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells. If a KeyError occurs while trying to access a cell, it is
    # caught and a message is printed.

    # your code here
    print("+---" * M + "+")
    for i in range(N):
        for j in range(M):
            cell = maze.get((i, j), 0)
            if cell == 0:
                print("|   ", end="")
            elif cell == 1:
                print("| X ", end="")
            else:
                print("| O ", end="")
        print("|")
        print("+---" * M + "+")

def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here    #main fucntion that runs the whole program
    try:
        filename = input("Enter the maze grid blueprint filename: ")
        maze_file = open(filename, 'r')
        N = int(filename[4])
        M = int(filename[5])
        maze_file.close()
    except IOError:
        print("Error: File not found.")
        return

    maze = generate_path(N, M, filename)
    try:
        min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
        if min_obstacles < 0:
            raise ValueError
    except ValueError:
        print("Invalid number of obstacles. Please enter a non-negative integer.")
        return

    add_obstacles(maze, min_obstacles, N, M)

    while True:
        print("Menu:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Print maze")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                set_obstacle(maze, N, M)
            elif choice == 2:
                remove_obstacle(maze, N, M)
            elif choice == 3:
                print_maze(maze, N, M)
            elif choice == 4:
                print("Exiting the program...")
                break
            else:
                print("Error: Invalid choice. Please enter a number from 1 to 4.")
        except ValueError:
            print("Error: Invalid choice. Please enter a number.")

main()

import tkinter as tk
from PIL import Image, ImageTk
from time import strftime

class ImageGridApp:
    def __init__(self, root):
        version = 0.03
        self.root = root
        self.root.title(str(version))

        self.image_paths = [
            "PizzaStoreTracker/image3.png", "PizzaStoreTracker/image2.png",
            "PizzaStoreTracker/pizza.jpg", "PizzaStoreTracker/image4.png",
            "PizzaStoreTracker/image5.jpg", "PizzaStoreTracker/image6.png",
            "PizzaStoreTracker/image7.jpg", "PizzaStoreTracker/maze.jpg"]
        self.rows, self.columns = 2, 4
        self.create_image_grid()
        self.root.bind("<ButtonRelease-1>", self.on_thumbnail_click)
        
    def create_image_grid(self):
        self.frame = tk.Frame(self.root) 
        self.frame.grid(row=0, column=0)

        self.photo_images = []  
        self.labels = []  

        for i in range(self.rows):
            for j in range(self.columns):
                img = Image.open(self.image_paths[i * self.columns + j])
                img.thumbnail((200, 200))  
                tk_img = ImageTk.PhotoImage(img)
                self.photo_images.append(tk_img)  
                label = tk.Label(self.frame, image=tk_img)
                label.grid(row=i, column=j, padx=5, pady=5)
                label_button = tk.Label(self.frame, image=tk_img, cursor="hand2")
                label_button.grid(row=i, column=j, padx=5, pady=5)
                label_button.bind("<Button-1>", lambda event, i=i, j=j: self.on_thumbnail_click(i, j))
                self.labels.append(label_button)

    def create_time_grid(self):
        frame = tk.Frame(self.root, width=800, height=400)
        frame.grid(row=1, column=3, padx=5, pady=5)
        frame.config(bg="black")
        self.time_frame = frame  
        time_label = tk.Label(frame, font=('Courier', 85, 'bold'), background='black', foreground='white')
        time_label.place(relx=0.5, rely=0.5, anchor='center')
        back_button = tk.Button(frame, font=('Courier', 30, 'bold'), background='black', foreground='red', cursor="hand2", command=self.back)
        back_button.place(x=25,y=300)
        self.update_time(time_label)
        self.update_back(back_button)

    def create_calculator_grid(self):
        frame = tk.Frame(self.root, width = 800, height = 400)
        frame.grid(row=1, column=3, padx=5, pady=5)
        frame.config(bg="black")
        self.time_frame = frame
        back_button = tk.Button(frame, font=('Courier', 30 , 'bold'), background = 'black', foreground ='red', cursor = "hand2", command = self.back)
        back_button.place(x=25,y=300)
        self.update_back(back_button)
        
    def create_temp_grid(self):
        frame = tk.Frame(self.root, width = 800, height = 400)
        frame.grid (row =1, column = 3, padx= 5, pady = 5)
        frame.config(bg="black")
        self.time_frame = frame
        temp_label = tk.Label(frame, font=('Courier', 85, 'bold'), background='black', foreground='white')
        temp_label.place(relx=0.5, rely=0.5, anchor='center')
        back_button = tk.Button(frame, font = ('Courier', 30 , 'bold'), background = 'black', foreground = 'red', cursor = 'hand2', command = self.back)
        back_button.place(x=25, y = 300)
        self.update_temp(temp_label)
        self.update_back(back_button)

    def create_maze_grid(self):
        import pygame
        import sys
        import random

        # Initialize Pygame
        pygame.init()

        # Constants
        WIDTH, HEIGHT = 800, 400  # Previous screen size
        FPS = 60
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        PLAYER_SIZE = 50

        # Maze dimensions
        MAZE_WIDTH = WIDTH // PLAYER_SIZE
        MAZE_HEIGHT = HEIGHT // PLAYER_SIZE

        # Initialize the screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Game")
        clock = pygame.time.Clock()

        # Generate a random maze using Recursive Backtracking algorithm
        def generate_maze():
            maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
            stack = []
            start_x, start_y = random.randint(1, (MAZE_WIDTH // 2) - 1) * 2, random.randint(1, (MAZE_HEIGHT // 2) - 1) * 2
            stack.append((start_x, start_y))
            maze[start_y][start_x] = 0

            while stack:
                current_x, current_y = stack[-1]

                neighbors = [(current_x + 2, current_y), (current_x - 2, current_y),
                            (current_x, current_y + 2), (current_x, current_y - 2)]

                unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == 1]

                if unvisited_neighbors:
                    next_x, next_y = random.choice(unvisited_neighbors)
                    maze[next_y][next_x] = 0
                    maze[(current_y + next_y) // 2][(current_x + next_x) // 2] = 0
                    stack.append((next_x, next_y))
                else:
                    stack.pop()

            return maze

        # Initialize maze, player position, and completion counter
        maze = generate_maze()
        player_x, player_y = 1, 1
        goal_x, goal_y = MAZE_WIDTH - 2, MAZE_HEIGHT - 2
        completed_mazes = 0

        # Arrow buttons
        arrow_buttons = {
            "left": pygame.Rect(50, 300, 50, 50),
            "right": pygame.Rect(150, 300, 50, 50),
            "up": pygame.Rect(100, 250, 50, 50),
            "down": pygame.Rect(100, 350, 50, 50),
        }

        font = pygame.font.Font(None, 36)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        for direction, rect in arrow_buttons.items():
                            if rect.collidepoint(event.pos):
                                # Simulate arrow key presses based on clicked button
                                if direction == "left":
                                    player_x = max(0, player_x - 1) if maze[player_y][player_x - 1] != 1 else player_x
                                elif direction == "right":
                                    player_x = min(MAZE_WIDTH - 1, player_x + 1) if maze[player_y][player_x + 1] != 1 else player_x
                                elif direction == "up":
                                    player_y = max(0, player_y - 1) if maze[player_y - 1][player_x] != 1 else player_y
                                elif direction == "down":
                                    player_y = min(MAZE_HEIGHT - 1, player_y + 1) if maze[player_y + 1][player_x] != 1 else player_y

            # Check if the player reaches the goal
            if player_x == goal_x and player_y == goal_y:
                completed_mazes += 1
                maze = generate_maze()
                player_x, player_y = 1, 1

            # Draw the maze
            screen.fill(WHITE)
            for row in range(MAZE_HEIGHT):
                for col in range(MAZE_WIDTH):
                    if maze[row][col] == 1:
                        pygame.draw.rect(screen, RED, (col * PLAYER_SIZE, row * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE))
                    elif maze[row][col] == 0 and (col != goal_x or row != goal_y):
                        pygame.draw.rect(screen, WHITE, (col * PLAYER_SIZE, row * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE))
                    elif col == goal_x and row == goal_y:
                        pygame.draw.rect(screen, GREEN, (col * PLAYER_SIZE, row * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE))

            # Draw the player
            pygame.draw.rect(screen, (0, 0, 255), (player_x * PLAYER_SIZE, player_y * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE))

            # Draw arrow buttons
            for rect in arrow_buttons.values():
                pygame.draw.rect(screen, (100, 100, 100), rect)

            # Draw completion counter
            text = font.render(f"Completed Mazes: {completed_mazes}", True, (0, 0, 0))
            screen.blit(text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)


    def on_thumbnail_click(self, row, column):
        print(f"Thumbnail clicked! Row: {row}, Column: {column}")

        if row == 0 and column == 0:
            self.function_0_0()
        elif row == 0 and column ==1:
            self.function_0_1()
        elif row == 0 and column ==2:
            self.function_0_2()
        elif row == 0 and column ==3:
            self.function_0_3()
        elif row == 1 and column ==0:
            self.function_1_0()
        elif row == 1 and column ==1:
            self.function_1_1()
        elif row == 1 and column ==2:
            self.function_1_2()
        elif row == 1 and column ==3:
            self.function_1_3()

    def back(self):
        print("I HATE YOU")
        self.time_frame.grid_forget()
        self.create_image_grid()
    
    def update_temp(self, temp):
        string_temp = "21.5 C"
        temp.config(text=string_temp)

    def update_back(self, back):
        string_back = "back"
        back.config(text=string_back)
        self.frame.grid_forget()

    def update_time(self, label):
        string_time = strftime('%H:%M:%S %p')
        label.config(text=string_time)
        self.root.after(1000, lambda: self.update_time(label))

    def function_0_0(self):
        print("Function for button at Row: 0, Column: 0")
        self.frame.grid_forget()
        self.create_time_grid()

    def function_0_1(self):
        print("Function for button at Row: 0, Column: 1")
        self.frame.grid_forget()
        self.create_calculator_grid()

    def function_0_2(self):
        print("Function for button at Row: 0, Column: 2")

    def function_0_3(self):
        print("Function for button at Row: 0, Column: 3")

    def function_1_0(self):
        print("Function for button at Row: 1, Column: 0")

    def function_1_1(self):
        print("Function for button at Row: 1, Column: 1")

    def function_1_2(self):
        print("Function for button at Row: 1, Column: 2")
        self.frame.grid_forget()
        self.create_temp_grid()

    def function_1_3(self):
        print("Function for button at Row: 1, Column: 3")
        self.frame.grid_forget()
        self.create_maze_grid()

    def refresh_window(self):
        self.frame.grid_forget()
        self.create_image_grid()

    def show_labels(self):
        self.frame.grid_forget()

    def hide_labels(self, event):
        self.frame.grid()
        self.frame.update()

def main():
    root = tk.Tk()
    app = ImageGridApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

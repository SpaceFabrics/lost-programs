import tkinter as tk
from PIL import Image, ImageTk

class ImageGridApp:
    def __init__(self, root):
        version = 0.01
        self.root = root
        self.root.title(str(version))

        # Replace these with the actual paths to your images
        self.image_paths = [
            "PizzaStoreTracker/pizza.jpg", "PizzaStoreTracker/image2.png",
            "PizzaStoreTracker/image3.png", "PizzaStoreTracker/image4.png",
            "PizzaStoreTracker/image5.jpg", "PizzaStoreTracker/image6.png",
            "PizzaStoreTracker/image7.jpg", "PizzaStoreTracker/maze.jpg"
        ]

        self.rows, self.columns = 2, 4
        self.create_image_grid()

        self.root.bind("<Button-1>", self.show_labels)
        self.root.bind("<ButtonRelease-1>", self.hide_labels)

    def create_image_grid(self):
        self.frame = tk.Frame(self.root)  # Create a frame to hold the labels
        self.frame.grid(row=0, column=0)

        self.photo_images = []  # Keep references to PhotoImage objects
        self.labels = []  # Keep references to Label objects

        for i in range(self.rows):
            for j in range(self.columns):
                img = Image.open(self.image_paths[i * self.columns + j])
                img.thumbnail((200, 200))  # Adjust the size as needed
                tk_img = ImageTk.PhotoImage(img)
                self.photo_images.append(tk_img)  # Keep a reference to the PhotoImage
                label = tk.Label(self.frame, image=tk_img)
                label.grid(row=i, column=j, padx=5, pady=5)

                # Create invisible label on top of each thumbnail
                label_button = tk.Label(self.frame, image=tk_img, cursor="hand2")
                label_button.grid(row=i, column=j, padx=5, pady=5)
                label_button.bind("<Button-1>", lambda event, i=i, j=j: self.on_thumbnail_click(i, j))
                self.labels.append(label_button)

    def on_thumbnail_click(self, row, column):
        print(f"Thumbnail clicked! Row: {row}, Column: {column}")
        # Refresh the window after every button click
        self.refresh_window()

    def refresh_window(self):
        # Hide the frame and show it after updating
        self.frame.grid_forget()
        self.create_image_grid()

    def show_labels(self, event):
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

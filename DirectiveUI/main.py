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
        self.frame.grid_forget()

    def function_0_0(self):
        print("Function for button at Row: 0, Column: 0")
        self.frame.grid_forget()
        self.create_time_grid()
        #self.back()

    def create_time_grid(self):
        frame = tk.Frame(self.root, width=800, height=400)
        frame.grid(row=1, column=3, padx=5, pady=5)
        frame.config(bg="black")
        time_label = tk.Label(frame, font=('Courier', 85, 'bold'), background='black', foreground='white')
        time_label.place(relx=0.5, rely=0.5, anchor='center')
        back_button = tk.Button(frame, font=('Courier', 30, 'bold'),background='black', foreground='red', cursor="hand2", command = self.back())
        back_button.place(x=25,y=300)
        self.update_time(time_label)
        self.update_back(back_button)

    def update_back(self, back):
        string_back = "back"
        back.config(text=string_back)

    def update_time(self, label):
        string_time = strftime('%H:%M:%S %p')
        label.config(text=string_time)
        self.root.after(1000, lambda: self.update_time(label))

    def function_0_1(self):
        print("Function for button at Row: 0, Column: 1")

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

    def function_1_3(self):
        print("Function for button at Row: 1, Column: 3")

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

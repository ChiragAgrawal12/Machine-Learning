import tkinter as tk
import random
import time

# Game Settings
WIDTH, HEIGHT = 500, 600
NINJA_SPEED = 20
SHURIKEN_SPEED = 10  # Increased speed
SHURIKEN_INTERVAL = 1000  # New shuriken every 1 second (faster)

def move_left(event):
    x, y = canvas.coords(ninja)
    if x > 50:
        canvas.move(ninja, -NINJA_SPEED, 0)

def move_right(event):
    x, y = canvas.coords(ninja)
    if x < WIDTH - 50:
        canvas.move(ninja, NINJA_SPEED, 0)

def spawn_shuriken():
    if game_running:
        x_pos = random.randint(50, WIDTH - 50)
        shuriken = canvas.create_text(x_pos, 0, text="🌀", font=("Arial", 30))
        shurikens.append(shuriken)
        root.after(SHURIKEN_INTERVAL, spawn_shuriken)

def move_shurikens():
    global game_running
    for shuriken in shurikens[:]:
        canvas.move(shuriken, 0, SHURIKEN_SPEED)
        if check_collision(shuriken):
            game_over()
            return
        if canvas.coords(shuriken)[1] > HEIGHT:
            canvas.delete(shuriken)
            shurikens.remove(shuriken)
    if game_running:
        root.after(40, move_shurikens)  # Reduced delay for smoother movement

def check_collision(shuriken):
    ninja_x, ninja_y = canvas.coords(ninja)
    shuriken_x, shuriken_y = canvas.coords(shuriken)
    return abs(ninja_x - shuriken_x) < 30 and abs(ninja_y - shuriken_y) < 30

def game_over():
    global game_running
    game_running = False
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", font=("Arial", 30, "bold"), fill="red")
    retry_btn.pack()

def restart_game():
    global shurikens, game_running
    canvas.delete("all")
    shurikens = []
    create_ninja()
    game_running = True
    retry_btn.pack_forget()
    spawn_shuriken()
    move_shurikens()

def create_ninja():
    global ninja
    ninja = canvas.create_text(WIDTH // 2, HEIGHT - 50, text="🥷", font=("Arial", 40))

# Initialize Game Window
root = tk.Tk()
root.title("Ninja Dodge 🏯⚔️")
root.geometry(f"{WIDTH}x{HEIGHT}")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

shurikens = []
game_running = True

# Create game objects
create_ninja()
spawn_shuriken()
move_shurikens()

# Bind controls
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Retry Button
retry_btn = tk.Button(root, text="Retry", font=("Arial", 14), command=restart_game)

root.mainloop()

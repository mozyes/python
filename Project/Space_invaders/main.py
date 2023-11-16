import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Space Invaders")

# Set up the canvas
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Player
player_size = 50
player_x = canvas_width // 2 - player_size // 2
player_y = canvas_height - 2 * player_size
player_speed = 20  # Increased player speed

# Bullet
bullet_size = 10
bullet_speed = 7
bullets = []

# Enemy
enemy_size = 50
enemy_base_speed = 1.5  # Base speed of enemies
enemy_speed = enemy_base_speed
enemies = []

score = 0
score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16), fg="white", bg="black")
score_label.pack()

game_running = True

def create_enemy():
    enemy_x = random.randint(0, canvas_width - enemy_size)
    enemy_y = 0
    enemy = canvas.create_rectangle(
        enemy_x, enemy_y, enemy_x + enemy_size, enemy_y + enemy_size, fill="red"
    )
    enemies.append(enemy)

def draw_player():
    canvas.delete("player")  # Delete previous drawing of the player
    canvas.create_rectangle(
        player_x, player_y, player_x + player_size, player_y + player_size, fill="white", tags="player"
    )

def draw_bullet(bullet):
    x, y = canvas.coords(bullet)
    canvas.create_rectangle(
        x, y, x + bullet_size, y + bullet_size, fill="white"
    )

def move_player(event):
    global player_x
    if event.keysym == "Left" and player_x > 0:
        player_x -= player_speed
    elif event.keysym == "Right" and player_x < canvas_width - player_size:
        player_x += player_speed
    draw_player()

def shoot(event):
    x = player_x + player_size // 2 - bullet_size // 2
    y = player_y
    bullet = canvas.create_rectangle(x, y, x + bullet_size, y + bullet_size, fill="white")
    bullets.append(bullet)

def update_game():
    global score, game_running, enemy_speed
    if game_running:
        for bullet in bullets[:]: 
            if canvas.coords(bullet): 
                canvas.move(bullet, 0, -bullet_speed)
                if canvas.coords(bullet)[1] < 0:
                    canvas.delete(bullet)
                    bullets.remove(bullet)

        for enemy in enemies[:]: 
            if canvas.coords(enemy):  
                canvas.move(enemy, 0, enemy_speed)
                if canvas.coords(enemy)[1] > canvas_height:
                    game_over()

        for bullet in bullets:
            for enemy in enemies:
                if (
                    canvas.coords(bullet)
                    and canvas.coords(enemy)
                    and canvas.coords(bullet)[0] < canvas.coords(enemy)[0] + enemy_size
                    and canvas.coords(bullet)[0] + bullet_size > canvas.coords(enemy)[0]
                    and canvas.coords(bullet)[1] < canvas.coords(enemy)[1] + enemy_size
                    and canvas.coords(bullet)[1] + bullet_size > canvas.coords(enemy)[1]
                ):
                    canvas.delete(bullet)
                    bullets.remove(bullet)
                    canvas.delete(enemy)
                    enemies.remove(enemy)
                    score += 10
                    score_label.config(text="Score: {}".format(score))

        # Check if any enemy crossed the player
        for enemy in enemies:
            if canvas.coords(enemy)[1] + enemy_size > player_y or canvas.coords(enemy)[1] > canvas_height:
                game_over()

        if not enemies:
            create_enemy()

        # Increase enemy speed every 100 points
        if score % 100 == 0 and score > 0:
            enemy_speed = min(enemy_speed + 0.5, 5.0)

        root.after(30, update_game)

def game_over():
    global game_running
    game_running = False
    canvas.create_text(
        canvas_width // 2,
        canvas_height // 2,
        text="Game Over",
        font=("Helvetica", 36),
        fill="white",
    )

# Bind keys and set focus on the canvas
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)
root.bind("<space>", shoot)
canvas.focus_set()

# Initial setup
for _ in range(5):
    create_enemy()

draw_player()
update_game()

# Run the main loop
root.mainloop()

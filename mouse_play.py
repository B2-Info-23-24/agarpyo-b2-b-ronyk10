import pygame

def play_with_mouse():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_radius = 40

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # distance between player and mouse
        distance = ((mouse_pos[0] - player_pos.x) ** 2 + (mouse_pos[1] - player_pos.y) ** 2) ** 0.5

        # if distance !=null, player going on mouse
        if distance > 0:
            # Displacement based on speed
            speed = 300 * dt
            dx = speed * (mouse_pos[0] - player_pos.x) / distance
            dy = speed * (mouse_pos[1] - player_pos.y) / distance

            # update player position
            player_pos.x += dx
            player_pos.y += dy

        # draw player position
        pygame.draw.circle(screen, "red", player_pos, player_radius)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

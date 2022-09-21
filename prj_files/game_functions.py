# Functions about various functions of the game, game_fuction.py
import sys  # Use the sys module to exit the game
import pygame  # It contains the functions required for game development
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Operate in response to the key"""
    if event.key == pygame.K_RIGHT:  # Determine whether the right arrow is pressed
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # Determine whether the left arrow is pressed
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # Determine whether the space is pressed
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # Judge whether Q is pressed. If Q is pressed, quit the game
        sys.exit()


def check_keyup_events(event, ship):
    """Response release key"""
    if event.key == pygame.K_RIGHT:  # Right arrow when judging the released
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # Judge whether there is an arrow loosened
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the type of event is exit, it is equivalent to mouse click ×
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Determine whether a key is pressed
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # Judge whether the key is released
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Determine whether the mouse is pressed
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Returns the coordinates of the pressed point
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Click on the player Play Start a new game after"""
    # Judge whether the position of the mouse click is within the key and whether the game state is active at this time
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # Reset game settings
        ai_settings.initialize_dynamic_speed()
        # hide cursor
        pygame.mouse.set_visible(False)
        # Reset game statistics
        stats.reset_stats()
        stats.game_active = True
        # Reset scoreboard image
        sb.prep_score()  # Reset current score
        sb.prep_high_score()  # Reset maximum score
        sb.prep_level()  # Reset game level
        sb.prep_ships()  # Reset available ships
        # Clear alien and bullet list
        aliens.empty()
        bullets.empty()
        # Create a new group of aliens and center it
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update the image on the screen and switch to a new screen"""
    screen.fill(ai_settings.bg_color)  # Fills the screen with the specified color
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()  # Display the spacecraft on the screen
    aliens.draw(screen)  # Let aliens appear on the screen
    sb.show_score()  # Print scoring information
    if not stats.game_active:  # Print the start button if the game is inactive
        play_button.draw_button()
    pygame.display.flip()  # Displays the most recently drawn screen


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update the location of bullets and delete bullets that have disappeared"""
    bullets.update()

    # The number of lists or groups should not be modified in the for loop, which will lead to the loss of traversal
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    # print(len(bullets)) # Show how many bullets there are. This knowledge test. Deleting this statement at run time can reduce memory


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to the collision between bullets and aliens, and generate a new group of aliens after all aliens die"""
    # Detect whether a bullet hit the alien. If so, delete the bullet and alien

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:  # Increase score when hitting aliens
        for aliens in collisions.values():
            stats.score += ai_settings.alien_point * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # If all aliens are eliminated, delete the existing bullets and regenerate aliens
        bullets.empty()
        ai_settings.increase_speed()
        # Raise the level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """If the firing limit is not reached, fire a bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  # Create an instance of the bullet
        bullets.add(new_bullet)  # Place bullet instances in groups


def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate how many lines the screen can hold"""
    # Calculate how much space is left on the screen
    available_space_y = ai_settings.screen_height - 4 * alien_height - ship_height
    # How many lines are there on the calculation screen
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_alien_x(ai_settings, alien_width):
    """Calculate how many aliens each row can hold"""
    # Calculate how many positions there are in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # Calculate how many aliens a row can hold
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and put it in the current line"""
    alien = Alien(ai_settings, screen)  # Create an alien
    alien_width = alien.rect.width  # Get the width of an alien
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number  # Set the initial position of each alien
    alien.rect.x = alien.x

    # Determine the vertical position of each alien
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)  # Adding aliens to a group


def create_fleet(ai_settings, screen, ship, aliens):
    """Create alien groups"""
    alien = Alien(ai_settings, screen)  # Create an alien
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Create first row
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """When aliens reach the edge, take corresponding measures"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move all aliens down and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Responding to a spaceship hit by aliens"""

    if stats.ships_left > 0:
        stats.ships_left -= 1  # Reduce the number of ships by one
        sb.prep_ships()  # Update scoreboard
        # Clear the list of bullets and aliens
        aliens.empty()
        bullets.empty()

        # Create a new group of aliens and put the spacecraft in the center of the screen
        create_fleet(ai_settings, screen, ship, aliens)  # Create new aliens
        ship.center_ship()  # Move the spacecraft to the center of the screen

        # suspend
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Check if aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()  # Read the matrix information of the screen
    for alien in aliens:

        # If the coordinates of the alien's bottom matrix are larger than the screen, the collision response is performed
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Update the location of Aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Detect the collision between aliens and spacecraft
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def check_high_score(stats, sb):
    """Check whether the highest score is born"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

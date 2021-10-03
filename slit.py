import pygame

BLACK = (0, 0, 0)


class Slit(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, 1])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, 1])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

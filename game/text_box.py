import pygame

class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = True
        self.font = pygame.font.SysFont(None, 34)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit() or (event.unicode == "-" and len(self.text) == 0):
                if len(self.text) < 6:
                    self.text += event.unicode

    def clear(self):
        self.text = ""

    def render(self, surface):
        border_color = (70, 140, 240) if self.active else (110, 115, 125)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=6)
        pygame.draw.rect(surface, border_color, self.rect, width=3, border_radius=6)

        text_surf = self.font.render(self.text, True, (25, 25, 30))
        surface.blit(text_surf, (self.rect.x + 14, self.rect.y + 7))
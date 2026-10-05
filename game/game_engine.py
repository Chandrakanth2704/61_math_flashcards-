import random
import pygame
from game.text_box import TextBox


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Score and attempts
        self.score = 0
        self.total_attempts = 0

        # Streak system
        self.streak = 0
        self.multiplier = 1

        # Feedback
        self.feedback_msg = "Solve the card and press Enter!"
        self.feedback_color = (200, 205, 215)

        # Current question
        self.num_a = 0
        self.num_b = 0
        self.operator = "+"

        # Timer
        self.timer_duration = 10.0
        self.time_remaining = self.timer_duration
        self.last_update_time = pygame.time.get_ticks()

        # Input box
        box_w, box_h = 130, 44

        self.input_box = TextBox(
            width // 2 - 110,
            255,
            box_w,
            box_h
        )

        # Submit button
        self.submit_btn = pygame.Rect(
            width // 2 + 30,
            255,
            90,
            box_h
        )

        # Fonts
        self.font_title = pygame.font.SysFont(
            None,
            38
        )

        self.font_hud = pygame.font.SysFont(
            None,
            26
        )

        self.font_card = pygame.font.SysFont(
            None,
            56
        )

        self.font_btn = pygame.font.SysFont(
            None,
            24
        )

        # Generate first question
        self.generate_new_card()

    def generate_new_card(self):
        """Generate a new math question and reset the timer."""

        # Select an operator
        self.operator = random.choice([
            "+",
            "-",
            "*",
            "/"
        ])

        if self.operator == "/":
            # Generate divisor and quotient first
            self.num_b = random.randint(2, 12)
            quotient = random.randint(2, 12)

            # Calculate dividend so division is always exact
            self.num_a = self.num_b * quotient

        else:
            # Generate normal operands
            self.num_a = random.randint(3, 15)
            self.num_b = random.randint(2, 12)

            # Prevent negative subtraction results
            if (
                self.operator == "-"
                and self.num_a < self.num_b
            ):
                self.num_a, self.num_b = (
                    self.num_b,
                    self.num_a
                )

        # Clear previous answer
        self.input_box.clear()

        # Reset timer for the new question
        self.time_remaining = self.timer_duration
        self.last_update_time = pygame.time.get_ticks()

    def compute_expected_answer(self):
        """Calculate the correct integer answer."""

        if self.operator == "+":
            return self.num_a + self.num_b

        elif self.operator == "-":
            return self.num_a - self.num_b

        elif self.operator == "*":
            return self.num_a * self.num_b

        elif self.operator == "/":
            # Integer division.
            # Question generation guarantees no remainder.
            return self.num_a // self.num_b

    def submit_answer(self):
        """Check the user's answer and update score/streak."""

        val_str = self.input_box.text.strip()

        # Prevent empty submissions
        if not val_str or val_str == "-":
            self.feedback_msg = "Type an answer first!"
            self.feedback_color = (240, 175, 40)
            return

        user_answer = int(val_str)
        expected = self.compute_expected_answer()

        # Every submitted answer counts as an attempt
        self.total_attempts += 1

        if user_answer == expected:

            # Increase consecutive correct streak
            self.streak += 1

            # Determine multiplier
            if self.streak >= 5:
                self.multiplier = 3

            elif self.streak >= 3:
                self.multiplier = 2

            else:
                self.multiplier = 1

            # Award points according to multiplier
            points = self.multiplier
            self.score += points

            self.feedback_msg = (
                f"CORRECT! +{points} point"
                f"{'s' if points > 1 else ''} "
                f"({self.multiplier}x multiplier)"
            )

            self.feedback_color = (80, 230, 110)

            # Generate the next question
            self.generate_new_card()

        else:

            # Incorrect answer resets streak
            self.streak = 0
            self.multiplier = 1

            self.feedback_msg = (
                f"WRONG! Expected {expected}."
            )

            self.feedback_color = (240, 75, 75)

            # Allow another attempt at the same question
            self.input_box.clear()

    def handle_event(self, event):
        """Handle keyboard and mouse input."""

        self.input_box.handle_event(event)

        # Enter key
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                self.submit_answer()

        # Mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if self.submit_btn.collidepoint(event.pos):
                    self.submit_answer()

    def update(self):
        """Update the countdown timer and handle timeout."""

        current_time = pygame.time.get_ticks()

        elapsed = (
            current_time - self.last_update_time
        ) / 1000.0

        self.last_update_time = current_time

        # Decrease remaining time
        self.time_remaining -= elapsed

        # Handle timeout
        if self.time_remaining <= 0:

            self.time_remaining = 0

            # Timeout counts as an incorrect attempt
            self.total_attempts += 1

            # Reset streak and multiplier
            self.streak = 0
            self.multiplier = 1

            # Display timeout message
            self.feedback_msg = "TIME'S UP!"
            self.feedback_color = (240, 75, 75)

            # Generate a new question
            self.generate_new_card()

    def render(self, screen):
        """Render the complete game interface."""

        screen.fill(
            (25, 29, 37)
        )

        # ===================================
        # TITLE
        # ===================================

        title_surf = self.font_title.render(
            "Math Flashcards Arena",
            True,
            (245, 245, 245)
        )

        screen.blit(
            title_surf,
            (
                self.width // 2
                - title_surf.get_width() // 2,
                18
            )
        )

        # ===================================
        # SCORE
        # ===================================

        score_surf = self.font_hud.render(
            f"Score: {self.score} / {self.total_attempts}",
            True,
            (255, 220, 80)
        )

        screen.blit(
            score_surf,
            (
                self.width // 2
                - score_surf.get_width() // 2,
                58
            )
        )

        # ===================================
        # STREAK
        # ===================================

        streak_surf = self.font_hud.render(
            f"Streak: {self.streak}",
            True,
            (245, 245, 245)
        )

        screen.blit(
            streak_surf,
            (20, 20)
        )

        # ===================================
        # MULTIPLIER
        # ===================================

        multiplier_surf = self.font_hud.render(
            f"Multiplier: {self.multiplier}x",
            True,
            (255, 220, 80)
        )

        screen.blit(
            multiplier_surf,
            (
                self.width
                - multiplier_surf.get_width()
                - 20,
                20
            )
        )

        # ===================================
        # QUESTION CARD
        # ===================================

        card_rect = pygame.Rect(
            self.width // 2 - 130,
            95,
            260,
            110
        )

        pygame.draw.rect(
            screen,
            (240, 242, 245),
            card_rect,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (85, 120, 175),
            card_rect,
            width=3,
            border_radius=12
        )

        card_str = (
            f"{self.num_a} "
            f"{self.operator} "
            f"{self.num_b}"
        )

        card_surf = self.font_card.render(
            card_str,
            True,
            (25, 30, 42)
        )

        screen.blit(
            card_surf,
            (
                card_rect.centerx
                - card_surf.get_width() // 2,

                card_rect.centery
                - card_surf.get_height() // 2
            )
        )

        # ===================================
        # TIMER BAR
        # ===================================

        timer_x = self.width // 2 - 130
        timer_y = 215
        timer_width = 260
        timer_height = 12

        # Timer background
        pygame.draw.rect(
            screen,
            (60, 65, 75),
            (
                timer_x,
                timer_y,
                timer_width,
                timer_height
            ),
            border_radius=6
        )

        # Calculate remaining percentage
        timer_ratio = (
            self.time_remaining
            / self.timer_duration
        )

        timer_ratio = max(
            0,
            min(1, timer_ratio)
        )

        current_width = int(
            timer_width * timer_ratio
        )

        # Timer foreground
        if current_width > 0:

            pygame.draw.rect(
                screen,
                (80, 200, 110),
                (
                    timer_x,
                    timer_y,
                    current_width,
                    timer_height
                ),
                border_radius=6
            )

        # ===================================
        # TIMER TEXT
        # ===================================

        timer_text = self.font_hud.render(
            f"{self.time_remaining:.1f}s",
            True,
            (245, 245, 245)
        )

        screen.blit(
            timer_text,
            (
                self.width // 2
                - timer_text.get_width() // 2,
                timer_y + 16
            )
        )

        # ===================================
        # INPUT BOX
        # ===================================

        self.input_box.render(screen)

        # ===================================
        # SUBMIT BUTTON
        # ===================================

        pygame.draw.rect(
            screen,
            (45, 140, 80),
            self.submit_btn,
            border_radius=6
        )

        pygame.draw.rect(
            screen,
            (215, 225, 220),
            self.submit_btn,
            width=2,
            border_radius=6
        )

        btn_txt = self.font_btn.render(
            "SUBMIT",
            True,
            (255, 255, 255)
        )

        screen.blit(
            btn_txt,
            (
                self.submit_btn.centerx
                - btn_txt.get_width() // 2,

                self.submit_btn.centery
                - btn_txt.get_height() // 2
            )
        )

        # ===================================
        # FEEDBACK MESSAGE
        # ===================================

        msg_surf = self.font_hud.render(
            self.feedback_msg,
            True,
            self.feedback_color
        )

        screen.blit(
            msg_surf,
            (
                self.width // 2
                - msg_surf.get_width() // 2,
                340
            )
        )
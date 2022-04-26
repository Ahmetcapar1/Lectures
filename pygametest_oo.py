import pygame

class Game:

    _window_width, _window_height = 1550, 900
    _window_size = (_window_width, _window_height)
    _black = (255, 120, 0)
    _screen = pygame.display.set_mode(_window_size)

    def __init__(self):

        self._inter_move_wait_time = 20
        self._clock = pygame.time.Clock()
        self._ball = Ball()

    def _slow_down(self):

        self._inter_move_wait_time = self._inter_move_wait_time + 1

    def _speed_up(self):

        self._inter_move_wait_time = self._inter_move_wait_time - 1

    def play(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self._slow_down()
                    elif event.key == pygame.K_UP:
                        self._speed_up()

            if self._ball.is_time_to_move(self._clock.get_time(), game._inter_move_wait_time):
                self._ball.move(Game._window_width, Game._window_height)

                Game._screen.fill(Game._black)
                self._ball.draw(Game._screen)
                pygame.display.flip()

            self._clock.tick()


class Ball:

    _ball_image_template = pygame.image.load("ball.gif") # class variable

    def __init__(self):

        self._ball_rect = Ball._ball_image_template.get_rect() # instance variable
        self._direction = [1, 1]
        self._total_wait_since_last_move = 0

    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):

        self._total_wait_since_last_move = self._total_wait_since_last_move + time_since_last_tick
        if self._total_wait_since_last_move <= inter_move_wait_time:
             return False
        else:
            return True

    def move(self, window_width, window_height):

        self._total_wait_since_last_move = 0
        self._ball_rect = self._ball_rect.move(self._direction)
        if self._ball_rect.left < 0 or self._ball_rect.right > window_width:
            self._direction[0] = -self._direction[0]
        if self._ball_rect.top < 0 or self._ball_rect.bottom > window_height:
            self._direction[1] = -self._direction[1]

    def draw(self, screen):

        screen.blit(Ball._ball_image_template, self._ball_rect)


        

pygame.init()

game = Game()
game.play()

pygame.quit()
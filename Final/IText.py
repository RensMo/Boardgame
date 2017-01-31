import pygame

class Textbg:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x,y), (sx,sy))

    def draw(self, surface):
        surface.blit(self.I, (self.rect))

class IText:
    def __init__(self, x, y, btext, size, width, rI, color=pygame.Color("black"), underline=None):
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", self.size)
        self.underline = underline
        if self.underline == True:
            print("underline = true")
            self.font.set_underline(True)
        elif self.underline == False:
            print("underline = true")
            self.font.set_underline(False)
        self.color = color
        self.btext = btext
        self.atext = ""
        self.etext = self.font.render(self.btext + self.atext, 1, (self.color))
        self.shifted = False
        self.maxlength = 16
        self.focus = 0
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.size))
        self.srect = pygame.Surface((int(self.width), int(self.size)))
        self.rI = rI

    def update(self, events, x, y, size, width):
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.size))
        self.srect = pygame.Surface((int(self.width), int(self.size)))
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", self.size)

        if self.underline == True:
            print("underline = true")
            self.font.set_underline(True)
        elif self.underline == False:
            print("underline = true")
            self.font.set_underline(False)

        if self.rI == 0:
            if self.focus == 0:
                self.color = pygame.Color("Black")
            if self.focus == 1:
                self.color = pygame.Color("Red")
        elif self.rI == 1:
            if self.focus == 0:
                self.color = pygame.Color("Black")
            elif self.focus == 1:
                self.color = pygame.Color("Red")
                if self.width < self.size * len(self.atext) * 0.6:
                    self.rect = pygame.Rect((self.x, self.y), (self.size * len(self.atext) * 0.6, self.size))
                for event in events:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.shifted = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE: self.atext = self.atext[:-1]
                        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.shifted = True
                        elif event.key == pygame.K_SPACE: self.atext += " "
                        if not self.shifted:
                            if event.key == pygame.K_a: self.atext += "a"
                            elif event.key == pygame.K_b: self.atext += "b"
                            elif event.key == pygame.K_c: self.atext += "c"
                            elif event.key == pygame.K_d: self.atext += "d"
                            elif event.key == pygame.K_e: self.atext += "e"
                            elif event.key == pygame.K_f: self.atext += "f"
                            elif event.key == pygame.K_g: self.atext += "g"
                            elif event.key == pygame.K_h: self.atext += "h"
                            elif event.key == pygame.K_i: self.atext += "i"
                            elif event.key == pygame.K_j: self.atext += "j"
                            elif event.key == pygame.K_k: self.atext += "k"
                            elif event.key == pygame.K_l: self.atext += "l"
                            elif event.key == pygame.K_m: self.atext += "m"
                            elif event.key == pygame.K_n: self.atext += "n"
                            elif event.key == pygame.K_o: self.atext += "o"
                            elif event.key == pygame.K_p: self.atext += "p"
                            elif event.key == pygame.K_q: self.atext += "q"
                            elif event.key == pygame.K_r: self.atext += "r"
                            elif event.key == pygame.K_s: self.atext += "s"
                            elif event.key == pygame.K_t: self.atext += "t"
                            elif event.key == pygame.K_u: self.atext += "u"
                            elif event.key == pygame.K_v: self.atext += "v"
                            elif event.key == pygame.K_w: self.atext += "w"
                            elif event.key == pygame.K_x: self.atext += "x"
                            elif event.key == pygame.K_y: self.atext += "y"
                            elif event.key == pygame.K_z: self.atext += "z"
                            elif event.key == pygame.K_0 or event.key == pygame.K_KP0: self.atext += "0"
                            elif event.key == pygame.K_1 or event.key == pygame.K_KP1: self.atext += "1"
                            elif event.key == pygame.K_2 or event.key == pygame.K_KP2: self.atext += "2"
                            elif event.key == pygame.K_3 or event.key == pygame.K_KP3: self.atext += "3"
                            elif event.key == pygame.K_4 or event.key == pygame.K_KP4: self.atext += "4"
                            elif event.key == pygame.K_5 or event.key == pygame.K_KP5: self.atext += "5"
                            elif event.key == pygame.K_6 or event.key == pygame.K_KP6: self.atext += "6"
                            elif event.key == pygame.K_7 or event.key == pygame.K_KP7: self.atext += "7"
                            elif event.key == pygame.K_8 or event.key == pygame.K_KP8: self.atext += "8"
                            elif event.key == pygame.K_9 or event.key == pygame.K_KP9: self.atext += "9"
                            elif event.key == pygame.K_BACKQUOTE: self.atext += "`"
                            elif event.key == pygame.K_MINUS: self.atext += "-"
                            elif event.key == pygame.K_EQUALS: self.atext += "="
                            elif event.key == pygame.K_LEFTBRACKET: self.atext += "["
                            elif event.key == pygame.K_RIGHTBRACKET: self.atext += "]"
                            elif event.key == pygame.K_BACKSLASH: self.atext += "\\"
                            elif event.key == pygame.K_SEMICOLON: self.atext += ";"
                            elif event.key == pygame.K_QUOTE: self.atext += "\""
                            elif event.key == pygame.K_COMMA: self.atext += ","
                            elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD: self.atext += "."
                            elif event.key == pygame.K_SLASH: self.atext += "/"
                        elif self.shifted:
                            if event.key == pygame.K_a: self.atext += 'A'
                            elif event.key == pygame.K_b: self.atext += 'B'
                            elif event.key == pygame.K_c: self.atext += 'C'
                            elif event.key == pygame.K_d: self.atext += 'D'
                            elif event.key == pygame.K_e: self.atext += 'E'
                            elif event.key == pygame.K_f: self.atext += 'F'
                            elif event.key == pygame.K_g: self.atext += 'G'
                            elif event.key == pygame.K_h: self.atext += 'H'
                            elif event.key == pygame.K_i: self.atext += 'I'
                            elif event.key == pygame.K_j: self.atext += 'J'
                            elif event.key == pygame.K_k: self.atext += 'K'
                            elif event.key == pygame.K_l: self.atext += 'L'
                            elif event.key == pygame.K_m: self.atext += 'M'
                            elif event.key == pygame.K_n: self.atext += 'N'
                            elif event.key == pygame.K_o: self.atext += 'O'
                            elif event.key == pygame.K_p: self.atext += 'P'
                            elif event.key == pygame.K_q: self.atext += 'Q'
                            elif event.key == pygame.K_r: self.atext += 'R'
                            elif event.key == pygame.K_s: self.atext += 'S'
                            elif event.key == pygame.K_t: self.atext += 'T'
                            elif event.key == pygame.K_u: self.atext += 'U'
                            elif event.key == pygame.K_v: self.atext += 'V'
                            elif event.key == pygame.K_w: self.atext += 'W'
                            elif event.key == pygame.K_x: self.atext += 'X'
                            elif event.key == pygame.K_y: self.atext += 'Y'
                            elif event.key == pygame.K_z: self.atext += 'Z'
                            elif event.key == pygame.K_0: self.atext += ')'
                            elif event.key == pygame.K_1: self.atext += '!'
                            elif event.key == pygame.K_2: self.atext += '@'
                            elif event.key == pygame.K_3: self.atext += '#'
                            elif event.key == pygame.K_4: self.atext += '$'
                            elif event.key == pygame.K_5: self.atext += '%'
                            elif event.key == pygame.K_6: self.atext += '^'
                            elif event.key == pygame.K_7: self.atext += '&'
                            elif event.key == pygame.K_8: self.atext += '*'
                            elif event.key == pygame.K_9: self.atext += '('
                            elif event.key == pygame.K_BACKQUOTE: self.atext += '~'
                            elif event.key == pygame.K_MINUS: self.atext += '_'
                            elif event.key == pygame.K_EQUALS: self.atext += '+'
                            elif event.key == pygame.K_LEFTBRACKET: self.atext += '{'
                            elif event.key == pygame.K_RIGHTBRACKET: self.atext += '}'
                            elif event.key == pygame.K_BACKSLASH: self.atext += '|'
                            elif event.key == pygame.K_SEMICOLON: self.atext += ':'
                            elif event.key == pygame.K_QUOTE: self.atext += '"'
                            elif event.key == pygame.K_COMMA: self.atext += '<'
                            elif event.key == pygame.K_PERIOD: self.atext += '>'
                            elif event.key == pygame.K_SLASH: self.atext += '?'

        if len(self.atext) > self.maxlength and self.maxlength >= 0: self.atext = self.atext[:-1]
        self.etext = self.font.render(self.btext + self.atext, 1, (self.color))

    def draw(self, surface):
        self.srect.fill(pygame.Color("Black"))
        self.srect.set_alpha(68)
        surface.blit(self.srect, (int(self.x), int(self.y)))
        surface.blit(self.etext, (self.x, self.y))

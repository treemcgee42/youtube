from manimlib.imports import *

class PlayingCard:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = str(number)

    def make_card(self):
        card_rectangle = RoundedRectangle(
            corner_radius=.25, height=2.5, fill_opacity=1
        ).rotate(90*DEGREES).set_fill(BLACK)
        number_mob = TexMobject(self.number)
        svg_heart = SVGMobject("card_class/heart-outline.svg").scale(.2)
        svg_club = SVGMobject("card_class/club.svg").scale(.2)
        svg_diamond = SVGMobject("card_class/diamond.svg").scale(.2)
        svg_spade = SVGMobject("card_class/spade.svg", stroke_width=0).scale(.2).rotate(180*DEGREES)

        if self.suit=="hearts":
            suit_mob = svg_heart
        elif self.suit=="clubs":
            suit_mob = svg_club
        elif self.suit=="diamonds":
            suit_mob = svg_diamond
        elif self.suit=="spades":
            suit_mob = svg_spade
        
        number_and_suit = VGroup(
            number_mob,
            suit_mob
        ).arrange_submobjects(
            DOWN,
            buff=.1
        ).scale(.75).move_to(
            card_rectangle.get_vertices()[0]
        ).shift(3.5*UP,.1*RIGHT)
        the_card = VGroup(
            card_rectangle,
            number_and_suit.copy(),
            number_and_suit.copy().shift(1.8*RIGHT),
            number_and_suit.copy().rotate(180*DEGREES).shift(3*DOWN),
            number_and_suit.copy().rotate(180*DEGREES).shift(3*DOWN, 1.8*RIGHT),
            suit_mob.copy().scale(2.5).shift(1.3*DOWN,.9*RIGHT)
        )
        return the_card

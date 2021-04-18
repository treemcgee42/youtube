from manimlib.imports import *
from manimlib.PlayingCard import PlayingCard
from manimlib.CardDeck import CardDeck

class test(Scene):
    def construct(self):
        deck = CardDeck()
        deck.shuffle()

        hand = deck.get_hand()
        for card in hand:
            card.shift(2.5*LEFT,1*DOWN)
        selected_card = hand[5]

        self.play(
            *[FadeIn(card) for card in hand]
        )
        self.wait(2)
        self.play(
            Transform(selected_card, selected_card.copy().shift(.5*UP))
        )
        self.wait(2)

        hand_wo_selected_card = []
        for card in hand:
            if card != selected_card:
                hand_wo_selected_card.append(card)

        self.play(
            *[Transform(card, card.copy().shift(10*DOWN)) for card in hand_wo_selected_card],
            Transform(selected_card, selected_card.copy().shift(3*RIGHT, .5*UP))
        )
        self.wait(2)

        compare_card_spade = PlayingCard("spades", 3).make_card().move_to(selected_card).shift(6.5*LEFT)
        compare_arrow = Arrow().shift(.25*RIGHT)

        self.play(
            FadeIn(compare_card_spade)
        )
        self.play(
            ShowCreation(compare_arrow)
        )
        self.wait()

        compare_card_heart = PlayingCard("hearts", 7).make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_spade)
        )
        self.play(
            FadeIn(compare_card_heart)
        )
        self.wait()

        compare_card_club = PlayingCard("clubs", 7).make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_heart)
        )
        self.play(
            FadeIn(compare_card_club)
        )
        self.wait()

        compare_card_diamond = PlayingCard("diamonds", 7).make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_club)
        )
        self.play(
            FadeIn(compare_card_diamond)
        )
        self.wait(2)

        compare_card_diamond2 = PlayingCard("diamonds", 2).make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_diamond)
        )
        self.play(
            FadeIn(compare_card_diamond2)
        )
        self.wait()

        compare_card_diamond10 = PlayingCard("diamonds", 10).make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_diamond2)
        )
        self.play(
            FadeIn(compare_card_diamond10)
        )
        self.wait()

        compare_card_diamondK = PlayingCard("diamonds", "K").make_card().move_to(compare_card_spade)

        self.play(
            FadeOut(compare_card_diamond10)
        )
        self.play(
            FadeIn(compare_card_diamondK)
        )
        self.wait(2)
        self.clear()

from manimlib.imports import *

class intro(Scene):
    """
    The Yoneda lemma is one of the cornerstones of category theory. It's a really important
    result, don't let the fact that it's a lemma hide that. In this video, I hope to sort of
    informally motivate it, because I think the philosophy of the Yoneda lemma is its true
    greatness.
    So let's say we have some mystery object in some category, say its some topological space.
    How might we study it? 
    """
    def construct(self):
        t = TextMobject("The Yoneda Perspective")
        self.play(
            Write(t)
        )
        self.wait(2)
        self.clear()

class card_scene(Scene):
    """
    use card_test.py

    How about we play a game first. I have a deck of cards. You're going to close your eyes
    while I pick a card. Ok, now you need to
    guess what card I picked. You only get one guess, but you can ask me as many questions
    about my card as you want, as long as its not a guess of course. Well ok, you could ask me,
    is it a spade? No. Is it a heart? No. A club? No. Alright, so it must be a diamond then.
    What about its value? Greater than 2? 10? Less than King? By asking these questions, you could
    pretty easily determine what card I have. 
    The point is, the card I chose, indeed any card,
    is completely determined by its relationship to other cards.
    Likewise, the Yoneda perspective in category theory is the following- an object in a category
    is completely determined by its relationship to other objects in the category.
    """

class torus(Scene):
    """
    Let's return to our example. I picked a mystery topological space. How can you determine it?
    Well, it lives in the category of topological spaces, so you could consider its relationship to
    other topoligcal spaces! Relationships in a category are morphisms, specifically in the category
    of topological spaces they are continuous functions between topological spaces.
    So, for instance, try mapping the unit interval continuously onto my mystery object.
    Now try it with a circle, try mapping a circle onto my mystery object.
    In this way, we can get a pretty good idea of what this mystery object is. The
    Yoneda lemma tells us that my mystery space X is entirely determined by its relationship to
    other topological spaces.
    But in what sense?
    """
    def construct(self):
        # just the torus
        torus_file = SVGMobject("assets/svg_images/yoneda/torus.svg", fill_opacity=0, stroke_width=2)\
            .scale(1.5)
        the_torus = torus_file[:8]
        # first path, I -> torus
        path1 = torus_file[8:11]
        path1.set_color(PINK)
        path1_1 = path1[1]
        path1_1.set_stroke(opacity=.4)
        # second path, S^1 -> torus
        path2 = torus_file[11:13]
        path2.set_color(BLUE)
        path2_1 = path2[1].set_stroke(opacity=.4)
        # box
        box = torus_file[13]

        # Tex
        i_to_x = TexMobject("I\\longrightarrow X").scale(.75).next_to(box,direction=UP, buff=.75)
        s1_to_x = TexMobject("S^1\\longrightarrow X").scale(.75).next_to(box,direction=DOWN, buff=.75)

        # Animation
        self.play(
            GrowFromCenter(box)
        )
        self.wait(2)
        self.play(
            FadeIn(i_to_x)
        )
        self.wait(2)
        self.play(
            ShowCreation(path1[0])
        )
        self.play(
            ShowCreation(path1_1)
        )
        self.play(
            ShowCreation(path1[2])
        )
        self.wait(2)
        self.play(
            FadeIn(s1_to_x)
        )
        self.play(
            ShowCreation(path2[0])
        )
        self.play(
            ShowCreation(path2_1)
        )
        self.wait(2)
        self.play(
            FadeOut(box),
            ShowCreation(the_torus)
        )
        self.wait(2)
        self.clear()

class explanation(Scene):
    """
    X and Hom X are certainly not isomorphic, as they may not even lie in the same category.
    Indeed, in our previous example X was a topological space, and its Hom set was just that, a set
    in the category of Sets. But what we can say is that they carry the same information in the 
    following sense- X is isomorphic to another space Y if and only if Hom X is isomorphic to Hom Y.
    This is one corollary of the Yoneda lemma.
    We'd also like this isomorphism to respect the morphisms about X, and this the case, as maps
    from X to Y correspond bijectively to maps from Hom X to Hom Y, i.e. since Hom X and Hom Y are
    functors, this is equivalently a bijection to natural transformations from Hom X to Hom Y.
    But let's write this a little more suggestively- Hom X Y is just Hom Y applied to X. The
    incredible result that is the Yoneda lemma says that in fact this not only holds for Hom Y
    applied to X, but for any functor F applied to X! That is, F of X is truly isomorphic to
    the set of natural transformation from the representation of X to F, i.e. from Hom X to F.
    This means for example that the set of natural transformations from Hom X to F, which is
    really abstract and not immediately clear, is just isomorphic to F(X). 

    But that's the Yoneda lemma at first blush! What is really remarkable is what this tells
    us philosophically, that an object living in a category is entirely determined by its
    relationship to other objects in that category.
    In fact, this philosophy runs much deeper then you might first expect. Recently, in 
    my study of stable homotopy theory, I've been utilizing what is called the enriched
    Yoneda lemma. It's the same philosophy, but upgraded in a sense. The idea of enriched
    category theory is that the maps between objects in an enriched category are not only
    sets, but elements of some nice category themselves. A category can be, but not necssarily,
    be enriched over itself, The idea is just that the category you are enriching over has
    nice properties. The prototypical example is that of pointed compactly generated topological
    spaces, which is enriched over itself. In algebraic topology we have for example the
    notion of a path space. As a set, it is the set of maps from the interavl to X. But it's a 
    very useful fact from topology that this is itself a topological space.
    I'm rambling on, but the amazing this is that the Yoneda philosophy remains in this crazy
    situation. Which is to say, the set of enriched natural transformations from Hom X to F
    is isomorphic as an OBJECT, e.g. a topological space, to F(X).
    It's the same amazing idea that we can understand an object by understanding its relationship
    to other objects in the category, whether that set of relationships be a Set or a topological space
    or whatever.
    """
    def construct(self):
        y_embedding = TexMobject(r"""
            y(X): X\mapsto Hom(-,X)
        """)
        statement_iff = TexMobject(r"""
            X\cong Y\quad\iff\quad Hom(-,X)\cong Hom(-,Y)
        """).shift(1*DOWN)
        bij = TexMobject(r"""
            (X\to Y)\quad\leftrightarrow\quad(Hom(-,X)\to Hom(-,Y))
        """).shift(1*DOWN)
        iso_hom = TexMobject(r"""
            Hom(X,Y)\cong [Hom(-,X), Hom(-Y)]
        """).move_to(bij)
        more_suggestive = TexMobject(r"""
            Hom(-,Y)(X)\cong [Hom(-,X), Hom(-Y)]
        """).move_to(iso_hom)
        final_form = TexMobject(r"""
            F(X)\cong [Hom(-,X), F(-)]
        """).move_to(more_suggestive)
        presheaf = TexMobject(r"""
            F:C^{op}\longrightarrow Set
        """).shift(2*DOWN).scale(.75)


        self.play(
            FadeIn(y_embedding)
        )
        self.wait(2)
        self.play(
            Transform(y_embedding, y_embedding.copy().shift(1*UP))
        )
        self.play(
            FadeIn(statement_iff)
        )
        self.wait(2)
        self.play(
            FadeOut(statement_iff)
        )
        self.play(
            FadeIn(bij)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(bij, iso_hom)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(iso_hom, more_suggestive)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(more_suggestive, final_form)
        )
        self.wait(2)
        self.play(
            FadeIn(presheaf)
        )
        self.wait(2)
        self.clear()

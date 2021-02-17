# Date: 2/9/21
# Purpose: prelude to section "abstract homotopy theory" on nLab
# Notes: uploaded 2/17


from manimlib.imports import *
fn = "transition_to_abstract_homotopy"


class threeclasses(Scene):
    """
    So we now want to generalize homotopy theory. To do that, let's think
    about what were particularly important classes of functions in our
    topological homotopy theory. That is, from which things were we able
    to develop a lot of theory?
    Well it seemed, particularly in the last video, that these three were
    central: weak homotopy equivalences, relative cell complexes, and Serre
    fibrations. The idea when we build this general setting for homotopy
    is to construct analogs to these classes of functions in such a way that
    their relationships with each other, some of which we saw last time via
    lifting properties, is maintained.
    This is the profound insight formalized by Daniel Quillen, and the axioms
    he came up with form what is called the model category structure.
    It turns out that this is a particular presentation of a more general
    structure of infinity 1 categories, which again are a kind of m n category,
    but as is often the case with higher levels of abstraction, it becomes
    difficult to compute things at these higher levels of abstractions.
    Model categories form a nice setting that is sufficiently general yet
    easy enough for computations.
    At first blush, it might be difficult to see why we would need to generalize
    past the category Top. It's not so much that we want to to homotopy theory on
    an entirely different type of spaces, but that we can specialize and extend 
    the theory for certain situations. I guess I'm thinking in particular of
    how for example pointed compactly generated topological spaces have their
    own model structure, as do spectra, which are a whole collection of topological
    spaces. But we can extend to other things to, such as a particular set of functors!
    These are called topologically enriched functors.
    """
    def construct(self):
        the_three = TextMobject(r"""
            \begin{enumerate}
                \item weak homotopy equivalences
                \item relative cell complexes
                \item Serre fibrations
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [the_three]
        )

class def21(Scene):
    """
    So here's a starting point. We want to first generalize this notion
    of a weak homotopy equivalence.
    A category with weak equivalences is a category that has a subclass W of
    its morphisms with the following properties:
    W contains all the isomorphisms of C, and it is closed under two out of three.
    This is basically like transitive equivalence on steroids, so if any two of the morphisms
    are in W, then so is the third.
    """
    def construct(self):
        title = make_title("Definition", 2.1)

        self.play(
            Write(title)
        )
        self.wait(2)

        d1 = TextMobject("A ", "category with weak equivalences", " \
            is", r"""
            \begin{enumerate}
                \item a category $\mathcal{C}$
                \item a sub-class $W\subset\text{Mor}(\mathcal{C})$ such that:
            \end{enumerate}
            """, alignment="").scale(.65).to_edge(LEFT, buff=.5)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
            \begin{enumerate}
                \item $W$ contains all isomorphisms
                \item $W$ is closed under two-out-of-three:
            \end{enumerate}
        """, alignment="").scale(.65).to_edge(RIGHT, buff=.75).shift(1*UP)

        d3 = tikz("cat_weak_equivs_d3", r"""
            \begin{tikzcd}
                & Y \arrow{dr} & \\
                X \arrow{ur} \arrow{rr} & & Z
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=1).scale(.9)

        self.cycle(
            [d1, d2, d3],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class rmk22(Scene):
    """
    So I can't speak to some of this remark, but the essense of what it says is this:
    We in fact can already determine a homotopy theory with just a category of weak equivalences.
    The specific way in which is done is by forcing weak equivalences to become actual
    homotopy equivalences, but as you can imagine we lose some nuance when we do this.
    The idea that nLab refers to as simplicial localization is that this is useful
    really only when we introduce further structure, which I assume is to make up for this
    gap. I might go into this later, but for now that is all I can say on the subject.
    nLab provides references, as usual. But yeah, the further axioms we introduce will be
    for the purposes of making the resulting model category more tractable and easier to
    work with.
    """
    def construct(self):
        title = make_title("Remark", 2.2)

        self.play(
            Write(title)
        )
        self.wait(2)

        r1 = TextMobject(r"""
            \begin{enumerate}
                \item this already determines a homotopy theory
                \item the furter axioms make model categories more tractable
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def23(Scene):
    """
    So here's the definition for a model category. It is of course
    a category along with three particular classes of morphisms. So
    just to mention terminology first of all, cof and fib are obviously
    shorthand for cofibrations and fibrations. We will also call
    elements of W intersect Cof as acyclic cofibrations, and W intersect
    Fib as acyclic fibrations. This should immediately remind you of the analogies
    from topological homotopy theory. But remember how we wanted to somehow distill
    enough properties about these analogues from topological homotopy theory
    so that their essential relationships remained? Well, here is one set of 
    requirements that does that- we require that W makes the category into a
    category with weak equivalences, and that the pair of acyclic cofibartions
    comma fibrations and the pair cofibrations comma acyclic fibrations are
    weak factorization systems. We will define weak factorization systems in the next
    video.
    But this should immediately remind you of the strange lifting duality we
    uncovered last time, that the maps that lifted against the acyclic generating
    cofibrations were the regular Serre fibrations, and the maps that lifted against
    the regular generating cofibrations were acyclic Serre fibrations.
    Once we've solidified these definitions, we'll come back and formally prove
    the model category structure on topological spaces proper, which our intuition is
    already leading us to believe exists and is as we expect.
    """
    def construct(self):
        title = make_title("Definition", 2.3)

        self.play(
            Write(title)
        )
        self.wait(2)

        d1 = TextMobject("A ", "model category", " is", r"""
            \begin{enumerate}
                \item a category $\mathcal{C}$ with all limits and colimits
                \item three sub-classes $W$, $\text{Fib}$, $\text{Cof} \ 
                    \subset \text \ \text{Mor}(\mathcal{C})$
            \end{enumerate}
            such that
            \begin{itemize}
                \item $W$ makes $\mathcal{C}$ into a category with weak equivalences
                \item $(W\cap\text{Cof},\text{Fib})$ and $(\text{Cof}, W\cap\text{Fib})$
                         are weak factorization systems
            \end{itemize}
        """, alignment="").scale(.65)

        self.cycle(
            [d1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

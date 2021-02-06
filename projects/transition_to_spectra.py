# Date: 1/27/21
# Purpose: covers introduction to part a of spectra on nlab
from manimlib.imports import *


fn = "transition_to_spectra"

"""
INTRODUCTION:
The topic of spectra is incredibly deep, and I can't hope to do it justice
at the level of understanding I currently am at. Hopefully I can return
to that at a later time, but for now I'd like to motivate the construction
of spectra in the way with its historical motivation, a motivation which
first led me down the rabbit hole of homotopy theory.
It lies in a phenomenon in the homotopy groups of spheres. This is the
Freudenthal suspension theorem, a consequence of which we observe here:
the diagonals stabilize. Now this is quite incredible on its own,
but we don't actually understand the pattern yet! And the more we look
into it, we uncover deeper and more profound results.
So the question is, how do we study this stable phenomenon? And the first
step was a good insight for me into how a mathmatecian thinks:
we'd like a place to work in. Specifically, we'd like a category which
essentializes this stable phenomenon. At a basic level, this would mean
that, in this stable category, the 0th homotopy group of the quote on quote
sphere would be that first blue nontrivial diagonal consisting of Z. The
1st would be the next green diagonal Z_2, and so on so forth.
But this immediately would make you point out, that we want our
homotopy groups to correspond to diagonals, so it doesn't make sense to 
talk about a stable homotopy group of a single sphere, but rather of all
spheres. Call this "all spheres object" S, and we'd like the second homotopy
group of S to equal the 6th homotopy group of S^4, the 7th homotopy group
of S^5, etc.
And so we immediately realize that our objects in this category are
probably not going to topological spaces, they're going to be sequences
of objects. In this sphere example, how do we connect consecutive spheres, 
for example S^3 to S^4? Well, we use the suspension functor! In particular,
we apply it iteratively to a point to get all spheres. What if we started
with some other topological space X rather than a point? Does this stable
phenomenon continue?
Before I get ahead of myself, I want to point out that this is roughly what
spectra are- they are objects of the stable homotopy category. Hence,
to study the stable phenomenon we work with spectra.
Before we get into the nLab, I want to point out that there are deep 
and far-reaching applications of spectra. For example, the are extremely 
intimately related to ALL generalized cohomology theories, which is just
incredible. I'll leave some resources down below where you can begin to
look for some applications and generalized motivation for spectra.
But lets get into the nLab for now. 
"""

class def01(Scene):
    """
    We start out by recalling that for the category of compactly generated
    pointed topological spaces, there is an smash-tensor/hom adjunction
    via the reduced suspension and looping operations.
    """
    def construct(self):
        title = make_title("Definition", 0.1)

        pic1 = tikz("def01pic", r"""
            \begin{tikzcd}[column sep=huge]
                (\Sigma \dashv \Omega): \cat{Top}_{\text{cg}}^{\ast /} 
                \arrow[yshift=-.5em]{r}[below]{\cat{Maps}(S^1,-)}[above]{\perp} & 
                \cat{Top}_{\text{cg}}^{\ast /} \arrow[yshift=.5em]{l}[above]{S^1\wedge(-)}
            \end{tikzcd}
        """, fn).shift(.5*LEFT)

        self.play(Write(title))
        self.wait(2)
        self.play(FadeIn(pic1))
        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class prop02(Scene):
    """
    Taking this one step further, we found that if we imposed the classical
    model structure on the category of compactly generated pointed topological
    spaces, we got that our suspension/looping adjunction was upgraded to a
    Quillen adjunction. Technically speaking, the suspension/looping operations
    are derived functors of the aforementioned adjoint pair with respect
    to the homotopy category of the previous category.
    """
    def construct(self):
        title = make_title("Proposition", 0.2)

        self.play(Write(title))
        self.wait(2)

        pic1 = tikz("prop02pic1", r"""
            \begin{tikzcd}[column sep=huge]
                (\Sigma \dashv \Omega): (\cat{Top}_{\text{cg}}^{\ast /})_{\text{Quillen}}
                \arrow[yshift=-.5em]{r}[below]{\cat{Maps}(S^1,-)}[above]{\perp} & 
                (\cat{Top}_{\text{cg}}^{\ast /})_{\text{Quillen}} \arrow[yshift=.5em]{l}[above]{S^1\wedge(-)}
            \end{tikzcd}
        """, fn).scale(.75).shift(1*UP)

        pic2 = tikz("prop02pic2", r"""
            \begin{tikzcd}[column sep=huge]
                (\Sigma \dashv \Omega): \cat{Ho}(\cat{Top}^{\ast /})
                \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\perp} & 
                \cat{Ho}(\cat{Top}^{\ast /}) \arrow[yshift=.5em]{l}[above]{\Sigma}
            \end{tikzcd}
        """, fn).scale(.6).shift(1*DOWN)

        self.play(FadeIn(pic1))
        self.wait()
        self.play(FadeIn(pic2))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class hospectra(Scene):
    """
    If you recall, the homotopy groups of spheres stabilized after,
    roughly speaking, applying the suspension functor iteratively,
    which equated to moving to higher dimensional spheres in that case.
    So, roughly speaking, we'd like to think about passing
    from the category of topological spaces to the stable homotopy
    category by applying an infinite suspension functor.
    Ho(Spectra) is the stable homotopy category here.
    Again, we'd like to upgrade this so that we have a complete
    homotopy theory for spectra, i.e. wed like to upgrade the previous
    diagram to preserve model category structures between all categories
    presented.
    You might have noticed the slight of hand here- that we didn't go
    from Ho(Spectra) to the category Spectra, but instead to the 
    category Sequential Spectra.
    """
    def construct(self):
        cat = TextMobject("Stable Homotopy Category")\
            .scale(.75).to_edge(UP,buff=.5).set_color(BLUE)

        self.play(
            Write(cat)
        )
        self.wait(2)

        pic1 = tikz("hospectrapic1", r"""
            \begin{tikzcd}[column sep=huge, row sep=huge]
                (\Sigma \dashv \Omega): \cat{Ho}(\cat{Top}^{\ast /})
                \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\perp}
                \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} & 
                \cat{Ho}(\cat{Top}^{\ast /}) \arrow[yshift=.5em]{l}[above]{\Sigma}
                \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} \\
                \cat{Ho}(\cat{Spectra})\arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\simeq}
                \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
                 & \cat{Ho}(\cat{Spectra})\arrow[yshift=.5em]{l}[above]{\Sigma}
                 \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
            \end{tikzcd}
        """, fn).scale(1.5)

        pic2 = tikz("hospectrapic2", r"""
            \begin{tikzcd}[column sep=huge, row sep=huge]
                (\Sigma \dashv \Omega): (\cat{Top}_{\text{cg}}^{\ast /})_{\text{Quillen}}
                \arrow[yshift=-.5em]{r}[below]{\cat{Maps}(S^1,-)}[above]{\perp}
                \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} & 
                (\cat{Top}_{\text{cg}}^{\ast /})_{\text{Quillen}}
                 \arrow[yshift=.5em]{l}[above]{S^1\wedge(-)}
                \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} \\
                \cat{SeqSpec}(\cat{Top}_{\text{cg}})_{\text{stable}}
                \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\simeq_Q}
                \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
                 & \cat{SeqSpec}(\cat{Top}_{\text{cg}})_{\text{stable}}
                 \arrow[yshift=.5em]{l}[above]{\Sigma}
                 \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeIn(pic1)
        )
        self.wait(3)
        self.play(
            FadeOut(pic1)
        )
        self.play(
            FadeIn(pic2)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class typesofspectra(Scene):
    """
    This is in light of the fact that there are several
    different kinds of spectra and hence categories of
    spectra. Examples listed here are sequential spectra,
    symmetric spectra, orthogonal spectra, and excisive
    functors, and each has their own model structure!
    The reason we said Ho(Spectra) and not Ho(SeqSpec) 
    is because, remarkably, almost all of the different
    spectra categories induce equivalent stable homotopy
    categories.
    The reason so many spectra exist is not purely a 
    historical artifact, though. As you go down the list,
    you get a richer structure, but on the other hand
    it is harder to construct and work with them.
    But that's all I wanted to say as far as introductions go.
    Next time, we'll begin with the actual rigour.
    """
    def construct(self):
        thelist = TextMobject(r"""
            \begin{enumerate}
                \item Sequential spectra
                \item Symmetric spectra
                \item Orthogonal spectra
                \item Excisive functors
            \end{enumerate}
        """).scale(.75)

        self.play(
            FadeIn(thelist)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


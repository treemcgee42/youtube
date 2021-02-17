from manimlib.imports import *
from NumberCreature.NumberCreature import *

class title(Scene):
    def construct(self):
        dforms = TextMobject("Differential Forms")\
                .shift(.5*UP)
        p1 = TextMobject("Part 1a: Tangent Spaces (Visually/Intuitively)")\
                .scale(.75)\
                .next_to(dforms, direction=DOWN, buff=MED_SMALL_BUFF)

        self.wait()
        self.play(  Write(dforms,run_time=3))
        self.wait()
        self.play(  FadeIn(p1, run_time=3))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ting(Scene):
    def construct(self):
        surface = SVGMobject("tangentspaces/localmanifold.svg")
        surface[0].set_color(BLUE)
        surface[1].set_color(RED)
        surface[2].set_color(WHITE).set_opacity(.2)

        s2 = SVGMobject("tangentspaces/localmanifold.svg",stroke_width=0)
        s2[2].set_color(WHITE).set_opacity(.3)
        
        """
        sphere = Sphere(stroke_widdth=0).scale(1.5)
        pt = Dot((0,-.75,.5)).rotate(PI/2,axis=UP).scale(.4).set_color(RED)
        #ptlabel = TexMobject("x_0").move_to(pt).rotate(PI/2,axis=UP).rotate(PI/2,axis=RIGHT)\
        #            .set_color(RED).scale(.5).shift(.25*RIGHT)
        self.set_camera_orientation(phi=80 * DEGREES,theta=0*DEGREES,distance=5)
        self.play(  GrowFromCenter(sphere))
        self.wait()
        self.play(  GrowFromCenter(pt))
        self.wait()
        
        #self.set_camera_orientation(phi=0 * DEGREES,theta=-90*DEGREES,distance=5)
        self.move_camera(phi=-80*DEGREES)
        self.play(  Transform(sphere,surface))
        """

        self.play(  GrowFromCenter(surface[0]))
        self.wait()
        self.play(  GrowFromCenter(surface[1]))

        ptlabel = TexMobject("x_0",background_stroke_width=0).scale(.5).set_color(RED)\
                    .next_to(surface[1],direction=LEFT,buff=SMALL_BUFF)\
                    .shift(SMALL_BUFF*DOWN)

        self.play(  FadeIn(ptlabel))
        self.wait()

        tv1 = Arrow(surface[1],(-1,.5,0)).shift(.22*RIGHT,.04*DOWN)
        tv2 = tv1.copy().rotate(-130*DEGREES).shift(.64*RIGHT,.09*UP)
        self.add(tv1,tv2)
        self.play(  ShowCreation(tv1), ShowCreation(tv2))
        self.wait()

        origin = (-3,-2,0)
        zax = Line(origin,(-3,3,0)).add_tip()
        xax = Line(origin,(3,-2,0)).add_tip()
        yax = Line(origin,(-4,-3,0)).add_tip()

        self.play(  ShowCreation(zax), ShowCreation(xax), ShowCreation(yax))
        self.wait()
        self.play(  FadeIn(s2[2]))
        self.wait()

        self.play(  *[FadeOut(mob) for mob in [zax,xax,yax,s2[2]]])
        self.wait()
        self.play(  *[FadeOut(mob)for mob in [ptlabel,tv2,tv1]])
        self.wait()

        coordchart = TexMobject("\phi:","U","\\to\\mathbb{R}^{n}").shift(2.5*UP)
        coordchart[1].set_color(RED)

        self.play(  ShowCreation(coordchart))
        self.wait()

        # setup for curves business
        u = SVGMobject("tangentspaces/nhoodu.svg", stroke_width=0).shift(4*LEFT)
        u[0].set_color(RED).set_opacity(.2)
        u[1].set_color(RED)
        ulabel = TexMobject("U").set_color(RED).next_to(u,direction=DOWN,buff=MED_SMALL_BUFF)

        r2 = SVGMobject("tangentspaces/utor2.svg", stroke_width=1.25).shift(4*RIGHT)
        r2[2].set_color(RED)
        r2label = TexMobject("\\mathbb{R}^2").next_to(r2,direction=DOWN,buff=MED_SMALL_BUFF)

        self.play(  *[FadeIn(mob)for mob in (u[0],ulabel,r2[0],r2[1],r2label)])
        self.wait()
        self.play(  *[FadeIn(mob)for mob in [u[1],r2[2]]])

        # curves 1
        ucurves = SVGMobject("tangentspaces/nhoodu.svg", fill_opacity=0,\
                        stroke_width=1.25).shift(4*LEFT)
        for mob in [ucurves[2],ucurves[3],ucurves[4]]:
            mob.set_color(GREEN)
        r2curves = SVGMobject("tangentspaces/utor2.svg", stroke_width=1.25,\
                        fill_opacity=0).shift(4*RIGHT)
        for mob in [r2curves[3],r2curves[4],r2curves[5]]:
            mob.set_color(GREEN)

        self.play(  FadeIn(ucurves[2]))
        self.play(  ReplacementTransform(ucurves[2], r2curves[3]))
        self.play(  FadeIn(ucurves[3]))
        self.play(  ReplacementTransform(ucurves[3], r2curves[4]))
        self.play(  FadeIn(ucurves[4]))
        self.play(  ReplacementTransform(ucurves[4], r2curves[5]))
        self.wait()

        r2curvesv1 = tv2.copy().move_to(r2[2]).shift(.3*RIGHT,.21*UP)
        self.play(  ShowCreation(r2curvesv1))
        self.wait()
        self.play(  ReplacementTransform(r2curvesv1,tv2), *[FadeOut(mob)for mob in [r2curves[3],r2curves[4],r2curves[5]]])
        self.wait()

        # curves 2
        for mob in [ucurves[5],ucurves[6],ucurves[7]]:
            mob.set_color(GREEN)
        for mob in [r2curves[6],r2curves[7],r2curves[8]]:
            mob.set_color(GREEN)
        
        self.play(  FadeIn(ucurves[5]))
        self.play(  ReplacementTransform(ucurves[5], r2curves[6]))
        self.play(  FadeIn(ucurves[6]))
        self.play(  ReplacementTransform(ucurves[6], r2curves[7]))
        self.play(  FadeIn(ucurves[7]))
        self.play(  ReplacementTransform(ucurves[7], r2curves[8]))
        self.wait()

        r2curvesv2 = tv1.copy().move_to(r2[2]).shift(.3*LEFT,.09*UP)
        self.play(  ShowCreation(r2curvesv2))
        self.wait()
        self.play(  ReplacementTransform(r2curvesv2,tv1), *[FadeOut(mob)for mob in [r2curves[6],r2curves[7],r2curves[8]]])
        self.wait()
        self.play(  FadeIn(s2[2]))
        self.wait()

        self.play(  *[FadeOut(mob)for mob in self.mobjects[2:]])
        self.wait()

        # derivations
        deriv = TexMobject("\\{\\mbox{derivations}\\}\\longleftrightarrow \\{\\mbox{directional derivatives}\\}")\
                .shift(2*UP).scale(.75)
        derivdef = TexMobject("D(fg)=D(f)\cdot g(x)+f(x)\cdot D(g)").scale(.75).shift(2*DOWN)
        
        self.play(  ShowCreation(deriv))
        self.wait()
        self.play(  ShowCreation(derivdef))
        self.wait()
        self.play(  FadeIn(tv1), FadeIn(tv2))
        self.play(  FadeIn(s2[2]))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])
        self.wait()

class conclusion(Scene):
    def construct(self):
        vfield = TextMobject("Generalizing Vector Fields:").set_color(RED).scale(.75).shift(2*UP)
        pathto = TexMobject("\\mbox{point in manifold}\\to\\mbox{tangent vector at point}")\
                    .scale(.75)

        self.play(  ShowCreation(vfield))
        self.wait()
        self.play(  Write(pathto))
        self.wait()

        self.play(  *[FadeOut(mob)for mob in self.mobjects])
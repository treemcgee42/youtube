from manimlib.imports import *
from NumberCreature.NumberCreature import *

class surfaceintegral(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                -1*u**2+1.5
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)
        
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)

        self.add(axes)
        self.play(  Write(paraboloid))
        self.wait()

        pt = Dot((-.75,-.075,0)).scale(.35)
        ru = Arrow().scale(.25).move_to(pt, aligned_edge=LEFT).rotate(-5*DEGREES,about_point=pt.get_center())
        rv = Arrow().scale(.25).move_to(pt, aligned_edge=LEFT).rotate(-100*DEGREES,about_point=pt.get_center())
        self.add_fixed_in_frame_mobjects(   ru.set_opacity(0),rv.set_opacity(0),pt.set_opacity(0)) #
        tvecs = VGroup( pt,ru,rv)
        for m in tvecs:
            m.set_color(YELLOW)
            self.play(  ShowCreation(m.set_opacity(1)))

        # oriented region

        rec = Rectangle(height=.35,width=.35,fill_opacity=.25,fill_color=YELLOW,stroke_width=0)\
                .move_to(pt, aligned_edge=LEFT+UP).rotate(-5*DEGREES, about_point=pt.get_center())\
                .shift(.025*DOWN)
        orarr = TexMobject("\\circlearrowleft").scale(.5).shift(.25*DOWN,.61*LEFT).set_color(YELLOW)
        self.add_fixed_in_frame_mobjects(rec,orarr)
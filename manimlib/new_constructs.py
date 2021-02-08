# Date: 1/27/21
# Purpose: to create a file to have extra functions based on personal usability


from manimlib.imports import *
from shutil import *
import os
import os.path
from os import path

TIKZ_TEMPLATE_FILE = "tikz_template.tex"
MANIM_LOC = "/Users/ogmalladii/Documents/manim-master/"


# Purpose: create titles such as "Definition 1.1" or "Lemma 1.1" in upper left corner
# Parameters: str and str/int
def make_title(type_of_title, numbering):
    t = str(type_of_title)
    no = str(numbering)
    return TextMobject("\\textsc{%s %s}" % (t, no)).scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)


# Purpose: returns a png file (image mobject) of some tikz input
# Parameters: strings filename and tex and file_name. The png will be found at /file_name/filename.png
def tikz(filename, tex, file_name):
    global MANIM_LOC

    media_directory = MANIM_LOC + "media/tikz/"
    tikz_template_loc = MANIM_LOC + "manimlib/" + TIKZ_TEMPLATE_FILE
    current_file_name = file_name
    exit
    working_path = os.path.join(media_directory, current_file_name)
    new_tex_file = working_path + "/" + filename + ".tex"

    try:
        os.mkdir(working_path)
    except:
        pass

    if not path.exists(new_tex_file):
        open(new_tex_file, "x")
    else:       # if the tex is the same as last time, don't run the whole thing again
        with open(new_tex_file) as myfile:
            if tex in myfile.read():
                return ImageMobject(new_tex_file[:-4]+".png")

    copy(tikz_template_loc, working_path)       # temporary file
    os.replace(working_path + "/" + TIKZ_TEMPLATE_FILE, new_tex_file)

    with open(new_tex_file, "r") as file:
        data = file.readlines()

    for i, j in enumerate(data):
        if data[i] == "YourTextHere\n":
            data[i] = tex
    
    with open(new_tex_file, "w") as file:
        file.writelines( data )

    os.system("pdflatex --output-directory=%s -no-shell-escape %s >/dev/null 2>&1" % \
        (working_path, new_tex_file))
    os.system("convert -density 600x600 %s -quality 90 -resize 1080x800 %s" % \
        (new_tex_file[:-4]+".pdf", new_tex_file[:-4]+".png"))

    return ImageMobject(new_tex_file[:-4]+".png")

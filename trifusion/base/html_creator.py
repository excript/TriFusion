#!/usr/bin/env python2
#
#  Copyright 2012 Unknown <diogo@arch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


class HtmlTemplate:
    """
    Data must be a list of tuples (title, image, description)
    """
    def __init__(self, folder, data):
        if not folder.endswith("/"):
            folder += "/"
        self.folder = folder
        self.data = data

    def write_file(self):
        if not self.data:
            return None

        #add header, styles basic html info
        html = "<!DOCTYPE html>\n\
<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n\
<html>\n\
<head>\n\
     <style type=\"text/css\">\n\
        .flex-container {\n\
            display: -webkit-flex;\n\
            display: flex;\n\
            -webkit-flex-direction: row;\n\
            flex-direction: row;\n\
        }\n\
        .flex-item {\n\
            display:flex;\n\
            margin: 3px;\n\
            padding: 10px 0 0 10px;\n\
        }\n\
        .flex-item img{\n\
            width: 100%;\n\
        }\n\
        span {\n\
            min-width: 5em;\n\
            margin-top: 3em;\n\
            padding-right: 1em;\n\
        }\n\
        .img-wrapper {\n\
            display: inline-block;\n\
            overflow: hidden;\n\
            border: 1px solid gray;\n\
        }\n\
    </style>\n\
    <script type=\"text/javascript\">\n\
        var images = ["
        #add images names
        for (_, img, _) in self.data[:-1]:
            html += "\"" + img + "\","
        html += "\"" + self.data[-1][1] + "\"];\n"

        #add descriptions
        html += "\t\tvar descriptions = ["
        for (_, _, desc) in self.data[:-1]:
            html += "\"" + desc + "\","
        html += "\"" + self.data[-1][2] + "\"];\n"

        #add titles
        html += "\t\tvar titles = ["
        for (title, _, _) in self.data[:-1]:
            html += "\"" + title + "\","
        html += "\"" + self.data[-1][0] + "\"];\n"

        #add data changing funtion
        html += "\t\tfunction changeImage(index){\n\
                var img = document.getElementById(\"img_place\");\n\
                img.src = images[index];\n\
                document.getElementById(\"desc_place\").textContent = descriptions[index];\n\
                document.getElementById(\"title\").textContent = titles[index];\n\
            }\n\
    </script>\n"

        #add actual html
        #place 1st image visible by default
        html += "</head>\n\
<body>\n\
    <h2 id=\"title\">" + self.data[0][0] + "</h2>\n\
    <div class=\"flex-container\">\n\
        <div class=\"flex-item\">\n\
            <span>\n"

        #for each image add code to change them
        for x in xrange(len(self.data)):
            html += "\t\t\t\t<a href=\"#\" onclick=\"changeImage(" + str(x) + ")\">Img #" + str(x) + "</a></p>\n"

        #insert remainder html
        html += "\t\t\t</span>\n\
            <div class=\"img-wrapper\">\n\
                <img id=\"img_place\" src=\"" + self.data[0][1] + "\"/>\n\
           </div>\n\
        </div>\n\
    </div>\n\
    <span id=\"desc_place\">" + self.data[0][2] + "</span>\n\
</body>\n\
</html>"

        output_handle = open(self.folder + "index2.html", "w")
        output_handle.write(html)
        output_handle.close()

if __name__ == "__main__":
    html = HtmlTemplate("/home/fernando-work/Documents/trihtml", [("ay ay", "Species_copy_number.png", "desc"), ("ay ay ay", "Species_coverage.png", "desc2")])
    html.write_file()

__author__ = "Diogo N. Silva and Fernando Alves"

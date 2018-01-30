# GW2-Dye-Schemer
Uses RGB to HSL color conversions to generate common color scheme patterns mapped to the dye system of Guild Wars 2.

# Requirements
This script uses JuxhinDB's GW2API wrapper for Python, located here: https://github.com/JuxhinDB/gw2-api-interface
I have included the files required to make this script work in this repository, but check out his work, it's great! All credit for the API wrapper goes to him, with a minor bug fix implemented by myself (it has been pulled into his master branch, don't worry).

# About
This script uses colorspace conversions in order to map the Guild Wars 2 Dye System to common RGB color schemes (Monochromatic, Complimentary, Split-Complimentary, Triadic, Tetradic, etc.). It does this by querying the Guild Wars 2 API for the dye database's RGB value data on every dye color in every material (cloth, leather, metal). From there, it converts these RGB (Red, Green, Blue) values into HSL (Hue, Saturation, Lightness) equivalents, that way the schemes can be calculated with a color-wheel based model instead of the 3D cube representation that RGB format gives us. These HSL values are rotated and scaled around the color wheel and then converted back into RGB values, and the Euclidean distance is calculated to find the nearest matching Guild Wars 2 dye that matches each color in the scheme for any given material. The results? Full color schemes by dye name for many different formats and every single material... all from just typing in your dominant dye color of choice!

# Usage
In order to run this script, you must first clone or download the zip file from this repository and then unzip it. Then follow the following steps:
1. Navigate in your command line/terminal to your folder that contains the files in this repository.
2. While in the directory containing "gw2_dye_schemer.py" run the following command:
    python gw2_dye_schemer.py [DYE NAME HERE]
(type the name of the dye you want where it says "[DYE NAME HERE]" without the quotes or brackets. eg. If you want Sky Dye, type "Sky" or "sky", case does not matter. Spelling does!)
3. Enjoy the results!

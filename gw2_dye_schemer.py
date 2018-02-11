from client import GuildWars2Client
from collections import defaultdict
import math, random, argparse, colors

parser = argparse.ArgumentParser()
parser.add_argument('dye_input', help='The input dye the user wants color schemes for.', type=str)
args = parser.parse_args()

dye_input = args.dye_input
gw2client = GuildWars2Client(version='v2')
dye_ids = []
dyes_data = []
dye_map = defaultdict(str)
materials = ['cloth', 'leather', 'metal']

def client_settings():
	print("Welcome to the Guild Wars 2 Dye Schemer\n\nClient Settings:")
	print(gw2client)

def client_directory():
	print(dir(gw2client))

def init_dyes():
	global dye_ids
	global dyes_data
	global dye_map
	dye_ids = gw2client.colors.get()
	dyes_data = gw2client.colors.get(ids=dye_ids[:199]) + gw2client.colors.get(ids=dye_ids[199:398]) + gw2client.colors.get(ids=dye_ids[398:])
	for dye in dyes_data:
		dye_map[dye['name'].lower()] = dye

def get_nearest_dye(rgb_y, material):
	distances = defaultdict(int)
	r_y = rgb_y[0]
	g_y = rgb_y[1]
	b_y = rgb_y[2]
	rgb_x = []
	for color in dyes_data:
		rgb_x = color[material]['rgb']
		name = color['name']
		r_x = rgb_x[0]
		g_x = rgb_x[1]
		b_x = rgb_x[2]
		dist = ((r_y-r_x)**2) + ((g_y-g_x)**2) + ((b_y-b_x)**2)
		distances[name] = dist
	min_name = ''
	min_dist = 999999999999
	for name, dista in distances.items():
		if dista < min_dist:
			min_dist = dista
			min_name = name
	return min_name

def get_monochromatic_dyes(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	monochrome_rgb_1 = colors.get_monochromatic_color(rgb[0], rgb[1], rgb[2], 0.2)[1]
	monochrome_rgb_2 = colors.get_monochromatic_color(rgb[0], rgb[1], rgb[2], 0.4)[1]
	monochromatic_dye_1 = get_nearest_dye(monochrome_rgb_1, material)
	monochromatic_dye_2 = get_nearest_dye(monochrome_rgb_2, material)
	return [monochromatic_dye_1, monochromatic_dye_2]

def get_complimentary_dye(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	complimentary_rgb = colors.get_complimentary_color(rgb[0], rgb[1], rgb[2])[1]
	complimentary_dye = get_nearest_dye(complimentary_rgb, material)
	return [complimentary_dye]

def get_split_complimentary_dyes(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	split_comp_rgb = colors.get_split_complimentary(rgb[0], rgb[1], rgb[2])
	split_comp_dye_1 = get_nearest_dye(split_comp_rgb[1], material)
	split_comp_dye_2 = get_nearest_dye(split_comp_rgb[2], material)
	return [split_comp_dye_1, split_comp_dye_2]

def get_analogous_dyes(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	analogous_rgb = colors.get_analogous_colors(rgb[0], rgb[1], rgb[2])
	analogous_1 = get_nearest_dye(analogous_rgb[1], material)
	analogous_2 = get_nearest_dye(analogous_rgb[2], material)
	return [analogous_1, analogous_2]

def get_triadic_dyes(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	triadic_rgb = colors.get_triadic_colors(rgb[0], rgb[1], rgb[2])
	triadic_dye_1 = get_nearest_dye(triadic_rgb[1], material)
	triadic_dye_2 = get_nearest_dye(triadic_rgb[2], material)
	return [triadic_dye_1, triadic_dye_2]

def get_tetradic_dyes(dye_name, material):
	dye = dye_map[dye_name]
	rgb = dye[material]['rgb']
	tetradic_rgb = colors.get_tetradic_colors(rgb[0], rgb[1], rgb[2])
	tetradic_dye_1 = get_nearest_dye(tetradic_rgb[1], material)
	tetradic_dye_2 = get_nearest_dye(tetradic_rgb[2], material)
	tetradic_dye_3 = get_nearest_dye(tetradic_rgb[3], material)
	return [tetradic_dye_1, tetradic_dye_2, tetradic_dye_3]

def get_dye_scheme(dye_name, material):
	if dye_name.lower() in dye_map:
		print("\nColor Schemes for " + dye_name + " (" + material + "): ")
		print("Monochromatic Dyes for " + dye_name + " (" + material + "): " + str(get_monochromatic_dyes(dye_name, material)))
		print("Complimentary Dye for " + dye_name + " (" + material + "): " + str(get_complimentary_dye(dye_name, material)))
		print("Split-Complimentary Dyes for " + dye_name + " (" + material + "): " + str(get_split_complimentary_dyes(dye_name, material)))
		print("Analogous Dyes for " + dye_name + " (" + material + "): " + str(get_analogous_dyes(dye_name, material)))
		print("Triadic Dyes for " + dye_name + " (" + material + "): " + str(get_triadic_dyes(dye_name, material)))
		print("Tetradic Dyes for " + dye_name + " (" + material + "): " + str(get_tetradic_dyes(dye_name, material)))
		print("\n")
	else:
		print("Error: No such dye exists. Check your spelling or that you are asking for an existing dye.")
	
def get_random_scheme():
	get_dye_scheme(random.choice(dye_map.keys()), random.choice(materials))


client_settings()
init_dyes()
get_dye_scheme(dye_input, 'cloth')
get_dye_scheme(dye_input, 'leather')
get_dye_scheme(dye_input, 'metal')

#Colorspace conversions

def rgb_to_hsl(r, g, b):
	norms = [(r/255.0), (g/255.0), (b/255.0)] 
	min_val = min(norms)
	max_val = max(norms)
	luminance = ((min_val + max_val)/2)
	saturation = 0
	hue = 0
	if min_val != max_val:
		if luminance < 0.5:
			saturation = ((max_val - min_val)/(max_val + min_val))
		elif luminance >= 0.5:
			saturation = ((max_val - min_val)/(2.0 - max_val - min_val))
	else:
		return [hue, saturation, luminance]
	if max_val == norms[0]:
		hue = ((norms[1] - norms[2])/(max_val - min_val))
	elif max_val == norms[1]:
		hue = 2.0 + ((norms[2] - norms[0])/(max_val - min_val))
	elif max_val == norms[2]:
		hue = 4.0 + ((norms[0] - norms[1])/(max_val - min_val))
	hue *= 60
	if hue < 0:
		hue += 360
	return [hue, saturation, luminance]

def hsl_to_rgb(h, s, l):
	#s = s / 100 #only if numbers are rounded whole numbers
	#l = l / 100 #only if numbers are rounded whole numbers
	r = 0
	g = 0
	b = 0
	tmp1 = 0
	tmp2 = 0
	t_r = 0
	t_g = 0
	t_b = 0
	if s == 0:
		color = int(round(l * 255))
		return [color, color, color]
	else:
		if l < 0.5:
			tmp1 = (l * (1.0 + s))
		elif l >= 0.5:
			tmp1 = (l + s - (l * s))
	tmp2 = (2 * l - tmp1)
	h = h/360
	t_r = h + 0.333
	if t_r < 0:
		t_r += 1
	elif t_r > 1:
		t_r -= 1
	t_g = h
	if t_g < 0:
		t_g += 1
	elif t_g > 1:
		t_g -= 1
	t_b = h - 0.333
	if t_b < 0:
		t_b += 1
	elif t_b > 1:
		t_b -= 1
	r = rgb_tests(t_r, tmp1, tmp2)
	g = rgb_tests(t_g, tmp1, tmp2)
	b = rgb_tests(t_b, tmp1, tmp2)
	return [r, g, b]

def rgb_tests(channel, tmp1, tmp2):
	color = 0
	if (channel * 6) < 1:
		color = (tmp2 + (tmp1 - tmp2) * 6 * channel)
	else:
		if (channel * 2) < 1: 
			color = tmp1
		else:
			if (channel * 3) < 2: 
				color = (tmp2 + (tmp1 - tmp2) * (0.666 - channel) * 6)
			else:
				color = tmp2
	return int(round(color * 255))

def round_vals(color, convert_type):
	if convert_type == 'rgb':
		channel_1 = int(round(color[0]))
		channel_2 = int(round(color[1]))
		channel_3 = int(round(color[2]))
	else:
		channel_1 = int(round(color[0]))
		channel_2 = int(round(color[1]*100))
		channel_3 = int(round(color[2]*100))
	return [channel_1, channel_2, channel_3]

def get_monochromatic_color(r, g, b, intensity):
	new_r = r - (100*intensity)
	if new_r < 0:
		new_r += 255
	new_g = g + (100*intensity)
	if new_g > 255:
		new_g -= 255
	new_b = b + (100*intensity)
	if new_b > 255:
		new_b -= 255
	return [[r, g, b], [int(round(new_r)), int(round(new_g)), int(round(new_b))]]

def get_complimentary_color(r, g, b):
	hsl = rgb_to_hsl(r, g, b)
	rounded_hsl = round_vals(hsl, 'hsl')
	compliment = rounded_hsl[0] + 180
	if compliment > 360:
		compliment -= 360
	elif compliment < 0:
		compliment += 360
	comp = hsl_to_rgb(compliment, hsl[1], hsl[2])
	return [[r, g, b], comp]

def get_split_complimentary(r, g, b):
	hsl = rgb_to_hsl(r, g, b)
	rounded_hsl = round_vals(hsl, 'hsl')
	compliment = rounded_hsl[0] + 180
	if compliment > 360:
		compliment -= 360
	elif compliment < 0:
		compliment += 360
	split_comp1 = compliment + 30
	split_comp2 = compliment - 30
	if split_comp1 > 360:
		split_comp1 -= 360
	elif split_comp1 < 0:
		split_comp1 += 360
	if split_comp2 > 360:
		split_comp2 -= 360
	elif split_comp2 < 0:
		split_comp2 += 360
	sc_1 = hsl_to_rgb(split_comp1, hsl[1], hsl[2])
	sc_2 = hsl_to_rgb(split_comp2, hsl[1], hsl[2])
	return [[r, g, b], sc_1, sc_2]

def get_analogous_colors(r, g, b):
	hsl = rgb_to_hsl(r, g, b)
	rounded_hsl = round_vals(hsl, 'hsl')
	analogous_1 = rounded_hsl[0] + 30
	analogous_2 = rounded_hsl[0] - 30
	if analogous_1 > 360:
		analogous_1 -= 360
	elif analogous_1 < 0:
		analogous_1 += 360
	if analogous_2 < 0:
		analogous_2 += 360
	elif analogous_2 > 360:
		analogous_2 -= 360
	a_1 = hsl_to_rgb(analogous_1, hsl[1], hsl[2])
	a_2 = hsl_to_rgb(analogous_2, hsl[1], hsl[2])
	return [[r, g, b], a_1, a_2]

def get_triadic_colors(r, g, b):
	hsl = rgb_to_hsl(r, g, b)
	rounded_hsl = round_vals(hsl, 'hsl')
	triadic_1 = rounded_hsl[0] + 120
	triadic_2 = rounded_hsl[0] - 120
	if triadic_1 > 360:
		triadic_1 -= 360
	elif triadic_1 < 0:
		triadic_1 += 360
	if triadic_2 < 0:
		triadic_2 += 360
	elif triadic_2 > 360:
		triadic_2 -= 360
	t_1 = hsl_to_rgb(triadic_1, hsl[1], hsl[2])
	t_2 = hsl_to_rgb(triadic_2, hsl[1], hsl[2])
	return [[r, g, b], t_1, t_2]

def get_tetradic_colors(r, g, b):
	hsl = rgb_to_hsl(r, g, b)
	rounded_hsl = round_vals(hsl, 'hsl')
	tetra_1 = rounded_hsl[0] + 60
	if tetra_1 > 360:
		tetra_1 -= 360
	tetra_2 = rounded_hsl[0] + 180
	if tetra_2 > 360:
		tetra_2 -= 360
	tetra_3 = tetra_1 + 180
	if tetra_3 > 360:
		tetra_3 -= 360
	t_1 = hsl_to_rgb(tetra_1, hsl[1], hsl[2])
	t_2 = hsl_to_rgb(tetra_2, hsl[1], hsl[2])
	t_3 = hsl_to_rgb(tetra_3, hsl[1], hsl[2])
	return [[r, g, b], t_1, t_2, t_3]

#print("Monochromatic: " + str(get_monochromatic_color(255, 54, 51, 0.2)))
#print("Complimentary: " + str(get_complimentary_color(255, 54, 51)))
#print("Split Complimentary: " + str(get_split_complimentary(255, 54, 51)))
#print("Analogous: " + str(get_analogous_colors(255, 54, 51)))
#print("Triadic: " + str(get_triadic_colors(255, 54, 51)))
#print("Tetratic: " + str(get_tetradic_colors(255, 54, 51)))

"""
RGB (Red Green Blue) to HSL (Hue Saturation Lightness)

1. Normalize RGB values to numbers between 0-1
	R = r/255
	G = g/255
	B = b/255

2. Find the min and max values of R, G, B
	Example RG = [0.09, 0.38, 0.46]
	min = 0.09 (R)
	max = 0.46 (B)

3. Calculate Luminace value L
	L = (min + max)/2 and round to nearest whole number

4. Find the Saturation S
	If min = max, no saturation. 
	If R=G=B, you have a shade of grey... Depending on brightness it's somewhere between black and white.
	If there is no saturation, we don't need to calculate the Hue, So we set it to 0 degrees.

	In this case, we do have saturation
		If L < 0.5, Saturation S = (max-min)/(max+min)
		If L > 0.5, Saturation S = (max-min)/(2.0-max-min)

		Round to nearest whole number * 100 for percentage

5. Calculate the Hue H
	If max = Red, Hue H = (G-B)/(max-min)
	If max = Green, Hue H = 2.0 + (B-R)/(max-min)
	If max = Blue, Hue H = 4.0 + (R-G)/(max-min)

	Then, multiply H by 60 to convert it to degrees.
		If the result is negative, add 360 degrees. Round to nearest whole number.

HSL to RGB

1. If there is no saturation it means it's a shade of grey, so we just need to convert the Luminance and set RGB to that level:
	H = 0, S = 0 and L = 40%, we get 0.4*255 so R, G, B = 102

2. If there is saturation, we go ahead:
	If L < 0.5, tmp1 = L * (1.0+S)
	If L >= 0.5, tmp1 = L + S - (L * S)

3. We continue with a second tmp variable tmp2
	tmp2 = 2 * L - tmp1

4. Take the Hue and convert
	H/360

5. We need temp color channel variables, t_r, t_g, t_b
	t_r = H + 0.333
	t_g = H
	t_b = H - 0.333

	If any of these are negative, add 1.
	If any of these are > 1, subtract 1.

6. Do up to 3 tests to select correct formula for each color channel.

	Test1: if t_r * 6 < 1: Red = tmp2 + (tmp1 - tmp2) * 6 * t_r
		If this is larger than 1, do Test2

	Test2: if t_r * 2 < 1: Red = tmp1
		If this is also larger than 1, do Test3

	Test3: If t_r * 3 < 2, Red = tmp2 + (tmp1 - tmp2) * (0.666 - t_r) * 6
		If this is larger than 2, then Red = tmp2

7. Convert to RGB by multiplying by 255 and round to nearest whole number.
"""
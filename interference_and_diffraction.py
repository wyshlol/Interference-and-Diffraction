import math

def average(to_avg: list):
	return sum(to_avg) / len(to_avg)

def cm_to_m(convert: list):
	return_list = []
	for i in convert:
		return_list.append(round(i / 100, 3))
	return return_list

def theta(y: list, L: float):
	return_list = []
	for i in y:
		return_list.append(math.atan(i / L))
	return return_list

def radians_to_degrees(convert: list):
	return_list = []
	for i in convert:
		return_list.append(math.degrees(i))
	return return_list

def slope(maxmin: list, theta: list):
	return_list = []
	for i in range(len(maxmin)):
		if float(theta[i]) != 0.0:
			return_list.append(float(maxmin[i]) / math.sin(theta[i]))
		else:
			return_list.append(0.0)
	return return_list

def wavelength(slit_var: float, slope: list):
	return_list = []
	for i in slope:
		if float(i) != 0.0:
			return_list.append(slit_var / i)
		else:
			return_list.append(0.0)
	return return_list

def m_to_nm(convert: list):
	return_list = []
	for i in convert:
		return_list.append(i * 10e8)
	return return_list


if __name__ == '__main__':

	print('--------- INTERFERENCE AND DIFFRACTION ---------\n')

	# distance to board
	L = 412 / 100 # cm
	err_L = 0.05 / 100 # cm

	# slit width
	a = 0.04 / 1000 # mm
	err_a = 0
	
	# slit seperation
	d = 0.125 / 1000 # mm
	err_d = 0


	print('-- PART 1 --------------------------------------')
	# number of maxima and distance from central maxima
	m = [-2, -1, 1, 2]
	err_m = 0.25
	y = cm_to_m([-4.3, -2.3, 1.7, 3.7]) # cm
	err_y = 0.05 / 100 # cm

	print(f' Maxima Distance:{y}')

	theta_m_rad = theta(y, L)
	theta_m = radians_to_degrees(theta_m_rad)

	max_slope = slope(m, theta_m_rad)
	print(f' Maxima Slope: {average(max_slope):32f}')

	max_wavelength = wavelength(d, max_slope)
	print(f' Maxima Wavelength: {average(m_to_nm(max_wavelength)):27f}')

	print('------------------------------------------------\n')

	print('-- PART 2 --------------------------------------')
	# number of minima and distance from central maxima
	p = [-2, -1, 1, 2]
	err_p = 0.25
	y2 = cm_to_m([-13.3, -7, 6.6, 13.6]) # cm
	err_y2 = 0.05 / 100 # cm

	print(f' Minima Distance: {y2}')

	theta_p_rad = theta(y2, L)
	theta_p = radians_to_degrees(theta_p_rad)

	min_slope = slope(p, theta_p_rad)
	print(f' Minima Slope: {average(min_slope):32f}')

	min_wavelength = wavelength(a, min_slope)
	print(f' Minima Wavelength: {average(m_to_nm(min_wavelength)):27f}')

	print('------------------------------------------------\n')


	print('---------------- ERROR ANALYSIS ----------------')
	err_slope_max = 16
	err_slope_min = 4.8
	
	err_max_wavelength = average(max_wavelength) * math.sqrt((err_slope_max / average(max_slope)) ** 2)
	err_min_wavelength = average(min_wavelength) * math.sqrt((err_slope_min / average(min_slope)) ** 2)
	print(f'Error Max Wavelength: {m_to_nm([err_max_wavelength])[0]:25f}')
	print(f'Error Min Wavelength: {m_to_nm([err_min_wavelength])[0]:25f}')

	print('------------------------------------------------\n')
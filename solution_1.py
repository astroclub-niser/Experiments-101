import numpy as np
import matplotlib.pyplot as plt

#problem 1: Aperture Photometry

np.random.seed(42)

def generate_toy_star():
    image = np.random.normal(loc=200, scale=15, size=(30, 30))
    y, x = np.mgrid[0:30, 0:30]
    distance_sq = (x - 15)**2 + (y - 15)**2
    star_flux = 5000 * np.exp(-distance_sq / 8) 
    
    image += star_flux
    return image, 15, 15 

image, x_c, y_c = generate_toy_star()

#Solution 1: 

# Re-calculating the distance grid for the whole image to use for area definitions
y, x = np.mgrid[0:30, 0:30]
distance_sq = (x - x_c)**2 + (y - y_c)**2

#  Aperture (Star + Sky)
# Circle with radius 5 (5 squared is 25)
aperture_area = distance_sq <= 25
aperture_pixel_list = image[aperture_area]

total_aperture_flux = np.sum(aperture_pixel_list)
total_aperture_pixel_count = len(aperture_pixel_list)

# Annulus (Sky Background)
# Ring starting at radius 7 and ending at 10
annulus_area = (distance_sq > 49) & (distance_sq <= 100)
annulus_pixel_list = image[annulus_area]

background_noise = np.median(annulus_pixel_list)

# Net Star Flux
# Subtracting the total background noise hidden inside aperture
net_star_flux = total_aperture_flux - (background_noise * total_aperture_pixel_count)

m_inst_1 = -2.5 * np.log10(net_star_flux)

# Results

print(f"Total Aperture Flux: {total_aperture_flux:<10.2f}")
print(f"Sky Background noise per pixel : {background_noise:<10.2f}")
print(f"Net Star Flux: {net_star_flux:<10.2f}")
print(f"Instrumental Magnitude (m_inst): {m_inst_1:<10.2f}")


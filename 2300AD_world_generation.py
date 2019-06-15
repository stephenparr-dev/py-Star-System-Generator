# from scipy.interpolate import interp1d


class StarData():
    pass


def main():
    star_name = "Sigma Draconis"
    star_x_coord = 2.5
    star_y_coord = -6.0
    star_z_coord = 17.3
    star_spectral_type = "K0"
    star_size = "V"
    star_magnitude = 5.92
    star_companions = False

    # StarData(star_spectral_type, star_size, star_magnitude, star_companions)

    print("Star Name:           {}".format(star_name))
    print("Star Coordinates:    x={}, y={}, z={}".format(star_x_coord, star_y_coord, star_z_coord))
    print("Star Spectral Type:  {}". format(star_spectral_type))
    print("Star Size:           {}".format(star_size))
    print("Star Magnitude:      {}".format(star_magnitude))
    print("Star Companions?:    {}".format(star_companions))


if __name__ == "__main__":
    main()

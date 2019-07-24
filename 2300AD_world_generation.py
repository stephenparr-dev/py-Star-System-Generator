# from scipy.interpolate import interp1d
import random
import pandas as pd


class Dice:  # Leave this class alone for now. Must be a way of getting it to work simply, but can't see it atm.

    def __init__(self, die):
        self.dice_roll = 0
        self.die = die

    def roll(self):
        j = 1
        die_multiple = int(self.die[0:1])
        die_type = int(self.die[2:5])
        while j < die_multiple + 1:
            die_roll = random.randint(1, die_type)
            self.dice_roll += die_roll
            j += 1


class StarData:

    def __init__(self, star_spectral_class, star_size, star_radius=0, star_mass=0, star_luminosity=0,
                 star_effective_temperature=0):
        self.star_spectral_class = star_spectral_class
        self.star_size = star_size
        self.star_radius = star_radius
        self.star_mass = star_mass
        self.star_luminosity = star_luminosity
        self.star_effective_temperature = star_effective_temperature

    def stellar_radius(self):
        df_rad = pd.read_csv("StellarRadius.csv", ',', index_col=0)
        self.star_radius = df_rad.loc[self.star_spectral_class, self.star_size]

    def stellar_mass(self):
        df_mass = pd.read_csv("StellarMass.csv", ',', index_col=0)
        self.star_mass = df_mass.loc[self.star_spectral_class, self.star_size]

    def stellar_luminosity(self):
        df_lum = pd.read_csv("StellarLuminosity.csv", ',', index_col=0)
        self.star_luminosity = df_lum.loc[self.star_spectral_class, self.star_size]

    def stellar_effective_temperature(self):
        df_et = pd.read_csv("StellarEffectiveTemp.csv", ',', index_col=0)
        self.star_effective_temperature = df_et.loc[self.star_spectral_class, self.star_size]


class OrbitData:

    def __init__(self, star_spectral_class, star_size, star_luminosity, star_radius):
        self.star_spectral_class = star_spectral_class
        self.star_size = star_size
        self.star_luminosity = star_luminosity
        self.star_radius = star_radius
        self.star_spectral_type = self.star_spectral_class[0:1]
        self.max_number_of_orbits_allowable = 0

    def allowable_orbits(self):
        chunks_only = ("A", "B", "O")
        if self.star_size == "VII":
            self.max_number_of_orbits_allowable = 0
        elif self.star_spectral_type in chunks_only:
            number_chunks = random.randint(1, 6)
            chunk_orbits = {}
            i = 1
            while i < number_chunks + 1:
                orbital_radius = random.randint(1, 10) + (random.randint(1, 10) * 0.1)
                chunk_orbits[i] = orbital_radius
                i += 1
        else:
            if self.star_spectral_type == "F":
                self.max_number_of_orbits_allowable = random.randint(1, 10)
            elif self.star_spectral_type == "G":
                self.max_number_of_orbits_allowable = random.randint(3, 18)
            elif self.star_spectral_type == "K":
                self.max_number_of_orbits_allowable = random.randint(2, 12)
            elif self.star_spectral_type == "M":
                self.max_number_of_orbits_allowable = random.randint(1, 6)
            else:
                raise ValueError("Spectral Type {} of this star is not currently covered by this app.".format(
                    self.star_spectral_type))

    def initial_orbit(self):
        innermost_orbit = random.randint(0, 9)
        if innermost_orbit == 0:
            orbit_status = "Empty"
            orbit_radius = random.randint(1, 9) * 0.1
        else:
            orbit_radius = innermost_orbit * 0.1
            if (orbit_radius * 150000000) <= (self.star_radius * 695510):
                orbit_status = "Empty"
            else:
                if self.star_luminosity >= 130 and orbit_radius == 0.1:
                    orbit_status = "Empty"
                elif self.star_luminosity >= 520 and orbit_radius == 0.2:
                    orbit_status = "Empty"
                elif self.star_luminosity >= 1170 and orbit_radius == 0.3:
                    orbit_status = "Empty"
                elif self.star_luminosity >= 2090 and orbit_radius == 0.4:
                    orbit_status = "Empty"
                elif self.star_luminosity >= 3270 and orbit_radius == 0.5:
                    orbit_status = "Empty"
                else:
                    orbit_status = "Populated"
        # Need to add in setting up the dictionaries for the orbit details (status, radius and zone)

    def subsequent_orbits(self):
        pass  # TODO


class WorldData:
    pass  # TODO


class SatelliteData:
    pass  # TODO


class ColonyData:
    pass  # TODO


def main():
    star_name = "Sigma Draconis"
    star_x_coord = 2.5
    star_y_coord = -6.0
    star_z_coord = 17.3
    star_spectral_class = "K0"
    star_size = "V"
    star_magnitude = 5.92
    star_companions = False  # Ignoring companion star systems for now. To come back to later

    star_data = StarData(star_spectral_class, star_size)
    star_radius = star_data.stellar_radius()
    star_mass = star_data.stellar_mass()
    star_luminosity = star_data.stellar_luminosity()
    star_effective_temperature = star_data.stellar_effective_temperature()

    orbit_data = OrbitData(star_spectral_class, star_size, star_luminosity, star_radius)
    max_number_of_orbits_allowable = orbit_data.allowable_orbits()

    print("Star Name:           {}".format(star_name))
    print("Star Coordinates:    x={}, y={}, z={} (ly from sol)".format(star_x_coord, star_y_coord, star_z_coord))
    print("Star Spectral Type:  {}". format(star_spectral_class))
    print("Star Size:           {}".format(star_size))
    print("Star Magnitude:      {} (sols)".format(star_magnitude))
    print("Star Companions?:    {}".format(star_companions))
    print("Star Radius:         {} (sols)".format(star_data.star_radius))
    print("Star Mass:           {} (sols)".format(star_data.star_mass))
    print("Star Luminosity      {} (sols)".format(star_data.star_luminosity))
    print("Star Effective Temp: {} (K)".format(star_data.star_effective_temperature))
    print("Allowable Orbits:    {}".format(orbit_data.max_number_of_orbits_allowable))

    # TODO
    # Update this to write the data to a file, preferably in csv format if possible.
    # Will likely need data converting to a DataFrame before writing it out to the file.
    # Will need some way of indexing it for easy retrieval, possibly by the ID number on the Near Star List,
    # or a variation thereof.


if __name__ == "__main__":
    main()

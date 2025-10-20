from datetime import date
from earthquakes import get_data, get_magnitude

import matplotlib.pyplot as plt


# def get_data():
#     """Retrieve the data we will be working with."""
#     ...


def get_year(earthquake):
    """Extract the year in which an earthquake happened."""
    timestamp = earthquake['properties']['time']
    # The time is given in a strange-looking but commonly-used format.
    # To understand it, we can look at the documentation of the source data:
    # https://earthquake.usgs.gov/data/comcat/index.php#time
    # Fortunately, Python provides a way of interpreting this timestamp:
    # (Question for discussion: Why do we divide by 1000?)
    year = date.fromtimestamp(timestamp/1000).year
    return year


# def get_magnitude(earthquake):
#     """Retrive the magnitude of an earthquake item."""
#     ...


# This is function you may want to create to break down the computations,
# although it is not necessary. You may also change it to something different.
def get_magnitudes_per_year(earthquakes):
    """Retrieve the magnitudes of all the earthquakes in a given year.
    
    Returns a dictionary with years as keys, and lists of magnitudes as values.
    """
    magnitudes_per_year = {}  
    
    for eq in earthquakes:
        year = get_year(eq)
        magnitude = get_magnitude(eq)
        
        if year not in magnitudes_per_year:
            magnitudes_per_year[year] = []
        magnitudes_per_year[year].append(magnitude)

    return magnitudes_per_year

def plot_average_magnitude_per_year(earthquakes):
    """Plot the average magnitude of earthquakes per year."""
    magnitudes_per_year = get_magnitudes_per_year(earthquakes)
    years = []
    average_magnitudes = []
    
    for year in sorted(magnitudes_per_year.keys()):
        years.append(year)
        magnitudes = magnitudes_per_year[year]
        average_magnitude = sum(magnitudes) / len(magnitudes)
        average_magnitudes.append(average_magnitude)
    
    plt.plot(years, average_magnitudes)
    plt.xlabel("Year")
    plt.ylabel("Average Magnitude")
    plt.title("Average Earthquake Magnitude per Year")
    plt.show()


def plot_number_per_year(earthquakes):
    """Plot the number of earthquakes per year."""
    magnitudes_per_year = get_magnitudes_per_year(earthquakes)
    years = []
    num_earthquakes = []

    for year in sorted(magnitudes_per_year.keys()):
        years.append(year)
        num_earthquakes.append(len(magnitudes_per_year[year]))

    plt.bar(years, num_earthquakes)
    plt.xlabel("Year")
    plt.ylabel("Number of Earthquakes")
    plt.title("Number of Earthquakes per Year")
    plt.show()



# # Get the data we will work with
# quakes = get_data()['features']

# # Plot the results - this is not perfect since the x axis is shown as real
# # numbers rather than integers, which is what we would prefer!
# plot_number_per_year(quakes)
# plt.clf()  # This clears the figure, so that we don't overlay the two plots
# plot_average_magnitude_per_year(quakes)

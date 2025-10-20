from datetime import date
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from earthquakes import get_data, get_magnitude


def get_year(earthquake):
    """Extract the year in which an earthquake happened.
    
    Args:
        earthquake: Dictionary containing earthquake data with timestamp
        
    Returns:
        int: Year when the earthquake occurred
    """
    timestamp = earthquake['properties']['time']
    # The time is given in milliseconds since Unix epoch.
    # Python's fromtimestamp expects seconds, so we divide by 1000.
    # See: https://earthquake.usgs.gov/data/comcat/index.php#time
    year = date.fromtimestamp(timestamp / 1000).year
    return year


def get_magnitudes_per_year(earthquakes):
    """Retrieve the magnitudes of all earthquakes grouped by year.
    
    Args:
        earthquakes: List of earthquake dictionaries
        
    Returns:
        dict: Dictionary with years as keys and lists of magnitudes as values
              Example: {2020: [5.2, 4.8, 6.1], 2021: [5.5, 4.9]}
    """
    # Initialize dictionary outside the loop to accumulate all data
    magnitudes_per_year = defaultdict(list)
    
    for eq in earthquakes:
        year = get_year(eq)
        magnitude = get_magnitude(eq)
        magnitudes_per_year[year].append(magnitude)
    
    # Convert defaultdict back to regular dict for clarity
    return dict(magnitudes_per_year)


def plot_average_magnitude_per_year(earthquakes):
    """Plot the average magnitude of earthquakes per year.
    
    Args:
        earthquakes: List of earthquake dictionaries
    """
    magnitudes_per_year = get_magnitudes_per_year(earthquakes)
    
    # Sort by year and extract data
    sorted_data = sorted(magnitudes_per_year.items())
    years = [year for year, _ in sorted_data]
    average_magnitudes = [np.mean(mags) for _, mags in sorted_data]
    
    # Create plot
    plt.figure(figsize=(10, 5))
    plt.plot(years, average_magnitudes, marker='o', linewidth=2, 
             color='orangered', markersize=6)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Average Magnitude", fontsize=12)
    plt.title("Average Earthquake Magnitude per Year", fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Force x-axis to show only integer years
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    plt.tight_layout()
    plt.show()


def plot_number_per_year(earthquakes):
    """Plot the number of earthquakes per year as a bar chart.
    
    Args:
        earthquakes: List of earthquake dictionaries
    """
    magnitudes_per_year = get_magnitudes_per_year(earthquakes)
    
    # Sort by year and count earthquakes
    sorted_data = sorted(magnitudes_per_year.items())
    years = [year for year, _ in sorted_data]
    num_earthquakes = [len(mags) for _, mags in sorted_data]
    
    # Create bar plot
    plt.figure(figsize=(10, 5))
    plt.bar(years, num_earthquakes, color='steelblue', alpha=0.7, edgecolor='black')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Number of Earthquakes", fontsize=12)
    plt.title("Number of Earthquakes per Year", fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Force x-axis to show only integer years
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    plt.tight_layout()
    plt.show()


def plot_earthquake_analysis(earthquakes):
    """Generate both earthquake analysis plots side by side.
    
    This function creates a combined visualization showing both the number
    of earthquakes and average magnitude per year in a single figure.
    
    Args:
        earthquakes: List of earthquake dictionaries
    """
    # Calculate once to avoid redundant computation
    magnitudes_per_year = get_magnitudes_per_year(earthquakes)
    
    sorted_data = sorted(magnitudes_per_year.items())
    years = [year for year, _ in sorted_data]
    num_earthquakes = [len(mags) for _, mags in sorted_data]
    avg_magnitudes = [np.mean(mags) for _, mags in sorted_data]
    
    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left plot: Number of earthquakes
    ax1.bar(years, num_earthquakes, color='steelblue', alpha=0.7, edgecolor='black')
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Number of Earthquakes", fontsize=12)
    ax1.set_title("Number of Earthquakes per Year", fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    # Right plot: Average magnitude
    ax2.plot(years, avg_magnitudes, marker='o', color='orangered', 
             linewidth=2, markersize=6)
    ax2.set_xlabel("Year", fontsize=12)
    ax2.set_ylabel("Average Magnitude", fontsize=12)
    ax2.set_title("Average Earthquake Magnitude per Year", fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    plt.tight_layout()
    plt.show()


# # Main execution
# if __name__ == "__main__":
#     # Get the earthquake data
#     quakes = get_data()['features']
    
#     # Option 1: Plot separately (original approach)
#     plot_number_per_year(quakes)
#     # plt.clf()  # Clear figure if you want to avoid overlap
#     plot_average_magnitude_per_year(quakes)
    
#     # Option 2: Plot side by side (recommended - more efficient)
#     # plot_earthquake_analysis(quakes)


# # Get the data we will work with
# quakes = get_data()['features']

# # Plot the results - this is not perfect since the x axis is shown as real
# # numbers rather than integers, which is what we would prefer!
# plot_number_per_year(quakes)
# plt.clf()  # This clears the figure, so that we don't overlay the two plots
# plot_average_magnitude_per_year(quakes)

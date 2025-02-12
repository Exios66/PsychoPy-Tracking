import matplotlib.pyplot as plt
import seaborn as sns

def plot_fixation_heatmap(df):
    """Generate heatmap of fixations."""
    sns.kdeplot(df['x'], df['y'], cmap='coolwarm', shade=True)
    plt.show()

def plot_velocity(df):
    """Plot eye movement velocity over time."""
    plt.figure(figsize=(10,4))
    plt.plot(df['timestamp'], df['velocity'], label='Velocity')
    plt.legend()
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic_bspline_pdf():
    """
    Plots the cardinal quadratic B-spline B_i^2(x) for t_i = i.
    This spline is non-zero on the support [i-1, i+2].
    We plot the "mother" spline B_0^2(x) on its support [-1, 2] (by setting i=0).
    """
    
    # We set i=0 for a concrete plot. The shape is the same for any i.
    i = 0
    
    # Define the piecewise intervals relative to i
    # x \in [i-1, i]
    x1 = np.linspace(i - 1, i, 100)
    # x \in [i, i+1]
    x2 = np.linspace(i, i + 1, 100)
    # x \in [i+1, i+2]
    x3 = np.linspace(i + 1, i + 2, 100)

    # Define the piecewise functions based on the derivation
    # S(x) = (x - i + 1)^2 / 2
    y1 = 0.5 * (x1 - i + 1)**2
    # S(x) = -(x-i)^2 + (x-i) + 0.5
    y2 = -(x2 - i)**2 + (x2 - i) + 0.5
    # S(x) = (i + 2 - x)^2 / 2
    y3 = 0.5 * (i + 2 - x3)**2

    # Create the plot
    plt.figure(figsize=(8, 6))
    
    # Plot the pieces
    plt.plot(x1, y1, 'b-', label=r'$B_i^2(x)$ (for $i=0$)')
    plt.plot(x2, y2, 'b-')
    plt.plot(x3, y3, 'b-')

    # Add labels and title
    plt.title(r'Quadratic B-spline $B_i^2(x)$ for $t_i = i$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$B_i^2(x)$')
    
    # Define ticks and labels relative to i
    knots = [i-1, i, i+1, i+2]
    labels = [r'$i-1$', r'$i$', r'$i+1$', r'$i+2$']
    plt.xticks(knots, labels)
    plt.yticks(np.arange(0, 1.0, 0.25))
    
    # Add key points
    plt.plot([i, i+1, i+0.5], [0.5, 0.5, 0.75], 'ro', markersize=5) # Knots and peak
    plt.text(i, 0.5, r' $(i, 0.5)$', verticalalignment='bottom')
    plt.text(i+1, 0.5, r' $(i+1, 0.5)$', verticalalignment='bottom')
    plt.text(i+0.5, 0.75, r' $(i+0.5, 0.75)$', horizontalalignment='center', verticalalignment='bottom')

    # Add grid and legend
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(i-1, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(i, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(i+1, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(i+2, color='gray', linestyle='--', linewidth=0.5)
    plt.ylim(-0.1, 0.9)

    # Save the figure as a PDF
    plt.savefig('B_spline_plot.pdf', format='pdf', bbox_inches='tight')
    print("Saved plot to B_spline_plot.pdf")

if __name__ == "__main__":
    plot_quadratic_bspline_pdf()
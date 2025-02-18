# Test Case 1: Basic Line Plot
fgmk2(1, [1, 2, 3, 4], [1, 4, 9, 16], 'X', 'Y', 'Basic Line Plot', splots=1, lst='-', c='tab:blue', ptype="plot")

# Test Case 2: Multiple Stem Plots
fgmk2(2, [1, 2, 3], [2, 4, 8], 'X', 'Y1', 'First Stem Plot', 
      [1, 2, 3], [1, 2, 3], 'Y2', 'X2', 'Second Stem Plot', '--', 'tab:green', 
      splots=2, ptype="stem")

# Test Case 3: Histogram with Confidence Intervals and Average
data = np.random.randn(1000)
fgmk2(3, data, 20, 'Values', 'Frequency', 'Histogram with Conf Intervals and Avg', 
      splots=1, conf_intervals=[-1, 1], average=True, bell_curve=False, ptype="hist")

# Test Case 4: Histogram with Bell Curve and x-axis Limit
fgmk2(4, data, 30, 'Values', 'Frequency', 'Histogram with Bell Curve', 
      splots=1, bell_curve=True, xmax=3, ptype="hist")

# Test Case 5: Mixed Plot Types (Histogram and Line Plot)
fgmk2(5, data, 30, 'Values', 'Frequency', 'Histogram', 
      [1, 2, 3, 4], [1, 4, 9, 16], 'X', 'Y', 'Line Plot', '-', 'tab:orange',
      splots=2, ptype="hist")

# Test Case 6: Multiple Histograms with Average and Bell Curve
data2 = np.random.randn(500)
fgmk2(6, data, 30, 'X', 'Y', 'Histogram 1', 
      data2, 20, 'X2', 'Y2', 'Histogram 2', '--', 'tab:green', 
      splots=2, average=True, bell_curve=True, ptype="hist")

# Test Case 7: Stem Plot with Custom Mark Values and Labels
fgmk2(7, [1, 2, 3, 4], [1, 4, 9, 16], 'X', 'Y', 'Custom Stem Plot', 
      splots=1, mark_values=[1, 2, 3], mark_labels=['One', 'Two', 'Three'], ptype="stem")

# Test Case 8: Stem Plot with Custom Dimensions and No Grid
fgmk2(8, [1, 2, 3, 4], [1, 4, 9, 16], 'X', 'Y', 'No Grid Stem Plot', 
      splots=1, grid=False, dim=(12, 6), ptype="stem")

# Test Case 9: Line Plot with Different Colors and Line Styles
fgmk2(9, [1, 2, 3, 4], [1, 4, 9, 16], 'X', 'Y', 'Line Plot', 
      [1, 2, 3, 4], [2, 3, 6, 12], 'X2', 'Y2', 'Line Plot 2',
      splots=2, ptype="plot")

# Test Case 10: Stem Plot with Large Number of Subplots
fgmk2(10, [1, 2, 3], [1, 4, 9], 'X', 'Y1', 'Plot 1', 
       [1, 2, 3], [2, 6, 12], 'X2', 'Y2', 'Plot 2',
       [1, 2, 3], [3, 9, 15], 'X3', 'Y3', 'Plot 3',
       [1, 2, 3], [4, 12, 18], 'X4', 'Y4', 'Plot 4',
       splots=4, ptype="stem")

# Test Case 11: Histogram with Custom Confidence Intervals, Average, and x Limit
fgmk2(11, data, 20, 'X', 'Y', 'Histogram Custom CI, Avg, xLimit', 
      splots=1, conf_intervals=[-1, 1, 2], average=True, xmax=2, ptype="hist")

# Test Case 12: Quadratic Line Plot - Subplot 1
fgmk2(12, np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)**2, 'X', 'Y', 'Quadratic Plot 1', 
      np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)**3, 'X', 'Y', 'Cubic Plot', 
      splots=2, grid=False, ptype="plot")

# Test Case 13: Multiple Quadratic Plots in Subplots
fgmk2(13, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X1', 'Y1', 'Quadratic Plot 1',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2 + 10, 'X3', 'Y3', 'Shifted Quadratic',
      np.linspace(-5, 5, 100), -np.linspace(-5, 5, 100)**2, 'X2', 'Y2', 'Quadratic Plot 2',
      splots=2, grid=False, ptype="plot")

# Test Case 15: Quadratic with Multiple Line Styles in Subplots
fgmk2(14, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X1', 'Y1', 'Quadratic Plot - Solid',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2 + 10, 'X3', 'Y3', 'Quadratic Plot - Dashed',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X2', 'Y2', 'Quadratic Plot - Dotted',
      splots=3, grid=False, ptype="plot")

# Test Case 13: Updated to use individual line styles and colors
fgmk2(16, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X1', 'Y1', 'Quadratic Plot 1',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2 + 10, 'X3', 'Y3', 'Shifted Quadratic',
      np.linspace(-5, 5, 100), -np.linspace(-5, 5, 100)**2, 'X2', 'Y2', 'Quadratic Plot 2',
      splots=3, grid=False, ptype="plot", c1="tab:orange", lst2="--",c3="red")

# Test Case 15: Quadratic with multiple line styles in subplots
fgmk2(15, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X1', 'Y1', 'Quadratic Plot - Solid',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2 + 10, 'X3', 'Y3', 'Quadratic Plot - Dashed',
      np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)**2, 'X2', 'Y2', 'Quadratic Plot - Dotted',
      splots=3, grid=False, ptype="plot")

# Example usage:
fgmk2(16, np.random.randn(1000), 20, 'Values', 'Frequency', 'Histogram with Options',
      splots=1, mark_values=[-5, 0, 5], mark_labels=['-5', '0', '5'], dim=(10, 6), ptype="hist",
      conf_intervals=[-1, 1], average=True, bell_curve=True, xmax=3)
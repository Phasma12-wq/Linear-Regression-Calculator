# Linear Regression Calculator


<!-- Table of Contents -->
<details>
<summary><strong>📑 Table of Contents</strong></summary>

- [1. Purpose](#1-purpose)
- [2. Functions](#2-functions)
- [3. Program Output](#3-program-output)
- [4. Additional Information](#4-additional-information)
- [5. Installation](#1-installation)

</details>

## [1. Purpose of Each Part](#1-purpose)

### Part 1: [Data Loading & Display](#part-1-data-loading-display)
- **Reads CSV data** - Loads x and y values from `data.csv` into a pandas DataFrame
- **Prints original data** - Shows the raw x and y arrays so you can verify the input

### Part 2: [Manual Mathematical Calculations](#part-2-manual-mathematical-calculations)
- **Calculates sums** - Computes `sum_x`, `sum_y`, `sum_xy`, `sum_x2`, and `sum_y2`
- **Builds intermediate arrays** - Uses helper functions to calculate products and squares
- **Why manual?** - The program demonstrates how linear regression works from scratch, without using built-in numpy functions like `np.polyfit()`

### Part 3: [Regression Coefficients](#part-3-regression-coefficients)
- **Calculates b0 (y-intercept)** - The starting point of the line when x = 0
- **Calculates b1 (slope)** - How much y changes for each unit increase in x
- **Formula used** - Standard least squares regression formulas

### Part 4: [Predictions](#part-4-predictions)
- **Single value prediction** - Calculates f(252) to show how to use the equation
- **Range predictions** - Generates predictions for x = 0 to 100 to demonstrate the full linear relationship

### Part 5: [Visualization](#part-5-visualization)
- **Plots data points** - Shows blue circles for actual data
- **Plots regression line** - Draws the best-fit line using the calculated b0 and b1
- **Opens graph window** - Lets you visually verify the fit quality

---

## [2. Functions for b0 and b1](#2-functions)

### `calc_b0(sum_x, sum_y, sum_x2, sum_xy, row_count)` <!-- -->
**Purpose:** Calculate the y-intercept of the regression line

**Formula:**
```
b0 = ((sum_y * sum_x2) - (sum_x * sum_xy)) / ((row_count * sum_x2) - (sum_x * sum_x))
```

**What it returns:** The y-intercept value rounded to 4 decimal places

**Real output from the program:**
```
b0:  32.783
```

**In plain English:** This is where the regression line crosses the y-axis. If x = 0, then y = 32.783.

---

### `calc_b1(sum_x, sum_y, sum_x2, sum_xy, row_count)` <!-- -->
**Purpose:** Calculate the slope of the regression line

**Formula:**
```
b1 = ((row_count * sum_xy) - (sum_x * sum_y)) / ((row_count * sum_x2) - (sum_x * sum_x))
```

**What it returns:** The slope value rounded to 4 decimal places

**Real output from the program:**
```
b1:  0.2001
```

**In plain English:** This is the rate of change. For every 1 unit increase in x, y increases by 0.2001 units.

---

### The Complete Linear Equation
**From the program output:**
```
function: f(x) =  32.783  +  0.2001 x
```

**To use this equation:**
- To find y when x = 50: y = 32.783 + 0.2001 × 50 = 42.788
- To find y when x = 100: y = 32.783 + 0.2001 × 100 = 52.793

---

## [3. Program Output](#3-program-output)

### What You See When You Run the Program

```bash
$ cd /home/phasma/Documents/Projects/Python/pandas
test.py
```

### 1. [Original Data Display](#1-original-data-display)
```
[140 155 159 179 192 200 212] 
[60 62 67 70 71 72 75] 
```

**What this means:** The program loaded 7 data points where:
- x values range from 140 to 212
- y values range from 60 to 75

### 2. [Summation Results](#2-summation-results)
```
Sum of x:  1237 
Sum of y:  477 
Sum of x*y:  85125 
Sum of x^2:  222755 
Sum of y^2:  32683 
```

**Why these matter:** These are the building blocks for calculating b0 and b1. The program shows them to demonstrate the mathematical process.

### 3. [Regression Coefficients](#3-regression-coefficients)
```
b0:  32.783 
b1:  0.2001 
```

**Interpretation:**
- **b0 = 32.783** - The line starts at y = 32.783 when x = 0
- **b1 = 0.2001** - For every 1 unit increase in x, y increases by 0.2001

### 4. [The Regression Equation](#4-the-regression-equation)
```
function: f(x) =  32.783  +  0.2001 x
```

**This is your answer!** The program has found the best-fit straight line through your data.

### 5. [Single Prediction Example](#5-single-prediction-example)
```
f(252) =  33.783500000000004
```

**What this means:** If you plug in x = 252 into the equation, the predicted y value is approximately 33.78.

### 6. [Range of Predictions (x = 0 to 100)](#6-range-of-predictions-x-0-to-100)
```
0   32.783
1   32.9831
2   33.1832
3   33.3833
4   33.583400000000005
...
50   42.788000000000004
...
100   52.793000000000006
```

**What this shows:** The program generates 101 predictions (from x=0 to x=100). Each line shows:
- The x value (left side)
- The predicted y value (right side)

**Pattern you can see:** y increases by exactly 0.2001 for each 1 unit increase in x, which matches the slope (b1).

### 7. [The Graph (Visual Output)](#7-the-graph-visual-output)

A window opens showing:
- **Blue circles (•)** = your 7 actual data points
- **Red line** = the regression line calculated from b0 and b1

**What to look for:**
- If the line passes through or near most points, the fit is good
- If the line misses many points, your data may not be perfectly linear
- The graph is your visual verification that the math makes sense

---

## [4. Additional Information](#4-additional-information)

### What is Linear Regression?
Linear regression finds the straight line that best fits a set of data points. It's used to:
- Predict future values based on known relationships
- Understand how two variables are related
- Simplify complex data into a simple mathematical formula

### Quick Reference for the Math

| Symbol | Name | Value | Meaning |
|--------|------|-------|--------|
| b0 | y-intercept | 32.783 | Starting point when x = 0 |
| b1 | slope | 0.2001 | Rate of change per x unit |
| f(x) | equation | 32.783 + 0.2001x | The regression formula |
| x | input | 0-100 (in range output) | Independent variable |
| y | output | varies | Dependent variable |

### Why Manual Calculation?
You might wonder why the program doesn't just use `np.polyfit()`. The answer:
- **Educational value** - Shows you understand the underlying math
- **Transparency** - Makes the algorithm visible and traceable
- **Learning tool** - Great for understanding statistics and data science concepts

---

## Summary

This program takes raw data, calculates the regression line manually, and shows you everything from raw sums to final predictions. It's a complete, working example of how linear regression works - perfect for understanding, testing, or demonstrating data analysis skills.

**Run it:** `test.py`  
**See:** Real math, real predictions, real graph  
**Learn:** Linear regression from data to equation

---

## [5. Installation & Quick Start](#1-installation)

### Prerequisites
- Python 3.7 or higher

### Create a Virtual Environment (Recommended)
Using a virtual environment keeps dependencies isolated and prevents conflicts with your system Python.

**Create and activate the virtual environment:**

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your command prompt when activated.

### Install Dependencies
With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This installs pandas, matplotlib, and numpy from the requirements file.

### Run the Program
1. Make sure your virtual environment is still activated (you should see `(venv)` in your prompt)
2. Make sure you have a `data.csv` file in the same directory
3. Navigate to the project folder:
4. Run the program:
   ```bash
   python test.py
   ```
5. A graph window will open showing your data points and the regression line

**To deactivate the virtual environment when done:**
```bash
deactivate
```
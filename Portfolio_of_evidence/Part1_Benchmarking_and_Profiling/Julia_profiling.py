# julia_profiling.py

import time

try:
    profile  # If kernprof is running, this will be defined
except NameError:
    def profile(func):
        return func  # Returns the same function if @profile is not defined

# Global constants for Julia set calculation
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193

# Function to generate the zs and cs values for the Julia set
def generate_zs_cs(width, x1, x2, y1, y2, c_real, c_imag):
    x_step = (float(x2) - float(x1)) / width
    y_step = (float(y1) - float(y2)) / width
    zs = []
    cs = []
    for ycoord in range(width):
        for xcoord in range(width):
            zs.append(complex(x1 + xcoord * x_step, y1 - ycoord * y_step))
            cs.append(complex(c_real, c_imag))
    return zs, cs

@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule."""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

# Main block to run the function if the script is executed directly
if __name__ == "__main__":
    desired_width = 1000
    max_iterations = 300
    zs, cs = generate_zs_cs(desired_width, x1, x2, y1, y2, c_real, c_imag)
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    print(f"Calculated {len(output)} points of the Julia set")

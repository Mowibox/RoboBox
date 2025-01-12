import numpy as np
import matplotlib.pyplot as plt

def reverse_rest_to_rest_motion(total_time, acceleration_value, speed_value, acceleration_time, initial_position, final_position):
    """
    This function simulates the motion profile of an object going from rest to rest in the reverse direction.
    
    Parameters:
    - total_time: Total time of the motion profile (in seconds).
    - acceleration_value: Magnitude of acceleration during the acceleration and deceleration phases (in units of distance/time^2).
    - speed_value: Constant speed during the coasting phase (in units of distance/time).
    - acceleration_time: Time duration of the acceleration and deceleration phases (in seconds).
    - initial_position: Initial position of the object.
    - final_position: Final position of the object.

    Outputs:
    - Plot of position vs time
    - Plot of velocity vs time
    - Plot of acceleration vs time
    """
    
    # Reverse acceleration and speed values for motion in the opposite direction
    acceleration_value = -acceleration_value
    speed_value = -speed_value
    
    # Calculate coast time
    coast_time = total_time - 2 * acceleration_time
    
    # Time vectors
    t1 = np.linspace(0, acceleration_time, 100)
    t2 = np.linspace(acceleration_time, acceleration_time + coast_time, 100)
    t3 = np.linspace(acceleration_time + coast_time, total_time, 100)
    time = np.concatenate([t1, t2, t3])
    
    # Acceleration profile
    a1 = np.ones_like(t1) * acceleration_value
    a2 = np.zeros_like(t2)
    a3 = np.ones_like(t3) * -acceleration_value
    acceleration = np.concatenate([a1, a2, a3])
    
    # Velocity profile
    v1 = np.cumsum(a1) * (t1[1] - t1[0])  # Cumulative sum to simulate integration
    v2 = np.ones_like(t2) * speed_value
    v3 = np.cumsum(a3) * (t3[1] - t3[0]) + v2[-1]
    velocity = np.concatenate([v1, v2, v3])
    
    # Position profile (updated integration with initial and final positions)
    x1 = initial_position + np.cumsum(v1) * (t1[1] - t1[0])  # Cumulative sum to simulate integration
    x2 = np.cumsum(v2) * (t2[1] - t2[0]) + x1[-1]
    x3 = np.cumsum(v3) * (t3[1] - t3[0]) + x2[-1] + final_position
    position = np.concatenate([x1, x2, x3])
    
    # Plotting the profiles
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))

    # Plot position vs time
    axs[0].plot(time, position, 'b.-')
    axs[0].set_title('Position vs Time')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Position')

    # Plot velocity vs time
    axs[1].plot(time, velocity, 'g.-')
    axs[1].set_title('Velocity vs Time')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Velocity')

    # Plot acceleration vs time
    axs[2].plot(time, acceleration, 'r.-')
    axs[2].set_title('Acceleration vs Time')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Acceleration')

    plt.tight_layout()
    plt.show()

# Example of usage
total_time = 10  # Total time for the motion (seconds)
acceleration_value = 2.0  # Acceleration magnitude (units of distance/time^2)
speed_value = 5.0  # Constant speed during the coast phase (units of distance/time)
acceleration_time = 2  # Time for acceleration phase (seconds)
initial_position = 10.0  # Initial position (units of distance)
final_position = 0.0  # Final position (units of distance)

reverse_rest_to_rest_motion(total_time, acceleration_value, speed_value, acceleration_time, initial_position, final_position)

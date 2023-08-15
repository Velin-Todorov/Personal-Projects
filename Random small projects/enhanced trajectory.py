from matplotlib import pyplot as plt
import math


def graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def frange(start, final, increment):
    nums = []
    while start < final:
        nums.append(start)
        start += increment

    return nums


def draw_trajectory(u, theta, flight):
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2 * u * math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u * math.sin(theta) * t - 0.5*g*t*t)

    graph(x, y)


if __name__ == '__main__':
    try:
        trajectories = int(input())
        velocity = []
        angles = []
        time_of_flight = []
        for i in range(1, trajectories + 1):
            u1 = float(input(f'Enter velocity for {i}: '))
            theta1 = math.radians(float(input(f'Angle of projection for {i}: ')))

            velocity.append(u1)
            angles.append(theta1)

        for i in range(trajectories):
            t_flight = 2 * velocity[i] * math.sin(angles[i]) / 9.8
            S_x = velocity[i] * math.cos(angles[i])*t_flight
            S_y = velocity[i] * math.sin(angles[i]) * (t_flight/2) - (1/2) * 9.8 * (t_flight / 2) ** 2
            print('Initial velocity: {0}  Angle of projection: {1}'.format(velocity[i], math.degrees(angles[i])))
            print('T: {0} S_x {1} S_y: {2}'.format(t_flight, S_x, S_y))
            print()
            draw_trajectory(velocity[i], angles[i], t_flight)

    except ValueError:
        print('You entered an invalid input')

    else:
        pass
        plt.show()



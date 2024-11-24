#!/usr/bin/python3
import math

# The math for this is 
# solar declination = 23.44º * sin((360/365)*(days + 10))

# Ultimate goal is to work this out so that I can calculate out the latitude and figure out
# the height of the shadow on various known objects.  Such as the Washington Monument.

def main():
    # Create a day of the calendar for each year
    days = [i + 1 for i in range(365)]

    # Going to create a list that will cover the following:
    # (360/365) * (n + 10) n is equal to the days in the list
    step_one = list()
    for i in days:
        a = (360/365) * (i + 10)
        step_one.append(a)

    # Going to take the sine of the step one
    step_two = list()
    for i in step_one:
        i = math.radians(i)
        b = math.sin(i)
        step_two.append(b)

    # Going to multiply step two by 23.44º
    # So it is going to look like 23.44 * b
    step_three = list()
    for i in step_two:
        c  = 23.44 * i
        step_three.append(c)

    # Finally, output.
    # print to screen in CSV format or output to file.
    # I am going to output to file.
    output = list(zip(days, step_three))
    f = open('declination.csv', 'w')
    f.write('Day,Declination\n')
    for i in output:
        out_string = str(i[0]) + ',' + str(i[1]) + '\n'
        f.write(out_string)

    f.close()
    print('Completed!')


if __name__ == '__main__':
    main()
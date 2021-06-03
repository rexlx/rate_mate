#!/usr/bin/python
import sys, argparse

def msg():
    """
    this function replaces the default usage message for argparser
    as it is misleading in this case
    """
    return """requires three args
    $ ./rate_mate.py START STOP STEP [-p] [-h]
    """

def get_args():
    """
    this function collects three mandatory postional args and one
    optional.
    """
    # create an instance of ArgumentParser named parser
    parser = argparse.ArgumentParser(usage=msg())
    # add the three mandatory positional args
    parser.add_argument("start", type=float, help="start rate")
    parser.add_argument("stop", type=float, help="final rate")
    parser.add_argument("step", type=float,
                        help="what to increase the rate by")
    # add this optional percent flag
    parser.add_argument('-p', '--percent', help="step is a percentage",
                        action="store_true")
    # parse it
    args = parser.parse_args()
    # store the values to be returned
    start = args.start
    stop = args.stop
    step = args.step
    # integer step is preferred
    step_is_percent = False
    # if you add the -p flag
    if args.percent:
        # then you will increase the rate by percent
        step_is_percent = True
    return start, stop, step, step_is_percent

def xml_entry(phase, rate):
    """
    creates the xml required for tsung (goes between the load tags)
    requires phase and rate parameters
    """
    entry = """  <arrivalphase phase="{PHASE}" duration="10" unit="minute">
    <users interarrival="{RATE}" unit="second"></users>
  </arrivalphase>"""
    line = entry.format(PHASE=phase, RATE=rate)
    return line

def integer_step(_start, _end, _step):
    """
    this is the default method for increasing the rate
    requires the start stop and step rate values as parameters
    """
    # args are taken in as floats, convert them to integers
    start, end, step = int(_start), int(_end), int(_step)
    # phases start at 1
    phase = 1
    for i in range(start, end, step):
        # convert number to rate value, round float to 4 places
        rate =  format(i ** -1, '.4f')
        # plug in the phase and rate to the xml_entry function
        rate_line = xml_entry(phase, rate)
        print(rate_line)
        phase += 1

def percent_step(start, end, step):
    """
    this is called when the -p flag is added, functions closely
    to integer_step
    """
    # create vals list for values
    vals = []
    # while the start rate is less than or equal to the final rate
    while start <= end:
        # add the number to the vals list
        vals.append(start)
        # get the next step as a fraction of the starting number
        x = start * step
        # the next starting number is that fraction + the last number
        # round that number to 2 places
        start = float(format(x + start, '.2f'))
    # if the final rate isn't in the list, add it
    if max(vals) < end:
        vals.append(end)
    phase = 1
    # this is the same as it is in integer_step
    for i in vals:
        rate =  format(i ** -1, '.4f')
        rate_line = xml_entry(phase, rate)
        print(rate_line)
        phase += 1

def main():
    """
    this is where is all happens
    """
    # get the args
    start, stop, step, step_is_percent = get_args()
    # if step_is_percent is True (see get_args)
    if step_is_percent:
        # increment rate by a percent
        percent_step(start, stop, step)
    else:
        # otherwise use the preferred method, by integer
        integer_step(start, stop, step)


# if the script is being ran as itself (not called in from another script)
if __name__ == '__main__':
    # do the dang thang
    main()

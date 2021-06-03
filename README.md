# rate_mate
create the xml needed for some basic html testing with tsung

```bash
rexfitzhugh scripts $ python rate_mate.py 25 50 5
  <arrivalphase phase="1" duration="10" unit="minute">
    <users interarrival="0.0400" unit="second"></users>
  </arrivalphase>
  <arrivalphase phase="2" duration="10" unit="minute">
    <users interarrival="0.0333" unit="second"></users>
  </arrivalphase>
  <arrivalphase phase="3" duration="10" unit="minute">
    <users interarrival="0.0286" unit="second"></users>
  </arrivalphase>
  <arrivalphase phase="4" duration="10" unit="minute">
    <users interarrival="0.0250" unit="second"></users>
  </arrivalphase>
  <arrivalphase phase="5" duration="10" unit="minute">
    <users interarrival="0.0222" unit="second"></users>
  </arrivalphase>
rexfitzhugh scripts $ python rate_mate.py -h
usage: requires three args
    $ ./rate_mate.py START STOP STEP [-p] [-h]
    

positional arguments:
  start          start rate
  stop           final rate
  step           what to increase the rate by

optional arguments:
  -h, --help     show this help message and exit
  -p, --percent  step is a percentage
  ```

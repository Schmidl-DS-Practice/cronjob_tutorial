### CRON JOB INFO
# order:
    minute |   hour    |   day(month)  |   month   |   day(week)
# minute:
    *  any value
    , value list separator
    - range of values
    / step values
    0-59 allowed values

# hour:
    *  any value
    , value list separator
    - range of values
    / step values
    0-23 allowed values

# day(month):
    * any value
    , value list separator
    - range of values
    / step values
    1-31 allowed values

# month:
    * any value
    , value list separator
    - range of values
    / step values
    1-12 allowed values
    JAN - DEC alternative single values

# day(week):
    * any value
    , value list separator
    - range of values
    / step values
    0-6 allowed values
    SUN - SAT alternative single values
    7 sunday (non-standard)
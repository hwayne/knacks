## Friendlist

During the Pandemic I wanted a system to regularly catch up with friends. "Friendlist" would run once a day and give me a list of friends to contact, weighted by how often I wanted to talk to them. Close friends I'd reach out every 2-3 days, more distant friends I still liked talking to would be 14 days to 2 months.

The first version was written in J, because I like J, and is `friendlist.ijs`. This is how I learned that J is very, *very* bad for batch jobs:

1. There's no public documentation on running a script from the command line.
2. When you *do* figure out how to run a script from the command line, you discover that any errors at all drop you into the REPL, so you have to exit out of the script manually.
3. The RNG uses a fixed seed, so every run will give you the same random picks.
4. Dealing with file paths is a morass of sadness.

So I then switched it over to python! I also used this as a chance to get more experience with TkInter GUIs. IMO lots of knacks would benefit from GUIs.

In the end, I only used this for a few weeks. After that I found a better way to keep in touch with friends: scheduling a time to find a time to chat. Like every three weeks we text back and forth to find a time to next talk on the phone. No knack yet to manage that, though!

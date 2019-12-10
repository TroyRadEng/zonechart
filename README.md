# zonechart

The Zone Chart Assigner assigns roommates to chores within the house by dividing the house into zones and assigning them to the roommates. The assignments are refreshed on regular intervals (probably weekly).  The Assigner works by keeping track of a "zone urgency" rating for each zone - that is, how urgently the zone needs to get taken care of. Each time period the urgency rating for a zone increases as the zone is not assigned to someone, and this increase is equal to the zone's "urgency delta". Different urgency deltas can be assigned to different zones based on how frequently they need to be dealt with.  For instance, bathroom cleaning might be a weekly task and have a delta of 1, whereas organizing the lounge area might be a monthly task and have a delta of 0.25.

There is also a "do not do this chore" list for each individual.  For instance, a person living downstairs may not want to clean an upstairs bathroom that they do not use. The Assigner makes sure that nobody is assigned a task on their "do not do list".

Ultimately the Assigner works like this: it shuffles the roomates into random order, then goes down the list of roommates and assigns them the most urgent chore (or a chore tied for most urgent) that is not on their "do not do" list.  It continues until all roommates have been assigned a chore for the time period.

## notes on UI / dashboard

* Each roommate's dashboard should list everyone's zone assignments for the period so that if anyone has an issue with the handling of a zone, they can take it up with the appropriate person.
* The tab should also contain a button that brings up a dialog box containing detailed notes on how to do the assigned zone task for that period (use this cleaning solution, reqired tools are located in this place, etc.)

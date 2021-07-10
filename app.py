import os
import cassiopeia as cass

api_key = os.environ['RIOT_API_KEY']

cass.set_riot_api_key(api_key)
cass.set_default_region('NA')

summoner = cass.get_summoner(name="mega sloppy")

league_entries = cass.get_paginated_league_entries(queue=cass.Queue.ranked_solo_fives, tier=cass.Tier.gold, division=cass.Division.three, region="NA")

print(league_entries)
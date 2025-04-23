import pandas as pd
import itertools

concerts = pd.DataFrame({
    'date': pd.to_datetime([
        '2024-01-12', '2024-01-20', '2024-01-21', '2024-02-14'
    ]),
    'artist': ['Taylor', 'Drake', 'Taylor', 'Drake'],
    'venue': ['Madison', 'Barclays', 'Madison', 'Madison']
})

concerts['year_month'] = concerts['date'].dt.to_period('M')

grouped = concerts.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

artists = pd.Series(['Taylor', 'Drake'])
venues = pd.Series(['Madison', 'Barclays'])

artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

all_months = concerts['year_month'].drop_duplicates().sort_values()
all_index = pd.MultiIndex.from_product([all_months, artist_venue_pairs], names=['year_month', 'artist', 'venue'])

full = grouped.set_index(['year_month', 'artist', 'venue']).reindex(all_index, fill_value=0).reset_index()

wide_table = full.pivot(index='year_month', columns=['artist', 'venue'], values='count')

wide_table.columns = [f'{a}_{v}' for a, v in wide_table.columns]
wide_table = wide_table.reset_index()

print(wide_table)

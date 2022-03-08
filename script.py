
def get_rank(country_code, df):
    rank = df.index[(df['Country Code'] == country_code)]
    if len(rank) == 0:
        return -1
    elif len(rank) == 1:
        return int(rank[0])

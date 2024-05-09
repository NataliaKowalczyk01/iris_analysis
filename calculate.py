import statistics

def calculate_statistics(data):
    stats = {}
    for key in data[0].keys():
        if key != 'variety':
            column_data = [float(row[key]) for row in data]
            stats[key] = {
                'mean': statistics.mean(column_data),
                'median': statistics.median(column_data),
                'std': statistics.stdev(column_data)
            }
    return stats

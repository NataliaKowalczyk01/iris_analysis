import csv

def save_results(stats, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['column', 'mean', 'median', 'std'])
        for column, values in stats.items():
            writer.writerow([column, values['mean'], values['median'], values['std']])

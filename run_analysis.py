import argparse
from data_io.load import load_data
from data_io.save import save_results
from calculate import calculate_statistics

def main(input_file, output_file):
    data = load_data(input_file)
    stats = calculate_statistics(data)
    save_results(stats, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate base statistics of iris data.')
    parser.add_argument('input_file', type=str, help='Path to input CSV file')
    parser.add_argument('output_file', type=str, help='Path to output CSV file')
    args = parser.parse_args()

    main(args.input_file, args.output_file)

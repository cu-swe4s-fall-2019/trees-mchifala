def main(data_struct, data_set, num_points):
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Key-value input")

    parser.add_argument('data_struct',
                        type=str,
                        help='The type of data structure')

    parser.add_argument('data_set',
                        type=int,
                        help='Type of data set')
    
     parser.add_argument('num_points',
                        type=int,
                        help='Number of data points')

    args = parser.parse_args()

    main(args.data_struct, args.data_set, args.num_points)

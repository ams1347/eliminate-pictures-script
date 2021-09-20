import csv
import os
import sys
#Author: Aaron Schwartz ams1347@uncw.edu

def main():
    if len(sys.argv) == 3:
        #User has entered 2 variables from command line
        image_directory = sys.argv[1]
        image_directory_path = os.getcwd() + '\\' + image_directory
        csv_file_name = sys.argv[2]
        #If user didn't put ".csv" at the end of the csv file name, add it.
        if csv_file_name.endswith('.csv') is False:
            csv_file_name = csv_file_name + '.csv'

        #Create list of all image names from csv file
        all_images = []
        with open(csv_file_name) as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for row in data_reader:
                if line_count == 0:
                    line_count = 1
                    pass
                else:
                    #change i in row[i] to append image name based on position of image name in csv file
                    all_images.append(row[1])

        #Go through image directory; if file isn't in csv file, delete it
        num_delete = 0
        for filename in os.listdir(image_directory_path):
            if filename not in all_images:
                num_delete += 1
                print("Deleting " + filename + ", No. of deletions: " + str(num_delete))
                os.remove(image_directory_path + "\\" + filename)
        print("Done. No. of deleted image files: " + str(num_delete))

    else:
        #User has not entered variables from command line
        print("Error - Please run script with image directory name and csv file name as arguments")


if __name__ == '__main__':
    main()
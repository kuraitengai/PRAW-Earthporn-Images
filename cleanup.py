# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:16:08 2020

@author: test
"""

import os
import shutil
import time

number_of_days = 30
path = 'C:/Users/LAPTOP/Pictures/Reddit/'

# main function
def main():

	# initializing the count
    deleted_files_count = 0

	# specify the path
    path = "C:/Users/LAPTOP/Pictures/Reddit/"

	# specify the days
    days = 30

	# converting days to seconds
	# time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

		# iterating over each and every folder and file in the path
    for root, dirs, files in os.walk(path):

			# checking the current directory files
        for file in files:

				# file path
                file_path = os.path.join(path, file)

				# comparing the days
                #if seconds >= os.path.getctime(file_path):
                if seconds >= get_file_age(file_path):

					# invoking the remove_file function
                    remove_file(file_path)
                    deleted_files_count += 1 # incrementing count

    print(f"Total files deleted: {deleted_files_count}")


def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")


def get_file_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	main()



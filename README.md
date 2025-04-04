# SFMConversion

Social Feed Manager Conversion Automation

## Background

SFM or Social Feed Manager is a tweet storage format that is used at many University Digital Research Laboratories including Virginia Tech and George Washington University. The goal of this script automation is to make it easier to convert from a SFM JSON format to a unified tweet JSON format.

## Usage

The simple way to use this script is to upload all of your input JSON files into the base directory of where your conversions scripts are located. Then, run the ```runner.sh``` file to run both of the automation scripts concurrently. The easiest way to do this is to input ```bash runner.sh``` into your command line.

The output json files are stored in the ```out``` directory and the collections outputs are stored under the ```collections``` directory. The output files are under the names of the input json file and the collection outputs are under the name ```collection-#inputfile.json```. Thus it should be easy to distinguish between the JSON files and formats, based on the names and directories.

To find the number of tweets converted in a conversion batch, please use the ```counter.sh``` script. You can run it by using the command ```bash counter.sh```. This script looks through all the files in the ```out``` directory and gets the line count, to identify how many tweets have been converted.

Also included is a test script that uses Python unit tests to verify the SFM conversions. The simple way to test this is to run ```python3 test_sfm.py```. The output should show a series of unit tests, which state if the tests have passed or not passed.
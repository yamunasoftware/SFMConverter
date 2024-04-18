# SFMConversion

Social Feed Manager Conversion Automation

## Background

SFM or Social Feed Manager is a tweet storage format that is used at many University Digital Research Laboratories including Virginia Tech and George Washington University. The goal of this script automation is to make it easier to convert from a SFM JSON format to a unified tweet JSON format.

## Usage

The simple way to use this script is to upload all of your input JSON files into the root directory of the project. Then, run the ```runner.sh``` or ```runner.bat``` file (based on your operating system) to run both of the automation scripts concurrently. The output json files are stored in the ```out``` directory and the collections outputs are stored under the ```collections``` directory. The output files are under the names of the input json file and the collection outputs are under the name ```collection-#inputfile.json```. Thus it should be easy to distinguish between the JSON files and formats, based on the names and directories.
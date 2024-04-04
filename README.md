# SFMConversion

Social Feed Manager Conversion Automation

## Background

SFM or Social Feed Manager is a tweet storage format that is used at many University Digital Research Laboratories including Virginia Tech and George Washington University. The goal of this script automation is to make it easier to convert from a SFM JSON format to a unified tweet JSON format.

## Usage

The simple way to use this script is to upload all of your input JSON files into the ```jsons``` directory. Then in your command line, simply run the command ```python automation.py``` or ```python3 automation.py``` for Linux users. The output json files are stored in the ```out``` directory under the names of the input json file and ```collection-#inputfile.json```. Thus it should be easy to distinguish between the JSON files and formats.
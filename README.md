# SFMConversion

Social Feed Manager Conversion Automation

## Background

SFM or Social Feed Manager is a tweet storage format that is used at many University Digital Research Laboratories including Virginia Tech and George Washington University. The goal of this script automation is to make it easier to convert from a SFM JSON format to a unified tweet JSON format.

## Usage

The simple way to use this script is to upload all of your input JSON files into the root directory of the project. Then, run the ```runner.sh``` file (you must use Linux) to run both of the automation scripts concurrently. The easiest way to do this is to input ```bash runner.sh``` into your command line.

The output json files are stored in the ```out``` directory and the collections outputs are stored under the ```collections``` directory. The output files are under the names of the input json file and the collection outputs are under the name ```collection-#inputfile.json```. Thus it should be easy to distinguish between the JSON files and formats, based on the names and directories.

If your system or environment is having problem with system resources when running the ```runner.sh``` script, it is because the script takes advantage of parallel computing, which may cause system crashes. In this case, you should run the ```sequential.sh``` file (you must use Linux). This method runs the conversion scripts sequentially. This method is slower; however, it requires far fewer system resources, which may solve some problems. Again, the easiest way to do this is to input ```bash sequential.sh``` into your command line.

## Dependencies

The conversion and automation scripts use the following python modules:

- ```os```
- ```sys```
- ```ujson```
- ```copy```

However, the only dependency that needs to be installed is ```ujson```. To install ```ujson``` you have to run the following command:

```pip3 install ujson```
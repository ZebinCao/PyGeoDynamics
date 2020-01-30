#!/usr/bin/env python

#############################################
#           Parse the input file
#          Zebin Cao, Jan 29, 2020
#############################################

class OneD_Parser():

    def __init__(self, inputfile):
        self.file = inputfile

    def parse_file(self):
        model_settings = {}
        with open(self.file) as fp:
            for line in fp:
                if line != '\n' and line[0] != '[':
                    key, value = line.split('=')
                    model_settings[key.rstrip().strip()] = value.rstrip().strip()
                else:
                    continue
        return model_settings

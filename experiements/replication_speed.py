#!/bin/python

import sys, subprocess

def main():
    bucktesizes = [1,2,4,8,16,32,64,128,256,512,1024,2048]
    locations   = ['UFlorida-SSERCA_FTP',
                   'BNL_ATLAS_2_FTP',
                   'FNAL_FERMIGRID_FTP',
                   'SPRACE_FTP',
                   'NYSGRID_CORNELL_NYS1',
                   'Purdue-Steele_FTP',
                   'MIT_CMS_CE2_FTP',
                   'UTA_SWT2_FTP',
                   'SWT2_CPB_FTP',
                   'AGLT2_CE_2_FTP',
                   'USCMS-FNAL-WC1-CE3_F']

    # Output is of the form:
    #   bucketsize;location;time

    for bucketsize in bucketsizes:
         for location in locations:

if __name__ == "__main__":
    sys.exit(main())        


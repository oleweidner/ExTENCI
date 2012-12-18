#!/bin/python

import sys, time, subprocess

def irods_repl(target, file):
    t1 = time.time()
    command = "irepl -R %s %s" % (target, file)
    print command
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    rc = proc.wait()
    td = time.time() - t1
    if rc != 0:
        return 'F'
    else:
        return str(td)

def main():
    bucketsizes = [16,32,64,128,256,512,1024,2048,4096]
    locations   = ['UFlorida-SSERCA_FTP',
    # source location 'BNL_ATLAS_2_FTP',
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
             timestamp = time.time()
             filename = "/osg/home/oweidner/speedtest/bucket_%sM.dat" % bucketsize
             print "Replicating %s to %s" % (filename, location)

             duration = irods_repl(location, filename)

             result = "%s;%s;%s;%s\n" % (timestamp, bucketsize, location, duration)
             print result
             with open("results_repl.dat", "a") as myfile:
                 myfile.write(result)


if __name__ == "__main__":
    sys.exit(main())        


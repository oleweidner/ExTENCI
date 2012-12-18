#!/usr/bin/python

""" This script creates files and different sizes and 
    uploads them to iRODS.
"""

import os, sys, subprocess

def create_file(name, size):
    proc = subprocess.Popen('dd if=/dev/urandom of=%s bs=16M count=%d' \
      % (name, size/16),  shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    rc = proc.wait()

def delete_file(name):
    proc = subprocess.Popen('rm %s' % name,
      shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    rc = proc.wait()

def irods_put(group, file, targetdir):
    command = "iput -f -R %s %s %s" % (group, file, targetdir)
    print command
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    rc = proc.wait()
    print proc

def main():
    bucketsizes = [16,32,64,128,256,512,1024,2048]

    for bucket in bucketsizes:
        filename  = os.path.normpath(os.path.join(os.getcwd(), "bucket_%sM.dat" % bucket))
        print "\nCreating bucket of size %s MB: %s" % (bucket, filename)
        create_file(filename, bucket) 
        print "Putting %s into iRODS..." % (filename)
        irods_put("osgGridFtpGroup", filename, "/osg/home/oweidner/speedtest/")
        print "Deleting source file %s" % (filename) 
        delete_file(filename)



if __name__ == "__main__":
    sys.exit(main())

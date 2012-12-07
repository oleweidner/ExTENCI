#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys, time
import bliss.saga as saga

BASEPATH = "/home/oweidner/ExTENCI/condor/irods_bowtie/"

def main():
    
    try:
        # describe our job
        jd = saga.job.Description()

        # job executable
        jd.executable  = '%s/bowtie2-wrapper.sh' % BASEPATH

        # output options
        jd.output = "%s/irods_bowtie.stdout" % BASEPATH
        jd.error  = "%s/irods_bowtie.stdout" % BASEPATH

        # define allocation (Condor : +Project)
        jd.project = 'TG-MCB090174'
        
        # This is equivalent to +SiteList = "xyz"
        jd.candidate_hosts = ['UFlorida-SSERC', 'BNL_ATLAS_2', 'UFlorida-SSERC', 
          'BNL_ATLAS_2', 'FNAL_FERMIGRID', 'SPRACE', 'NYSGRID_CORNELL_NYS1', 
          'Purdue-Steele', 'MIT_CMS_CE2', 'UTA_SWT2', 'SWT2_CPB', 'AGLT2_CE_2', 
          'USCMS-FNAL-WC1-CE3']

        # pre-stage executables (Condor: transfer_input_files)
        jd.file_transfer = ['%s/bowtie2 > bowtie2' % BASEPATH, 
                            '%s/bowtie2-align > bowtie2-align' % BASEPATH]

        # add extra Condor options as URL query parametersls /TG-MCB090174
        osg = saga.job.Service("condor://localhost?WhenToTransferOutput=ON_EXIT&should_transfer_files=YES&notification=Always")

        bowtie_job = osg.create_job(jd)

        print "Job ID    : %s" % (bowtie_job.jobid)
        print "Job State : %s" % (bowtie_job.get_state())

        print "\n...starting job...\n"
        bowtie_job.run()

        print "Job ID    : %s" % (bowtie_job.jobid)
        print "Job State : %s" % (bowtie_job.get_state())

        print "\n...waiting for job...\n"
        bowtie_job.wait()

        print "Job State : %s" % (bowtie_job.get_state())
        print "Exitcode  : %s" % (bowtie_job.exitcode)

    except saga.Exception, ex:
        print "An error occured during job execution: %s" % (str(ex))
        sys.exit(-1)

if __name__ == "__main__":
    main()


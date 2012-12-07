#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys, time
import bliss.saga as saga

BASEPATH = "/home/oweidner/ExTENCI/condor/simple_bowtie/"

def main():

    try:

        jd = saga.job.Description()

        # executable and arguents
        jd.executable = "%s/bowtie2" % BASEPATH
        jd.arguments  = ['--time','-x lambda_virus','-U longreads.fq','-S result.sam']
        
        # output options
        jd.output     = "%s/simple_bowtie.out" % BASEPATH 
        jd.error      = "%s/simple_bowtie.err" % BASEPATH

        # define allocation (Condor : +Project)
        jd.project = 'TG-MCB090174'

        # This is equivalent to +SiteList = "xyz"
        jd.candidate_hosts = ["FNAL_FERMIGRID", "cinvestav", "SPRACE", 
                              "NYSGRID_CORNELL_NYS1", "Purdue-Steele", "MIT_CMS_CE2", 
                              "SWT2_CPB", "AGLT2_CE_2", "UTA_SWT2", "GridUNESP_CENTRAL",
                              "USCMS-FNAL-WC1-CE3"]

        jd.file_transfer   = [# Stage-in
                              "%s/bowtie2                > bowtie2" % BASEPATH,
                              "%s/bowtie2-align          > bowtie2-align" % BASEPATH,
                              "%s/longreads.fq           > longreads.fq" % BASEPATH,
                              "%s/lambda_virus.1.bt2     > lambda_virus.1.bt2" % BASEPATH,
                              "%s/lambda_virus.2.bt2     > lambda_virus.2.bt2" % BASEPATH,
                              "%s/lambda_virus.3.bt2     > lambda_virus.3.bt2" % BASEPATH,
                              "%s/lambda_virus.4.bt2     > lambda_virus.4.bt2" % BASEPATH,
                              "%s/lambda_virus.rev.1.bt2 > lambda_virus.rev.1.bt2" % BASEPATH,
                              "%s/lambda_virus.rev.2.bt2 > lambda_virus.rev.2.bt2" % BASEPATH,
                              # Stage-out
                              #"results.sam << results.sam" # ? 
                              ]


        # create a condor job-service for OSG
        osg = saga.job.Service("condor://localhost?WhenToTransferOutput=ON_EXIT&should_transfer_files=YES&notification=Always")

        # create a new job from above description
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
        print "An error occured during OSG job execution: %s" % (str(ex))
        sys.exit(-1)

if __name__ == "__main__":
    main()


try:

    jd = saga.job.Description()

    jd.project    = 'TG-MCB090174'
    jd.executalbe = 'bowtie2'
    jd.arguments  = ['--time','-x lambda_virus','-U longreads.fq','-S result.sam']
    jd.output     = 'simple_bowtie.out' 
    jd.error      = 'simple_bowtie.err'

    # This is equivalent to +SiteList = "xyz"
    jd.candidate_hosts = ["FNAL_FERMIGRID", "cinvestav", "SPRACE", 
                          "NYSGRID_CORNELL_NYS1", "Purdue-Steele", "MIT_CMS_CE2", 
                          "SWT2_CPB", "AGLT2_CE_2", "UTA_SWT2", "GridUNESP_CENTRAL",
                          "USCMS-FNAL-WC1-CE3"]

    jd.file_transfer   = [# Stage-in
                          "./bowtie2 >> bowtie2",
                          "./bowtie2-align >> bowtie2-align",
                          "./longreads.fq >> longreads.fq",
                          "./lambda_virus.1.bt2 >> lambda_virus.1.bt2",
                          "./lambda_virus.2.bt2 >> lambda_virus.2.bt2",
                          "./lambda_virus.3.bt2 >> lambda_virus.3.bt2",
                          "./lambda_virus.4.bt2 >> lambda_virus.4.bt2",
                          "./lambda_virus.rev.1.bt2 >> lambda_virus.rev.1.bt2",
                          "./lambda_virus.rev.2.bt2 >> lambda_virus.rev.2.bt2",
                          # Stage-out
                          "results.sam << results.sam" # ? 
                          ]

    # stuff that needs to go into a .configuration file:
    # - notification = Always
    # - log = simple_bowtie_$(cluster).log
    # - should_transfer_files = YES
    # - WhenToTransferOutput  = ON_EXIT

    # create a condor job-service for OSG
    osg = saga.job.Service("condor://localhost?notifications=Always&WhenToTransferOutput=ON_EXIT")

    # create a new job from above description
    job = osg.create_job(jd)

    # run the job (submit the job to PBS)
    job.run()

    # wait for the job to either finish or fail
    myjob.wait()

    print "Job State : %s" % (myjob.get_state())
    print "Exitcode  : %s" % (myjob.exitcode)

except saga.Exception, ex:
    print "An error occured during OSG job execution: %s" % (str(ex))
    sys.exit(-1)


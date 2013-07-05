import sys
import os
import time
from pilot import PilotComputeService,  State
#PilotDataService, ComputeDataService, State

RUN_ID = "BJ-"
NUMBER_JOBS = 2
COORDINATION_URL = "redis://ILikeBigJob_wITH-REdIS@gw68.quarry.iu.teragrid.org:6379"

if __name__ == "__main__":

    print ("Start")
    sys.stdout.flush()
    if len(sys.argv) > 1:
        RUN_ID = sys.argv[1]
    pilot_compute_service = PilotComputeService(COORDINATION_URL)

    # create pilot job service
    pilot_compute_description = {
         "service_url": 'pbs+ssh://trestles.sdsc.edu',
         "number_of_processes": 1,
         "queue": "shared",
         "project": "TG-MCB090174",
         "working_directory": "/home/jweichel/agent",
         "walltime": 90
    #     'affinity_datacenter_label': "trestles",
    #     'affinity_machine_label': "mymachine"
                                }
    # initiate a pilot job
    pilotjob = pilot_compute_service.create_pilot(pilot_compute_description)

    # create pilot data service (factory for data pilots (physical,distributed storage))
    # and pilot data where data is to be moved
    #pilot_data_service = PilotDataService(COORDINATION_URL)
    #pilot_data_description = {
    #     "service_url":"ssh://localhost/"+os.getenv("HOME")+"/matrix/pilotdata",
    #     "size": 1,
    #     "affinity_datacenter_label":"trestles",
    #     "affinity_machine_label":"mymachine"
    #                         }

    #ps = pilot_data_service.create_pilot(pilot_data_description=pilot_data_description)

    #compute_data_service = ComputeDataService()
    #compute_data_service.add_pilot_compute_service(pilot_compute_service)
    #compute_data_service.add_pilot_data_service(pilot_data_service)

    ### Create Output DU to store the output files.
    #output_data_unit_description = { 
    #      "file_urls": [],
    #      "affinity_datacenter_label":"trestles",
    #      "affinity_machine_label":"mymachine"
    #                               }

    # submit pilot data to a pilot store
    #output_du = compute_data_service.submit_data_unit(output_data_unit_description)
    #output_du.wait()
    #print ("Finished Pilot Data setup.  Submitting compute units")
    print ("Finished Pilot-Job setup.  Submitting compute units")
    sys.stdout.flush()

    # start compute units
    for i in range(NUMBER_JOBS):
        compute_unit_description = {
            "executable": "/home/jweichel/runmatrix.sh",
            "arguments": [60, 10, RUN_ID],
            "number_of_processes": 1,
            "spmd_variation": "single",
            "output": "stdout.txt", RUN_ID+"out.txt"
            "error": "stderr.txt",
            #"output_data":[{ output_du.get_url(): ['std*', RUN_ID+"out.txt"]} ]
                                   }
        compute_unit = compute_data_service.submit_compute_unit(compute_unit_description)

    print ("Finished setup of PSS and PDS. Waiting for scheduling of PD")
    sys.stdout.flush()
    compute_service.wait()


    # export the output files to local directory.
    #print ("Returning output files")
    #sys.stdout.flush()
    #output_du.export(os.getcwd()+"/bigjob")

    print ("Terminate Pilot Compute/Data Services")
    sys.stdout.flush()
    compute_data_service.cancel()
    #pilot_data_service.cancel()
    pilot_compute_service.cancel()

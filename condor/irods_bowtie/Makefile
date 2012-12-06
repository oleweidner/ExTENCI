
. PHONY: clean, submit_condor, submit_saga, runlocal

clean:
	rm -vf irods_bowtie_*.out
	rm -vf irods_bowtie_*.err
	rm -vf irods_bowtie_*.log
	rm -rf result.sam
submit_condor:
	condor_submit irods_bowtie.condor

submit_saga:
	python irods_bowtie.py

#runlocal:
#	./bowtie2 --time  -x lambda_virus -U longreads.fq -S result.sam


. PHONY: clean, submit, runlocal

clean:
	rm -vf irods_bowtie_*.out
	rm -vf irods_bowtie_*.err
	rm -vf irods_bowtie_*.log

submit:
	condor_submit irods_bowtie.condor

#runlocal:
#	./bowtie2 --time  -x lambda_virus -U longreads.fq -S result.sam

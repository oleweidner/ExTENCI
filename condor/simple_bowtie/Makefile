
. PHONY: clean, submit, runlocal

clean:
	rm -vf simple_bowtie_*.out
	rm -vf simple_bowtie_*.err
	rm -vf simple_bowtie_*.log

submit:
	condor_submit simple_bowtie.condor

runlocal:
	./bowtie2 --time  -x lambda_virus -U longreads.fq -S result.sam

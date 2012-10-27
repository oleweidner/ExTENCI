
. PHONY: clean, submit, runlocal

clean:
	rm -vf simple_bowtie.out
	rm -vf simple_bowtie.err
	rm -vf simple_bowtie.log

submit:
	condor_submit simple_bowtie.condor

runlocal:
	./bowtie2 --time  -x lambda_virus -U longreads.fq -S result.sam

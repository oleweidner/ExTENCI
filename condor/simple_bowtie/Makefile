. PHONY: clean, submit_condor, submit_saga, runlocal

clean:
	rm -vf simple_bowtie_*.out
	rm -vf simple_bowtie_*.err
	rm -vf simple_bowtie_*.log
	rm -vf result.sam

submit_condor:
	condor_submit simple_bowtie.condor

submit_saga:
	python simple_bowtie.py

runlocal:
	./bowtie2 --time  -x lambda_virus -U longreads.fq -S result.sam

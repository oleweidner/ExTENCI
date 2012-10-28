

## Stage and Replicate Data in iRODS

The data we are working with in this example is publicly 
available. 

* Reference Data: ftp://ftp.cbcb.umd.edu/pub/data/bowtie2_indexes/incl/hg18.zip 
* Read Data:

In order for this example to work, all input data has to be 
staged into iRODS first. This is done via the iRODS command
line tools:

``` bash
iput -R osgGridFtpGroup hg18.1.bt2
iput -R osgGridFtpGroup hg18.2.bt2
iput -R osgGridFtpGroup hg18.3.bt2
iput -R osgGridFtpGroup hg18.4.bt2
iput -R osgGridFtpGroup hg18.rev.1.bt2
iput -R osgGridFtpGroup hg18.rev.2.bt2
iput -R osgGridFtpGroup Marisa_mRNA_C0.fq
```

Next, the data needs to be replicated to some more 
sites. That makes our jobs more likely to get scheduled faster:

```bash

```

The file in iRods can be listed with the ```ils``` command:

```bash
ils -l 

  oweidner          1 UFlorida-SSERCA_FTP    1436274378 2012-10-27.17:22 & Marisa_mRNA_C0.fq
  oweidner          1 UFlorida-SSERCA_FTP     961172069 2012-10-27.15:10 & hg18.1.bt2
  oweidner          1 UFlorida-SSERCA_FTP     717656024 2012-10-27.15:11 & hg18.2.bt2
  oweidner          1 UFlorida-SSERCA_FTP         76850 2012-10-27.15:43 & hg18.3.bt2
  oweidner          1 UFlorida-SSERCA_FTP     717656019 2012-10-27.15:44 & hg18.4.bt2
  oweidner          1 UFlorida-SSERCA_FTP     961172069 2012-10-27.15:46 & hg18.rev.1.bt2
  oweidner          1 UFlorida-SSERCA_FTP     717656024 2012-10-27.17:19 & hg18.rev.2.bt2
```



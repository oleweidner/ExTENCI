
## Stage and Replicate Data in iRODS

Before the bowtie job can be executed, the data needs to be staged into
iRods. Once the data is in iRods, it can be replicated 
accross multpile sites. After sucesfull replication, all
data in iRods will be available at the job execution
sites (i.e., available to the Condor jobs) via a local
mount: 

```bash
$OSG_DATA/osg/home/<username>
```

The data used in this example is publicly available. 

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

Next, the data should to be replicated to some  additional
sites. That makes our jobs more likely to get scheduled faster:

```bash
irepl-osg -f /osg/home/oweidner/hg18.1.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/hg18.2.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/hg18.3.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/hg18.4.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/hg18.rev.1.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/hg18.rev.2.bt2 -G osgGridFtpGroup
irepl-osg -f /osg/home/oweidner/Marisa_mRNA_C0.fq -G osgGridFtpGroup
```

The file in iRods can be listed with the ```ils``` command. The ```-l``` option
shows all replica locations":

```bash
ils -l 
  oweidner          1 UFlorida-SSERCA_FTP     717656024 2012-10-27.17:19 & hg18.rev.2.bt2
  oweidner          3 BNL_ATLAS_2_FTP         717656024 2012-10-27.19:37 & hg18.rev.2.bt2
  oweidner          4 FNAL_FERMIGRID_FTP      717656024 2012-10-27.19:37 & hg18.rev.2.bt2
  oweidner          5 SPRACE_FTP              717656024 2012-10-27.19:39 & hg18.rev.2.bt2
  oweidner          6 NYSGRID_CORNELL_NYS1    717656024 2012-10-27.19:39 & hg18.rev.2.bt2
  oweidner          7 Purdue-Steele_FTP       717656024 2012-10-27.19:40 & hg18.rev.2.bt2
  oweidner          8 MIT_CMS_CE2_FTP         717656024 2012-10-27.19:41 & hg18.rev.2.bt2
  oweidner          9 UTA_SWT2_FTP            717656024 2012-10-27.19:42 & hg18.rev.2.bt2
  oweidner         10 SWT2_CPB_FTP            717656024 2012-10-27.19:43 & hg18.rev.2.bt2
  oweidner         11 AGLT2_CE_2_FTP          717656024 2012-10-27.19:43 & hg18.rev.2.bt2
  oweidner         12 USCMS-FNAL-WC1-CE3_F    717656024 2012-10-27.19:43 & hg18.rev.2.bt2
  ...
```

## Run the Job

Before you run the job, have a look at [irods_bowtie.condor](https://github.com/oleweidner/ExTENCI/blob/master/condor/irods_bowtie/irods_bowtie.condor).
The line

```bash
+SiteList = "UFlorida-SSERC, BNL_ATLAS_2, FNAL_FERMIGRID, SPRACE, NYSGRID_CORNELL_NYS1, Purdue-Steele, MIT_CMS_CE2, UTA_SWT2, SWT2_CPB, AGLT2_CE_2, USCMS-FNAL-WC1-CE3"
```

Defines the list of sites that the job can execute on, i.e., the sites where the input data has been staged to.

The job is submitted by running ```make submit```. 


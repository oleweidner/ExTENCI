#!/bin/bash

# This is were the iRods data lives
$OSG_DATA_HOME=$OSG_DATA/osg/irods/oweidner

echo "Running on site: $OSG_SITE_NAME"
echo
echo "Running on host: "
/bin/hostname
echo
$OSG_DATA_HOME=$OSG_DATA/osg/irods/oweidner
echo "OSG_DATA location: $OSG_DATA_HOME"
echo
echo "Working directory: "
pwd

./bowtie2 --time -x $OSG_DATA_HOME/hg18 -U $OSG_DATA_HOME/Marisa_mRNA_C0.fq -S result.sam



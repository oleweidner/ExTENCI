#!/bin/bash

CWD=`pwd`
HOST=`/bin/hostname`
OSG_DATA_HOME=$OSG_DATA/osg/irods/oweidner

echo "Running on site   : $OSG_SITE_NAME"
echo "Running on host   : $HOST"
echo "OSG_DATA location : $OSG_DATA_HOME"
echo "Working directory : $CWD"

./bowtie2 --time -x $OSG_DATA_HOME/hg18 -U $OSG_DATA_HOME/Marisa_mRNA_C0.fq -S result.sam



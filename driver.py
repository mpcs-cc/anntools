################################################################################
#   Nov 17, 2011
#   Authors: Vlad Makarov, Chris Yoon
#   Language: Python
#   OS: UNIX/Linux, MAC OSX
#   Copyright (c) 2011, The Mount Sinai School of Medicine

#   Available under BSD  licence

#   Redistribution and use in source and binary forms, with or without modification,
#   are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#   IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#   INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#   OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#   EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
################################################################################

import sys
import os
import file_utils as fu
import annotate as ann

def run(infile, format):

    print("Running . . .")

    ann.getSnpsFromDbSnp(vcf=infile, format='vcf', tmpextin='', 
        tmpextout='.1')
    print("dbSNP - done.")
    tmpextin = 1
    tmpextout = 2

    ann.getBigRefGene(vcf=infile, format='vcf', tmpextin='.' + str(tmpextin),
        tmpextout='.' + str(tmpextout))
    print("BigRefGene - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.getGenes(vcf=infile, format='vcf', table='refGene', 
        promoter_offset=500, tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("BigRefGene - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCytoband(vcf=infile, format='vcf', table='cytoBand', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("Cytoband - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGadAll(vcf=infile, format='vcf', table='gadAll', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("gadAll - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGwasCatalog(vcf=infile, format='vcf', 
        table='gwasCatalog', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("GwasCatalog - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithMiRNA(vcf=infile, format='vcf', table='targetScanS', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("miRNA - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWitHUGOGeneNomenclature(vcf=infile, format='vcf', 
        table='hugo', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("HUGO Gene Nomenclature Committee - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, format='vcf', table='dgv_Cnv', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("dgv_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, format='vcf', 
        table='abParts_IG_T_CelReceptors', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("abParts_IG_T_CelReceptors - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, format='vcf', 
        table='mcCarroll_Cnv', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("mcCarroll_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, format='vcf', 
        table='conrad_Cnv', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("conrad_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGenomicSuperDups(vcf=infile, format='vcf', 
        table='genomicSuperDups', tmpextin='.' + str(tmpextin),
        tmpextout='.' + str(tmpextout))
    print("genomicSuperDups - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithTfbsConsSites(vcf=infile, table='tfbsConsSites',
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("addOverlapWithTfbsConsSites - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ## Cleanup
    for i in range(1, tmpextin):
        fu.delete(infile + '.' + str(i))

    os.rename(infile + '.' + str(tmpextin), infile + '.annot')
    finalout=(infile + '.annot').replace('.vcf.annot', '.annot.vcf')
    os.rename(infile + '.annot', finalout)

### EOF
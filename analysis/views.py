from django.shortcuts import render
from django import template
from django.template import Template
import operator
import json
import math
import urllib
import urllib.request
import re
import sys
import scipy
from scipy import stats
# Create your views here.

def analysis(request):
    return render(request, 'analysis/analysis.html')

def result(request):
    if request.method == 'POST':
        if request.POST.get('compareA', True):
            gidA = request.POST['compareA']
            GeneListA = gidA.splitlines()
            print (GeneListA)
        else:
            print ("A-Nothing")

        if request.POST.get('compareB', True):
            gidB = request.POST['compareB']
            GeneListB = gidB.splitlines()
            print (GeneListB)
        else:
            print ("B-Nothing")

        # if request.POST.get('correction', True):
        #     cor = request.POST['correction']
        #     print (cor)
        # else:
        #     print ("Nocorr")
    ### Group A - Total Gene Count / GO Annotation Names & Counts

    AGeneCount = 0
    AGOAnnos = []
    AKEGGAnnos = []
    APfamAnnos = []
    BGeneCount = 0
    BGOAnnos = []
    BKEGGAnnos = []
    BPfamAnnos = []
    for genefromlist in GeneListA:
        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=GO"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            AGeneCount += 1
            for anno in data[0][genefromlist][gene]:
                ### GO Annotation ###
                ### Create a list contains all the GO annotations in A (duplicated)###
                if type(anno) is dict:
                    FoundAnno = re.search(r'GO:\d+',anno["ID"])
                    if FoundAnno:
                        AGOAnnos.append(FoundAnno.group())
                        print("GO")

                elif type(anno) is str:
                    FoundAnno = re.search(r'GO:\d+',anno)
                    if FoundAnno:
                        AGOAnnos.append(FoundAnno.group())
                        print("GO")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=KEGG_Brite"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'ko\d+',anno["ID"])
                    if FoundAnno:
                        AKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Brite")

                elif type(anno) is str:
                    FoundAnno = re.search(r'ko\d+',anno)
                    if FoundAnno:
                        AKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Brite")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=Orthology"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'KO:K\d+',anno["ID"])
                    if FoundAnno:
                        AKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Orthology")

                elif type(anno) is str:
                    FoundAnno = re.search(r'KO:K\d+',anno)
                    if FoundAnno:
                        AKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Orthology")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=Pfam"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'PF\d+',anno["ID"])
                    if FoundAnno:
                        APfamAnnos.append(FoundAnno.group())
                        print("Pfam")

                elif type(anno) is str:
                    FoundAnno = re.search(r'PF\d+',anno)
                    if FoundAnno:
                        APfamAnnos.append(FoundAnno.group())
                        print("Pfam")


    ### Group B - Total Gene Count / GO Annotation Names & Counts
    for genefromlist in GeneListB:
        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=GO"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            BGeneCount += 1
            for anno in data[0][genefromlist][gene]:
                ### GO Annotation ###
                ### Create a list contains all the GO annotations in A (duplicated)###
                if type(anno) is dict:
                    FoundAnno = re.search(r'GO:\d+',anno["ID"])
                    if FoundAnno:
                        BGOAnnos.append(FoundAnno.group())
                        print("GO")

                elif type(anno) is str:
                    FoundAnno = re.search(r'GO:\d+',anno)
                    if FoundAnno:
                        BGOAnnos.append(FoundAnno.group())
                        print("GO")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=KEGG_Brite/"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'ko\d+',anno["ID"])
                    if FoundAnno:
                        BKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Brite")

                elif type(anno) is str:
                    FoundAnno = re.search(r'ko\d+',anno)
                    if FoundAnno:
                        BKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Brite")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=Orthology/"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'KO:K\d+',anno["ID"])
                    if FoundAnno:
                        BKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Orthology")

                elif type(anno) is str:
                    FoundAnno = re.search(r'KO:K\d+',anno)
                    if FoundAnno:
                        BKEGGAnnos.append(FoundAnno.group())
                        print("KEGG_Orthology")

        jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/extract=Pfam/"
        print(jsonurl)

        with urllib.request.urlopen(jsonurl) as url:
            data = json.loads(url.read().decode())

        for gene in data[0][genefromlist]:
            for anno in data[0][genefromlist][gene]:
                if type(anno) is dict:
                    FoundAnno = re.search(r'PF\d+',anno["ID"])
                    if FoundAnno:
                        BPfamAnnos.append(FoundAnno.group())
                        print("Pfam")

                elif type(anno) is str:
                    FoundAnno = re.search(r'PF\d+',anno)
                    if FoundAnno:
                        BPfamAnnos.append(FoundAnno.group())
                        print("Pfam")
    #
    # ### Group A - Total Gene Count / GO Annotation Names & Counts
    #
    # AGeneCount = 0
    # AGOAnnos = []
    # AKEGGAnnos = []
    # BGeneCount = 0
    # BGOAnnos = []
    # BKEGGAnnos = []
    # for genefromlist in GeneListA:
    #     jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json"
    #     print(jsonurl)
    #
    #     with urllib.request.urlopen(jsonurl) as url:
    #         data = json.loads(url.read().decode())
    #
    #     for gene in data[0][genefromlist]:
    #         AGeneCount += 1
    #         for anno in data[0][genefromlist][gene]:
    #             ### GO Annotation ###
    #             ### Create a list contains all the GO annotations in A (duplicated)###
    #             if type(anno) is dict:
    #                 FoundAnno = re.search(r'GO:\d+',anno["ID"])
    #                 if FoundAnno:
    #                     AGOAnnos.append(FoundAnno.group())
    #                     print("GO")
    #                 FoundAnno = re.search(r'ko\d+',anno["ID"])
    #                 if FoundAnno:
    #                     AKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #                 FoundAnno = re.search(r'KO:K\d+',anno["ID"])
    #                 if FoundAnno:
    #                     AKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #
    #             elif type(anno) is str:
    #                 FoundAnno = re.search(r'GO:\d+',anno)
    #                 if FoundAnno:
    #                     AGOAnnos.append(FoundAnno.group())
    #                     print("GO")
    #                 FoundAnno = re.search(r'ko\d+',anno)
    #                 if FoundAnno:
    #                     AKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #                 FoundAnno = re.search(r'KO:K\d+',anno)
    #                 if FoundAnno:
    #                     AKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #
    #
    # ### Group B - Total Gene Count / GO Annotation Names & Counts
    # for genefromlist in GeneListB:
    #     jsonurl = "http://link.g-language.org/"+genefromlist+"/format=json/filter=:repair"
    #     print(jsonurl)
    #
    #     with urllib.request.urlopen(jsonurl) as url:
    #         data = json.loads(url.read().decode())
    #
    #     for gene in data[0][genefromlist]:
    #         BGeneCount += 1
    #         for anno in data[0][genefromlist][gene]:
    #             ### GO Annotation ###
    #             ### Create a list contains all the GO annotations in A (duplicated)###
    #             if type(anno) is dict:
    #                 FoundAnno = re.search(r'GO:\d+',anno["ID"])
    #                 if FoundAnno:
    #                     BGOAnnos.append(FoundAnno.group())
    #                     print("GO")
    #                 FoundAnno = re.search(r'ko\d+',anno["ID"])
    #                 if FoundAnno:
    #                     BKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #                 FoundAnno = re.search(r'KO:K\d+',anno["ID"])
    #                 if FoundAnno:
    #                     BKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #
    #             elif type(anno) is str:
    #                 FoundAnno = re.search(r'GO:\d+',anno)
    #                 if FoundAnno:
    #                     BGOAnnos.append(FoundAnno.group())
    #                     print("GO")
    #                 FoundAnno = re.search(r'ko\d+',anno)
    #                 if FoundAnno:
    #                     BKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")
    #                 FoundAnno = re.search(r'KO:K\d+',anno)
    #                 if FoundAnno:
    #                     BKEGGAnnos.append(FoundAnno.group())
    #                     print("KEGG")

    ### GO annotation sorting ###

    ### A - sort
    AGOAnnosList = {}
    for anno in range(0,len(AGOAnnos)):
        exist = 0
        for Aanno in AGOAnnosList:
            if Aanno == AGOAnnos[anno]:
                exist = 1
                AGOAnnosList[Aanno] += 1
                print("AExist")
                break
        if exist == 0:
            AGOAnnosList[AGOAnnos[anno]] = 1
            print("A New Anno")
    sort_AGOAnnosList = sorted(AGOAnnosList.items(), key = lambda AGOAnnosList: AGOAnnosList[1], reverse = True)

    ### B - sort
    BGOAnnosList = {}
    for anno in range(0,len(BGOAnnos)):
        exist = 0
        for Banno in BGOAnnosList:
            if Banno == BGOAnnos[anno]:
                exist = 1
                BGOAnnosList[Banno] += 1
                print("B Exist")
                break
        if exist == 0:
            BGOAnnosList[BGOAnnos[anno]] = 1
            print("B New Anno")
    sort_BGOAnnosList = sorted(BGOAnnosList.items(), key = lambda BGOAnnosList: BGOAnnosList[1], reverse = True)

    # for anno in sort_BGOAnnosList:
    #     print(anno)

    ### KEGG Annotation Sorting ###

    ### A - sort
    AKEGGAnnosList = {}
    for anno in range(0,len(AKEGGAnnos)):
        exist = 0
        for Aanno in AKEGGAnnosList:
            if Aanno == AKEGGAnnos[anno]:
                exist = 1
                AKEGGAnnosList[Aanno] += 1
                print("AExist")
                break
        if exist == 0:
            AKEGGAnnosList[AKEGGAnnos[anno]] = 1
            print("A New Anno")
    sort_AKEGGAnnosList = sorted(AKEGGAnnosList.items(), key = lambda AKEGGAnnosList: AKEGGAnnosList[1], reverse = True)

    ### B - sort
    BKEGGAnnosList = {}
    for anno in range(0,len(BKEGGAnnos)):
        exist = 0
        for Banno in BKEGGAnnosList:
            if Banno == BKEGGAnnos[anno]:
                exist = 1
                BKEGGAnnosList[Banno] += 1
                print("B Exist")
                break
        if exist == 0:
            BKEGGAnnosList[BKEGGAnnos[anno]] = 1
            print("B New Anno")
    sort_BKEGGAnnosList = sorted(BKEGGAnnosList.items(), key = lambda BKEGGAnnosList: BKEGGAnnosList[1], reverse = True)

    ### Pfam Annotation Sorting ###
    ### A - sort
    APfamAnnosList = {}
    for anno in range(0,len(APfamAnnos)):
        exist = 0
        for Aanno in APfamAnnosList:
            if Aanno == APfamAnnos[anno]:
                exist = 1
                APfamAnnosList[Aanno] += 1
                print("AExist")
                break
        if exist == 0:
            APfamAnnosList[APfamAnnos[anno]] = 1
            print("A New Anno")
    sort_APfamAnnosList = sorted(APfamAnnosList.items(), key = lambda APfamAnnosList: APfamAnnosList[1], reverse = True)

    ### B - sort
    BPfamAnnosList = {}
    for anno in range(0,len(BPfamAnnos)):
        exist = 0
        for Banno in BPfamAnnosList:
            if Banno == BPfamAnnos[anno]:
                exist = 1
                BPfamAnnosList[Banno] += 1
                print("B Exist")
                break
        if exist == 0:
            BPfamAnnosList[BPfamAnnos[anno]] = 1
            print("B New Anno")
    sort_BPfamAnnosList = sorted(BPfamAnnosList.items(), key = lambda BPfamAnnosList: BPfamAnnosList[1], reverse = True)

    ### Chi-Squared ###
    # a -totalNumberCount, b - testedNumberCount, c - matchAnnoTotalCount, d - matchAnnoCount
    a = AGeneCount
    b = BGeneCount
    ### GO Chi-Squared
    GOChiSquareValue = {}
    for testedAnno in sort_BGOAnnosList:
        if testedAnno[0] in AGOAnnosList:
            c = AGOAnnosList[testedAnno[0]]
            d = testedAnno[1]
            n = a+b+c+d
            t = a*d - b-c
            x2 = (n*t*t)/((a+c)*(b+d)*(a+b)*(c+d))
            GOChiSquareValue[testedAnno[0]] = math.sqrt(x2)
    sort_GOChiSquareValue = sorted(GOChiSquareValue.items(), key = lambda GOChiSquareValue: GOChiSquareValue[1], reverse = True)
    output_for_A_GO_count = []
    output_for_B_GO_count = []
    output_go_match_anno = []
    output_go_chi_value = []
    output_go_p_value = []
    output_go_correction = []

    for anno in sort_GOChiSquareValue:
        output_for_A_GO_count.append(AGOAnnosList[anno[0]])
        output_for_B_GO_count.append(BGOAnnosList[anno[0]])
        output_go_match_anno.append(anno[0])
        output_go_chi_value.append("%.5g" %(anno[1]))
        output_go_p_value.append("%.5g" %(1 - stats.chi2.cdf(anno[1], 1)))
        output_go_correction.append("%.5g" %(1-pow(1-(1 - stats.chi2.cdf(anno[1], 1)),1/len(sort_GOChiSquareValue))))

    ### KEGG Chi-Squared
    KEGGChiSquareValue = {}
    for testedAnno in sort_BKEGGAnnosList:
        if testedAnno[0] in AKEGGAnnosList:
            c = AKEGGAnnosList[testedAnno[0]]
            d = testedAnno[1]
            n = a+b+c+d
            t = a*d - b-c
            x2 = (n*t*t)/((a+c)*(b+d)*(a+b)*(c+d))
            KEGGChiSquareValue[testedAnno[0]] = math.sqrt(x2)
    sort_KEGGChiSquareValue = sorted(KEGGChiSquareValue.items(), key = lambda KEGGChiSquareValue: KEGGChiSquareValue[1], reverse = True)

    print("CHI")
    output_for_A_KEGG_count = []
    output_for_B_KEGG_count = []
    output_kegg_match_anno = []
    output_kegg_chi_value = []
    output_kegg_p_value = []
    output_kegg_correction = []

    for anno in sort_KEGGChiSquareValue:
        output_for_A_KEGG_count.append(AKEGGAnnosList[anno[0]])
        output_for_B_KEGG_count.append(BKEGGAnnosList[anno[0]])
        output_kegg_match_anno.append(anno[0])
        output_kegg_chi_value.append("%.5g" %(anno[1]))
        output_kegg_p_value.append("%.5g" %(1 - stats.chi2.cdf(anno[1], 1)))
        output_kegg_correction.append("%.5g" %(1-pow(1-(1 - stats.chi2.cdf(anno[1], 1)),1/len(sort_KEGGChiSquareValue))))

    ### Pfam Chi-Squared
    PfamChiSquareValue = {}
    for testedAnno in sort_BPfamAnnosList:
        if testedAnno[0] in APfamAnnosList:
            c = APfamAnnosList[testedAnno[0]]
            d = testedAnno[1]
            n = a+b+c+d
            t = a*d - b-c
            x2 = (n*t*t)/((a+c)*(b+d)*(a+b)*(c+d))
            PfamChiSquareValue[testedAnno[0]] = math.sqrt(x2)
    sort_PfamChiSquareValue = sorted(PfamChiSquareValue.items(), key = lambda PfamChiSquareValue: PfamChiSquareValue[1], reverse = True)

    print("CHI")
    output_for_A_Pfam_count = []
    output_for_B_Pfam_count = []
    output_Pfam_match_anno = []
    output_Pfam_chi_value = []
    output_Pfam_p_value = []
    output_Pfam_correction = []

    for anno in sort_PfamChiSquareValue:
        output_for_A_Pfam_count.append(APfamAnnosList[anno[0]])
        output_for_B_Pfam_count.append(BPfamAnnosList[anno[0]])
        output_Pfam_match_anno.append(anno[0])
        output_Pfam_chi_value.append("%.5g" %(anno[1]))
        output_Pfam_p_value.append("%.5g" %(1 - stats.chi2.cdf(anno[1], 1)))
        output_Pfam_correction.append("%.5g" %(1-pow(1-(1 - stats.chi2.cdf(anno[1], 1)),1/len(sort_PfamChiSquareValue))))

    return render(request, 'analysis/result.html', {'gidA':gidA, 'gidB':gidB, 'a':a, 'b':b, 'matchAnno':output_go_match_anno, 'matchAnnoTotalCount':output_for_A_GO_count, 'matchAnnoCount':output_for_B_GO_count, 'chiValue':output_go_chi_value, 'pValue':output_go_p_value, 'correction':output_go_correction,'matchKEGGAnno':output_kegg_match_anno, 'matchKEGGAnnoTotalCount':output_for_A_KEGG_count, 'matchKEGGAnnoCount':output_for_B_KEGG_count, 'KEGGchiValue':output_kegg_chi_value, 'KEGGpValue':output_kegg_p_value, 'KEGGcorrection':output_kegg_correction,'matchPfamAnno':output_Pfam_match_anno, 'matchPfamAnnoTotalCount':output_for_A_Pfam_count, 'matchPfamAnnoCount':output_for_B_Pfam_count, 'PfamchiValue':output_Pfam_chi_value, 'PfampValue':output_Pfam_p_value, 'Pfamcorrection':output_Pfam_correction})

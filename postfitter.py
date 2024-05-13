import ROOT

inp_file = "/work/olavoryk/tau_pog_tau_sfs/tau_id_es_main/smhtt_ul/output/datacards_es_4_0_29Apr_morph_v1/2016postVFP_id_es_23Apr_es_4_0_v1-medium_vs_j_29Apr_v1/2016postVFP_tauid_medium/cmb/fitDiagnostics.2016postVFP.root"

file_inp = ROOT.TFile(inp_file)

out_fold = "/work/olavoryk/tau_pog_tau_sfs/tau_id_es_main/smhtt_ul/output/datacards_es_4_0_29Apr_morph_v1/2016postVFP_id_es_23Apr_es_4_0_v1-medium_vs_j_29Apr_v1/2016postVFP_tauid_medium/cmb/"

prefit_fold = "shapes_prefit"
postfit_folder = "shapes_fit_s"

prefit_in_folders_names = []
postfit_in_folders_names = []

prefit_keys = file_inp.Get(prefit_fold).GetListOfKeys()
postfit_keys = file_inp.Get(postfit_folder).GetListOfKeys()


for i in range(len(prefit_keys)):
    prefit_in_folders_names.append(file_inp.Get(prefit_fold).GetListOfKeys()[i].GetName())

for i in range(len(postfit_keys)):
    postfit_in_folders_names.append(file_inp.Get(postfit_folder).GetListOfKeys()[i].GetName())

postfit_in_folders_names

new_file = ROOT.TFile(out_fold+"postfitshape.root", "recreate")

for i in range(len(prefit_in_folders_names)):
    hist_list  = file_inp.Get("shapes_prefit/"+prefit_in_folders_names[i]).GetListOfKeys()

    hist_list_pre = []
    for j in range(len(hist_list)):
        hist_list_pre.append( file_inp.Get("shapes_prefit/"+prefit_in_folders_names[i]).GetListOfKeys()[j].GetName() )
    # print(hist_list_pre)

    new_file.mkdir(prefit_in_folders_names[i]+"_prefit")
    new_file.cd(prefit_in_folders_names[i]+"_prefit")

    for shap in hist_list_pre:
        hist_proc = file_inp.Get("shapes_prefit/"+prefit_in_folders_names[i]+"/"+shap)
        hist_proc.SetTitle("data_obs")
        if shap == "data":
            n = hist_proc.GetN()

            histogram = ROOT.TH1F("data_obs", "data_obs", n, 30, 125 )
            for k in range(1, n+1):
                histogram.SetBinContent(k, hist_proc.GetPointY(k-1))
                histogram.SetBinError(k, hist_proc.GetErrorYhigh(k-1))
            histogram.Write("data_obs")
        else:
            hist_proc.Write()

new_file.Close()

new_file1 = ROOT.TFile(out_fold+"postfitshape.root", "update")

for i in range(len(postfit_in_folders_names)):
    hist_list  = file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]).GetListOfKeys()

    hist_list_post = []
    for j in range(len(hist_list)):
        hist_list_post.append( file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]).GetListOfKeys()[j].GetName() )
    print(hist_list_post)
    

    new_file1.mkdir(postfit_in_folders_names[i]+"_postfit")
    new_file1.cd(postfit_in_folders_names[i]+"_postfit")

    for shap in hist_list_post:
        hist_proc1 = file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]+"/"+shap)
        hist_proc1.SetTitle("data_obs")
        if shap == "data":
            # hist_proc1.Write("data_obs")
            n1 = hist_proc1.GetN()

            
            histogram1 = ROOT.TH1F("data_obs", "data_obs", n, 30, 125 )
            for k in range(1, n+1):
                histogram1.SetBinContent(k, hist_proc1.GetPointY(k-1))
                histogram1.SetBinError(k, hist_proc1.GetErrorYhigh(k-1))
            histogram1.Write("data_obs")
        else:
            hist_proc1.Write()

new_file1.Close()
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

    new_file.mkdir(prefit_in_folders_names[i]+"_prefit")
    new_file.cd(prefit_in_folders_names[i]+"_prefit")

    for shap in hist_list_pre:
        hist_proc = file_inp.Get("shapes_prefit/"+prefit_in_folders_names[i]+"/"+shap)
        hist_proc.Write()

new_file.Close()

new_file1 = ROOT.TFile(out_fold+"postfitshape.root", "update")

for i in range(len(postfit_in_folders_names)):
    hist_list  = file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]).GetListOfKeys()

    hist_list_post = []
    for j in range(len(hist_list)):
        hist_list_post.append( file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]).GetListOfKeys()[j].GetName() )
    

    new_file1.mkdir(postfit_in_folders_names[i]+"_postfit")
    new_file1.cd(postfit_in_folders_names[i]+"_postfit")

    for shap in hist_list_post:
        hist_proc1 = file_inp.Get(postfit_folder+"/"+postfit_in_folders_names[i]+"/"+shap)
        hist_proc1.Write()

new_file1.Close()
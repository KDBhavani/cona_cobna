# -*- coding: utf-8 -*-
"""
Created on Sun May 15 03:32:39 2022

@author: sys
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 15 01:11:05 2022

@author: sys
"""
import json
# import os

cona_matched_data=[]
cobna_matched_data=[]
cona_cobna_matched_data=[]
dummy_cobna_matched_data=[]
dummy_cona_matched_data=[]
parent_matched_data=[]
bu_merged_to_21100_matched_data =[]
bu_move_to_sub_of_21100_matched_data=[]
sub_of_11015_matched_data=[]
bu_move_to_sub_of_21100_matched_data =[]
bu_move_to_sub_of_21100_matched_data =[]
bu_merged_to_21100_matched_data=[]
bu_move_to_sub_of_21100_matched_data=[]
bu_move_to_sub_of_21100_matched_data=[]
bu_move_to_sub_of_21100_becomes_parent_of_11120_matched_data=[]
bu_move_to_sub_of_21100_matched_data=[]
minority_owner_of_11020_and_11080_matched_data=[]
bu_merged_to_21100_matched_data=[]
cofc_elim_matched_data=[]
cona_consol_elim_matched_data=[]
cobna_consol_elim_only_ytd_ni_to_remain_matched_data=[]
move_to_new_cogc_consol_node_matched_data=[]
cofc_us_elim_matched_data=[]
cona_us_elim_matched_data=[]
cobna_us_elim_only_ytd_ni_to_remain_matched_data=[]
cofc_nonus_elim_matched_data=[]
cobna_non_us_elim_should_zero_out_matched_data=[]
nonus_elim_cap1_global_corp_should_zero_out_matched_data=[]
nonus_elim_cap_one_holdings_should_zero_out_matched_data=[]
nonus_elim_cobep_hfs_should_zero_out_matched_data=[]
bu_move_to_cona_for_consolidation_matched_data=[]
bu_to_be_dissolved_pre_lego_matched_data=[]
bu_to_be_dissolved_pre_lego_matched_data=[]
bu_moved_to_sub_of_11105_matched_data=[]
ic_loan_with_11110_to_be_terminated_matched_data=[]
cona_cobna_lst=["21100","11000"]
BU_LST=["10000","11000","11015","11016","11020","11051","11054","11060","11080","11105","11400","12000","22380","EC010","EC097","EC100","EC105","ED010","ED097","ED100","EF010","EF100","EF105","EF120","EF126","11030","11050","11110","11120","12020"]
for file in filelist:
    with open(file)as f:
        data = json.load(f)
    print(type(data))
    data_str = json.dumps(data)

    cona_key = data_str.find("21100")
    cobna_key = data_str.find("11000")
    dummy_cobna_key = data_str.find("DUMMY_COBNA")
    dummy_cona_key = data_str.find("DUMMY_CONA")
    parent_key = data.str.find("10000")
    bu_merged_to_21100_key = data_str.find("11000")
    bu_move_to_sub_of_21100_key = data_str.find("11015")
    sub_of_11015_key = data_str.find("11016")
    bu_move_to_sub_of_21100_key = data_str.find("11020")
    bu_move_to_sub_of_21100_key = data_str.find("11051")
    bu_merged_to_21100_key = data_str.find("11054")
    bu_move_to_sub_of_21100_key = data_str.find("11060")
    bu_move_to_sub_of_21100_key = data_str.find("11080")
    bu_move_to_sub_of_21100_becomes_parent_of_11120_key = data_str.find("11105")
    bu_move_to_sub_of_21100_key = data_str.find("11400")
    minority_owner_of_11020_and_11080_key =  data_str.find("12000")
    bu_merged_to_21100_key = data_str.find("22380")
    cofc_elim_key = data_str.find("EC010")
    cona_consol_elim_key = data_str.find("EC097")
    cobna_consol_elim_only_ytd_ni_to_remain_key = data_str.find("EC100")
    move_to_new_cogc_consol_node_key =  data_str.find("EC105")
    cofc_us_elim_key = data_str.find("ED010")
    cona_us_elim_key = data_str.find("ED097")
    cobna_us_elim_only_ytd_ni_to_remain_key = data_str.find("ED100")
    cofc_nonus_elim_key = data_str.find("EF010")
    cobna_non_us_elim_should_zero_out_key =  data_str.find("EF100")
    nonus_elim_cap1_global_corp_should_zero_out_key = data_str.find("EF105")
    nonus_elim_cap_one_holdings_should_zero_out_key = data_str.find("EF120")
    nonus_elim_cobep_hfs_should_zero_out_key = data_str.find("EF126")
    bu_move_to_cona_for_consolidation_key = data_str.find("11030")
    bu_to_be_dissolved_pre_lego_key = data_str.find("11050")
    bu_to_be_dissolved_pre_lego_key = data_str.find("11110")
    bu_moved_to_sub_of_11105_key = data_str.find("11120")
    ic_loan_with_11110_to_be_terminated_key = data_str.find("12020")
    
    
    if cona_key > 0 and cobna_key ==-1:
        cona_matched_data.append(file)
    elif dummy_cobna_key > 0:
        dummy_cobna_matched_data.append(file)
    elif dummy_cona_key > 0:
        dummy_cona_matched_data.append(file)
    elif cobna_key > 0 and cona_key ==-1:
        cobna_matched_data.append(file)
    elif parent_key > 0:
        parent_matched_data.append(file)
    elif bu_merged_to_21100_key > 0:
        bu_merged_to_21100_matched_data .append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data.append(file)
    elif sub_of_11015_key > 0:
        sub_of_11015_matched_data.append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data .append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data .append(file)
    elif bu_merged_to_21100_key > 0:
        bu_merged_to_21100_matched_data .append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data .append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data .append(file)
    elif bu_move_to_sub_of_21100_becomes_parent_of_11120_key > 0:
        bu_move_to_sub_of_21100_becomes_parent_of_11120_matched_data.append(file)
    elif bu_move_to_sub_of_21100_key > 0:
        bu_move_to_sub_of_21100_matched_data .append(file)
    elif minority_owner_of_11020_and_11080_key > 0:
        minority_owner_of_11020_and_11080_matched_data.append(file)
    elif bu_merged_to_21100_key > 0:
        bu_merged_to_21100_matched_data .append(file)
    elif cofc_elim_key > 0:
        cofc_elim_matched_data.append(file)
    elif cona_consol_elim_key > 0:
        cona_consol_elim_matched_data.append(file)
    elif cobna_consol_elim_only_ytd_ni_to_remain_key > 0:
        cobna_consol_elim_only_ytd_ni_to_remain_matched_data.append(file)
    elif move_to_new_cogc_consol_node_key > 0:
        move_to_new_cogc_consol_node_matched_data.append(file)
    elif cofc_us_elim_key > 0:
        cofc_us_elim_matched_data.append(file)
    elif cona_us_elim_key > 0:
        cona_us_elim_matched_data.append(file)
    elif cobna_us_elim_only_ytd_ni_to_remain_key > 0:
        cobna_us_elim_only_ytd_ni_to_remain_matched_data.append(file)
    elif cofc_nonus_elim_key > 0:
        cofc_nonus_elim_matched_data.append(file)
    elif cobna_non_us_elim_should_zero_out_key > 0:
         cobna_non_us_elim_should_zero_out_matched_data.append(file)
    elif nonus_elim_cap1_global_corp_should_zero_out_key > 0:
        nonus_elim_cap1_global_corp_should_zero_out_matched_data.append(file)
    elif nonus_elim_cap_one_holdings_should_zero_out_key > 0:
        nonus_elim_cap_one_holdings_should_zero_out_matched_data.append(file)
    elif nonus_elim_cobep_hfs_should_zero_out_key > 0:
        nonus_elim_cobep_hfs_should_zero_out_matched_data.append(file)
    elif bu_move_to_cona_for_consolidation_key > 0:
        bu_move_to_cona_for_consolidation_matched_data.append(file)
    elif bu_to_be_dissolved_pre_lego_key > 0:
        bu_to_be_dissolved_pre_lego_matched_data.append(file)
    elif bu_to_be_dissolved_pre_lego_key > 0:
         bu_to_be_dissolved_pre_lego_matched_data.append(file)
    elif bu_moved_to_sub_of_11105_key > 0:
        bu_moved_to_sub_of_11105_matched_data.append(file)
    elif ic_loan_with_11110_to_be_terminated_key > 0:
        ic_loan_with_11110_to_be_terminated_matched_data.append(file)
    if all(x in data_str for x in cona_cobna_lst):
        cona_cobna_matched_data.append(file)
       
        
print("cona_matched_data  results",cona_matched_data)
print("cobna_matched_data  results",cobna_matched_data)
print("cona_cobna_matched_data  results",cona_cobna_matched_data)
print("dummy_cona_matched_data  results",dummy_cona_matched_data)
print("dummy_cobna_matched_data  results",dummy_cobna_matched_data)
print("parent_matched_data  results",parent_matched_data)
print("bu_merged_to_21100_matched_data  results",bu_merged_to_21100_matched_data)
print("bu_move_to_sub_of_21100_matched_data  results",bu_move_to_sub_of_21100_matched_data)
print("sub_of_11015_matched_data  results", sub_of_11015_matched_data)
print("bu_move_to_sub_of_21100_matched_data results", bu_move_to_sub_of_21100_matched_data)
print("bu_move_to_sub_of_21100_matched_data  results",bu_move_to_sub_of_21100_matched_data)
print("bu_merged_to_21100_matched_data  results",bu_merged_to_21100_matched_data)
print("bu_move_to_sub_of_21100_matched_data  results",bu_move_to_sub_of_21100_matched_data)
print("bu_move_to_sub_of_21100_matched_data  results",bu_move_to_sub_of_21100_matched_data)
print("bu_move_to_sub_of_21100_becomes_parent_of_11120_matched_data results", bu_move_to_sub_of_21100_becomes_parent_of_11120_matched_data)
print("bu_move_to_sub_of_21100_matched_data  results",bu_move_to_sub_of_21100_matched_data)
print("minority_owner_of_11020_and_11080_matched_data  results", minority_owner_of_11020_and_11080_matched_data )
print("bu_merged_to_21100_matched_data  results",bu_merged_to_21100_matched_data)
print("cofc_elim_matched_data results", cofc_elim_matched_data)
print("cona_consol_elim_matched_data results",cona_consol_elim_matched_data)
print("cobna_consol_elim_only_ytd_ni_to_remain_matched_data results",cobna_consol_elim_only_ytd_ni_to_remain_matched_data)
print("move_to_new_cogc_consol_node_matched_data results",move_to_new_cogc_consol_node_matched_data)
print("cofc_us_elim_matched_data results", cofc_us_elim_matched_data)
print("cona_us_elim_matched_data results",cona_us_elim_matched_data)
print("cobna_us_elim_only_ytd_ni_to_remain_matched_data results", cobna_us_elim_only_ytd_ni_to_remain_matched_data)
print("cofc_nonus_elim_matched_data results",cofc_nonus_elim_matched_data)
print("cobna_non_us_elim_should_zero_out_matched_data  results", cobna_non_us_elim_should_zero_out_matched_data )
print("nonus_elim_cap1_global_corp_should_zero_out_matched_data  results", nonus_elim_cap1_global_corp_should_zero_out_matched_data )
print("nonus_elim_cap_one_holdings_should_zero_out_matched_data results",nonus_elim_cap_one_holdings_should_zero_out_matched_data)
print("nonus_elim_cobep_hfs_should_zero_out_matched_data results",nonus_elim_cobep_hfs_should_zero_out_matched_data)
print("bu_move_to_cona_for_consolidation_matched_data results", bu_move_to_cona_for_consolidation_matched_data )
print("bu_to_be_dissolved_pre_lego_matched_data results", bu_to_be_dissolved_pre_lego_matched_data)
print("bu_to_be_dissolved_pre_lego_matched_data results",bu_to_be_dissolved_pre_lego_matched_data) 
print("bu_moved_to_sub_of_11105_matched_data results", bu_moved_to_sub_of_11105_matched_data )
print("ic_loan_with_11110_to_be_terminated_matched_data results", ic_loan_with_11110_to_be_terminated_matched_data)


        
    
    
    
    


    
        
        
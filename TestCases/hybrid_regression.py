#!/usr/bin/env python

## \file parallel_regression.py
#  \brief Python script for automated regression testing of SU2 examples
#  \author A. Aranake, A. Campos, T. Economon, T. Lukaczyk, S. Padron
#  \version 7.0.4 "Blackbird"
#
# SU2 Project Website: https://su2code.github.io
# 
# The SU2 Project is maintained by the SU2 Foundation 
# (http://su2foundation.org)
#
# Copyright 2012-2020, SU2 Contributors (cf. AUTHORS.md)
#
# SU2 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# SU2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SU2. If not, see <http://www.gnu.org/licenses/>.

# make print(*args) function available in PY2.6+, does'nt work on PY < 2.6
from __future__ import print_function

import sys
from TestCase import TestCase    

def main():
    '''This program runs SU2 and ensures that the output matches specified values. 
       This will be used to do checks when code is pushed to github 
       to make sure nothing is broken. '''

    test_list = []

    ##########################
    ### Compressible Euler ###
    ##########################

    # Channel
    channel           = TestCase('channel')
    channel.cfg_dir   = "euler/channel"
    channel.cfg_file  = "inv_channel_RK.cfg"
    channel.test_iter = 20
    channel.test_vals = [-2.667326, 2.797439, 0.018717, 0.006906]
    channel.su2_exec  = "SU2_CFD -t 2"
    channel.timeout   = 600
    channel.tol       = 0.00001
    test_list.append(channel)

    # NACA0012 
    naca0012           = TestCase('naca0012')
    naca0012.cfg_dir   = "euler/naca0012"
    naca0012.cfg_file  = "inv_NACA0012_Roe.cfg"
    naca0012.test_iter = 20
    naca0012.test_vals = [-4.023999, -3.515034, 0.339426, 0.022217]
    naca0012.su2_exec  = "SU2_CFD -t 2"
    naca0012.timeout   = 600
    naca0012.tol       = 0.00001
    test_list.append(naca0012)

    # Supersonic wedge 
    wedge           = TestCase('wedge')
    wedge.cfg_dir   = "euler/wedge"
    wedge.cfg_file  = "inv_wedge_HLLC.cfg"
    wedge.test_iter = 20
    wedge.test_vals = [-0.942862, 4.784581, -0.208106, 0.036665]
    wedge.su2_exec  = "SU2_CFD -t 2"
    wedge.timeout   = 600
    wedge.tol       = 0.00001
    test_list.append(wedge)

    # ONERA M6 Wing
    oneram6           = TestCase('oneram6')
    oneram6.cfg_dir   = "euler/oneram6"
    oneram6.cfg_file  = "inv_ONERAM6.cfg"
    oneram6.test_iter = 10
    oneram6.test_vals = [0.281704, 0.011821]
    oneram6.su2_exec  = "SU2_CFD -t 2"
    oneram6.timeout   = 600
    oneram6.tol       = 0.00001
    test_list.append(oneram6)

    # Fixed CL NACA0012
    fixedCL_naca0012           = TestCase('fixedcl_naca0012')
    fixedCL_naca0012.cfg_dir   = "fixed_cl/naca0012"
    fixedCL_naca0012.cfg_file  = "inv_NACA0012.cfg"
    fixedCL_naca0012.test_iter = 10
    fixedCL_naca0012.test_vals = [-12.130263, -6.703735, 0.300000, 0.019470]
    fixedCL_naca0012.su2_exec  = "SU2_CFD -t 2"
    fixedCL_naca0012.timeout   = 600
    fixedCL_naca0012.tol       = 0.00001
    test_list.append(fixedCL_naca0012)

    # HYPERSONIC FLOW PAST BLUNT BODY          
    bluntbody           = TestCase('bluntbody')
    bluntbody.cfg_dir   = "euler/bluntbody"
    bluntbody.cfg_file  = "blunt.cfg"
    bluntbody.test_iter = 20
    bluntbody.test_vals = [0.540010, 6.916656, 0.000027, 1.869004]
    bluntbody.su2_exec  = "SU2_CFD -t 2"
    bluntbody.timeout   = 600
    bluntbody.tol       = 0.00001
    test_list.append(bluntbody)

    ##########################
    ###  Compressible N-S  ###
    ##########################

    # Laminar flat plate
    flatplate           = TestCase('flatplate')
    flatplate.cfg_dir   = "navierstokes/flatplate"
    flatplate.cfg_file  = "lam_flatplate.cfg"
    flatplate.test_iter = 20
    flatplate.test_vals = [-4.680775, 0.781235, -0.135957, 0.022978]
    flatplate.su2_exec  = "SU2_CFD -t 2"
    flatplate.timeout   = 600
    flatplate.tol       = 0.00001
    test_list.append(flatplate)

    # Laminar cylinder (steady)
    cylinder           = TestCase('cylinder')
    cylinder.cfg_dir   = "navierstokes/cylinder"
    cylinder.cfg_file  = "lam_cylinder.cfg"
    cylinder.test_iter = 25
    cylinder.test_vals = [-6.765432, -1.297428, 0.019596, 0.310245]
    cylinder.su2_exec  = "SU2_CFD -t 2"
    cylinder.timeout   = 600
    cylinder.tol       = 0.00001
    test_list.append(cylinder)

    # Laminar cylinder (low Mach correction)
    cylinder_lowmach           = TestCase('cylinder_lowmach')
    cylinder_lowmach.cfg_dir   = "navierstokes/cylinder"
    cylinder_lowmach.cfg_file  = "cylinder_lowmach.cfg"
    cylinder_lowmach.test_iter = 25
    cylinder_lowmach.test_vals = [-6.850130, -1.388096, -0.056203, 108.140820]
    cylinder_lowmach.su2_exec  = "SU2_CFD -t 2"
    cylinder_lowmach.timeout   = 600
    cylinder_lowmach.tol       = 0.00001
    test_list.append(cylinder_lowmach)

    # 2D Poiseuille flow (body force driven with periodic inlet / outlet)
    poiseuille           = TestCase('poiseuille')
    poiseuille.cfg_dir   = "navierstokes/poiseuille"
    poiseuille.cfg_file  = "lam_poiseuille.cfg"
    poiseuille.test_iter = 10
    poiseuille.test_vals = [-5.048279, 0.650817, 0.008715, 13.677768]
    poiseuille.su2_exec  = "SU2_CFD -t 2"
    poiseuille.timeout   = 600
    poiseuille.tol       = 0.001
    test_list.append(poiseuille)

    # 2D Poiseuille flow (inlet profile file)
    poiseuille_profile           = TestCase('poiseuille_profile')
    poiseuille_profile.cfg_dir   = "navierstokes/poiseuille"
    poiseuille_profile.cfg_file  = "profile_poiseuille.cfg"
    poiseuille_profile.test_iter = 10
    poiseuille_profile.test_vals = [-12.494741, -7.712718, -0.000000, 2.085796]
    poiseuille_profile.su2_exec  = "SU2_CFD -t 2"
    poiseuille_profile.timeout   = 600
    poiseuille_profile.tol       = 0.00001
    test_list.append(poiseuille_profile)

    ##########################
    ### Compressible RANS  ###
    ##########################

    # RAE2822 SA
    rae2822_sa           = TestCase('rae2822_sa')
    rae2822_sa.cfg_dir   = "rans/rae2822"
    rae2822_sa.cfg_file  = "turb_SA_RAE2822.cfg"
    rae2822_sa.test_iter = 20
    rae2822_sa.test_vals = [-2.021218, -5.268447, 0.807465, 0.060897]
    rae2822_sa.su2_exec  = "SU2_CFD -t 2"
    rae2822_sa.timeout   = 600
    rae2822_sa.tol       = 0.00001
    test_list.append(rae2822_sa)
    
    # RAE2822 SST
    rae2822_sst           = TestCase('rae2822_sst')
    rae2822_sst.cfg_dir   = "rans/rae2822"
    rae2822_sst.cfg_file  = "turb_SST_RAE2822.cfg"
    rae2822_sst.test_iter = 20
    rae2822_sst.test_vals = [-0.510637, 4.876603, 0.812485, 0.061969]
    rae2822_sst.su2_exec  = "SU2_CFD -t 2"
    rae2822_sst.timeout   = 600
    rae2822_sst.tol       = 0.00001
    test_list.append(rae2822_sst)

    # RAE2822 SST_SUST
    rae2822_sst_sust           = TestCase('rae2822_sst_sust')
    rae2822_sst_sust.cfg_dir   = "rans/rae2822"
    rae2822_sst_sust.cfg_file  = "turb_SST_SUST_RAE2822.cfg"
    rae2822_sst_sust.test_iter = 20
    rae2822_sst_sust.test_vals = [-2.429813, 4.876602, 0.812485, 0.061969]
    rae2822_sst_sust.su2_exec  = "SU2_CFD -t 2"
    rae2822_sst_sust.timeout   = 600
    rae2822_sst_sust.tol       = 0.00001
    test_list.append(rae2822_sst_sust)

    # Flat plate
    turb_flatplate           = TestCase('turb_flatplate')
    turb_flatplate.cfg_dir   = "rans/flatplate"
    turb_flatplate.cfg_file  = "turb_SA_flatplate.cfg"
    turb_flatplate.test_iter = 20
    turb_flatplate.test_vals = [-4.157169, -6.737133, -0.176253, 0.057446]
    turb_flatplate.su2_exec  = "SU2_CFD -t 2"
    turb_flatplate.timeout   = 600
    turb_flatplate.tol       = 0.00001
    test_list.append(turb_flatplate)

    # ONERA M6 Wing
    turb_oneram6           = TestCase('turb_oneram6')
    turb_oneram6.cfg_dir   = "rans/oneram6"
    turb_oneram6.cfg_file  = "turb_ONERAM6.cfg"
    turb_oneram6.test_iter = 10
    turb_oneram6.test_vals = [-2.372345, -6.579369, 0.229866, 0.147638]
    turb_oneram6.su2_exec  = "SU2_CFD -t 2"
    turb_oneram6.timeout   = 600
    turb_oneram6.tol       = 0.00001
    test_list.append(turb_oneram6)

    # NACA0012 (SA, FUN3D finest grid results: CL=1.0983, CD=0.01242)
    turb_naca0012_sa           = TestCase('turb_naca0012_sa')
    turb_naca0012_sa.cfg_dir   = "rans/naca0012"
    turb_naca0012_sa.cfg_file  = "turb_NACA0012_sa.cfg"
    turb_naca0012_sa.test_iter = 10
    turb_naca0012_sa.test_vals = [-12.076423, -16.147693, 1.064326, 0.019770]
    turb_naca0012_sa.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_sa.timeout   = 600
    turb_naca0012_sa.tol       = 0.00001
    test_list.append(turb_naca0012_sa)
    
    # NACA0012 (SST, FUN3D finest grid results: CL=1.0840, CD=0.01253)
    turb_naca0012_sst           = TestCase('turb_naca0012_sst')
    turb_naca0012_sst.cfg_dir   = "rans/naca0012"
    turb_naca0012_sst.cfg_file  = "turb_NACA0012_sst.cfg"
    turb_naca0012_sst.test_iter = 10
    turb_naca0012_sst.test_vals = [-15.273727, -6.243780, 1.049988, 0.019165]
    turb_naca0012_sst.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_sst.timeout   = 600
    turb_naca0012_sst.tol       = 0.00001
    test_list.append(turb_naca0012_sst)

    # NACA0012 (SST_SUST, FUN3D finest grid results: CL=1.0840, CD=0.01253)
    turb_naca0012_sst_sust           = TestCase('turb_naca0012_sst_sust')
    turb_naca0012_sst_sust.cfg_dir   = "rans/naca0012"
    turb_naca0012_sst_sust.cfg_file  = "turb_NACA0012_sst_sust.cfg"
    turb_naca0012_sst_sust.test_iter = 10
    turb_naca0012_sst_sust.test_vals = [-14.851214, -6.062557, 1.005233, 0.019014]
    turb_naca0012_sst_sust.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_sst_sust.timeout   = 600
    turb_naca0012_sst_sust.tol       = 0.00001
    test_list.append(turb_naca0012_sst_sust)

    # PROPELLER
    propeller           = TestCase('propeller')
    propeller.cfg_dir   = "rans/propeller"
    propeller.cfg_file  = "propeller.cfg"
    propeller.test_iter = 10
    propeller.test_vals = [-3.389576, -8.409529, 0.000048, 0.056329]
    propeller.su2_exec  = "SU2_CFD -t 2"
    propeller.timeout   = 600
    propeller.tol       = 0.00001
    test_list.append(propeller)
    
    #################################
    ## Compressible RANS Restart  ###
    #################################
    
    # NACA0012 SST Multigrid restart
    turb_naca0012_sst_restart_mg           = TestCase('turb_naca0012_sst_restart_mg')
    turb_naca0012_sst_restart_mg.cfg_dir   = "rans/naca0012"
    turb_naca0012_sst_restart_mg.cfg_file  = "turb_NACA0012_sst_multigrid_restart.cfg"
    turb_naca0012_sst_restart_mg.test_iter = 20
    turb_naca0012_sst_restart_mg.ntest_vals = 5
    turb_naca0012_sst_restart_mg.test_vals = [-7.653296, -7.729472, -1.981061, -0.000016, 0.079062]
    turb_naca0012_sst_restart_mg.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_sst_restart_mg.timeout   = 600
    turb_naca0012_sst_restart_mg.tol       = 0.000001
    test_list.append(turb_naca0012_sst_restart_mg)

    #############################
    ### Compressibele RANS UQ ###
    #############################

    # NACA0012 1c
    turb_naca0012_1c           = TestCase('turb_naca0012_1c')
    turb_naca0012_1c.cfg_dir   = "rans_uq/naca0012"
    turb_naca0012_1c.cfg_file  = "turb_NACA0012_uq_1c.cfg"
    turb_naca0012_1c.test_iter = 10
    turb_naca0012_1c.test_vals = [-4.906594, 1.338035, 6.086178, 2.412995]
    turb_naca0012_1c.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_1c.timeout   = 600
    turb_naca0012_1c.tol       = 0.00001
    test_list.append(turb_naca0012_1c)

    # NACA0012 2c
    turb_naca0012_2c           = TestCase('turb_naca0012_2c')
    turb_naca0012_2c.cfg_dir   = "rans_uq/naca0012"
    turb_naca0012_2c.cfg_file  = "turb_NACA0012_uq_2c.cfg"
    turb_naca0012_2c.test_iter = 10
    turb_naca0012_2c.test_vals = [-5.230219, 1.262228, 6.086155, 2.412757]
    turb_naca0012_2c.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_2c.timeout   = 600
    turb_naca0012_2c.tol       = 0.00001
    test_list.append(turb_naca0012_2c)

    # NACA0012 3c
    turb_naca0012_3c           = TestCase('turb_naca0012_3c')
    turb_naca0012_3c.cfg_dir   = "rans_uq/naca0012"
    turb_naca0012_3c.cfg_file  = "turb_NACA0012_uq_3c.cfg"
    turb_naca0012_3c.test_iter = 10
    turb_naca0012_3c.test_vals = [-5.277130, 1.246265, 6.086050, 2.412462]
    turb_naca0012_3c.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_3c.timeout   = 600
    turb_naca0012_3c.tol       = 0.00001
    test_list.append(turb_naca0012_3c)

    # NACA0012 p1c1
    turb_naca0012_p1c1           = TestCase('turb_naca0012_p1c1')
    turb_naca0012_p1c1.cfg_dir   = "rans_uq/naca0012"
    turb_naca0012_p1c1.cfg_file  = "turb_NACA0012_uq_p1c1.cfg"
    turb_naca0012_p1c1.test_iter = 10
    turb_naca0012_p1c1.test_vals = [-5.012853, 1.310014, 6.086064, 2.412930]
    turb_naca0012_p1c1.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_p1c1.timeout   = 600
    turb_naca0012_p1c1.tol       = 0.00001
    test_list.append(turb_naca0012_p1c1)

    # NACA0012 p1c2
    turb_naca0012_p1c2           = TestCase('turb_naca0012_p1c2')
    turb_naca0012_p1c2.cfg_dir   = "rans_uq/naca0012"
    turb_naca0012_p1c2.cfg_file  = "turb_NACA0012_uq_p1c2.cfg"
    turb_naca0012_p1c2.test_iter = 10
    turb_naca0012_p1c2.test_vals = [-5.264020, 1.251315, 6.086450, 2.413069]
    turb_naca0012_p1c2.su2_exec  = "SU2_CFD -t 2"
    turb_naca0012_p1c2.timeout   = 600
    turb_naca0012_p1c2.tol       = 0.00001
    test_list.append(turb_naca0012_p1c2)

    ######################################                                                                                  
    ### Harmonic Balance               ###                                                                                  
    ######################################                                                                                    

    # Description of the regression test 
    harmonic_balance           = TestCase('harmonic_balance')
    harmonic_balance.cfg_dir   = "harmonic_balance"
    harmonic_balance.cfg_file  = "HB.cfg"
    harmonic_balance.test_iter = 25
    harmonic_balance.test_vals = [-1.589863, 3.922098, -0.001443, 0.099457]
    harmonic_balance.su2_exec  = "SU2_CFD -t 2"
    harmonic_balance.timeout   = 600
    harmonic_balance.tol       = 0.00001
    harmonic_balance.new_output = False
    test_list.append(harmonic_balance)

    # Turbulent pitching NACA 64a010 airfoil
    hb_rans_preconditioning           = TestCase('hb_rans_preconditioning')
    hb_rans_preconditioning.cfg_dir   = "harmonic_balance/hb_rans_preconditioning"
    hb_rans_preconditioning.cfg_file  = "davis.cfg"
    hb_rans_preconditioning.test_iter = 25
    hb_rans_preconditioning.test_vals = [-1.909633, -5.954752, 0.007773, 0.131217]
    hb_rans_preconditioning.su2_exec  = "SU2_CFD -t 2"
    hb_rans_preconditioning.timeout   = 600
    hb_rans_preconditioning.tol       = 0.00001
    hb_rans_preconditioning.new_output = False
    test_list.append(hb_rans_preconditioning)

    ######################################
    ### Moving Wall                    ###
    ######################################

    # Lid-driven cavity
    cavity           = TestCase('cavity')
    cavity.cfg_dir   = "moving_wall/cavity"
    cavity.cfg_file  = "lam_cavity.cfg"
    cavity.test_iter = 25
    cavity.test_vals = [-5.627934, -0.164469, 0.051998, 2.547062]
    cavity.su2_exec  = "SU2_CFD -t 2"
    cavity.timeout   = 600
    cavity.tol       = 0.00001
    test_list.append(cavity)

    # Spinning cylinder
    spinning_cylinder           = TestCase('spinning_cylinder')
    spinning_cylinder.cfg_dir   = "moving_wall/spinning_cylinder"
    spinning_cylinder.cfg_file  = "spinning_cylinder.cfg"
    spinning_cylinder.test_iter = 25
    spinning_cylinder.test_vals = [-7.996310, -2.601760, 1.510694, 1.493879]
    spinning_cylinder.su2_exec  = "SU2_CFD -t 2"
    spinning_cylinder.timeout   = 600
    spinning_cylinder.tol       = 0.00001
    test_list.append(spinning_cylinder)

    ######################################
    ### Unsteady                       ###
    ######################################

    # Square cylinder
    square_cylinder           = TestCase('square_cylinder')
    square_cylinder.cfg_dir   = "unsteady/square_cylinder"
    square_cylinder.cfg_file  = "turb_square.cfg"
    square_cylinder.test_iter = 3
    square_cylinder.test_vals = [-1.162563, 0.066395, 1.399790, 2.220393]
    square_cylinder.su2_exec  = "SU2_CFD -t 2"
    square_cylinder.timeout   = 600
    square_cylinder.tol       = 0.00001
    square_cylinder.unsteady  = True
    test_list.append(square_cylinder)

    # Gust
    sine_gust           = TestCase('sine_gust')
    sine_gust.cfg_dir   = "gust"
    sine_gust.cfg_file  = "inv_gust_NACA0012.cfg"
    sine_gust.test_iter = 5
    sine_gust.test_vals = [-1.977545, 3.481778, -0.001667, -0.007429]
    sine_gust.su2_exec  = "SU2_CFD -t 2"
    sine_gust.timeout   = 600
    sine_gust.tol       = 0.00001
    sine_gust.unsteady  = True
    test_list.append(sine_gust)

    # Aeroelastic
    aeroelastic           = TestCase('aeroelastic')
    aeroelastic.cfg_dir   = "aeroelastic"
    aeroelastic.cfg_file  = "aeroelastic_NACA64A010.cfg"
    aeroelastic.test_iter = 2
    aeroelastic.test_vals = [0.079009, 0.033187, -0.001665, -0.000156]
    aeroelastic.su2_exec  = "SU2_CFD -t 2"
    aeroelastic.timeout   = 600
    aeroelastic.tol       = 0.00001
    aeroelastic.unsteady  = True
    test_list.append(aeroelastic)

    # Delayed Detached Eddy Simulation
    ddes_flatplate        = TestCase('ddes_flatplate')
    ddes_flatplate.cfg_dir   = "ddes/flatplate"
    ddes_flatplate.cfg_file  = "ddes_flatplate.cfg"
    ddes_flatplate.test_iter = 10
    ddes_flatplate.test_vals = [-2.714758, -5.883004, -0.215005, 0.023783]
    ddes_flatplate.su2_exec  = "SU2_CFD -t 2"
    ddes_flatplate.timeout   = 600
    ddes_flatplate.tol       = 0.00001
    ddes_flatplate.unsteady  = True
    test_list.append(ddes_flatplate)    

    ######################################
    ### NICFD                          ###
    ######################################	

    # Rarefaction shock wave edge_VW
    edge_VW           = TestCase('edge_VW')
    edge_VW.cfg_dir   = "nicf/edge"
    edge_VW.cfg_file  = "edge_VW.cfg"
    edge_VW.test_iter = 100
    edge_VW.test_vals = [-5.040282, 1.124488, -0.000009, 0.000000]
    edge_VW.su2_exec  = "SU2_CFD -t 2"
    edge_VW.timeout   = 600
    edge_VW.tol       = 0.00001
    test_list.append(edge_VW)

    # Rarefaction shock wave edge_PPR
    edge_PPR           = TestCase('edge_PPR')
    edge_PPR.cfg_dir   = "nicf/edge"
    edge_PPR.cfg_file  = "edge_PPR.cfg"
    edge_PPR.test_iter = 100
    edge_PPR.test_vals = [-5.401709, 0.738096, -0.000035, 0.000000]
    edge_PPR.su2_exec  = "SU2_CFD -t 2"
    edge_PPR.timeout   = 600
    edge_PPR.tol       = 0.00001
    test_list.append(edge_PPR)
    
    ######################################
    ### Turbomachinery                 ###
    ######################################	

    # Jones APU Turbocharger
    Jones_tc           = TestCase('jones_turbocharger')
    Jones_tc.cfg_dir   = "turbomachinery/APU_turbocharger"
    Jones_tc.cfg_file  = "Jones.cfg"
    Jones_tc.test_iter = 5
    Jones_tc.test_vals = [-5.280316, 0.379652, 44.725470, 2.271540]
    Jones_tc.su2_exec  = "SU2_CFD -t 2"
    Jones_tc.timeout   = 600
    Jones_tc.new_output = False
    Jones_tc.tol       = 0.00001
    test_list.append(Jones_tc)

	# Jones APU Turbocharger restart
    Jones_tc_rst           = TestCase('jones_turbocharger_restart')
    Jones_tc_rst.cfg_dir   = "turbomachinery/APU_turbocharger"
    Jones_tc_rst.cfg_file  = "Jones_rst.cfg"
    Jones_tc_rst.test_iter = 5
    Jones_tc_rst.test_vals = [-4.625318, -1.569633, 34.014100, 10.187650]
    Jones_tc_rst.su2_exec  = "SU2_CFD -t 2"
    Jones_tc_rst.timeout   = 600
    Jones_tc_rst.new_output = False
    Jones_tc_rst.tol       = 0.00001
    test_list.append(Jones_tc_rst)

    # 2D axial stage
    axial_stage2D           = TestCase('axial_stage2D')
    axial_stage2D.cfg_dir   = "turbomachinery/axial_stage_2D"
    axial_stage2D.cfg_file  = "Axial_stage2D.cfg"
    axial_stage2D.test_iter = 20
    axial_stage2D.test_vals = [-1.933199, 5.381564, 73.357910, 1.780510]
    axial_stage2D.su2_exec  = "SU2_CFD -t 2"
    axial_stage2D.timeout   = 600
    axial_stage2D.new_output = False
    axial_stage2D.tol       = 0.00001
    test_list.append(axial_stage2D)
    
    # 2D transonic stator
    transonic_stator           = TestCase('transonic_stator')
    transonic_stator.cfg_dir   = "turbomachinery/transonic_stator_2D"
    transonic_stator.cfg_file  = "transonic_stator.cfg"
    transonic_stator.test_iter = 20
    transonic_stator.test_vals = [-0.563532, 5.823231, 96.736000, 0.062426]
    transonic_stator.su2_exec  = "SU2_CFD -t 2"
    transonic_stator.timeout   = 600
    transonic_stator.new_output = False
    transonic_stator.tol       = 0.00001
    test_list.append(transonic_stator)
    
    # 2D transonic stator restart
    transonic_stator_rst           = TestCase('transonic_stator_restart')
    transonic_stator_rst.cfg_dir   = "turbomachinery/transonic_stator_2D"
    transonic_stator_rst.cfg_file  = "transonic_stator_rst.cfg"
    transonic_stator_rst.test_iter = 20
    transonic_stator_rst.test_vals = [-6.621624, -0.614368, 5.002986, 0.002951]
    transonic_stator_rst.su2_exec  = "SU2_CFD -t 2"
    transonic_stator_rst.timeout   = 600
    transonic_stator_rst.new_output = False
    transonic_stator_rst.tol       = 0.00001
    test_list.append(transonic_stator_rst)

    ######################################
    ### Sliding Mesh                   ###
    ######################################

    # Uniform flow
    uniform_flow         = TestCase('uniform_flow')
    uniform_flow.cfg_dir   = "sliding_interface/uniform_flow"
    uniform_flow.cfg_file  = "uniform_NN.cfg"
    uniform_flow.test_iter = 5
    uniform_flow.test_vals = [5.000000, 0.000000, -0.188748, -10.631524]
    uniform_flow.su2_exec  = "SU2_CFD -t 2"
    uniform_flow.timeout   = 600
    uniform_flow.tol       = 0.000001
    uniform_flow.unsteady  = True
    uniform_flow.multizone = True
    test_list.append(uniform_flow) 

    # Channel_2D
    channel_2D           = TestCase('channel_2D')
    channel_2D.cfg_dir   = "sliding_interface/channel_2D"
    channel_2D.cfg_file  = "channel_2D_WA.cfg"
    channel_2D.test_iter = 2
    channel_2D.test_vals = [2.000000, 0.000000, 0.397938, 0.352783, 0.405451]
    channel_2D.su2_exec  = "SU2_CFD -t 2"
    channel_2D.timeout   = 100
    channel_2D.tol       = 0.00001
    channel_2D.unsteady  = True
    channel_2D.multizone = True
    test_list.append(channel_2D)

    # Channel_3D
    channel_3D           = TestCase('channel_3D')
    channel_3D.cfg_dir   = "sliding_interface/channel_3D"
    channel_3D.cfg_file  = "channel_3D_WA.cfg"
    channel_3D.test_iter = 2
    channel_3D.test_vals = [2.000000, 0.000000, 0.620157, 0.505143, 0.415205]
    channel_3D.su2_exec  = "SU2_CFD -t 2"
    channel_3D.timeout   = 600
    channel_3D.tol       = 0.00001
    channel_3D.unsteady  = True
    channel_3D.multizone = True
    test_list.append(channel_3D)

    # Pipe
    pipe           = TestCase('pipe')
    pipe.cfg_dir   = "sliding_interface/pipe"
    pipe.cfg_file  = "pipe_NN.cfg"
    pipe.test_iter = 2
    pipe.test_vals = [0.150024, 0.491949, 0.677756, 0.963990, 1.006943]
    pipe.su2_exec  = "SU2_CFD -t 2"
    pipe.timeout   = 600
    pipe.tol       = 0.00001
    pipe.unsteady  = True
    pipe.multizone = True
    test_list.append(pipe)

    # Rotating cylinders
    rotating_cylinders           = TestCase('rotating_cylinders')
    rotating_cylinders.cfg_dir   = "sliding_interface/rotating_cylinders"
    rotating_cylinders.cfg_file  = "rot_cylinders_WA.cfg"
    rotating_cylinders.test_iter = 3
    rotating_cylinders.test_vals = [3.000000, 0.000000, 0.777267, 1.134746, 1.224125]
    rotating_cylinders.su2_exec  = "SU2_CFD -t 2"
    rotating_cylinders.timeout   = 600
    rotating_cylinders.tol       = 0.00001
    rotating_cylinders.unsteady  = True
    rotating_cylinders.multizone  = True
    test_list.append(rotating_cylinders)

    # Supersonic vortex shedding
    supersonic_vortex_shedding           = TestCase('supersonic_vortex_shedding')
    supersonic_vortex_shedding.cfg_dir   = "sliding_interface/supersonic_vortex_shedding"
    supersonic_vortex_shedding.cfg_file  = "sup_vor_shed_WA.cfg"
    supersonic_vortex_shedding.test_iter = 5
    supersonic_vortex_shedding.test_vals = [5.000000, 0.000000, 1.216554, 1.639121]
    supersonic_vortex_shedding.su2_exec  = "SU2_CFD -t 2"
    supersonic_vortex_shedding.timeout   = 600
    supersonic_vortex_shedding.tol       = 0.00001
    supersonic_vortex_shedding.unsteady  = True
    supersonic_vortex_shedding.multizone  = True
    test_list.append(supersonic_vortex_shedding)

    # Bars_SST_2D
    bars_SST_2D           = TestCase('bars_SST_2D')
    bars_SST_2D.cfg_dir   = "sliding_interface/bars_SST_2D"
    bars_SST_2D.cfg_file  = "bars.cfg"
    bars_SST_2D.test_iter = 13
    bars_SST_2D.test_vals = [13.000000, -0.619179, -1.564701]
    bars_SST_2D.su2_exec  = "SU2_CFD -t 2"
    bars_SST_2D.timeout   = 600
    bars_SST_2D.tol       = 0.00001
    bars_SST_2D.multizone = True
    test_list.append(bars_SST_2D)

    ##########################
    ### FEA - FSI          ###
    ##########################   

    # Static beam, 3d
    statbeam3d           = TestCase('statbeam3d')
    statbeam3d.cfg_dir   = "fea_fsi/StatBeam_3d"
    statbeam3d.cfg_file  = "configBeam_3d.cfg"
    statbeam3d.test_iter = 0
    statbeam3d.test_vals = [-8.500954, -8.212289, -8.117113, 64095.000000]
    statbeam3d.su2_exec  = "SU2_CFD -t 2"
    statbeam3d.timeout   = 600
    statbeam3d.tol       = 0.00001
    test_list.append(statbeam3d)

    # Dynamic beam, 2d
    dynbeam2d           = TestCase('dynbeam2d')
    dynbeam2d.cfg_dir   = "fea_fsi/DynBeam_2d"
    dynbeam2d.cfg_file  = "configBeam_2d.cfg"
    dynbeam2d.test_iter = 6
    dynbeam2d.test_vals = [-3.240015, 2.895057, -0.353146, 66127.000000]
    dynbeam2d.su2_exec  = "SU2_CFD -t 2"
    dynbeam2d.timeout   = 600
    dynbeam2d.unsteady  = True
    dynbeam2d.tol       = 0.00001
    test_list.append(dynbeam2d)

    # FSI, 2d
    fsi2d           = TestCase('fsi2d')
    fsi2d.cfg_dir   = "fea_fsi/WallChannel_2d"
    fsi2d.cfg_file  = "configFSI.cfg"
    fsi2d.test_iter = 4
    fsi2d.test_vals = [4.000000, 0.000000, -3.764089, -4.081119]
    fsi2d.su2_exec  = "SU2_CFD -t 2"
    fsi2d.timeout   = 600
    fsi2d.multizone= True
    fsi2d.unsteady = True
    fsi2d.tol       = 0.00001
    test_list.append(fsi2d)
    
    # FSI, Static, 2D, new mesh solver
    stat_fsi           = TestCase('stat_fsi')
    stat_fsi.cfg_dir   = "fea_fsi/stat_fsi"
    stat_fsi.cfg_file  = "config.cfg"
    stat_fsi.test_iter = 7
    stat_fsi.test_vals = [-3.242709, -4.866601, 0.000000, 11.000000]
    stat_fsi.su2_exec  = "SU2_CFD -t 2"
    stat_fsi.multizone = True
    stat_fsi.timeout   = 600
    stat_fsi.tol       = 0.00001
    test_list.append(stat_fsi)

    # FSI, Dynamic, 2D, new mesh solver
    dyn_fsi           = TestCase('dyn_fsi')
    dyn_fsi.cfg_dir   = "fea_fsi/dyn_fsi"
    dyn_fsi.cfg_file  = "config.cfg"
    dyn_fsi.test_iter = 4
    dyn_fsi.test_vals = [-4.379823, -4.005990, 0.000000, 0.000000]
    dyn_fsi.multizone = True
    dyn_fsi.unsteady  = True
    dyn_fsi.su2_exec  = "SU2_CFD -t 2"
    dyn_fsi.timeout   = 600
    dyn_fsi.tol       = 0.00001
    test_list.append(dyn_fsi)

    # FSI, Static, 2D, new mesh solver, restart
    stat_fsi_restart           = TestCase('stat_fsi_restart')
    stat_fsi_restart.cfg_dir   = "fea_fsi/stat_fsi"
    stat_fsi_restart.cfg_file  = "config_restart.cfg"
    stat_fsi_restart.test_iter = 1
    stat_fsi_restart.test_vals = [-3.474236, -4.250645, 0.000000, 35.000000]
    stat_fsi_restart.su2_exec  = "SU2_CFD -t 2"
    stat_fsi_restart.multizone = True
    stat_fsi_restart.timeout   = 600
    stat_fsi_restart.tol       = 0.00001
    test_list.append(stat_fsi_restart)

    ##############################################
    ### Method of Manufactured Solutions (MMS) ###
    ##############################################

    # FVM, compressible, laminar N-S
    mms_fvm_ns           = TestCase('mms_fvm_ns')
    mms_fvm_ns.cfg_dir   = "mms/fvm_navierstokes"
    mms_fvm_ns.cfg_file  = "lam_mms_roe.cfg"
    mms_fvm_ns.test_iter = 20
    mms_fvm_ns.test_vals = [-2.851428, 2.192348, 0.000000, 0.000000]
    mms_fvm_ns.su2_exec  = "SU2_CFD -t 2"
    mms_fvm_ns.timeout   = 600
    mms_fvm_ns.tol       = 0.0001
    test_list.append(mms_fvm_ns)
    
    ######################################
    ### RUN TESTS                      ###
    ######################################
    
    pass_list = [ test.run_test() for test in test_list ]

    # Tests summary
    print('==================================================================')
    print('Summary of the parallel tests')
    print('python version:', sys.version)
    for i, test in enumerate(test_list):
        if (pass_list[i]):
            print('  passed - %s'%test.tag)
        else:
            print('* FAILED - %s'%test.tag)

    if all(pass_list):
        sys.exit(0)
    else:
        sys.exit(1)
    # done

if __name__ == '__main__':
    main()

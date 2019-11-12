/*!
 * \file CAdjElasticityOutput.cpp
 * \brief Main subroutines for elasticity discrete adjoint output
 * \author R. Sanchez
 * \version 6.2.0 "Falcon"
 *
 * The current SU2 release has been coordinated by the
 * SU2 International Developers Society <www.su2devsociety.org>
 * with selected contributions from the open-source community.
 *
 * The main research teams contributing to the current release are:
 *  - Prof. Juan J. Alonso's group at Stanford University.
 *  - Prof. Piero Colonna's group at Delft University of Technology.
 *  - Prof. Nicolas R. Gauger's group at Kaiserslautern University of Technology.
 *  - Prof. Alberto Guardone's group at Polytechnic University of Milan.
 *  - Prof. Rafael Palacios' group at Imperial College London.
 *  - Prof. Vincent Terrapon's group at the University of Liege.
 *  - Prof. Edwin van der Weide's group at the University of Twente.
 *  - Lab. of New Concepts in Aeronautics at Tech. Institute of Aeronautics.
 *
 * Copyright 2012-2018, Francisco D. Palacios, Thomas D. Economon,
 *                      Tim Albring, and the SU2 contributors.
 *
 * SU2 is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * SU2 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with SU2. If not, see <http://www.gnu.org/licenses/>.
 */

#include "../../include/output/CAdjElasticityOutput.hpp"

#include "../../../Common/include/geometry_structure.hpp"
#include "../../include/solver_structure.hpp"

CAdjElasticityOutput::CAdjElasticityOutput(CConfig *config, unsigned short nDim) : COutput(config, nDim, false) {

  /*--- Initialize number of variables ---*/
  nVar_FEM = nDim;

  /*--- Set the default history fields if nothing is set in the config file ---*/

  if (nRequestedHistoryFields == 0){
    requestedHistoryFields.emplace_back("ITER");
    requestedHistoryFields.emplace_back("RESIDUALS");
    requestedHistoryFields.emplace_back("SENSITIVITY");
    nRequestedHistoryFields = requestedHistoryFields.size();
  }

  if (nRequestedScreenFields == 0){
    if (multiZone) requestedScreenFields.emplace_back("OUTER_ITER");
    requestedScreenFields.emplace_back("INNER_ITER");
    requestedScreenFields.emplace_back("ADJOINT_DISP_X");
    requestedScreenFields.emplace_back("ADJOINT_DISP_Y");
    requestedScreenFields.emplace_back("SENS_E");
    requestedScreenFields.emplace_back("SENS_NU");
    nRequestedScreenFields = requestedScreenFields.size();
  }

  if (nRequestedVolumeFields == 0){
    requestedVolumeFields.emplace_back("COORDINATES");
    requestedVolumeFields.emplace_back("SOLUTION");
    requestedVolumeFields.emplace_back("SENSITIVITY");
    nRequestedVolumeFields = requestedVolumeFields.size();
  }

  stringstream ss;
  ss << "Zone " << config->GetiZone() << " (Adj. Elasticity)";
  multiZoneHeaderString = ss.str();

  /*--- Set the volume filename --- */

  volumeFilename = config->GetAdj_FileName();

  /*--- Set the surface filename --- */

  surfaceFilename = config->GetSurfAdjCoeff_FileName();

  /*--- Set the restart filename --- */

  restartFilename = config->GetRestart_AdjFileName();

  /*--- Add the obj. function extension --- */

  restartFilename = config->GetObjFunc_Extension(restartFilename);

  /*--- Set the default convergence field --- */

  if (convFields.empty() ) convFields.emplace_back("ADJOINT_DISP_X");

}

CAdjElasticityOutput::~CAdjElasticityOutput(void) {}

void CAdjElasticityOutput::SetHistoryOutputFields(CConfig *config){

  // Residuals
  AddHistoryOutput("ADJOINT_DISP_X", "Res[Ux_adj]", ScreenOutputFormat::FIXED,   "RESIDUALS", "");
  AddHistoryOutput("ADJOINT_DISP_Y", "Res[Uy_adj]", ScreenOutputFormat::FIXED,   "RESIDUALS", "");
  AddHistoryOutput("ADJOINT_DISP_Z", "Res[Uz_adj]", ScreenOutputFormat::FIXED,   "RESIDUALS", "");

  //Sensitivities
  AddHistoryOutput("SENS_E", "Sens[E]",  ScreenOutputFormat::SCIENTIFIC, "SENSITIVITY", "");
  AddHistoryOutput("SENS_NU","Sens[Nu]", ScreenOutputFormat::SCIENTIFIC, "SENSITIVITY", "");


}

inline void CAdjElasticityOutput::LoadHistoryData(CConfig *config, CGeometry *geometry, CSolver **solver) {

  SetHistoryOutputValue("ADJOINT_DISP_X", log10(solver[ADJFEA_SOL]->GetRes_RMS(0)));
  SetHistoryOutputValue("ADJOINT_DISP_Y", log10(solver[ADJFEA_SOL]->GetRes_RMS(1)));
  if (nVar_FEM == 3){
    SetHistoryOutputValue("ADJOINT_DISP_Z", log10(solver[ADJFEA_SOL]->GetRes_RMS(2)));
  }
  su2double Total_SensE = 0.0; su2double Total_SensNu = 0.0;
  if (config->GetnElasticityMod() == 1){
    Total_SensE = solver[ADJFEA_SOL]->GetGlobal_Sens_E(0);
    Total_SensNu = solver[ADJFEA_SOL]->GetGlobal_Sens_Nu(0);
  }
  else{
    // TODO: Update this and change tests
    for (unsigned short iVar = 0; iVar < config->GetnElasticityMod(); iVar++){
      Total_SensE += pow(solver[ADJFEA_SOL]->GetGlobal_Sens_E(0),2);
      Total_SensNu += pow(solver[ADJFEA_SOL]->GetGlobal_Sens_Nu(0),2);
    }
  Total_SensE = sqrt(Total_SensE);
  Total_SensNu = sqrt(Total_SensNu);
  }
  SetHistoryOutputValue("SENS_E", Total_SensE);
  SetHistoryOutputValue("SENS_NU", Total_SensNu);

}

void CAdjElasticityOutput::LoadVolumeData(CConfig *config, CGeometry *geometry, CSolver **solver, unsigned long iPoint){

  CVariable* Node_Struc = solver[ADJFEA_SOL]->GetNodes();
  CPoint*    Node_Geo  = geometry->node[iPoint];

  SetVolumeOutputValue("COORD-X", iPoint,  Node_Geo->GetCoord(0));
  SetVolumeOutputValue("COORD-Y", iPoint,  Node_Geo->GetCoord(1));
  if (nDim == 3)
    SetVolumeOutputValue("COORD-Z", iPoint, Node_Geo->GetCoord(2));

  SetVolumeOutputValue("ADJOINT-X", iPoint, Node_Struc->GetSolution(iPoint, 0));
  SetVolumeOutputValue("ADJOINT-Y", iPoint, Node_Struc->GetSolution(iPoint, 1));
  if (nVar_FEM == 3)
    SetVolumeOutputValue("ADJOINT-Z", iPoint, Node_Struc->GetSolution(iPoint, 2));

  /*--- Load data for the discrete sensitivities. ---*/
  SetVolumeOutputValue("SENSITIVITY-X", iPoint, Node_Struc->GetSensitivity(iPoint, 0));
  SetVolumeOutputValue("SENSITIVITY-Y", iPoint, Node_Struc->GetSensitivity(iPoint, 1));
  if (nVar_FEM == 3) SetVolumeOutputValue("SENSITIVITY-Z", iPoint, Node_Struc->GetSensitivity(iPoint, 2));
}

void CAdjElasticityOutput::SetVolumeOutputFields(CConfig *config){

  // Grid coordinates
  AddVolumeOutput("COORD-X", "x", "COORDINATES", "x-component of the coordinate vector");
  AddVolumeOutput("COORD-Y", "y", "COORDINATES", "y-component of the coordinate vector");
  if (nDim == 3)
    AddVolumeOutput("COORD-Z", "z", "COORDINATES", "z-component of the coordinate vector");

  /// BEGIN_GROUP: SOLUTION, DESCRIPTION: Adjoint variables of the current objective function.
  /// DESCRIPTION: Adjoint x-component.
  AddVolumeOutput("ADJOINT-X", "Adjoint_x", "SOLUTION", "adjoint of displacement in the x direction");
  /// DESCRIPTION: Adjoint y-component.
  AddVolumeOutput("ADJOINT-Y", "Adjoint_y", "SOLUTION", "adjoint of displacement in the y direction");
  if (nVar_FEM == 3)
    /// DESCRIPTION: Adjoint z-component.
    AddVolumeOutput("ADJOINT-Z", "Adjoint_z", "SOLUTION", "adjoint of displacement in the z direction");
  /// END_GROUP

  /*--- Full field of sensitivity in each coordinate direction. ---*/
  AddVolumeOutput("SENSITIVITY-X",    "Sensitivity_x", "SENSITIVITY", "x-component of the coordinate sensitivity vector");
  AddVolumeOutput("SENSITIVITY-Y",    "Sensitivity_y", "SENSITIVITY", "y-component of the coordinate sensitivity vector");
  if (nVar_FEM == 3) AddVolumeOutput("SENSITIVITY-Z", "Sensitivity_Z", "SENSITIVITY", "z-component of the coordinate sensitivity vector");

  // /// BEGIN_GROUP: SENSITIVITY, DESCRIPTION: Geometrical sensitivities of the current objective function.
  // /// DESCRIPTION: Sensitivity in normal direction.
  // AddVolumeOutput("SENSITIVITY", "Surface_Sensitivity", "SENSITIVITY", "sensitivity in normal direction");
  // /// END_GROUP
}

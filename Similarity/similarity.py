# -*- coding:utf-8 -*-
# Author:Zhou Yang
# Time:2019/3/30



import tagme
import logging
import sys
import os.path

# 标注的“Authorization Token”，需要注册才有
tagme.GCUBE_TOKEN = "c6274227-4b42-4299-a9ef-6f932cfa75af-843339462"

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')


def similarity(A, B, flag=0):
    if flag == 0:
        rels = tagme.relatedness_title((A, B))
        return rels.relatedness[0].rel
    else:
        rels = tagme.relatedness_wid((A, B))
        return rels.relatedness[0].rel



if __name__ == '__main__':
    A, B = "Machine learning", "Artificial neural network"
    A_id, B_id = 21523, 233488
    obj = similarity(A, B)
    print(obj)
    obj = similarity(A_id, B_id, flag=1)
    print(obj)
#     obj = [['Attribution of recent climate change', 'Abstract (summary)', 'Carbon dioxide', 'Celsius', 'Climate oscillation', 'Coupling (physics)', 'Effects of global warming', 'El Niño–Southern Oscillation', 'Enteric fermentation', 'Environmental impact of aviation', 'Fertilizer', 'Global warming', 'IPCC First Assessment Report', 'Radiative forcing', 'Slash-and-burn', 'Water vapor']
# ,['Carbon cycle', 'Combustion', 'Deficit irrigation', 'Fermentation', 'Light-independent reactions', 'Ocean', 'Organic compound', 'Peat', 'Respiration (physiology)', 'Sediment trap', 'Solubility pump', 'Volcanic gas', 'Volcano']
# ,['Carbon dioxide', 'Apnea', 'Calcium hydroxide', 'Carbon dioxide sensor', 'Carbon monoxide', 'Carbon sequestration', 'Carboxylic acid', 'Combustion', 'Industrial Revolution', 'Must', 'Ocean acidification', 'Pascal (unit)', 'Sedimentary rock', 'Tin(IV) Oxide', 'Volcano']
# ,['Climate change', 'Altimeter', 'Anthropocene', 'Boundary current', 'Continental climate', 'Deforestation', 'Historical document', 'Ice age', 'Palynology', 'Pliocene', 'Polar desert', 'Primary production', 'Red giant', 'Solar cycle', 'Tide gauge', 'Toba catastrophe theory']
# ,['Climate change in the Arctic', 'Arctic Ocean Conference', 'Beaufort Sea', 'Canada', 'European Space Agency', 'Foreign minister', 'Greenland ice sheet', 'Habitat', 'Intergovernmental Panel on Climate Change', 'Ozone depletion', 'Per Stig Møller', 'Polar bear', 'Younger Dryas']
# ,['Climate model', 'Colorado', 'Albedo', 'Chemical species', 'Climate', 'Electromagnetic radiation', 'Energy', 'Greenhouse gas', 'Hadley Centre for Climate Prediction and Research', 'Infrared', 'Land use', 'New Jersey', 'Ocean current', 'Radiative forcing', 'Sea ice', 'Sea surface temperature', 'Stefan–Boltzmann law', 'Troposphere']
# ,['Fossil fuel', 'Abiogenic petroleum origin', 'Bottom ash', 'Coal', 'Energy development', 'Environmental law', 'Fly ash', 'Fossil fuel power station', 'Geothermal power', 'Redox', 'Renewable energy', 'Reserves-to-production ratio', 'Sawmill', 'Thorium']
# ,['Global warming', '2009 United Nations Climate Change Conference', '2010 United Nations Climate Change Conference', 'Abrupt climate change', 'Absorption (electromagnetic radiation)', 'Albrecht effect', 'American Meteorological Society', 'American Quaternary Association', 'Arctic methane emissions', 'Asian brown cloud', 'Attribution of recent climate change', 'Australia', 'Biosphere', 'Canada', 'Canadian Foundation for Climate and Atmospheric Sciences', 'Cancún', 'Carbon cycle', 'Carbon sequestration', 'Carbon sink', 'Caribbean', 'Climate change and agriculture', 'Climate change and ecosystems', 'Climate change in the Arctic', 'Climate commitment', 'Climate engineering', 'Climate model', 'Climatic Research Unit', 'Cloud condensation nuclei', 'Cloud forcing', 'Coal', 'Cosmic ray', 'Crop yield', 'Cryosphere', 'Deforestation', 'Deutsche Bank', 'Developed country', 'Developing country', 'Drought', 'Ecosystem', 'Effects of global warming', 'El Niño–Southern Oscillation', 'Emission spectrum', 'European Academy of Sciences and Arts', 'European Geosciences Union', 'European Science Foundation', 'Extinction', 'Extinction risk from global warming', 'Extreme weather', 'Flood', 'Fluid dynamics', 'Fossil fuel', 'Geological Society of America', 'Geological Society of London', 'George W. Bush', 'Germany', 'Global dimming', 'Global warming controversy', 'Glossary of climate change', 'Gray whale', 'Greenhouse gas', 'Group of 77', 'HadCM3', 'Henrik Svensmark', 'History of climate change science', 'Hydrosphere', 'Index of climate change articles', 'India', 'Industrial Revolution', 'Infrared', 'Instrumental temperature record', 'InterAcademy Partnership', 'Intergovernmental Panel on Climate Change', 'International Union of Geodesy and Geophysics', 'Ireland', 'Irradiance', 'James Hansen', 'Japan', 'Joseph Fourier', 'Keeling Curve', 'Kyoto Protocol', 'List of countries by greenhouse gas emissions per capita', 'List of parties to the Kyoto Protocol', 'Malnutrition', 'Mangrove', 'Maunder Minimum', 'Mean', 'Methane', 'Mexico', 'Moving average', 'NASA', 'NASA Earth Observatory', 'National Academies of Sciences, Engineering, and Medicine', 'National Climatic Data Center', 'National Oceanic and Atmospheric Administration', 'National Snow and Ice Data Center', 'Network of African Science Academies', 'New Zealand', 'Nitrous oxide', 'Ocean current', 'OR Books', 'Orbital forcing', 'China', 'Permafrost', 'Pew Research Center', 'Polish Academy of Sciences', 'Pollutant', 'Positive feedback', 'Power station', 'Proxy (climate)', 'Radiative cooling', 'Radiative forcing', 'Radiosonde', 'Renewable energy', 'Retreat of glaciers since 1850', 'Royal Society', 'Salinity', 'Satellite temperature measurements', 'Science (journal)', 'Sea ice', 'Sea level rise', 'Skeptical Science', 'Soot', 'South Africa', 'Southern Hemisphere', 'Southern Ocean', 'Special Report on Emissions Scenarios', 'Spring (season)', 'Stefan–Boltzmann law', 'Svante Arrhenius', 'Technology', 'Temperature record of the past 1000 years', 'Thermodynamics', 'Tundra', 'Twomey effect', 'United Nations Environment Programme', 'United Nations Framework Convention on Climate Change', 'United States', 'Volumetric heat capacity', 'Wallace Smith Broecker', 'Wet-bulb temperature', 'World Meteorological Organization']
# ,['Greenhouse gas', 'Absorption (electromagnetic radiation)', 'Atmospheric methane', 'Bio-energy with carbon capture and storage', 'Carbon emissions reporting', 'Diatomic molecule', 'Eddy covariance', 'Fluorocarbon', 'Fossil fuel', 'Limestone', 'Nitrogen trifluoride', 'Organofluorine chemistry', 'Redox', 'Tire-derived fuel', 'Year']
# ,['Gross domestic product', 'Gross domestic product', 'Household final consumption expenditure', 'International Monetary Fund', 'Lists of countries by GDP', 'Monetization', 'New Economics Foundation', 'Penn effect', 'Private product remaining', 'Profit (accounting)', 'Real gross domestic product', 'Uneconomic growth', 'United Nations']
# ,['Instrumental temperature record', 'Antarctic Peninsula', 'Arctic oscillation', 'Attribution of recent climate change', 'Berkeley Earth', 'Celsius', 'Central England temperature', 'EdGCM', 'Global warming', 'IPCC Fourth Assessment Report', 'MMTS (meteorology)', 'National Academy of Sciences', 'National Climatic Data Center', 'North Atlantic oscillation', 'Pacific decadal oscillation', 'Stevenson screen']
# ,['Intergovernmental Panel on Climate Change', 'European Geosciences Union', 'Geophysical Fluid Dynamics Laboratory', 'House of Lords', 'InterAcademy Partnership', 'IPCC Summary for Policymakers', 'Joseph J. Romm', 'Methane', 'Peer review', 'Rajendra K. Pachauri', 'Raymond S. Bradley', 'Scientific opinion on climate change', 'United Nations Environment Programme', 'Wikipedia', 'Working group']
# ,['IPCC Fourth Assessment Report', 'Afforestation', 'Building-integrated photovoltaics', 'Halocarbon', 'Intergovernmental Panel on Climate Change', 'Oil shale', 'RealClimate', 'Regenerative brake', 'Sea ice', 'Tide', 'Transportation planning', 'United Nations Environment Programme', 'United States', 'World Health Organization']
# ,['Kyoto Protocol', 'Aggregate data', 'Bangladesh', 'Carbon sink', 'Caribbean', 'Chile', 'Costa Rica', 'Egypt', 'Group of 77', 'Liberia', 'Mozambique', 'Nauru', 'New Zealand', 'São Tomé and Príncipe', 'Tokyo Metropolitan Government']
# ,['Northern Hemisphere', 'Arctic', 'Asia', 'Atlantic Ocean', 'Axial tilt', 'Equator', 'North America', 'Pacific Ocean', 'South America', 'South Pole', 'Sphere', 'Tropical cyclone', 'Tropics']
# ,['Sea level rise', 'Antarctic', 'Economic growth', 'Gravimetry', 'Greenland ice sheet', 'Ice age', 'Kilometre', 'Lake', 'Meltwater pulse 1A', 'Northern Hemisphere', 'Sea ice', 'Southern Hemisphere', 'Surveying', 'University of Kiel', 'West Caicos']
# ,['Stratosphere', 'Airliner', 'Altitude', 'Atmosphere of Earth', 'Celsius', 'Concorde', 'Convective overshoot', 'Geographical pole', 'Gravity wave', 'Ivory Coast', 'Léon Teisserenc de Bort', 'Methane', 'Northrop Grumman RQ-4 Global Hawk', 'Richard Assmann', 'Rossby wave']
# ,['Troposphere', 'Atmosphere', 'Energy', 'Gas constant', 'Heat', 'Heat capacity ratio', 'Hydrostatics', 'Ideal gas', 'Landform', 'Lapse rate', 'Meteorology', 'Pascal (unit)', 'Vapor pressure', 'Water vapor', 'Zonal and meridional']
# ,['United Nations Framework Convention on Climate Change', 'Earth Summit', 'Greece', 'Greenhouse gas inventory', 'Human impact on the environment', 'Iceland', 'Indonesia', 'Methane', 'Montreal Protocol', 'Nusa Dua', 'South Africa', 'Transition economy', 'United Nations Convention to Combat Desertification', 'United States', 'Yvo de Boer']
# ,['World Meteorological Organization', 'Alexander Bedritsky', 'BUFR', 'Geophysics', 'Hydrology', 'Intergovernmental organization', 'Intergovernmental Panel on Climate Change', 'List of states with limited recognition', 'Nauru', 'Palau', 'SYNOP', 'United Nations Development Group', 'Weather']]
#
#     for i in range(len(obj)):
#         word = obj[i]
#         A = word[0]
#         for j in range(1, len(word)):
#             B = word[j]
#             score = similarity(A, B)
#             print(A + "  " + B + "   " + str(score))


    pass



































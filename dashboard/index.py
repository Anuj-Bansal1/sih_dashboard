#!/usr/bin/env python
# coding: utf-8

# In[1]:


import panel as pn
import pandas as pd

pn.extension('tabulator')


# In[2]:


import hvplot.pandas


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# html_content = '''<!DOCTYPE html> <html> <body> <button onclick="toggleFullscreen()">Go Fullscreen</button> <iframe id="myIframe" src="https://copilotstudio.microsoft.com/environments/Default-1be3a563-7207-487a-a1bf-4c69e3e4930e/bots/cre45_vannaDemo/webchat?__version__=2" frameborder="0" style="width: 100%; height: 100%;" allowfullscreen></iframe> <script> function toggleFullscreen() { var iframe = document.getElementById("myIframe"); if (iframe.requestFullscreen) { iframe.requestFullscreen(); } else if (iframe.mozRequestFullScreen) { // Firefox iframe.mozRequestFullScreen(); } else if (iframe.webkitRequestFullscreen) { // Chrome, Safari, and Opera iframe.webkitRequestFullscreen(); } else if (iframe.msRequestFullscreen) { // IE/Edge iframe.msRequestFullscreen(); } } </script> </body> </html> '''
html_content = ''' <!DOCTYPE html> <html> <body> <button onclick="goFullScreen()">Go Fullscreen</button> <iframe id="myIframe" src="https://copilotstudio.microsoft.com/environments/Default-1be3a563-7207-487a-a1bf-4c69e3e4930e/bots/cre45_testCaseAi/webchat?__version__=2" frameborder="0" style="width: 100%; height: 100%;"></iframe> <script> function goFullScreen() { window.location.href = "https://copilotstudio.microsoft.com/environments/Default-1be3a563-7207-487a-a1bf-4c69e3e4930e/bots/cre45_testCaseAi/webchat?__version__=2"; } </script> </body> </html> '''
html_pane = pn.pane.HTML(html_content, sizing_mode='stretch_both')
# Generating synthetic data
states = ["Maharashtra", "Harayana", "Assam", "Himachal pradesh"]

# Define the courts
case_type = ["Criminal","Divorce","Fraud","Robbery"]

# Define the dummy data generation function with the "State" column
def dummy_(case_type = case_type, states=states):
    years = list(range(2010, 2022))
    all_combinations = list(product(states, case_type, years))

    # Generate random data for cases filed and resolved for each combination
    np.random.seed(42)
    cases_filed = [np.random.randint(1000, 5000) for _ in range(len(all_combinations))]
    cases_resolved = [np.random.randint(800, 4500) for _ in range(len(all_combinations))]

    # Create a DataFrame
    df = {
        "States": [combo[0] for combo in all_combinations],
        "Case_type": [combo[1] for combo in all_combinations],
        "Year": [combo[2] for combo in all_combinations],
        "Cases Filed": cases_filed,
        "Cases Resolved": cases_resolved
    }


    return df
'''def categorize_court(court_name):
    if court_name in ["District Court A", "District Court B", "District Court C", "District Court D"]:
        return "District_Court"
    elif court_name in ["High Court A", "High Court B", "High Court C", "High Court D"]:
        return "High_Court"
    else:
        return "Supreme_Court"

'''

data = dummy_()
idf1 = pd.DataFrame(data)
#idf1["Court_Type"] = idf1["Court Name"].apply(categorize_court)


idf = idf1.interactive()


# In[4]:


slider = pn.widgets.IntSlider(start=2011, end=2022, step=1, name="year Value", value = 2015)


# In[5]:


select_opt = list(idf1["States"].unique())
select = pn.widgets.Select(options= select_opt)
select


# In[6]:


select_court =pn.widgets.Select(options= list(idf1["Case_type"].unique())
)
select_court


# In[7]:


import folium
m = folium.Map(location=[20.5937,78.9629], zoom_start=7)
folium.Marker([20.5937,78.9629], tooltip='Marker Tooltip').add_to(m)


# In[8]:


def update_map(event):
    selected_location = event.new

    # Use a dictionary or another data structure to map location names to coordinates
    coordinates = {
    'Andhra Pradesh': (15.9129, 79.7400),
    'Arunachal Pradesh': (27.1004, 93.6166),
    'Assam': (26.2006, 92.9376),
    'Bihar': (25.0961, 85.3131),
    'Chhattisgarh': (21.2787, 81.8661),
    'Goa': (15.2993, 74.1240),
    'Gujarat': (22.2587, 71.1924),
    'Harayana': (29.0588, 76.0856),
    'Himachal pradesh': (31.1048, 77.1734),
    'Jharkhand': (23.6102, 85.2799),
    'Karnataka': (15.3173, 75.7139),
    'Kerala': (10.8505, 76.2711),
    'Madhya Pradesh': (22.9734, 78.6569),
    'Maharashtra': (19.7515, 75.7139),
    'Manipur': (24.6637, 93.9063),
    'Meghalaya': (25.4670, 91.3662),
    'Mizoram': (23.1645, 92.9376),
    'Nagaland': (26.1584, 94.5624),
    'Odisha': (20.9517, 85.0985),
    'Punjab': (31.1471, 75.3412),
    'Rajasthan': (27.0238, 74.2179),
    'Sikkim': (27.5330, 88.5122),
    'Tamil Nadu': (11.1271, 78.6569),
    'Telangana': (18.1124, 79.0193),
    'Tripura': (23.9408, 91.9882),
    'Uttar Pradesh': (26.8467, 80.9462),
    'Uttarakhand': (30.0668, 79.0193),
    'West Bengal': (22.9868, 87.8550),
    'Andaman and Nicobar Islands': (11.7401, 92.6586),
    'Chandigarh': (30.7333, 76.7794),
    'Dadra and Nagar Haveli and Daman and Diu': (20.1809, 73.0169),
    'Lakshadweep': (10.5667, 72.6417),
    'Delhi': (28.6139, 77.2090),
    'Puducherry': (11.9416, 79.8083)
}

# Example usage:
# To get the coordinates of a specific state:
# latitude, longitude = india_states_coordinates['Karnataka']

    # Clear previous markers
    m = folium.Map(location=coordinates[selected_location], zoom_start=7)
    folium.Marker(coordinates[selected_location],tooltip=f"{selected_location}").add_to(m)
    
    district_courts = {
    'Assam': [
        ('Guwahati District Court', 26.1942, 91.7239),
        ('Jorhat District Court', 26.7586, 94.2021),
        ('Dibrugarh District Court', 27.4781, 94.9090),
        ('Tezpur District Court', 26.6339, 92.7973)
    ],
    'Maharashtra': [
        ('Mumbai District Court', 19.0760, 72.8777),
        ('Pune District Court', 18.5204, 73.8567),
        ('Nagpur District Court', 21.1466, 79.0882),
        ('Nashik District Court', 20.0059, 73.7613)
    ],
    'Haryana': [
        ('Chandigarh District Court', 30.7333, 76.7794),
        ('Faridabad District Court', 28.4022, 77.3130),
        ('Gurgaon District Court', 28.4595, 77.0266),
        ('Rohtak District Court', 28.8955, 76.6066)
    ],
    'Himachal Pradesh': [
        ('Shimla District Court', 31.1048, 77.1734),
        ('Kangra District Court', 32.1664, 76.3247),
        ('Mandi District Court', 31.7116, 76.9329),
        ('Solan District Court', 30.9178, 77.0960)
    ]
}

# Add markers for district courts in each state
    for state, courts in district_courts.items():
        for court_name, lat, lon in courts:
            folium.Marker([lat, lon], tooltip=court_name,icon=folium.Icon(color='red')).add_to(m)

    
    # Update the Panel object with the updated map
    map_panel.object = m


# In[9]:


select.param.watch(update_map, 'value')
map_panel = pn.panel(m, width=500, height=400)


# In[10]:


m = folium.Map(location=[20.5937,78.9629], zoom_start=5)

folium_pane = pn.pane.plot.Folium(m, height=400,sizing_mode= 'stretch_width')


# Add a marker to the map
folium.Marker(
    [20.5937, 78.9629], popup="<i> India </i>", tooltip="Click me!"
).add_to(m)

folium_pane.object = m
folium_pane


# In[11]:


case_status = pn.widgets.RadioButtonGroup(
            name = "Y-axis",
    options = ["Cases Filed","Cases Resolved"],
    button_type = 'success'
)


# In[12]:


data_pipeline =( idf[(idf.Year <= slider) & (idf.States == select)]).reset_index(drop= True).sort_values(by ='Year').groupby(["Case_type","Year"])[case_status].mean()
data_pipeline1 =( idf[(idf.Year <= slider)&(idf.States == select)&(idf["Case_type"] == select_court)]).sort_values(by ='Year').reset_index(drop= True)


# In[13]:


plot_pipeline= data_pipeline.hvplot(x='Year',by = 'Case_type',y = case_status ,line_width = 2 ,title = case_status)
plot_pipeline


# In[14]:


tabular_frame = data_pipeline1.pipe(pn.widgets.Tabulator,pagination ='remote',page_size= 10,sizing_mode= 'stretch_width')
tabular_frame


# In[19]:


# Create a Panel app
def create_dashboard():
    row1 = pn.Column(case_status,plot_pipeline.panel())
    row2 = pn.Row(row1,html_pane)
    template = pn.template.FastGridTemplate(
        title = 'Dashboard',
        sidebar = [pn.pane.Markdown("## Indian Evault"),
                  pn.pane.Markdown("##### Evault is a blockchain based system that can store, manage, and share legal records securely and efficiently. It ensures privacy and confidentiality of legal records, with appropriate access controls, encryption, and authentication mechanisms."),
                  select,select_court,
                   pn.pane.Markdown("##"),
                   slider,
                   pn.pane.Markdown("##"),
                pn.pane.PNG("supppp.png", sizing_mode = 'scale_both' ),
                  ],

        main = [row2,
               pn.Row(tabular_frame.panel(),map_panel)],
        header_background = "#96695E",
        background_color= "#EDE7DE",
        theme_toggle = False,
        row_height = 400,
        sidebar_width = 310,
        site = "Evault",
        
    )

    
    return template

# Run the Panel app
if __name__ == "__main__":
    app = create_dashboard()
    app.servable()
    app.show()
if __name__.startswith("bokeh"):
    # start with panel serve script.py
    app = create_dashboard()
    app.servable()


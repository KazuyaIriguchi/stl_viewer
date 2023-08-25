import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

import os

pv.global_theme.show_scalar_bar = False

st.title("STL Viewer")

uploaded_file = st.file_uploader("Choose a STL file", type="stl")

if uploaded_file:
    temp_file = "temp_stl_file.stl"
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # load stl
    mesh = pv.read(temp_file)
    plotter = pv.Plotter(window_size=[400, 400])
    plotter.add_mesh(mesh)
    plotter.view_isometric()
    plotter.background_color = "white"

    stpyvista(plotter, key="pv_stl")

    os.remove(temp_file)

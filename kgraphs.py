# -*- coding: utf-8 -*-
"""KnowledgeGraph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16FLyT_QQtDcieYhjUps6fjXaDizatNAN
"""
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def create_knowledge_graph(df, source_col, target_col, relation_col):
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_node(row[source_col])
        G.add_node(row[target_col])
        G.add_edge(row[source_col], row[target_col], relation=row[relation_col])

    return G

def draw_knowledge_graph(G, node_size, edge_width):
    pos = nx.circular_layout(G)  # Using a circular layout for simplicity
    edge_labels = nx.get_edge_attributes(G, 'relation')

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_size=node_size, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', width=edge_width)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    st.pyplot(fig)

def main():
    st.title("Dynamic Knowledge Graph App")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Get column names dynamically
        source_col, target_col, relation_col = st.columns(3)
        source_col_name = source_col.text_input("Enter Source Column Name", value=df.columns[0])
        target_col_name = target_col.text_input("Enter Target Column Name", value=df.columns[1])
        relation_col_name = relation_col.text_input("Enter Relation Column Name", value=df.columns[2])

        knowledge_graph = create_knowledge_graph(df, source_col_name, target_col_name, relation_col_name)

        st.subheader("Data Preview:")
        st.write(df.head())

        st.subheader("Knowledge Graph Visualization:")

        # Sliders for customization
        node_size = st.slider("Node Size", min_value=1, max_value=100, value=20)
        edge_width = st.slider("Edge Width", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

        draw_knowledge_graph(knowledge_graph, node_size, edge_width)

if __name__ == "__main__":
    main()

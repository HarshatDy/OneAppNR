import matplotlib.pyplot as plt
from matplotlib import pyplot as plt, patches
import base64
from io import BytesIO
import plotly.express as px

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    # print(image_png)
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y,title,namex,namey):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.legend()
    plt.xlabel(namex)
    plt.ylabel(namey) 
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar(x,y,namex,namey,title,color,edgecolor):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    # plt.plot(x,y)
    plt.bar(x,y,color=color,edgecolor=edgecolor)
    plt.xticks(rotation=45)
    plt.legend()
    # plt.show()
    # tmpfile = BytesIO()
    # fig.savefig(tmpfile, format='png')
    # encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    plt.xlabel(namex)
    plt.ylabel(namey) 
    plt.tight_layout()
    graph = get_graph()
    # graph =1
    print(graph)
    return graph

def get_single_plot(x,title,namex):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.plot(x)
    # px.plo`t(x)
    plt.xticks(rotation=45)
    plt.xlabel(namex)
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_scatter(x,y,title):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.scatter(x,y)
    plt.xlabel("SCatter")
    plt.ylabel("YLabel")
    plt.tight_layout()
    graph = get_graph()
    return graph
    

def get_line(x,title,namex,namey):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    # px.Figure()
    graph = px.line(x,x=namex,y=namey,title=title)
    # graph = get_graph()
    # graph.show()
    # graph_new = graph.to_image(format='png')

    # plt.tight_layout()
    # graph = get_graph()
    return graph


# def get_patch_rect(title, a , offsetToPointA, b , offsetToPointA2, edgecolor, facecolor,linewidth):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(10,5))
#     plt.title(title)
#     ssb_plot = patches.Rectangle((1, offsetToPointA), 1, offsetToPointA2, edgecolor,facecolor, linewidth)
#     return ssb_plot

    
def get_patch(ax,ssb_plot,sss_plot):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    ax.add_patch(ssb_plot)
    ax.add_patch(sss_plot)
    plt.plot()
    plt.tight_layout()
    # plt.show()
    graph=get_graph()
    return graph


def only_plot(df):
    plt.switch_backend('AGG')
    # plt.figure(figsize=(10,5))
    # px.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    graph = px.line(df,x="%CPU", y="P", title="trial")
    # plt.show()
    print("printed")
    # plt.tight_layout()
    return graph
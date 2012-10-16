#-*- coding: utf-8 -*-

# Very good: http://matplotlib.sourceforge.net/leftwich_tut.txt

import scipy.interpolate
import matplotlib
import matplotlib.figure
#http://matplotlib.sourceforge.net/faq/installing_faq.html
#from matplotlib.backends.backend_macosx import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#matplotlib.use('GtkAGG')
# ['ps', 'Qt4Agg', 'GTK', 'GTKAgg', 'svg', 'agg', 'cairo', 'MacOSX', 'GTKCairo', 'WXAgg', 'TkAgg', 'QtAgg', 'FltkAgg', 'pdf', 'CocoaAgg', 'emf', 'gdk', 'template', 'WX']
#from matplotlib.pylab import *

def interp_array(A, folds=10, start_year=1985):
    yorg = A[:,1:]
    x = linspace(start_year, start_year+yorg.shape[1]-1, yorg.shape[1]*folds)
    xorg = linspace(start_year, start_year+yorg.shape[1]-1, yorg.shape[1])
    intf = scipy.interpolate.interp1d(xorg, yorg, axis=1)
    return x, intf(x)

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def draw_half_pyramid(x, ax=None, patch_kw={'facecolor':'orange', 'lw':1},\
                          step_size=1):
    """
    Pathces keywords, see help(patches.Patch)
    """
    verts = [(0., 0.)]
    codes = [Path.MOVETO]
    for i in range(len(x)):
        verts.append((x[i],i*step_size))
        verts.append((x[i],(i+1)*step_size))
        codes.append(Path.LINETO)
        codes.append(Path.LINETO)
    verts.append((0., len(x)*step_size))
    codes.append(Path.LINETO)
    verts.append((0., 0.))
    codes.append(Path.CLOSEPOLY,)

    path = Path(verts, codes)

    if ax==None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, **patch_kw)
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(0, len(x))
    ax.add_patch(patch)


def group_ages(X, group_size=5):
    """
    """
    G = X.shape[0]/group_size
    res = np.zeros((G, X.shape[1]))
    for i in range(G):
        res[i, :] = np.mean(X[i*group_size:(i+1)*group_size, :], axis=0)
    return res

def make_plot(f, t_idx=0, group_size=1):
    # http://matplotlib.github.com/api/figure_api.html
    ax_left = f.add_axes(rect_left)
    ax_right = f.add_axes(rect_right)
    
    year = int(years[t_idx]) #1985 + t_idx/factor
    print year
    overlap = 0.1
    l = 0.25
    e = 0.2
    patch_men_kw={'facecolor':(l,l,1), 'lw':1, 'edgecolor':(e,e,e)}
    patch_women_kw={'facecolor':(1,l,l), 'lw':1, 'edgecolor':(e,e,e)}
    draw_half_pyramid(-men[:, t_idx], ax=ax_left, patch_kw=patch_men_kw, step_size=group_size)
    draw_half_pyramid(women[:, t_idx], ax=ax_right, patch_kw=patch_women_kw, step_size=group_size)

    tt = []
    dmen = []
    dwomen = [] 
    for i in range(0, men.shape[0]):
        tt.append(i)
        tt.append(i+1)
        dmen.append(-men[i, 0])
        dmen.append(-men[i, 0])
        dwomen.append(women[i, 0])
        dwomen.append(women[i, 0])
    ax_left.plot(dmen, np.array(tt)*group_size, 'k')
    ax_right.plot(dwomen, np.array(tt)*group_size, 'k')

    ax_right.set_xlim(0, 500)
    ax_left.set_xlim(-500, 0)
    ax_right.set_ylim(0, 103)
    ax_left.set_ylim(0, 103)

    age_ticks = range(10, 110, 10)
    ticks = [0,100,200,300,400,500]
    ax_left.set_xticks([-x for x in ticks])
    ax_left.set_xticklabels([str(s) for s in ticks])
    ax_left.set_yticks(age_ticks)
    ax_left.set_yticklabels([])
    ax_left.grid()
    ax_left.set_xlabel(u'Menn')
    ax_right.set_yticks(age_ticks)
    age_tick_strs = [str(x) for x in age_ticks]
    age_tick_strs[-1] = 'Aldur'
    ax_right.set_yticklabels(age_tick_strs)
    ax_right.grid()
    ax_right.set_xlabel(u'Kvinnur')
    #figtext(0.5, 0.1, u'Tal av fólki', ha='center', fontsize='large')
    ax_right.text(-450, 87, str(year), fontsize=32)
    f.text(0.5, 0.89, 'Aldurspyramida', ha='center', fontsize=30)
    return f

video_dim = [640, 480]
dpi = 80

width = 0.80 # Of whole pop. pyramid
height = 0.65
left = (1.0-width)/2
bottom = (1.0-height)/2
rect_left = [left, bottom, width/2, height]
rect_right = [left+width/2, bottom, width/2, height]

factor = 25
wt, women = interp_array(konufolk, folds=factor)
mt, men = interp_array(mannfolk, folds=factor)
years = wt

group_size = 5
men = group_ages(men, group_size=group_size)
women = group_ages(women, group_size=group_size)

def make_movie():
    f = matplotlib.figure.Figure(figsize=[x/dpi for x in video_dim], dpi=dpi)
    canvas=FigureCanvas(f)
    for idx in range(0, men.shape[1]): # len(wt)):
        f.clf()
        f = make_plot(f, t_idx=idx, group_size=group_size)
        f.savefig('movie%.4d.png'%idx)


# Aldurspyramida 1985-2011

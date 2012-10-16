# coding=utf-8

def plot_data(data, title_str='', p_col_min=None, p_col_max=None, cb_label=None):
    pcolor(data[:,1:], vmin=p_col_min, vmax=p_col_max)
    xlabel(u'Árstal')
    ylabel(u'Aldur')
    title(title_str)
    start_ar = 1985
    tal_av_ar = data.shape[1]-1
    ar = range(start_ar, start_ar + tal_av_ar)
    xticks(np.array(range(tal_av_ar)) + 0.5, ar, rotation=90)
    fig = gcf()
    fig.subplots_adjust(right=0.8, bottom=0.15)
    y_t = np.linspace(0,100,11)
    yticks(y_t, [str(int(y)) for y in y_t])
    axis('tight')
    grid()
    cax = fig.add_axes([0.825, 0.1, 0.025, 0.8])
    cb = colorbar(cax=cax,orientation='vertical')
    if cb_label==None:
        cb.set_label(u'Tal av fólki')
    else:
        cb.set_label(cb_label)
        
fig_folk = figure()
plot_data(data, title_str=u'Fólk í Føroyum')

fig_konufolk = figure()
plot_data(konufolk, title_str=u'Konufólk í Føroyum', p_col_max=500)

fig_mannfolk = figure()
plot_data(mannfolk, title_str=u'Mannfólk í Føroyum', p_col_max=500)

fig_munur = figure()
plot_data(munur, title_str=u'Munur av talið á konufólkum og mannfólkum', cb_label=u'Tal av mannfólk - tal av konufólkum', p_col_min=-150, p_col_max=150)

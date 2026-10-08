"""Figures scientifiques originales, issues des mêmes modèles que les TP."""
from __future__ import annotations
import json
from pathlib import Path
import textwrap
from catalogue import LABS
from modeles import calculate

def export(destination, png_destination=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    if png_destination:Path(png_destination).mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','axes.titleweight':'normal'})
    palette=['#217865','#c87540','#8075bb','#b9903e','#b15268'];catalogue=[]
    for lab in LABS:
        r=calculate({'lab':lab['id']});charts=list(r['charts']);sc=r['scene']
        if sc['kind']=='spectrogram':charts.insert(0,dict(title='Spectrogramme : STFT et fréquence instantanée',x_label='t / s',y_label='ν / Hz',series=[],special='spectrogram'))
        if sc['kind']=='poles':charts=[dict(title='Pôles dans le plan complexe',x_label='Re(p) / s⁻¹',y_label='Im(p) / s⁻¹',series=[],special='poles')]+charts[:-1]
        count=len(charts);rows=(count+1)//2
        fig,axes=plt.subplots(rows,2,figsize=(11.5,3.5*rows+1.5),squeeze=False)
        fig.patch.set_facecolor('#f8f7f1');fig.suptitle('\n'.join(textwrap.wrap(lab['title'],76)),fontsize=16,color='#162f43',x=.055,ha='left',y=.97)
        for ax,ch in zip(axes.flat,charts):
            ax.set_facecolor('#ffffff');seen=set()
            if ch.get('special')=='spectrogram':
                image=ax.pcolormesh(sc['times'],sc['frequencies'],sc['db'],shading='auto',cmap='magma',vmin=-65,vmax=0);ax.plot(sc['times'],sc['ridge'],'w--',lw=1,label='ν(t) exacte');fig.colorbar(image,ax=ax,label='dB relatifs',pad=.02)
            elif ch.get('special')=='poles':
                poles=sc['poles'];ax.scatter([v[0] for v in poles],[v[1] for v in poles],marker='x',s=90,c='#c87540',label='Pôles');ax.axhline(0,color='#a3b7bd',lw=.8);ax.axvline(0,color='#a3b7bd',lw=.8);ax.set_xlim(left=min(v[0] for v in poles)*1.3,right=max(1,abs(min(v[0] for v in poles))*.35))
            for k,curve in enumerate(ch['series']):
                color=palette[(0 if ch.get('same_color') else k)%len(palette)];label=curve['label'] if curve['label'] not in seen else '_nolegend_';seen.add(curve['label'])
                if curve.get('style')=='dots':ax.scatter(curve['x'],curve['y'],s=12,color=color,label=label,zorder=4)
                elif curve.get('style')=='stems':
                    ax.vlines(curve['x'],0,curve['y'],color=color,lw=2,label=label);ax.scatter(curve['x'],curve['y'],s=8,color=color)
                else:ax.plot(curve['x'],curve['y'],lw=1.7,color=color,label=label)
            if ch.get('x_scale')=='log':ax.set_xscale('log')
            if ch.get('y_scale')=='log':ax.set_yscale('log')
            if ch.get('x_reverse'):ax.invert_xaxis()
            ax.set_title('\n'.join(textwrap.wrap(ch['title'],46)),fontsize=10,loc='left',pad=11,color='#162f43')
            ax.set_xlabel(ch['x_label'],fontsize=8);ax.set_ylabel(ch['y_label'],fontsize=8);ax.grid(alpha=.17)
            ax.legend(loc='best',fontsize=6.7,framealpha=.9)
        for ax in list(axes.flat)[count:]:ax.axis('off')
        parameters=' · '.join(f"{key}={value:g}" if isinstance(value,(int,float)) else f'{key}={value}' for key,value in r['params'].items())
        footer='Paramètres : '+parameters+'\n'+r['assumptions'][0]
        fig.text(.055,.025,'\n'.join(textwrap.wrap(footer,151)),fontsize=7.8,color='#56707c',va='bottom')
        fig.subplots_adjust(left=.075,right=.97,top=.81 if rows==1 else .86,bottom=.2 if rows==1 else .14,hspace=.65,wspace=.29)
        filename=lab['id']+'.svg';fig.savefig(destination/filename,facecolor=fig.get_facecolor())
        svg_path=destination/filename
        svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
        if png_destination:fig.savefig(Path(png_destination)/(lab['id']+'.png'),dpi=110,facecolor=fig.get_facecolor())
        plt.close(fig)
        catalogue.append(dict(file=filename,title=lab['title'],labs=[lab['id']],caption='Paramètres : '+parameters+'. '+r['assumptions'][0]))
    (destination/'catalogue.json').write_text(json.dumps(catalogue,ensure_ascii=False,indent=2),encoding='utf8')
    (destination/'README.md').write_text('# Galerie scientifique\n\nTrente figures originales, calculées avec les modèles de l’atelier. Les paramètres et le cadre du modèle figurent dans chaque légende.\n\n'+'\n\n'.join(f"## {i+1}. {f['title']}\n\n![{f['title']}]({f['file']})\n\n{f['caption']}" for i,f in enumerate(catalogue))+'\n',encoding='utf8')
    return f'{len(catalogue)} figures SVG originales créées.'

if __name__=='__main__':print(export(Path(__file__).with_name('illustrations')))

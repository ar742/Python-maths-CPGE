'use strict';
const get=id=>document.getElementById(id);
const make=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;};
const labels={socle:'Techniques incontournables',approfondissement:'Approfondissement CPGE',prolongement:'Au-delà du programme'};
async function load(){
    try{
        const response=await fetch('/api/bootstrap');if(!response.ok)throw Error('Le serveur local ne répond pas.');
        const data=await response.json(),p=data.progression,links=data.progression_links;
        get('title').textContent=p.title;document.title=p.title+' · Python-maths-CPGE';
        for(const id of ['intro','duration','scope'])get(id).textContent=p[id];
        for(const item of p.prerequisites)get('prerequisites').append(make('li','',item));
        for(const item of p.method)get('method').append(make('li','',item));
        for(const stage of p.stages){
            const section=make('section','stage');section.id='stage-'+stage.id;
            section.append(make('h2','',stage.title),make('p','stage-intro',stage.intro));
            const jump=make('a','jump',stage.title);jump.href='#'+section.id;get('jumps').append(jump);
            for(const session of stage.sessions){
                const card=make('article','session '+session.status);card.id=session.id;
                const tags=make('div','tags');tags.append(make('span','badge '+session.status,labels[session.status]),make('span','',session.level));
                card.append(tags,make('h3','',session.title),make('p','objective',session.objective));
                const fields=make('div','fields');
                for(const [title,key] of [['À faire','task'],['Acquis attendu','success'],['Limites et compléments','limits']]){const field=make('div');field.append(make('b','',title),make('p','',session[key]));fields.append(field);}
                card.append(fields);const actions=make('div','actions');
                for(const id of session.labs){const link=links.find(l=>l.id===id);if(!link)throw Error('TP absent du parcours : '+id);const a=make('a','open','Ouvrir · '+link.title);a.href=link.href+(link.href.includes('?')?'&':'?')+'seance='+encodeURIComponent(session.id);actions.append(a);}
                card.append(actions);section.append(card);
            }
            get('stages').append(section);
        }
        for(const source of p.sources){const a=make('a','',source.label+' ↗');a.href=source.url;a.target='_blank';a.rel='noopener';get('sources').append(a);}
        get('document').href=p.document_url;
        if(location.hash){const id=decodeURIComponent(location.hash.slice(1)),target=document.getElementById(id);if(target)target.scrollIntoView({block:'start'});}
    }catch(error){get('error').textContent='Impossible de charger le parcours : '+error.message;get('error').hidden=false;}
}
load();

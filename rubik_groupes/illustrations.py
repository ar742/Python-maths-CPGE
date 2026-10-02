"""Exporter les illustrations vectorielles exactes du modèle Python."""
from html import escape
from math import cos, sin
from pathlib import Path
import cube


def text(x, y, value, size=16, fill="#183040", weight="400"):
    return f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}">{escape(str(value))}</text>'


def scene(state, cx, cy, scale=60):
    yaw, pitch = -.62, .48

    def project(v):
        x, y, z = v
        px, pz = cos(yaw)*x+sin(yaw)*z, -sin(yaw)*x+cos(yaw)*z
        return cx+scale*px, cy-scale*(cos(pitch)*y-sin(pitch)*pz), sin(pitch)*y+cos(pitch)*pz

    tiles = []
    for i, (pos, normal) in enumerate(cube.GEOMETRY):
        if project(normal)[2] <= 0:
            continue
        axes = [j for j in range(3) if normal[j] == 0]
        center = [pos[j]+.505*normal[j] for j in range(3)]
        vertices = [[center[j]+(a*.46 if j == axes[0] else b*.46 if j == axes[1] else 0)
                     for j in range(3)] for a,b in ((-1,-1),(1,-1),(1,1),(-1,1))]
        points = " ".join(f"{project(v)[0]:.2f},{project(v)[1]:.2f}" for v in vertices)
        color = cube.COLORS[cube.FACES[state[i]//9]]
        stroke = "#bd9335" if state[i] != i else "#203744"
        fragment = f'<polygon points="{points}" fill="{color}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>'
        if i % 9 == 4:
            x,y,_ = project(center)
            fragment += text(round(x-5,2), round(y+5,2), cube.FACES[i//9], 15, weight="600")
        tiles.append((project(center)[2], fragment))
    return f'<ellipse cx="{cx}" cy="{cy+scale*2.1}" rx="{scale*1.7}" ry="{scale*.18}" fill="#e1e8e2"/>'+"".join(fragment for _,fragment in sorted(tiles))


def net(state, x, y, tile=18):
    positions = {"U": (1,0), "L": (0,1), "F": (1,1), "R": (2,1), "B": (3,1), "D": (1,2)}
    result = ""
    for i in range(54):
        face = cube.FACES[i//9]
        gx,gy = positions[face]
        xx,yy = x+gx*(tile*3+9)+(i%3)*tile, y+gy*(tile*3+9)+(i%9//3)*tile
        color = cube.COLORS[cube.FACES[state[i]//9]]
        stroke = "#bd9335" if state[i] != i else "#203744"
        result += f'<rect x="{xx}" y="{yy}" width="{tile-2}" height="{tile-2}" rx="2" fill="{color}" stroke="{stroke}" stroke-width="1"/>'
        if i%9 == 4:
            result += text(xx+tile*.25, yy+tile*.7, face, tile*.5, weight="600")
    return result


def document(body, width=1200, height=900):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#f5f6f3"/>{body}</svg>'


def export(destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    ab = cube.apply(cube.IDENTITY, cube.parse("R U"))
    ba = cube.apply(cube.IDENTITY, cube.parse("U R"))
    c = cube.apply(cube.IDENTITY, cube.parse("R U R' D R U' R' D'"))
    body = text(45,55,"Rubik & Groupes",30,weight="600")+text(45,88,"Quatre illustrations pour passer du geste à l'algèbre",16,"#647584")
    for x,y in ((35,115),(615,115),(35,495),(615,495)):
        body += f'<rect x="{x}" y="{y}" width="550" height="355" rx="14" fill="#fff" stroke="#dde4df"/>'
    body += text(60,151,"01 · Une transformation est une permutation",19,weight="600")
    body += scene(cube.IDENTITY,185,290,49)+net(cube.IDENTITY,316,212,18)
    body += text(60,435,"G = ⟨U, R, F, D, L, B⟩ ⊂ S₄₈",18,"#217960")
    body += text(640,151,"02 · Le groupe n'est pas abélien",19,weight="600")
    body += scene(ab,770,290,48)+scene(ba,1023,290,48)
    body += text(744,420,"R puis U",17)+text(997,420,"U puis R",17)
    body += text(640,451,"RU ≠ UR · même ordre 105, effets différents",14,"#647584")
    body += text(60,531,"03 · Un commutateur pour agir localement",19,weight="600")
    body += scene(c,190,657,48)+net(c,326,588,18)
    body += text(60,790,"C = [R U R', D] = R U R' D R U' R' D'",15,"#217960")
    body += text(60,820,"3 coins affectés · 0 arête · ordre 3",16)
    body += text(640,531,"04 · Les contraintes de résolubilité",19,weight="600")
    for y,value in ((588,"Σ co ≡ 0 (mod 3)"),(637,"Σ eo ≡ 0 (mod 2)"),(686,"sgn(σc) = sgn(σe)")):
        body += text(660,y,value,24,"#217960")
    body += text(660,745,"|G| = 8! × 12! × 3⁷ × 2¹⁰",19)
    body += text(660,780,f"= {cube.GROUP_SIZE:,}".replace(","," "),19)
    body += text(640,821,"Un seul coin tourné ou une seule arête retournée",13,"#647584")+text(640,841,"ne s'obtient pas par des tours de faces.",13,"#647584")
    body += text(45,879,"Convention : les mots se lisent de gauche à droite. Centres fixes, cube standard 3×3.",12,"#647584")
    (destination/"apercu.svg").write_text(document(body), encoding="utf-8")
    (destination/"cube_et_patron.svg").write_text(document(scene(cube.IDENTITY,180,170,58)+net(cube.IDENTITY,355,55,25),700,350),encoding="utf-8")
    (destination/"non_commutativite.svg").write_text(document(text(30,35,"RU ≠ UR",24)+scene(ab,180,210,62)+scene(ba,500,210,62)+text(120,365,"R puis U",18)+text(440,365,"U puis R",18),700,400),encoding="utf-8")
    (destination/"commutateur_trois_coins.svg").write_text(document(text(25,35,"[R U R', D] · trois coins, aucune arête",23)+scene(c,180,220,62)+net(c,370,105,24)+text(30,380,cube.info(c)["corner_cycle_text"],16),730,410),encoding="utf-8")
    return destination


if __name__ == "__main__":
    print(export(Path(__file__).resolve().parent/"illustrations"))

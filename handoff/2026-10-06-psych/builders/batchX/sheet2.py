import sys, pathlib
from PIL import Image, ImageDraw
out, files = sys.argv[1], sys.argv[2:]
W, H = 330, 700; cols = 6; rows = (len(files)+cols-1)//cols
sh = Image.new("RGB", (W*cols, (H+20)*rows), "white"); d = ImageDraw.Draw(sh)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB"); im.thumbnail((W-6, H))
    x, y = (i%cols)*W, (i//cols)*(H+20)
    sh.paste(im, (x, y+20)); d.text((x+4, y+4), pathlib.Path(f).stem[-40:], fill="black")
sh.save(out, quality=85)

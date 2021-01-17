import os, asyncio, tempfile, shutil
from aiohttp import web, ClientSession
from PIL import Image
from motya.font import Font
from motya.motya import Motya
from motya.template import Template, Frame

# Костыль
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

app = web.Application()
routes = web.RouteTableDef()

motyapage = open("web/motya.html", "r").read()

@routes.post("/motya")
async def motya_api(req):
    temp = tempfile.mkdtemp(dir=tempfile.gettempdir())

    fontfile = "times.ttf"
    fontsize = 45
    text = ""

    try:
        async for entry in (await req.multipart()):
            if entry.name == "photo":
                photo = temp + "/" + entry.filename
                f = open(photo, "wb")

                while True:
                    chunk = await entry.read_chunk()

                    if not chunk:
                        break

                    f.write(chunk)

                f.close()
            elif entry.name == "text":
                text = (await entry.read()).decode()
            elif entry.name == "fontsize":
                try:
                    fontsize = int((await entry.read()).decode())
                except:
                    pass
            elif entry.name == "font":
                if not entry.filename:
                    continue

                fontfile = temp + "/" + entry.filename
                f = open(fontfile, "wb")

                while True:
                    chunk = await entry.read_chunk()

                    if not chunk:
                        break

                    f.write(chunk)

                f.close()
    except:
        shutil.rmtree(temp)
        return web.Response(text="An error occured while trying to parse multipart data")

    if text == "":
        shutil.rmtree(temp)
        return web.Response(text="Please provide text")

    try:
        template = Template(
            image=Image.open("template.jpg"),
            width=574,
            height=522,
            frame=Frame(x_start=75, y_start=45, x_end=499, y_end=373),
            padding=10,
        )

        font = Font(fontfile, size=fontsize, font_y=390)

        motya = Motya(
            template=template,
            phrases=[text],
            images=[Image.open(photo)],
            font=font
        )

        dem = motya.generate()
        dem.save(temp + "/dem.png")
    except:
        shutil.rmtree(temp)
        return web.Response(text="An error occured while trying to create demotivator")

    response = web.StreamResponse(
        headers={
            "Content-Disposition": "attachment; filename=\"dem.png\"",
            "Content-Length": str(os.path.getsize(temp + "/dem.png"))
        }
    )
    await response.prepare(req)

    f = open(temp + "/dem.png", "rb")

    while True:
        chunk = f.read(65535)

        if not chunk:
            break

        await response.write(chunk)

    f.close()

    await response.write_eof()

    shutil.rmtree(temp)

    return response

@routes.get("/")
async def motya_web(req):
    return web.Response(text=motyapage, content_type="text/html")

async def s(): return ClientSession()
session = asyncio.get_event_loop().run_until_complete(s())

app.add_routes(routes)
web.run_app(app, port=os.environ.get("PORT", 8080))

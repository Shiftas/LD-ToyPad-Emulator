import requests
from PIL import Image
from io import BytesIO
import os

def download_and_resize_image(url, character_name, index):
    try:
        # Ensure the output directory exists
        if not os.path.exists('server/images'):
            os.makedirs('server/images')

        character_name_sanitized = character_name.replace(' ', '_')
        image_path = f"server/images/{index:03d}_{character_name_sanitized}.jpg"

        # Check if the image already exists
        if os.path.exists(image_path):
            # print(f"Image for {character_name} already exists. Skipping download.")
            return
        # print(f"{image_path} ")
        # return

        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')  # Convert image mode to RGB

        # Maintain aspect ratio and resize within 150x150 bounding box
        max_size = (150, 150)
        img.thumbnail(max_size, Image.LANCZOS)

        img.save(image_path, quality=95)  # Save image with high JPEG quality
        print(f"Downloaded and resized image for {character_name}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image for {character_name} from {url}: {e}")
    except (PIL.UnidentifiedImageError, OSError) as e:
        print(f"Failed to process image for {character_name}: {e}")

# Example usage
image_links = {
    'Batman': 'https://m.media-amazon.com/images/I/61Hl5GKJXdL._AC_UF894,1000_QL80_.jpg',
    'Gandalf': 'https://m.media-amazon.com/images/I/61d5AJJTiOL._AC_UF894,1000_QL80_.jpg',
    'Wyldstyle': 'https://m.media-amazon.com/images/I/51qnro877GL._AC_UF894,1000_QL80_.jpg',
    'Aquaman': 'https://m.media-amazon.com/images/I/61MvpTACuVL._AC_UF894,1000_QL80_.jpg',
    'Bad Cop': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn9sdJ0ASfmHoseZxjIOHvfuZTvNiTC0vchw&s',
    'Bane': 'https://i.ebayimg.com/images/g/XxMAAOSw~91bmEl4/s-l1600.jpg',
    'Bart Simpson': 'https://m.media-amazon.com/images/I/61FnemwB2IL.jpg',
    'Benny': 'https://static.wikia.nocookie.net/lego/images/9/99/Spaceman-legos-lego-movie.jpg/revision/latest?cb=20190520234640',
    'Chell': 'https://static.wikia.nocookie.net/lego/images/d/d0/Chell.JPG/revision/latest?cb=20170822120718',
    'Cole': 'https://i.ebayimg.com/images/g/Ha8AAOSwX3dkZbks/s-l1200.webp',
    'Cragger': 'https://m.media-amazon.com/images/I/41gTbODlqhL._AC_UF894,1000_QL80_.jpg',
    'Cyborg': 'https://ideascdn.lego.com/media/generate/lego_ci/0dc0a54e-4653-4643-a77e-6912aa7a3d31/resize:950:633/legacy',
    'Cyberman': 'https://img.bricklink.com/ItemImage/ML/dim014.png',
    'Doc Brown': 'https://img.bricklink.com/ItemImage/MN/0/btf002.png',
    'The Doctor': 'https://m.media-amazon.com/images/I/61OH6dw6QlL.jpghttps://www.steinelager.de/img/sets/7/1/2/0/4/71204-1_2.jpg',
    'Emmet': 'https://m.media-amazon.com/images/I/61C35mvgOtS._AC_UF894,1000_QL80_.jpg',
    'Eris': 'https://static.wikia.nocookie.net/legolegendsofchima/images/e/ed/Eris1.PNG/revision/latest?cb=20141214024035',
    'Gimli': 'https://m.media-amazon.com/images/I/71Kwvh938dL._AC_UF894,1000_QL80_.jpg',
    'Gollum': 'https://m.media-amazon.com/images/I/31pKwY7G1uL._AC_UF894,1000_QL80_.jpg',
    'Harley Quinn': 'https://m.media-amazon.com/images/I/617ZgtYowZL._AC_UF894,1000_QL80_.jpg',
    'Homer Simpson': 'https://m.media-amazon.com/images/I/51C-iSW6giL.jpg',
    'Jay': 'https://i.ebayimg.com/images/g/YhkAAOSwTh1gEAka/s-l1200.webp',
    'Joker': 'https://m.media-amazon.com/images/I/81zdQczhOCL.jpg',
    'Kai': 'https://i.redd.it/hp0c3vtoq3cc1.jpeg',
    'ACU Trooper': 'https://static.wikia.nocookie.net/lego-dimensions/images/e/ed/ACUTrooper.png/revision/latest?cb=20151005195137',
    'Gamer Kid': 'https://static.wikia.nocookie.net/p__/images/1/12/Gamer_Kid.png/revision/latest?cb=20170121185124&path-prefix=protagonist',
    'Krusty the Clown': 'https://m.media-amazon.com/images/I/410DoCXQGpL.jpg',
    'Laval': 'https://static.wikia.nocookie.net/legolegendsofchima/images/8/82/1828abf66b7cd32659bfc1cfaeb99b50.png/revision/latest/scale-to-width/360?cb=20180827031751',
    'Legolas': 'https://m.media-amazon.com/images/I/41VbJ-TtBeL._AC_UF894,1000_QL80_.jpg',
    'Lloyd': 'https://static.wikia.nocookie.net/ninjago/images/5/58/LloydDR2Part1infobox.png/revision/latest?cb=20240413051908',
    'Marty McFly': 'https://m.media-amazon.com/images/I/41Osb1eBMwL._AC_UF894,1000_QL80_.jpg',
    'Nya': 'https://m.media-amazon.com/images/I/51bWZ1XvToL.jpg',
    'Owen Grady': 'https://m.media-amazon.com/images/I/41upBp7IkkL._AC_UF894,1000_QL80_.jpg',
    'Peter Venkman': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL1OkqFbz2iKZm96MaewF2A0saMSRCYj2-bA&s',
    'Slimer': 'https://m.media-amazon.com/images/I/712pgY8RPVL._AC_UF894,1000_QL80_.jpg',
    'Scooby-Doo': 'https://m.media-amazon.com/images/I/41RAFSZ-AiL._AC_UF894,1000_QL80_.jpg',
    'Sensei Wu': 'https://m.media-amazon.com/images/I/417hDY-xtbL._AC_UF894,1000_QL80_.jpg',
    'Shaggy': 'https://m.media-amazon.com/images/I/41k1-oh1DcL._AC_UF894,1000_QL80_.jpg',
    'Stay Puft': 'https://i.ebayimg.com/images/g/wZwAAOSwuVFhlIIW/s-l1200.webp',
    'Superman': 'https://m.media-amazon.com/images/I/41hjCc+ZlDL._AC_UF894,1000_QL80_.jpg',
    'Unikitty': 'https://oyster.ignimgs.com/mediawiki/apis.ign.com/lego-dimensions/e/e0/Unikitty.jpg',
    'Wicked Witch of the West': 'https://static.wikia.nocookie.net/lego/images/9/93/Wicked_Witch_of_the_West.png/revision/latest?cb=20230509041502',
    'Wonder Woman': 'https://www.lego.com/cdn/cs/set/assets/blt6cc079042b6b9f3a/DC_-_Characters_Overview_-_Standard-Block_-_Wonder_Woman.jpg?fit=crop&format=jpg&quality=80&width=800&height=426&dpr=1',
    'Zane': 'https://m.media-amazon.com/images/I/41DuunFjgAL._AC_UF894,1000_QL80_.jpg',
    'Green Arrow': 'https://m.media-amazon.com/images/I/41F-8dAvCkL._AC_UF894,1000_QL80_.jpg',
    'Supergirl': 'https://m.media-amazon.com/images/I/41AbmWjjm2L._AC_UF894,1000_QL80_.jpg',
    'Abby Yates': 'https://static.wikia.nocookie.net/lego-dimensions/images/d/d4/AbbyNew.png/revision/latest?cb=20160929055748',
    'Finn the Human': 'https://i.ebayimg.com/images/g/xGgAAOSwcT1jZrEa/s-l1600.jpg',
    'Ethan Hunt': 'https://static.wikia.nocookie.net/lego-dimensions/images/1/1f/Ethan_Hunt_%28Tuxedo%29.png/revision/latest?cb=20160708220634',
    'Lumpy Space Princess': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPVPZKWj9P_woEGElq4_8bvaPXaBVr0ysD3g&s',
    'Jake the Dog': 'https://i.pinimg.com/736x/1a/b6/ce/1ab6ce4f84044b75cad8e72433574d37.jpg',
    'Harry Potter': 'https://www.lego.com/cdn/cs/set/assets/blt65da66f0583ac02f/71247_alt2.jpg',
    'Lord Voldemort': 'https://www.lego.com/cdn/cs/set/assets/blt16e474815da1372e/HP-Char_Voldemort_2-Sidekick-XL4492c984eb3c37652f7ee1bb57055d67d68ac72ceff7963497ee55640f5ddd80.jpg?fit=crop&format=jpg&quality=80&width=800&height=600&dpr=1',
    'Michael Knight': 'https://m.media-amazon.com/images/I/51u8LA4phpL.jpg',
    'B.A. Baracus': 'https://i.ebayimg.com/images/g/aNsAAOSwMVdYHJ6f/s-l400.jpg',
    'Newt Scamander': 'https://cdn.toypro.com/media/cache/tp_product_detail/uploads/images/custom/25860-src.webp',
    'Sonic the Hedgehog': 'https://img.brickowl.com/files/image_cache/larger/lego-sonic-the-hedgehog-level-pack-set-71244-623991.jpg',
    'Future Update (unreleased)': 'https://m.media-amazon.com/images/I/817VIwphrlL._AC_UF1000,1000_QL80_.jpg',
    'Gizmo': 'https://ideascdn.lego.com/media/generate/lego_ci/79742894-317c-41ef-b040-3dfca800d328/resize:950:633/legacy',
    'Stripe': 'https://static.wikia.nocookie.net/lego/images/3/37/Stripe-physical.PNG/revision/latest?cb=20170822020959',
    'E.T.': 'https://www.lego.com/cdn/cs/set/assets/blt78b39f5757ec88eb/40649_alt1.png',
    'Tina Goldstein': 'https://static.wikia.nocookie.net/lego/images/3/3e/Tina_Goldstein.JPG/revision/latest?cb=20170822123218',
    'Marceline the Vampire Queen': 'https://static.wikia.nocookie.net/lego/images/4/4c/Marceline-physical.JPG/revision/latest?cb=20170821062343',
    'Batgirl': 'https://static.wikia.nocookie.net/lego/images/a/ae/LEGO_Batgirl_Rebirth.png/revision/latest?cb=20230502025631',
    'Robin': 'https://m.media-amazon.com/images/I/71t0ox5zWDL.jpg',
    'Sloth': 'https://i.ebayimg.com/images/g/0AMAAOSwdhdlBWN0/s-l1200.jpg',
    'Hermione Granger': 'https://www.lego.com/cdn/cs/set/assets/bltdf80dfb6e99f19f5/HP-Char_Hermione_2-Sidekick-XL.jpg?fit=crop&format=jpg&quality=80&width=800&height=800&dpr=1',
    'Chase McCain': 'https://static.wikia.nocookie.net/lego/images/6/60/Chase_McCain_2017.jpg/revision/latest?cb=20230614070009',
    'Excalibur Batman': 'https://i.ebayimg.com/images/g/63wAAOSwiHVfn-bK/s-l1600.jpg',
    'Raven': 'https://static.wikia.nocookie.net/lego/images/1/1d/Raven_TTG_Physical.jpeg/revision/latest?cb=20171103084312',
    'Beast Boy': 'https://i.ebayimg.com/images/g/aQAAAOSwe45kJ2EB/s-l1200.webp',
    'Betelgeuse': 'https://static.wikia.nocookie.net/lego/images/a/ac/Betelgeuse.png/revision/latest/thumbnail/width/360/height/360?cb=20180218000156',
    'Lord Vortech (unreleased)': 'https://static.wikia.nocookie.net/lego-dimensions-2-the-rise-of-enoch/images/0/0d/Vortechius_Vortell_Vortech.png/revision/latest?cb=20201119144623',
    'Blossom': 'https://m.media-amazon.com/images/I/41JWqZ0EqNL._AC_UF894,1000_QL80_.jpg',
    'Bubbles': 'https://static.wikia.nocookie.net/lego/images/6/6d/41287_Bubbles.jpeg/revision/latest?cb=20180517230457',
    'Buttercup': 'https://static.wikia.nocookie.net/lego/images/c/ca/41288_Buttercup.jpeg/revision/latest?cb=20180531173803',
    'Starfire': 'https://m.media-amazon.com/images/I/41muhStNdRL._AC_UF894,1000_QL80_.jpg',
    'Supergirl Red Lantern': 'https://m.media-amazon.com/images/I/41AbmWjjm2L._AC_UF894,1000_QL80_.jpg',
}

for index, (name, url) in enumerate(image_links.items(), start=1):
    download_and_resize_image(url, name, index)
#from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts
from yaml import load
import pathlib
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def clean_f_string(string):
    return '\n'.join([m.lstrip() for m in string.split('\n')])

def build_from_repos(repos):
    grid_cards = []
    for repo_id, repo in repos.items():
        new_card = f"""
            :::{{grid-item-card}} {repo['title']}
            :shadow: md
            :link: {repo['url']}
            :img-top: {repo['thumbnail']}
            {repo['description']}
            :::
        """
        grid_cards.append(clean_f_string(new_card))
   
    grid_cards = "\n".join(grid_cards)

    grid_body = f"""
        ::::{{grid}} 2
        :gutter: 3
        {grid_cards}
        ::::
    """
    return clean_f_string(grid_body)
    

def main(app):
    # read main page content
    main_content = ""
    with open("main.md") as fid:
        for line in fid:
            main_content += line
    main_content += "\n \n"

    # get repositories to be included in gallery
    with open("notebook_gallery.yaml") as fid:
        config = load(fid, Loader=Loader)
    
    grid = build_from_repos(config["domains"])

    main_content += grid
    if pathlib.Path(f"index.md").is_file():
        pathlib.Path(f"index.md").unlink()
    pathlib.Path(f"index.md").write_text(main_content)
   

    # repo_dicts = generate_repo_dicts(all_items)

    # title = "Notebook Gallery"

    # subtext = ""
    # with open("notebook_gallery_intro.md") as fid:
    #     for line in fid:
    #         subtext = subtext + line

    # submit_btn_link = "https://projectpythia.org/cookbook-guide.html"
    # submit_btn_txt = "How can I create a new Cookbook?"
    # menu_html = generate_menu(
    #     repo_dicts, submit_btn_txt=submit_btn_txt, submit_btn_link=submit_btn_link
    # )

    # build_from_repos(
    #     repo_dicts, "index", title=title, subtext=subtext, menu_html=menu_html
    # )
    pass

def setup(app):
    app.connect("builder-inited", main)
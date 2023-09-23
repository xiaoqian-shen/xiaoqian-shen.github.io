from pybtex.database.input import bibtex


def get_personal_data():
    name = ["Xiaoqian", "Shen", "沈晓倩"]
    email = "xiaoqian.shen@kaust.edu.sa"
    twitter = "xiaoqian_shen"
    github = "xiaoqian-shen"
    linkedin = "xiaoqian-shen"
    bio_text = f"""
                <p>
                <span style="font-weight: bold;">Bio:</span>
                I am currently a Master student of Computer Science at <a href="https://cemse.kaust.edu.sa/" target="_blank">King
                Abdullah University of Science and Technology</a> supervised by <a
                    href="https://cemse.kaust.edu.sa/people/person/mohamed-elhoseiny" target="_blank">Mohamed
                Elhoseiny</a>.
                Before that, I received BSc in Computer Science from <a href="https://global.jlu.edu.cn/"
                                                                        target="_blank">Jilin University</a>, China.
            </p>
            <p>
                <span style="font-weight: bold;">Research:</span>
                I am excited about complex problems that can be tackled with learning-based systems. Currently, my
                research focuses on generative models, spatiotemporal representation and low-resource learning.
            <p>
            <span style="font-family: Monaco, monospace;">Feel free to reach out to me:</span>  <span style="font-weight: bold;"><a style="color: black;" href="mailto:xiaoqian.shen@kaust.edu.sa">xiaoqian.shen@kaust.edu.sa</a></span></p> 
            </p>
            <p>
                <a href="assets/pdf/resume.pdf" target="_blank"
                   style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> Resume</a>
                <a href="https://twitter.com/xiaoqian_shen" target="_blank" style="margin-right: 15px"><i
                        class="fab fa-twitter fa-lg"></i> Twitter</a>
                <a href="https://scholar.google.com/citations?hl=en&user=uToGtIwAAAAJ" target="_blank"
                   style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                <a href="https://github.com/xiaoqian-shen" target="_blank" style="margin-right: 15px"><i
                        class="fab fa-github fa-lg"></i> Github</a>
                <a href="https://www.linkedin.com/in/xiaoqian-shen-759991264/" target="_blank"
                   style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
            </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    Feel free to use this website as a template! It is fully responsive and very easy to use and maintain as it uses a python script that crawls your bib files to automatically add the papers and talks. If you find it helpful, please add a link to my website - I will also add a link to yours (if you want). <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Checkout the github repository for instructions on how to use it</a>. <br>
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kait0.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer


def get_author_dict():
    return {
    }


def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name=['Xiaoqian Shen', 'Xiaoqian Shen*'], add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'):
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'{string_part_i}</a>'
        if make_bold and string_part_i in make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{string_part_i}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-4">"""
    s += f"""<img src="{entry.fields['img']}" border="0" class="img-fluid" width="300" height="60" alt="Project image">"""
    s += """</div><div class="col-sm-8">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<span style= "font-weight: bold;font-size: 18px;font-family: normal;">{entry.fields['title']}</span> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    if 'journal' in entry.fields.keys():
        try:
            year = entry.fields['year']
        except:
            year = ''
        s += f"""<span style="font-style: italic;">{entry.fields['journal']} {year} </span> <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplementary', 'code': 'Code', 'video': 'Video', 'model': 'Model','data':'Dataset'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' '
            # s += f"""<a href="{entry.fields[k]}" target="_blank">[{v}]</a>"""
            s += f"""<a class="btn btn-outline-primary my-1 mr-1 btn-sm" href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    # cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    # cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    # for entr in ['title', 'journal', 'year']:
    #     cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    # cite += """}</pre></code>"""
    # s += f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> <hr> </div>"""
    return s


def get_proj_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-4">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid" alt="Project image">"""
    s += """</div><div class="col-sm-8">"""
    s += f"""<span style= "font-weight: bold;font-size: 18px;font-family: normal;">{entry.fields['title']}</span><br>"""
    s += f"""{entry.fields['group']},   <span style="color: blue;">{entry.fields['org']}</span> <br> {entry.fields['place']}, {entry.fields['year']} <br>"""
    if 'info' in entry.fields.keys():
        s += f"""<span style="font-family: Verdana;">{entry.fields['info']}</span><br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            # s += f"""<a class="btn btn-outline-primary my-1 mr-1 btn-sm" href="{entry.fields[k]}" target="_blank" rel="noopener">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> <hr> </div>"""
    return s


def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('files/publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_projects_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('files/project.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_proj_entry(k, bib_data.entries[k])
    return s


def get_index_html():
    pub = get_publications_html()
    project = get_projects_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container" style="alignment: center;">
        <div class="row" style="margin-top: 3em;">
            <div class="col-md-11" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}&emsp;{name[2]}</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <img src="assets/img/profile.jpg" class="hoverZoomLink" width="300px" style="border-radius: 50%;" width="240px" alt="Profile picture">
            </div>
        </div>
        
        <h3>News</h3>
        <table width="100%" align="center" border="0" cellspacing="0">
          <tr>
            <td width="60%" valign="middle">
              <ul>
                <li> <b>2023-07</b> One paper (HRS-Bench) gets accepted to ICCV'23 </li>
                <li> <b>2023-04</b> We released MiniGPT-4 and received github 10k stars in 3 days </li>
                <li> <b>2023-02</b> One paper (MoStGAN-V) gets accepted to CVPR'23 </li>
                <li> <b>2022-09</b> Start my Master jounery in King Abdullah University of Science and Technology (KAUST) </li>
                <li> <b>2022-07</b> One paper gets accepted to ECCV'22 </li>
                <li> <b>2021-12</b> Join Vision-CAIR at King Abdullah University of Science and Technology as a visiting research student</li>
              </ul>
            </td>
          </tr>
        </table>
        
        <div class="row" style="margin-top: 1em;">
            <div class="col-md-10" style="">
                <h3>Publications</h3>
                <br>
                {pub}
            </div>
        </div>
        <div class="row" style="margin-top: 1em;">
            <div class="col-md-10" style="">
                <h3>Experience</h3>
                <br>
                {project}
            </div>
        </div>
        <!-- <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer} 
        </div> -->
    </div>
    
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')


if __name__ == '__main__':
    write_index_html('index.html')

# autograph_behavior
Calculating statistics and making graphs of behavioral data\
Run in terminal with:
    
    python autograph_behavior.py params.py

## Program Definitions
- **Parameters** - Identified by keywords at beginning of lines, and lines that do not begin with a recognized keyword or ignored.
  - Parameters are case-sensitive and must be in the 'param_name = param_def' format including spaces.
  - All parameters are required except for edge_colors and fill_colors.
  - Recognized keywords and default values are:

        infileName = projectInputExample.csv  # name of csv behavior input file
        pptName = project.pptx                # name of PowerPoint file to be created
        grp1 = iso                            # name of group 1
        grp2 = gh                             # name of group 2
        num_IV = 3                            # number of independent variable columns (identifiers, such as group, drug, con. side, etc) prior to behavior data columns
        edge_colors = k tab:red               # color of bar edges for graph
        fill_colors = tab:grey xkcd:salmon    # color of bars on graph

## Contributors
### [Zelikowsky Lab - University of Utah School of Medicine](https://www.zelikowskylab.com/)

- **December 2022:**
  - Original functionality provided by Jordan Grammer and Donzelle Taylor
  - See [og_doc.md](og_doc.md) for the Dec 2022 documentation
  

- **June 2023 - present:**
  - The following provided by Alan Mo:\
**Optimized** - reduced memory and cpu usage and decreased time to compute.\
**Naming conventions** - converted variable and file names to use underscores exclusively, eliminating camelCase.\
**Documentation** - improved documentation and comments, created README, uploaded project to GitHub.\
  - Currently working on
**Upgrading** - add functionality to support more than two groups.
  
#### Sources

- Colors:\
https://matplotlib.org/stable/tutorials/colors/colors.html

- List of colors for params file:\
https://members.cbio.mines-paristech.fr/~nvaroquaux/tmp/matplotlib/users/colors.html

- Thanks to Thomas Winters for:\
https://pythonprogramming.altervista.org/inserting-an-image-in-powerpoint-with-python/ \
used for the _add_image function

- create_graph function adapted from:\
https://stackoverflow.com/questions/51027717/pyplot-bar-charts-with-individual-data-points

- create_ppt function adapted from :\
https://python-pptx.readthedocs.io/en/latest/user/slides.html

- delete_graphs function adapted from:\
https://stackoverflow.com/questions/17358722/python-3-how-to-delete-images-in-a-folder
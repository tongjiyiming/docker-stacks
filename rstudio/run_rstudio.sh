docker run -d --name rstudio -p 8787:8787 -v "$HOME":$PWD -w $PWD -e ROOT=TRUE -e PASSWORD=111111 tongjiyiming/r-geo

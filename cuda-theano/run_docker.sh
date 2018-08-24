sudo nvidia-docker run $4 --name $1 -e NB_USER=lem -e GRANT_SUDO=yes --user root \
-v "$PWD":$PWD -w $PWD -p $3 $2 \
start-notebook.sh \
#--NotebookApp.password='sha1:559f89535f2d:c320212e6708222a537f4f1d3efada91c1a8c5ca' \
#--NotebookApp.certfile = '/home/lem/.jupyter/mycert.pem'
#--NotebookApp.keyfile = '/home/lem/.jupyter/mykey.key'


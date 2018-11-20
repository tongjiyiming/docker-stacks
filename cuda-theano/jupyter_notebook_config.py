# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from jupyter_core.paths import jupyter_data_dir
import subprocess
import os
import errno
import stat
from subprocess import call

decrypted = call(["openssl", "req", "-x509", "-nodes", "-days", "365", "-subj", "/C=US/ST=VA", "-newkey", "rsa:1024", "-keyout", "/home/lem/.jupyter/mykey.key", "-out", "/home/lem/.jupyter/mycert.pem"])
print(decrypted)

### test for theano gpu running
decrypted = call(["python", "/home/lem/gpu_test.py"])
print(decrypted)
##################

c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.password='sha1:559f89535f2d:c320212e6708222a537f4f1d3efada91c1a8c5ca' \

c.NotebookApp.keyfile = '/home/lem/.jupyter/mykey.key'
c.NotebookApp.certfile = '/home/lem/.jupyter/mycert.pem'

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False

# Generate a self-signed certificate
if 'GEN_CERT' in os.environ:
    dir_name = jupyter_data_dir()
    pem_file = os.path.join(dir_name, 'notebook.pem')
    try:
        os.makedirs(dir_name)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(dir_name):
            pass
        else:
            raise
    # Generate a certificate if one doesn't exist on disk
    subprocess.check_call(['openssl', 'req', '-new',
                           '-newkey', 'rsa:2048',
                           '-days', '365',
                           '-nodes', '-x509',
                           '-subj', '/C=XX/ST=XX/L=XX/O=generated/CN=generated',
                           '-keyout', pem_file,
                           '-out', pem_file])
    # Restrict access to the file
    os.chmod(pem_file, stat.S_IRUSR | stat.S_IWUSR)
    c.NotebookApp.certfile = pem_file

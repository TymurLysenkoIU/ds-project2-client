# ds-project2-client
Distributed file system client for Distributed Systems course of Innopolis University.


## Follow these steps to lauch the cleint

### Clone the repository

git clone https://github.com/TymurLysenkoIU/ds-project2-client.git

### Open terminal in the project directory and run command to launch the client

```python
python client.py
```

### Now we can start using the service (if nameserver and storage services launched already)

This command will initialize storage and delete everything that was stored there before.
```python
init
```

### List of valid commands



```
start a working area
       init       'init'   
                  Reinitialize an existing distributed storage
    
work on the current change
       create     'create', path, filename
                  create file 'filename' in remote directory 'path'
       delete     'delete', path, filename
                  delete file 'filename' in remote directory 'path'
       write      'write', path, filename, filepath
                  copy local file 'filepath' to remote directory
                  'path' into file 'filename'
       info       'info', path, filename
                  get filesize of remote file 'filename' in 'path'
                  directory
       read       'read', path, filename, filepath
                  copy remote file 'filename' in 'path' directory
                  to local file 'filepath'
       copy       'copy', path, filename, new_path, new_filename
                  copy remote file 'filename' at directory 'path'
                  to remote file 'new_filename' at directory 
                  'new_path'
       move       'move', path, filename, new_path, new_filename
                  move remote file 'filename' at directory 'path'
                  to remote file 'new_filename' at directory 
                  'new_path'
                  
       
       opendir    'opendir', path
                  open remote directory 'path'
       readdir    'readdir', path
                  read remote directory 'path'
       makedir    'makedir', path, dirname
                  make remote directory 'dirname' in directory 
                  'path'
       deletedir  'deletedir', path
                  delete remote directory 'path

```

### Examples 

```
init
create / file.txt
write / file2.txt .gitignore
read / file2.txt copy_file2.txt
delete / file.txt
info / file2.txt

makedir / dir1
copy / file2.txt /dir1 file3.txt
move /dir1 file3.txt / file4.txt


opendir /dir1
create / example1.txt
create / example2.txt
create / example3.txt
makedir . dir2
readdir .
readdir /dir1


opendir ..

help
help create
help write
help read
...
```


## Command line mode

In some cases it is not convenient to open the client app

For those cases you can use the client directly from terminal using command line arguments

### Example

```
python client.py create / file.txt
```

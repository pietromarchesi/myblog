Run 
```
fab build 
```
in the source directory to build the website from the content directory.
To test locally, you can do 
```
fab reserve
```
Which builds and serves to localhost. 

Update the output directory linked to the github pages repo
```
rsync -av output/ ../output/
```
This will automatically sync the content with pietromarchesi.github.io (in the settings of that repo we then redirect to pietromarchesi.net)

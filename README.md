### Machine Learning Project 
To complete this House Predection Project following setup required 
### Requiremts 
1. [github account] (https://github.com/prashant0708/house_predection-)
2. [Heroku Account] (https://dashboard.heroku.com/apps)
3. [VC CODE IDE] (https://code.visualstudio.com/docs/?dv=win)
4. [GIT CLI] (https://git-scm.com/downloads)


Creating Conda enviroment 

'''
 conda create -p venv python==3.7 -y

''''

''''
conda activate venv/

'''

or 

'''
conda activate venv

'''


pip install -r requirements.txt

To add file into git 

'''

git add . 

'''
or 

'''

git add <file name >

''''

> Note: To ignore file or folder to uploded inot git we can write name of file / folder in .gitignore file 

To check the git status 

'''
git status 

'''
To check all the version maintained by git 

'''

git log 

'''

To create version /commit all changes by git 

'''

git commit -m "messages"

'''

To send version / changes to github 

''''

git push origin main 

'''

To check remote url 

'''

git remote  -v

'''

To setup CI/CD pipeline in heroku we need three information 

1. Heroku_email = prashant.singh2012p@gmail.com
2. Heroku_API_KEY= 8fb94ea9-9ae7-43a9-9ee8-bd4bfb3e6478
3. hEROKU_app_name = house-ml-project

BUILD DOCKER IMAGES 

'''
docker build -t <image_name>:<tagname>.

'''
> Note: Image name for docker must be lower case 


To list docker image 

''''

docker images 

''''

Run Dokcer images 

'''
docker run -p 5000:5000 -e PORT=5000 c1b8cbd98dbd

'''

To check running container in docker 

'''
docker ps 

'''

To stop docker container 

'''
docker stop <container_id>
'''

'''
python setup.py install

'''
Install ipykernel 

'''
pip install ipykernel
'''
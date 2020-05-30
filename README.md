##In Machine Learning need to change the model several times to find the best accuracy model manually. So this required lots of efforts and time for making a machine learning model precisely. so there's is obvious need to automate all this process of tweaking the code and retesting until the model gives a good level of accuracy .So here comes the role of Devops , Using Devops we can automate all these so it will save a lot of time and the developer can work on other project with a free mind.

##I am using jenkins for automation,github for deployment our code,and docker image for trainig our model.
##Before going to problem statement i need Docker image for trainig my model . this image depend on our model. In the my case i train a deep learning model so i need my image contain some deep learing modules. so i create Dockerfile for creating my custom image.Here i am creating 6 jobs for automation and for visual i use  build pipeline plugin

##
![DOCKERFILE](img/Dockerfile.jpg)
##PROBLEM STATEMENT :
###JOB 1 :


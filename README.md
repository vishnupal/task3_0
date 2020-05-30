## In Machine Learning need to change the model several times to find the best accuracy model manually. So this required lots of efforts and time for making a machine learning model precisely. so there's is obvious need to automate all this process of tweaking the code and retesting until the model gives a good level of accuracy .So here comes the role of Devops , Using Devops we can automate all these so it will save a lot of time and the developer can work on other project with a free mind.

## I am using jenkins for automation,github for deployment our code,and docker image for trainig our model.
## Before going to problem statement i need Docker image for trainig my model . this image depend on our model. In the my case i train a deep learning model so i need my image contain some deep learing modules. so i create Dockerfile for creating my custom image.Here i am creating 6 jobs for automation and for visual i use  build pipeline plugin

##
![DOCKERFILE](img/Dockerfile.jpg)
## PROBLEM STATEMENT :
### JOB 1 : Pull  the Github repo automatically when some developers push repo to Github

### Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

### Job3 : Train your model and predict accuracy or metrics.

### Job4 : if metrics accuracy is less than 80%  , then tweak the machine learning model architecture.
### Job5: Retrain the model or notify that the best model is being created

### Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left


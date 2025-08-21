docker build -t avigoldshtein/hostile-tweets-ex-app .
docker push avigoldshtein/hostile-tweets-ex-app:latest

oc apply -f secrets.yaml
oc apply -f deployment.yaml
oc apply -f service.yaml
oc apply -f route.yaml
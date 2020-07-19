# filestoreservice
Clone repo
- docker clone https://github.com/NavyaEV/filestoreservice.git

Command to build docker images
- docker build .

To run docker container using compose
- docker-compose up

API calls
List files:
- curl -i -X GET http://localhost:5110/v1/files

Add file
- curl -i -X POST http://localhost:5110/v1/files -F 'file=@/root/temp/sample.tar'

Delete file
- curl -i -X DELETE http://localhost:5110/v1/files -F 'file=sample.tar.gz'

Download file
- curl -D Header.txt -X GET http://localhost:5110/v1/files/download -F 'file=sample.tar' -OJ
- cat Header.txt

To deploy image on kubernetes environment
- kubectl apply -f ./filestoreservice-deployment.yaml
- kubectl expose deployment/filestoreservice
- kubectl get pods -o wide

Run API calls using podIP after creating pod using above method

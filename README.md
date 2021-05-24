# DNS_Remote
## Chạy các container docker
Ta chạy docker-compose:
```
$ docker-compose build
$ docker-compose up
```
## Vào máy attacker
```
$ docker ps //Dùng để lấy ID của container attacker
$ docker exec -it <ID> bash //Vào terminal của máy attacker
$ apt-get update
$ apt-get install gcc
```
## Biên dịch chương trình và tấn công
```
$ cd home
$ gcc attack.c -o attack
```

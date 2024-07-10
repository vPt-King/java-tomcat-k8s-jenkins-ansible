1. Ngrok http 8080 -> vào github repo java-tomcat-k8s-jenkins-ansible đổi lại link
2. Bật minikube
3. update chmod 777 /var/run/docker.sock
4. push to github






------------------------------------------------------------------------

Lỗi: 
+ Lỗi không tìm thấy kubectl khi chạy ansible => fix: tải binary kubectl và thông báo viết rõ đường dẫn kubectl đồng thời thêm file kubeconfig

+ Thực thi với quyền jenkins: chỉnh lại mật khẩu của jenkins user: sudo passwd jenkins, thêm user jenkins vào sudoers



